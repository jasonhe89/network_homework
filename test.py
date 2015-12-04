import multiprocessing as mp

class pClient(object):
    def __init__(self):
        print('do some initialization here')

    def compute(self,data):
        print('Computing things!')
        return data * data

    def produce_data(self):
        yield -100
        for i in range(10):
            yield i
        yield 100

if __name__=="__main__":
    #pool = multiprocessing.Pool(processes=4)
    #p = mp.Pool(processes = 4,
     #           initializer = pClient)
    #print(p.map(pClient.compute, pClient.produce_data()))
    ll=range(10)
    ll[0:5]
    ll[5:10]