from datetime import datetime


def log(req, resp, time, filename='log.txt'):
    with open(filename, 'a') as file:
        file.write('[' + str(datetime.now()) + ']: ' + str(req) +
                   ', ' + str(resp) + ', ' + str(time) + ' sec\n')
        file.close()
