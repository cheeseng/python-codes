# This code uses genetic algorithm to find sequence of numbers with 
# arithematic operators in between so that result is closest to 'target'
# eg if target is 45 then 9*5 or 9*4+9 or 8*5+5 are exact matching strings
# while 8*5+4 is a close string

import GALib, re
expr_len = 44	# size of expression = 11, ie. max 6 digits and 5 operators
target = 120.27

def process(chromosome):
	# Break chromosome into 4 bit groups. 0-9 number and 10-15 operators
	lis = [chromosome[i:i+4] for i in range(0, len(chromosome), 4)]

	# Seperate numbers and operators
	isDigit = lambda x: int(x, 2) >= 0 and int(x, 2) <= 9
	isOp = lambda x: x in op

	# Create expression of number and operators
	rep =  ''.join(map(lambda x: isDigit(x) and str(int(x, 2)) or isOp(x)
	 and op[x] or 'X', lis))

	# Find valid expression
	lis2 = re.findall('((\d|\d\.\d)([\+\-\*\/]\d)+)', rep)
	return lis2

def myeval(expr):
	# Evaluate expression
	try:
		ans = eval(expr[0])
		err = abs(ans - target)
		ans = str(ans) + ', ' + expr[0]
		if err == 0:
			return 100, ans
		mywt = 50/err
		return mywt, ans
	except:
		return 0, 0
	
def optimize(chromosome):
	# Get chromosome weight
	wts = []
	lst = process(chromosome)
	for l in lst:
		w, val = myeval(l)
		wts.append(w)

	# Return maximum weight for this chromosome
	try:
		return max(wts)
	except:
		return 0

op = {'1010':'+',
	  '1011':'.',
	  '1100':'+',
	  '1101':'-',
	  '1110':'*',
	  '1111':'/'}

GALib.init(optimize, expr_len, no_of_iterations=200)
print "Target %.2f"%target
for i in range(10):
	
	lst = GALib.iterate()
	# Iterate returns list of tuples of chromosome and weight
	# Get chromosome with max weight(best in current lot)
	c = sorted(lst, key=lambda x: x[1])[-1][0]
	# Show corresponding expression
	print str(i+1),
	lst = process(c)
	for l in lst:
		print myeval(l)[1],
	print ''
