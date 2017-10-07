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
        self._dm = [0]*16

    def __str__(self):
        ''' String representation of the mircoprocessor state'''
        registers = 'Registers:\n'
        registers += f'x0:{self.x0}   x1:{self.x1}   y0:{self.y0}   y1:{self.y1}\n'
        registers += f'i:{self.i}   m:{self.m}   r:{self.r}  o_reg:{self.o_reg}  i_pins:{self.i_pins}\n'
        memory = 'Memory:\n'
        memory += str(self._dm)
        return registers+memory

    @property
    def dm(self):
        val = self._dm[self.i]
        self.i += self.m
        if self.i == 16:
            self.i = 0
        return val

    @dm.setter
    def dm(self, val):
        self._dm[self.i] = val
        self.i += self.m
        # i is only 4 bits...
        if self.i == 16:
            self.i = 0

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
            self.dm = data
        else:
            raise ValueError('Invalid destination register')

    def mov(self, dest, source):
        ''' Move data from one register to another'''
        if dest in ['i_pins', 'r']:
            raise ValueError('Invalid destination register')
        if dest == source:
            setattr(self, dest, self.i_pins)
        else:
            if dest == 'i' and source == 'dm':
                # don't auto increment i
                self.i = self._dm[self.i]
            setattr(self, dest, getattr(self, source))

    def neg(self, reg):
        if reg == 'x0':
            self.r = -1*self.x0
        elif reg == 'x1':
            self.r = -1*self.x0
        else:
            raise ValueError('Can only negate X0 or X1')

    def add(self, reg1, reg2):
        if reg1 == 'x0':
            if reg2 == 'y0':
                self.r = self.x0 + self.y0
            elif reg2 == 'y1':
                self.r = self.x0 + self.y1
            else:
                raise ValueError('Invalid registers for addition')
        elif reg1 == 'x1':
            if reg2 == 'y0':
                self.r = self.x0 + self.y0
            elif reg2 == 'y1':
                self.r = self.x0 + self.y1
            else:
                raise ValueError('Invalid registers for addition')
        else:
            raise ValueError('Invalid registers for addition')


    def sub(self, reg1, reg2):
        raise NotImplementedError()

    def mulhi(self, reg1, reg2):
        raise NotImplementedError()

    def mullo(self, reg1, reg2):
        raise NotImplementedError()

    def and_op(self, reg1, reg2):
        raise NotImplementedError()

    def xor(self, reg1, reg2):
        raise NotImplementedError()

    def com(self, reg):
        raise NotImplementedError()
