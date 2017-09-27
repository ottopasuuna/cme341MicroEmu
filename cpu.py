''' Model of the CME341 mircoprocessor'''


class Micro(object):

    def __init__(self):
        ''' Initialize registers to 0.
            Also initializes RAM unit and i_pins
        '''
        self.x0    = 0
        self.x1    = 0
        self.y0    = 0
        self.y1    = 0
        self.i     = 0
        self.m     = 0
        self.r     = 0
        self.o_reg  = 0
        self.i_pins = 0
        self.dm = [0]*16

    def __str__(self):
        ''' String representation of the mircoprocessor state'''
        registers = 'Registers:\n'
        registers += f'x0:{self.x0}   x1:{self.x1}   y0:{self.y0}   y1:{self.y1}\n'
        registers += f'i:{self.i}   m:{self.m}   r:{self.r}  o_reg:{self.o_reg}  i_pins:{self.i_pins}\n'
        memory = 'Memory:\n'
        memory += str(self.dm)
        return registers+memory

    def load(self, dest, data):
        ''' Load a valid register with a value'''
        if dest == 'x0':
            self.x0 = data
        elif dest == 'x1':
            self.x1 = data
        elif dest == 'y0':
            self.y0 = data
        elif dest == 'y1':
            self.y1 = data
        elif dest == 'i':
            self.i = data
        elif dest == 'm':
            self.m = data
        elif dest == 'o_reg':
            self.o_reg = data
        elif dest == 'dm':
            self.dm[self.i] = data
        else:
            raise ValueError('Invalid destination register')

    def mov(self, dest, source):
        ''' Move data from one register to another'''
        if dest in ['i_pins', 'r']:
            raise ValueError('Invalid destination register')
        if dest == source:
            setattr(self, dest, self.i_pins)
        else:
            setattr(self, dest, getattr(self, source))



