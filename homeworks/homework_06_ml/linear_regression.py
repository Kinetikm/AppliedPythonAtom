import numpy as np
from metrics import mse


class LinearRegression:
    def __init__(self, lambda_coef=0.1, regulatization=None, alpha=0.5):
        """
        :param lambda_coef: constant coef for gradient descent step
        :param regulatization: regularizarion type ("L1" or "L2") or None
        :param alpha: regularizarion coefficent
        """
        self.lambda_coef = lambda_coef
        self.regularizarion = regulatization
        self.alpha = alpha
        self.train = False

    def fit(self, X_train, y_train, iterations=1000, delta=0.1 ** 10):
        """
        Fit model using gradient descent method
        :param X_train: training data
        :param y_train: target values for training data
        :return: None
        """
        assert X_train.shape[0] == y_train.shape[0], 'Model is not trained'
        self.train = True
        x_train = np.hstack([np.ones((X_train.shape[0], 1)), X_train])
        columns = x_train.shape[1]
        hist0 = 0
        hist1 = 0
        x_train = np.hstack([np.ones((X_train.shape[0], 1)), X_train])
        columns = x_train.shape[1]
        self.w = np.zeros(columns)
        for i in range(iterations):
            # https://habr.com/ru/company/ods/blog/322076/ брал отсюда
            if self.regularizarion == 'L1':
                r = self.alpha * np.absolute(0.5 * self.w)
                r[0] = 0
            elif self.regularizarion == 'L2':
                r = self.alpha * np.square(self.w * 0.25)
                r[0] = 0
            else:
                r = 0
            prediction = self.predict(x_train)
            self.w -= (2 / x_train.shape[0]) * self.lambda_coef * (x_train.T.dot(
                (prediction - y_train)) + r)
            if i % 2 == 0:
                hist0 = mse(y_train, prediction)
            else:
                hist1 = mse(y_train, prediction)
            if i > 0 and np.abs(hist1 - hist0) < delta:
                # print(i)
                break
        return self

    def predict(self, X_test):
        """
        Predict using model.
        :param X_test: test data for predict in
        :return: y_test: predicted values
        """
        if all(X_test[:, 0] == 1):
            return X_test.dot(self.w)
        else:
            ones = np.ones((X_test.shape[0], 1))
            x_test = np.hstack([ones, X_test])
            return x_test.dot(self.w)

    def get_weights(self):
        """
        Get weights from fitted linear model
        :return: weights array
        """
        assert self.train, 'Model is not trained'
        return self.w
