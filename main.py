from md5 import MD5

if __name__ == '__main__':

    string = "this is a test string"
    md5 = MD5(string)


    def test_pad():
        msg = bytearray("test", "ascii")
        print(msg)
        padded_msg = md5.pad(msg)
        print(padded_msg)


    test_pad()

    print("MD5 hash of {} is: {}".format(string, md5.md5()))
    print("The degree of agreement with the actual value: {}%".format(md5.evaluator()))