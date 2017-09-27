''' Model of the CME341 mircoprocessor'''


class Micro(object):

    def __init__(self):
        self.x0     = 0
        self.x1     = 0
        self.y0     = 0
        self.y1     = 0
        self.i      = 0
        self.m      = 0
        self.o_reg  = 0
        self.i_pins = 0

        self._dm = [0]*16

    def __str__(self):
        registers = 'Registers:\n'
        registers += f'x0:{self.x0}   x1:{self.x1}   y0:{self.y0}   y1:{self.y1}\n'
        registers += f'i:{self.i}   m:{self.m}   o_reg:{self.o_reg}  i_pins:{self.i_pins}\n'
        memory = 'Memory:\n'
        memory += str(self._dm)
        return registers+memory

