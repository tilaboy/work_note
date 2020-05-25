import sys

def _revers(arr):
    return arr[::-1]

def _comple(arr):
    return ''.join(['1' if ele=='0' else '0' for ele in arr])

def _both(arr):
    return _revers(_comple(arr))
#  sol: 0000111011
#  sol: 0010001111
#  sol: 1101110000
#  sol: 1111000100
a_ori = '0001101111'
a_com = '1110010000'
a_rev = '1111011000'
a_bot = '0000100111'

assert a_com == _comple(a_ori)
assert a_rev == _revers(a_ori)
assert a_bot == _both(a_ori)

for ele in [a_ori, a_com, a_rev, a_bot]:
    print(int(ele, 2), ele,
          int(_comple(ele), 2), _comple(ele),
          int(_revers(ele), 2), _revers(ele),
          int(_both(ele), 2), _both(ele))
