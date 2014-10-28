import pdb

def add_one(num):
	result = num + 1 # set breakpoint here : b 4, checking result
	print result
	return result

def main():
	pdb.set_trace()
	for num in xrange(0, 10):
		add_one(num) # set breaskpoint here : b 11, checking num = num +1

if __name__ == "__main__":
	main()