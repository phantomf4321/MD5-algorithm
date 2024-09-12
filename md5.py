import math

class MD5:
    def __init__(self, string):
        print("MD5 constructor is called on {}".format(string))
        self.string = string

    def get_string(self):
        return self.string