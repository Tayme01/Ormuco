from lib import number_comparator

first = input('Input the first version string: ')
second = input('Input the second version string: ')

v = number_comparator.VersionComparator(first, second)
print(v.compare())