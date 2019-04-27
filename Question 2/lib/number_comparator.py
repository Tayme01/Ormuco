class VersionComparator:

    def __init__(self, first='nan', second='nan'):
        try:
            self.first = float(first)
            self.second = float(second)
        except (TypeError, ValueError):
            self.first = float('nan')
            self.second = float('nan')

    def compare(self):
        if self.first > self.second:
            return '"{0}” is greater than “{1}”.'.format(self.first, self.second)
        elif self.first < self.second:
            return '"{0}” is less than “{1}”.'.format(self.first, self.second)
        elif self.first == self.second:
            return '"{0}” is equal to “{1}”.'.format(self.first, self.second)
        else:
            return 'Invalid input passed! Check and try again.'

