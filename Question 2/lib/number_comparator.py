class VersionComparator:
    def __init__(self, first, second):
        try:
            self.first = float(first)
            self.second = float(second)
        except (TypeError, ValueError):
            self.first = float('nan')
            self.second = float('nan')

    def compare(self):
        if self.first > self.second:
            return '"{0}” is greater than “{1}”. '.format(self.first, self.second)
        elif self.second > self.first:
            return '"{0}” is greater than “{1}”. '.format(self.second, self.first)
        elif self.first == self.second:
            return '"{0}” is equal to “{1}”. '.format(self.first, self.second)
        else:
            return 'Invalid Input(s)!'

