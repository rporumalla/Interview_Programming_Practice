import pdb

class MyObj(object):

    def __init__(self, num_loops):
        self.count = num_loops

    def go(self):
        for i in range(self.count):
            pdb.set_trace()
            print i
        return

if __name__ == '__main__':
    MyObj(5).go()
