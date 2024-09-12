import math

class MD5:
    def __init__(self, string):
        print("MD5 constructor is called on {}".format(string))
        self.string = string
        self.buffers_rotate =  [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
			 5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20,
			 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
			 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]

        self.constant = [int(abs(math.sin(i+1)) * 4294967296) & 0xFFFFFFFF for i in range(64)]

    def get_string(self):
        return self.string

    def get_buffers_rotate(self):
        # This list maintains the amount by which to rotate the buffers during processing stage
        return self.buffers_rotate

    def get_constant(self):
        # This list maintains the additive constant to be added in each processing step.
        return self.constant

    def pad(self, msg):
        msg_len_in_bits = (8 * len(msg)) & 0xffffffffffffffff
        msg.append(0x80)

        while len(msg) % 64 != 56:
            msg.append(0)

        msg += msg_len_in_bits.to_bytes(8, byteorder='little')

        return msg

