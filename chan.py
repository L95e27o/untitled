class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value < 10 or value > 100:
            print 'error'
        else:
            self._width = value
    @property
    def high(self):
        return self._high
    @high.setter
    def high(self, cath):
        if cath >=220 or cath<= 10:
            print 'error'
        else :
            self.__high = cath
    @property
    def resolution(self):
        return  786432

s = Screen()
s.width = 1024
s.height = 768
print 'resolution =', s.resolution
if s.resolution == 786432:
    print 'true'
else:
    print 'false'

