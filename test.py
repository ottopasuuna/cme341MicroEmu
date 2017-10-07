import random
from cpu import Micro

registers = ['x0', 'x1', 'y0', 'y1', 'o_reg', 'i_pins', 'i', 'm', 'r']

def test_init():
    m = Micro()
    assert(m.x0 == 0)
    assert(m.x1 == 0)
    assert(m.y0 == 0)
    assert(m.y1 == 0)
    assert(m.i == 0)
    assert(m.m == 0)
    assert(m.r == 0)
    assert(m.i_pins == 0)
    assert(m.o_reg == 0)
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
        assert(getattr(m, reg) == data)

    # Test valid registers
    # TODO: use random numbers for data
    for reg in registers:
        if reg not in ['i_pins', 'r']:
            check_load(reg, 1)

    try:
        m.load('i_pins', 1)
        raise RuntimeError('Did not handle invalid destination')
    except ValueError:
        pass

def test_ram_load():
    m = Micro()
    m.i = 0
    m.m = 1
    for x in range(0,16):
        m.load('dm', x)

    for x in range(0,16):
        assert(m.dm == x)


def test_valid_mov():
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
                m.r = val # can't use m.load
            # Make i_pins different so we know the cpu isn't cheating
            m.i_pins = val+4

            m.mov(dest, source)
            if dest != source and source != 'i_pins':
                print(dest, source)
                assert(getattr(m, dest) == val)
            else:
                assert(getattr(m, dest) == m.i_pins)
def test_invalid_mov():
    for source in registers:
        for dest in ['i_pins', 'r']:
            m = Micro()
            val = random.randint(0,255)
            try:
                m.mov(dest, source)
                raise RuntimeError('Did not handle invalid destination')
            except ValueError:
                pass

def test_mem_dest_mov():
    for source in registers:
        if source in ['i', 'm']:
            continue
        m = Micro()
        m.i = 0
        m.m = 1
        for val in range(0,16):
            setattr(m, source, val)
            m.mov('dm', source)
        for val in range(0,16):
            assert(m.dm == val)

def test_mem_source_mov():
    for dest in registers:
        if dest in ['i_pins', 'r', 'i', 'm']:
            continue # TODO: test i and m registers
        m = Micro()
        m.i = 0
        m.m = 1
        for val in range(0,16):
            m._dm[val] = val
        for val in range(0,16):
            m.mov(dest, 'dm')
            print(getattr(m, dest))
            assert(getattr(m, dest) == val)

def test_valid_negate():
    m = Micro()
    val = random.randint(0,255)
    for reg in ['x0', 'x1']:
        setattr(m, reg, val)
        m.neg(reg)
        assert(m.r == -1*val)

def test_invalid_negate():
    m = Micro()
    val = random.randint(0,255)
    for reg in registers:
        if reg in ['x0', 'x1']:
            continue
        setattr(m, reg, val)
        try:
            m.neg(reg)
            raise RuntimeError('Did not detect invalid register for negate instruction')
        except ValueError:
            pass


def test_valid_add():
    m = Micro()
    xval = random.randint(0,255)
    yval = random.randint(0,255)
    for x in ['x0', 'x1']:
        setattr(m, x, xval)
        for y in ['y0', 'y1']:
            setattr(m, y, yval)
            m.add(x,y)
            assert(m.r == xval+yval)


def test_invalid_add():
    m = Micro()
    for x in registers:
        if x in ['x0', 'x1']:
            continue
        y = 'y0'
        try:
            m.add(x, y)
            print(x, y)
            raise RuntimeError('Failed to catch invalid add operation')
        except ValueError:
            pass
    for y in registers:
        if y in ['y0', 'y1']:
            continue
        x = 'x0'
        try:
            m.add(x, y)
            print(x, y)
            raise RuntimeError('Failed to catch invalid add operation')
        except ValueError:
            pass

def test_valid_sub():
    m = Micro()
    xval = random.randint(0,255)
    yval = random.randint(0,255)
    for x in ['x0', 'x1']:
        setattr(m, x, xval)
        for y in ['y0', 'y1']:
            setattr(m, y, yval)
            m.sub(x,y)
            assert(m.r == xval-yval)


def test_invalid_sub():
    m = Micro()
    for x in registers:
        if x in ['x0', 'x1']:
            continue
        y = 'y0'
        try:
            m.sub(x, y)
            print(x, y)
            raise RuntimeError('Failed to catch invalid sub operation')
        except ValueError:
            pass
    for y in registers:
        if y in ['y0', 'y1']:
            continue
        x = 'x0'
        try:
            m.sub(x, y)
            print(x, y)
            raise RuntimeError('Failed to catch invalid sub operation')
        except ValueError:
            pass


def test_valid_and():
    m = Micro()
    xval = random.randint(0,255)
    yval = random.randint(0,255)
    for x in ['x0', 'x1']:
        setattr(m, x, xval)
        for y in ['y0', 'y1']:
            setattr(m, y, yval)
            m.and_op(x,y)
            assert(m.r == xval & yval)


def test_invalid_and():
    m = Micro()
    for x in registers:
        if x in ['x0', 'x1']:
            continue
        y = 'y0'
        try:
            m.and_op(x, y)
            print(x, y)
            raise RuntimeError('Failed to catch invalid and operation')
        except ValueError:
            pass
    for y in registers:
        if y in ['y0', 'y1']:
            continue
        x = 'x0'
        try:
            m.and_op(x, y)
            print(x, y)
            raise RuntimeError('Failed to catch invalid and operation')
        except ValueError:
            pass


def test_valid_xor():
    m = Micro()
    xval = random.randint(0,255)
    yval = random.randint(0,255)
    for x in ['x0', 'x1']:
        setattr(m, x, xval)
        for y in ['y0', 'y1']:
            setattr(m, y, yval)
            m.xor(x,y)
            assert(m.r == xval ^ yval)


def test_invalid_xor():
    m = Micro()
    for x in registers:
        if x in ['x0', 'x1']:
            continue
        y = 'y0'
        try:
            m.xor(x, y)
            print(x, y)
            raise RuntimeError('Failed to catch invalid xor operation')
        except ValueError:
            pass
    for y in registers:
        if y in ['y0', 'y1']:
            continue
        x = 'x0'
        try:
            m.xor(x, y)
            print(x, y)
            raise RuntimeError('Failed to catch invalid xor operation')
        except ValueError:
            pass


