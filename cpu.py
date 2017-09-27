''' Model of the CME341 mircoprocessor'''


class Micro(object):

    def __init__(self):
        ''' Initialize registers to 0.
            Also initializes RAM unit and i_pins
        '''
        self._x0    = 0
        self._x1    = 0
        self._y0    = 0
        self._y1    = 0
        self._i     = 0
        self._m     = 0
        self._r     = 0
        self._o_reg  = 0
        self._i_pins = 0
        self._dm = [0]*16

    def __str__(self):
        ''' String representation of the mircoprocessor state'''
        registers = 'Registers:\n'
        registers += f'x0:{self._x0}   x1:{self._x1}   y0:{self._y0}   y1:{self._y1}\n'
        registers += f'i:{self._i}   m:{self._m}   r:{self._r}  o_reg:{self._o_reg}  i_pins:{self.i_pins}\n'
        memory = 'Memory:\n'
        memory += str(self._dm)
        return registers+memory

    @property
    def o_reg(self):
        return self._o_reg

    @property
    def i_pins(self):
        return self._i_pins

    @i_pins.setter
    def i_pins(self, val):
        self._i_pins = val


    def load(self, dest, data):
        ''' Load a valid register with a value'''
        if dest == 'x0':
            self._x0 = data
        elif dest == 'x1':
            self._x1 = data
        elif dest == 'y0':
            self._y0 = data
        elif dest == 'y1':
            self._y1 = data
        elif dest == 'i':
            self._i = data
        elif dest == 'm':
            self._m = data
        elif dest == 'o_reg':
            self._o_reg = data
        elif dest == 'dm':
            self._dm[self._i] = data
        else:
            raise ValueError('Invalid destination register')

    def mov(self, dest, source):
        ''' Move data from one register to another'''
        if dest in ['i_pins', 'r']:
            raise ValueError('Invalid destination register')
        if dest == source:
            if dest == 'o_reg' and source == 'r':
                self._o_reg = self._r
            else:
                setattr(self, '_'+dest, self.i_pins)
        else:
            setattr(self, '_'+dest, getattr(self, '_'+source))



