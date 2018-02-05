#!/usr/bin/env python
#Reduce function for computing matrix multiply A*B

#Input arguments:
#variable n should be set to the inner dimension of the matrix product (i.e., the number of columns of A/rows of B)

import sys
import string
import numpy

#number of columns of A/rows of B
n = int(sys.argv[1]) 

#Create data structures to hold the current row/column values (if needed; your code goes here)
a={}  
b={}  


currentkey = None

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

	#Remove leading and trailing whitespace
	line = line.strip()

	#Get key/value 
	key,v0,v1,v2 = line.split('\t',3)

	#Parse key/value input (your code goes here)
	v1=int(v1)
	v2=float(v2)
	


	#If we are still on the same key...
	if key==currentkey:

		#Process key/value pair (your code goes here)
		if v0=='A':
			a[(key,v1)]=v2
		else:
			b[(key,v1)]=v2


	#Otherwise, if this is a new key...
	else:
		s=0.0;
		#If this is a new key and not the first key we've seen
		if currentkey:
			#compute/output result to STDOUT (your code goes here)
			for i in range(0,n): 
				s=s+(a[(currentkey,i)]*b[(currentkey,i)])
				#s[int(currentkey)]=s[int(currentkey)]+(a[(intcurrentkey,i)]*b[(currentkey,i)])
			print "(%c, %c), %f" % (currentkey[0],currentkey[1],s)


	
		currentkey = key
			
		#Process input for new key (your code goes here)
		if v0=='A':
			a[(key,v1)]=v2
		else:
			b[(key,v1)]=v2




#Compute/output result for the last key (your code goes here)
s=0.0;
for i in range(0,n): 
	s=s+(a[(currentkey,i)]*b[(currentkey,i)])
print "(%c, %c), %f" % (currentkey[0],currentkey[1],s)



