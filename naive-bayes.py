import argparse
import time
import math
import sys

def verify_naive_bayes(prob,
		       space,
		       plus,
		       haash,
		       digit):

	test = open(sys.argv[1], 'r')
	labels = open(sys.argv[2], 'r')

        '''print "Character count obtained from training"
        for w in range(10):
                print "Digit = ", w
                print "Digit count = ", digit[w]
                print "Space count = ", space[w][7][13]
                print "+ count = ", plus[w][7][13]
                print "# count = ", haash[w][7][13]
                print "==========================="'''

	#import pudb
	#pudb.set_trace()
	accuracy = 0
	error = [0 for j in xrange(10)]
	correct = [0 for j in xrange(10)]
	test_digit = [0 for j in xrange(10)]
	for w in range(1000):
		temp = labels.readline()
		val = int(temp)
		test_digit[val] = test_digit[val] + 1
		
		image = [[0 for j in xrange(29)] for i in xrange(29)]
		for i in range(28):
			image[i] = test.readline()

		#import pudb
		#pudb.set_trace()
		reference = float(-10000)
		this_digit = -1
		for indi_dig in range(10):
			#reference = -1000000
			prod = float(0)
			for i in range(28):
				q = len(image[i])
				if q != 29:
					print "Un-expected data in testing data !!!"
					sys.exit(1)
                        	#read file data
                        	for j in range(28):
					#print testline
					if image[i][j] == '+':
						#import pudb
						#pudb.set_trace()
						prod = prod + 0.5*math.log(plus[indi_dig][i][j]+1)
						prod = prod - 0.5*math.log(digit[indi_dig]+11)
					elif image[i][j] == '#':
						#import pudb
						#pudb.set_trace()
						prod = prod + math.log(haash[indi_dig][i][j]+1)
						prod = prod - math.log(digit[indi_dig]+11)

					elif image[i][j] == ' ':
						prod = prod + 0.5*math.log(space[indi_dig][i][j]+1)
						prod = prod - 0.5*math.log(digit[indi_dig]+11)
			
			prod = prod + math.log(digit[indi_dig])
			#prod = prod - math.log(5000, 2)
			#print "Probability of ",indi_dig,"is ",str(prod)
			if prod > reference:
				reference = prod
				this_digit = indi_dig

		if this_digit == val:
			accuracy = accuracy + 1
			correct[val] = correct[val] + 1
		else:	
			error[val] = error[val] + 1
			#print "mismatch !!!"
		#print "Actual value of digit is ", val
		#print "This data is classified as ", this_digit
		#print "==========================="

	print "========================"
        print "Correctly Classified:"
        print "============================================================"
        print "Digit            Correctly Classified		Percentage"
        print "===================================================================="

        for i in range(10):
		#print("%.2f" % round(a,2))
		t = float(correct[i])/test_digit[i]*100
                print i,"               ",correct[i],"				",round(t,2),"%"
        print "========================"

	'''print ""	
	print "Incorrectly classified:"
	print "============================================================"
	print "Digit		In-correct classified		Percentage"
	print "============================================================"
	for i in range(10):
		t = float(error[i])/test_digit[i]*100
		print i,"		",error[i],"				",round(t,2),"%"
	print "========================"'''

	print "Total accuracy in classifying data = ", float(accuracy)/10,"%"

def train_naive_bayes():

    	#Reading file
    	training = open("trainingimages.txt", 'r')
    	labels = open("traininglabels.txt", 'r')
	
    	prob = [[[0 for k in xrange(28)] for j in xrange(28)] for i in xrange(10)]
    	count_space = [[[0 for k in xrange(28)] for j in xrange(28)] for i in xrange(10)]
    	count_plus = [[[0 for k in xrange(28)] for j in xrange(28)] for i in xrange(10)]
    	count_hash = [[[0 for k in xrange(28)] for j in xrange(28)] for i in xrange(10)]
    	digit_count = [0 for k in xrange(10)]

	print "Training Naive-Bayes ..."
    	tic = time.clock()
    	for w in range(5000):
        	temp = labels.readline()
        	digit = int(temp)
        	#print "Digit = ", digit
        	digit_count[digit] = digit_count[digit] + 1

        	for i in range(28):
			train = training.readline()
	        	#read file data
		    	for j in range(28):
		        	if train[j] == ' ':
					count_space[digit][i][j] = count_space[digit][i][j] + 1
		        	elif train[j] == '+':
			        	count_plus[digit][i][j] = count_plus[digit][i][j] + 1
		        	elif train[j] == '#':
		            		count_hash[digit][i][j] = count_hash[digit][i][j] + 1
    	

    	toc = time.clock()
    	timeItr = toc - tic
	print "Training done in ",round(float(timeItr),2),"seconds"
	print ""
	print "Now checking testing data ..."
	tic = time.clock()
	verify_naive_bayes(prob,count_space,count_plus,count_hash,digit_count)
	toc = time.clock()
        timeItr = toc - tic
        print "Testing done in ",round(float(timeItr),2),"seconds"

	
def main():
	train_naive_bayes()

if __name__ == "__main__":
	#parser = argparse.ArgumentParser(description="HomeWork Five")
	#parser.add_argument("--input", type=str)
	#parser.add_argument("--flag", type = int)
	#args = parser.parse_args()
	main()

