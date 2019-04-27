class VersionComparator:
    """
        Takes two strings, each representing a version number and compares both to determine if one is greater than the
        other or both are equal.
    """
    def __init__(self, first='nan', second='nan'):
        # Ensure the right parameters are passed. If not, gracefully handle error.
        try:
            if not isinstance(first, str) or not isinstance(second, str):
                raise TypeError()

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

