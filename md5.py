import math
import hashlib
class MD5:
    def __init__(self, string):
        print("MD5 constructor is called on {}".format(string))
        self.string = string
        self.buffers_rotate =  [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
			 5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20,
			 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
			 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]

        self.constants = [int(abs(math.sin(i+1)) * 4294967296) & 0xFFFFFFFF for i in range(64)]
        # Initial values initialized in the buffer.
        self.init_MDBuffer = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476] #4 words A, B, C and D each of 32-bits. we use this values in third step.


    def get_string(self):
        return self.string

    def get_buffers_rotate(self):
        # This list maintains the amount by which to rotate the buffers during processing stage
        return self.buffers_rotate

    def get_constant(self):
        # This list maintains the additive constant to be added in each processing step.
        return self.constants

    def get_init_MDBuffer(self):
        return self.init_MDBuffer

    """
    The first  step  in  the  MD5  algorithm  involves padding 
    the input message so its  length  (in  bits)  is congruent 
    to 448  modulo  512.  This is  done by  appending a single 
    '1' bit followed by enough '0' bits  to reach the required
    length, ensuring the total message length is a multiple of
    512 bits.
    """
    def pad(self, msg):

        # append an 0x80 byte in initial step
        msg_len_in_bits = (8 * len(msg)) & 0xffffffffffffffff
        msg.append(0x80)

        """
        step2:
        appending  0x00  bytes until the total  length 
        of the message in  bytes mod 64) is exactly 56
        """
        while len(msg) % 64 != 56:
            msg.append(0)


        # little endian convention
        msg += msg_len_in_bits.to_bytes(8, byteorder='little')

        return msg

    # UTILITY/HELPER FUNCTION:
    def leftRotate(self, x, amount):
        x &= 0xFFFFFFFF
        return (x << amount | x >> (32 - amount)) & 0xFFFFFFFF

    def processMessage(self, msg):
        init_temp = self.init_MDBuffer[
                    :]

        for offset in range(0, len(msg), 64):
            A, B, C, D = init_temp
            block = msg[offset: offset + 64]

            for i in range(64):
                if i < 16:
                    func = lambda b, c, d: (b & c) | (~b & d)
                    index_func = lambda i: i

                elif i >= 16 and i < 32:
                    func = lambda b, c, d: (d & b) | (~d & c)
                    index_func = lambda i: (5 * i + 1) % 16

                elif i >= 32 and i < 48:
                    func = lambda b, c, d: b ^ c ^ d
                    index_func = lambda i: (3 * i + 5) % 16

                elif i >= 48 and i < 64:
                    func = lambda b, c, d: c ^ (b | ~d)
                    index_func = lambda i: (7 * i) % 16

                F = func(B, C, D)
                G = index_func(
                    i)

                to_rotate = A + F + self.constants[i] + int.from_bytes(block[4 * G: 4 * G + 4], byteorder='little')
                newB = (B + self.leftRotate(to_rotate, self.buffers_rotate[i])) & 0xFFFFFFFF

                A, B, C, D = D, newB, B, C

            for i, val in enumerate([A, B, C, D]):
                init_temp[i] += val
                init_temp[i] &= 0xFFFFFFFF


        return sum(buffer_content << (32 * i) for i, buffer_content in enumerate(init_temp))

    def MD_to_hex(self, digest):
        raw = digest.to_bytes(16, byteorder='little')
        return '{:032x}'.format(int.from_bytes(raw, byteorder='big'))

    def md5(self):
        msg = bytearray(self.string,
                        'ascii')
        msg = self.pad(msg)
        processed_msg = self.processMessage(msg)
        message_hash = self.MD_to_hex(processed_msg)

        return message_hash

    def evaluator(self):

        str1 = self.string
        str2 = hashlib.md5(self.string.encode("utf-8")).hexdigest()

        str1 = str1 + ' ' * (len(str2) - len(str1))
        str2 = str2 + ' ' * (len(str1) - len(str2))
        return 100 - sum(1 if i == j else 0
                   for i, j in zip(str1, str2)) / float(len(str1))*100