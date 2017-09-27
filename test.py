import random
from cpu import Micro

registers = ['x0', 'x1', 'y0', 'y1', 'o_reg', 'i_pins', 'i', 'm', 'r']
int_registers = ['_x0', '_x1', '_y0', '_y1', '_o_reg', 'i_pins', '_i', '_m', '_r']

def test_init():
    m = Micro()
    assert(m._x0 == 0)
    assert(m._x1 == 0)
    assert(m._y0 == 0)
    assert(m._y1 == 0)
    assert(m._i == 0)
    assert(m._m == 0)
    assert(m._r == 0)
    assert(m.i_pins == 0)
    assert(m._o_reg == 0)
    assert(m._dm == [0]*16)

def test_string():
    m = Micro()
    print(m)
    expected =\
'''Registers:
x0:0   x1:0   y0:0   y1:0
i:0   m:0   r:0  o_reg:0  i_pins:0
Memory:
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]'''
    assert(str(m) == expected)

def test_load():
    m = Micro()
    def check_load(reg, data):
        m.load(reg, data)
        reg_str = '_'+reg
        assert(getattr(m, reg_str) == data)

    # Test valid registers
    # TODO: use random numbers for data
    for reg in registers:
        if reg not in ['i_pins', 'r']:
            check_load(reg, 1)

    # Test RAM
    # TODO: make this more thurough
    m.load('dm', 1)
    assert(m._dm[m._i] == 1)

    try:
        m.load('i_pins', 1)
        raise RuntimeError('Did not handle invalid destination')
    except ValueError:
        pass

def test_mov():
    for source in registers:
        for dest in registers:
            if dest in ['i_pins', 'r']:
                continue
            m = Micro()
            val = random.randint(0,255)

            # load source with a value
            if source not in ['i_pins', 'r']:
                m.load(source, val)
            elif source == 'r':
                m._r = val # can't use m.load
            # Make i_pins different so we know the cpu isn't cheating
            m.i_pins = val+4

            m.mov(dest, source)
            if dest != source and source != 'i_pins':
                print(dest, source)
                assert(getattr(m, '_'+dest) == val)
            else:
                assert(getattr(m, '_'+dest) == m.i_pins)

        for dest in ['i_pins', 'r']:
            m = Micro()
            val = random.randint(0,255)
            try:
                m.mov(dest, source)
                raise RuntimeError('Did not handle invalid destination')
            except ValueError:
                pass


