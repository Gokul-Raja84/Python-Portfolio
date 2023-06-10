def binary_search(l, target, low=None, high=None):

	if low is None:
		low = 0
	if high is None:
		high = len(l) - 1

	if high < low:
		return -1

	midpoint = (low + high) // 2

	# we'll check if l[midpoint] == target, and if not, we can find out if
	# target will be to the left or right of midpoint
	# we know everything to the left of midpoint is smaller than the midpoint
	# and everything to the right is larger

	if l[midpoint] == target:
		return midpoint
	elif target < l[midpoint]:
		return binary_search(l, target, low, midpoint-1)
	else:
		return binary_search(l, target, midpoint+1, high)

if __name__ == '__main__':
	l = [1, 3, 5, 10, 12]
	target = 12
	print(binary_search(l, target))