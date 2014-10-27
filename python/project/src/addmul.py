#!/usr/bin/python 


class AddMul:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def do(self):
        if len(self.a) != len(self.b):
            return None
        
        return [x*y for x,y in zip(self.a, self.b)]



if __name__ == "__main__":

    ad = AddMul([1,2,3], [4,5,6])
    result = ad.do()

    print result

