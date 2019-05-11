from gensim.models import Word2Vec
import pickle
from os import path

W2V_PATH = path.join("data/word2vec.model")
PKL_PATH = path.join("data/Product_dict.pkl")


class Model:

    def __init__(self):
        self.w2v = Word2Vec.load(W2V_PATH)
        with open(PKL_PATH, 'rb') as f:
            pkl = pickle.load(f)
        self.products = dict()
        for i in pkl:
            try:
                self.products[int(i)] = pkl[i].split(") ")[1]
            except IndexError:
                pass

    def most_similar_id(self, id: int):
        try:
            out = self.w2v.wv.most_similar([str(id)], topn=1)
        except KeyError:
            return None
        try:
            return self.products[int(out[0][0])]
        except KeyError:
            print("WTF")
            return None

    def predict_output_id(self, id: int):
        try:
            out = self.w2v.predict_output_word([str(id)], topn=1)
        except KeyError:
            return None
        try:
            return self.products[int(out[0][0])]
        except KeyError:
            print("WTF")
            return None
