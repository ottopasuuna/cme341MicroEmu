''' Model of the CME341 mircoprocessor'''


class Micro(object):

    def __init__(self):
        ''' Initialize registers to 0'''
        self._x0     = 0
        self._x1     = 0
        self._y0     = 0
        self._y1     = 0
        self._i      = 0
        self._m      = 0
        self.o_reg  = 0
        self.i_pins = 0
        self._dm = [0]*16

    def __str__(self):
        ''' String representation of the mircoprocessor state'''
        registers = 'Registers:\n'
        registers += f'x0:{self._x0}   x1:{self._x1}   y0:{self._y0}   y1:{self._y1}\n'
        registers += f'i:{self._i}   m:{self._m}   o_reg:{self.o_reg}  i_pins:{self.i_pins}\n'
        memory = 'Memory:\n'
        memory += str(self._dm)
        return registers+memory

