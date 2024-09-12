from md5 import MD5

if __name__ == '__main__':

    string = "this is a test string"
    md5 = MD5(string)

    print("MD5 hash of {} is {}".format(string, md5.md5()))
    print("The degree of agreement with the actual value: {}%".format(md5.evaluator()))