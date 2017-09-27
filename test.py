from cpu import Micro


def test_init():
    m = Micro()
    assert(m._x0 == 0)
    assert(m._x1 == 0)
    assert(m._y0 == 0)
    assert(m._y1 == 0)
    assert(m._i == 0)
    assert(m._m == 0)
    assert(m.i_pins == 0)
    assert(m.o_reg == 0)
    assert(m._dm == [0]*16)

def test_string():
    m = Micro()
    print(m)
    expected =\
'''Registers:
x0:0   x1:0   y0:0   y1:0
i:0   m:0   o_reg:0  i_pins:0
Memory:
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]'''
    assert(str(m) == expected)
