"""
left shift
shift left 
x << y
Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y.

shift right
x >> y
Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y.

and
x & y
Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.

  1010 1100
& 1111 0000
-----------
  1010 0000

if you & a number with 1111 1111

n & 1111 1111 -> n
n & 0000 0000 -> 0

or
x | y
Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.

xxxx xxxx
1111 1111
---------
1111 1111

n | 1111 1111 -> 1111 1111
n | 0000 0000 -> n

complement (flip all of the bits)
~ x
Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1.

~ 0110 0011
->1001 1100


xor
x ^ y
Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1.

calculates to 1 if the inputs are different
calculates to 0 if the inputs are the same

1111 0000
0001 1100
---------
1110 1100

0 ^ 0 = 0
1 ^ 0 = 1

0 ^ 1 = 1
1 ^ 1 = 0

n ^ 0000 0000 = n
n ^ 1111 1111 = ~n


7  = 0111 -> 3 = 0011
14 = 1110

x >> 1 << 1


pretend an integer is 8 bits

1010 1101
0101 1010

2's complement


 0 1 0 1 = 5
-8 4 2 1  

 1 1 0 1 = -3
-8 4 2 1  


 1 0 0 0 = -8
-8 4 2 1  


 0 1 1 1 = 7
-8 4 2 1  

unsigned integer
integer: -2147483648 to 2147483647
unsigned integer: 0 to 4294967295


"""

# print out 8 bits
"""
1010 1001


how do i print out the last bit in a binary number?



n >> 7 0000 0001 % 2 = 1
n >> 6 0000 0010 % 2 = 0

mask
n >> 7 0000 0001 & 1 = 1
       0000 0001
       ---------
       0000 0001

n >> 6 0000 0010 & 1 = 0
       0000 0001 
       ---------
       0000 0000     = 0

1010 1100
0000 1111
---------
0000 1100
       
"""

"""
input:
    num: 1001 1101
              ^
    n: 3

    num >> n
    1001 1101 >> 3
    xxxx xxx1
  & 0000 0001
  -----------
            1


    1001 1101
    0000 1000 == 1 << n
    ---------
    0000 1000 >> 3

    num & (1 << n)
"""
def get_nth_bit(num, n):
    return num >> n & 1

def get_nth_bit2(num, n):
    mask = 1 << n
    return (num & mask) >> n

def print_last_bit(n):
    return n & 0b1

def print_n_bits(num, num_bits):
    for i in range(num_bits, -1, -1):
        print(get_nth_bit(num, i), end='')
    print('')


def print_binary(n):
    print(bin(n))


n = 0b10101100

print_n_bits(n, 8)
print_n_bits(n, 16)

# leetcode
# https://leetcode.com/problems/reverse-bits/
class Solution:
    def reverseBits(self, n: int) -> int:
        """
        0000 0000 0101 1111 0000 1111 1010 1100

        swap first half with second half
        0000 1111 1010 1100 0000 0000 0101 1111

        1010 1100 0000 1111 0101 1111 0000 0000

        1100 1010 1111 0000 1111 0101 0000 0000
        
        0011 0101 1111 0000 1111 1010 0000 0000
        
        0000 0000 0101 1111 0000 1111 1010 1
        last_bit = n & 1
        n = n >> 1
        result = result << 1
        result = result | last_bit
                                              
        0000 0000 0000 0000 0000 0000 0000 0001
                                            ***
        
        """

        # result = 0

        # for num_bits in range(32):
        #     last_bit = n & 1
        #     n = n >> 1
        #     result = result << 1
        #     result = result | last_bit
        
        rev = 0

        for _ in range(32):
            rev = rev << 1
            bit = n & 1
            rev = rev | bit
            n = n >> 1

        """
        0000 0000 0101 1111 0000 1111 1010 0101
                                               

        0000 0000 0000 0000 0000 0000 0000 0000
    +   1000 0000 0000 0000 0000 0000 0000 0000
    +   0000 0000 0000 0000 0000 0000 0000 0000
    +   0010 0000 0000 0000 0000 0000 0000 0000
        101
        def reverseBits(self, n: int) -> int:
            ret, power = 0, 31
            while n:
                ret += (n & 1) << power
                n = n >> 1
                power -= 1
            return ret
        """

        """
        log 2 = 1        log(0000 0000 001x) 1.xxxx
        log 3 = 1.xxxx
        log 4 = 2        log(0000 0000 01xx) 2.xxxx
        log 5 = 2.xxxx
                         0000 0000 1xxx
        """
        return rev