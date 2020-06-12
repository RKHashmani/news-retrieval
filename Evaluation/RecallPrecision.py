#!/usr/bin/env python3

import math
from math import ceil
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

#Add queries here, in this format:


#query7 = [[20,2], [56,3], [57,3], [58,3], [19,4]]
#retrieve7 = [[3,0], [20,2], [56,3], [57,3], [58,3], [19,4], [1,0], [300,0]]

query6 = [[99,2], [115,3], [257,3], [258,3]]
retrieve6 = [[99,2], [20,2], [115,3], [257,3], [58,3], [19,4], [1,0], [300,0]]



# For testing Recall/Prec plot. Ignore:
relevant = [[1,2], [4,3], [6,3], [9,3], [14,4], [17,0], [19,2], [21,3], [23,3], [29,3], [36,4], [37,0], [38,0]]
retrieved = [[22,2], [4,3], [36,3], [39,3], [38,4], [6,0], [24,2], [15,3], [23,3], [14,3], [19,4], [18,0], [20,0], [8,0], [1,0]]

relevant2 = [[5,2], [15,3], [25,3], [36,3]]
retrieved2 = [[25,2], [12,3], [4,3], [5,3], [13,4], [16,0], [35,2], [32,3], [28,3], [17,3], [21,4], [15,0], [23,0], [36,0], [1,0]]



# For Testing NDCG:
#relevant = [[1,3], [2,3], [3,3], [4,2], [5,2], [6,1], [7,1], [8,0], [9,0], [10,0]]
#retrieved = [[5,2], [2,3], [1,3], [10,0], [6,1], [4,2], [7,1], [9,0], [3,3], [8,0]]


def RetrieveCheck (retrieved, relevant):
	for i in range(len(retrieved)):
		totalNo = 0
		for j in range(len(relevant)):
			if retrieved[i][0] == relevant[j][0]:
				print ('Match for %d' %i)
			else:
				totalNo+=1
		if totalNo == len(relevant):
				print ('No Match for %d' %i)

def basicRecall (retrieved, relevant):
	totalRet = 0.0
	for i in range(len(retrieved)):
		for j in range(len(relevant)):
			if retrieved[i][0] == relevant[j][0]:
				totalRet +=1
	return totalRet / float (len(relevant))

def basicPrecision (retrieved, relevant):
	totalRet = 0.0
	for i in range(len(retrieved)):
		for j in range(len(relevant)):
			if retrieved[i][0] == relevant[j][0]:
				totalRet +=1
	return totalRet / float (len(retrieved))

def F1(retrieved, relevant):
	return (2 * basicPrecision(retrieved, relevant) * basicRecall(retrieved, relevant)) / (basicPrecision(retrieved, relevant) + basicRecall(retrieved, relevant))

def RecallTable (retrieved, relevant):
	recallK = []
	matched = 0
	for i in range(len(retrieved)):
		totalChecked = 0
		for j in range(len(relevant)):
			if retrieved[i][0] == relevant[j][0]:
				matched += 1
				recallK.append(matched / len(relevant))
			else:
				totalChecked += 1
		if totalChecked == len(relevant):
			recallK.append(matched / len(relevant))
	return recallK

def PrecTable (retrieved, relevant):
	precK = []
	matched = 0
	for i in range(len(retrieved)):
		totalChecked = 0
		for j in range(len(relevant)):
			if retrieved[i][0] == relevant[j][0]:
				matched += 1
				precK.append(matched / (i+1))
			else:
				totalChecked += 1
		if totalChecked == len(relevant):
			precK.append(matched / (i+1))
	return precK

def extendWith0 (recall, precision):
	if recall[-1] < 1:
		a = ceil(recall[-1]*10)/10
		recall.append(a)
		while recall[-1] < 1:
			b = recall[-1] + 0.1
			b = round(b,1)
			recall.append(b)
	#print (recall)

	return recall, precision + [0]*(len(recall) - len(precision))

def PlotPrecRecall (retrieved, relevant):
	recall = RecallTable(retrieved, relevant)
	precision = PrecTable(retrieved, relevant)

	recall, precision = extendWith0 (recall, precision)
	
	plt.plot (recall, precision)
	plt.xlabel ('Recall')
	plt.ylabel ('Precision')
	plt.grid()
	plt.legend()
	plt.savefig('test.png')
	plt.show()

def InterpolatedValues (retrieved, relevant):
	interpolRecall = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
	interpolPrec = []

	recall = RecallTable(retrieved, relevant)
	precision = PrecTable (retrieved, relevant)
	recall, precision = extendWith0 (recall, precision)

	for i in range(len(interpolRecall)):
		largestTotal = 0
		for j in range(len(recall)):
			if recall[j] >= interpolRecall[i]:
				slicedPrec = precision[j:len(precision)]
				largest = max(slicedPrec)
				if largest > largestTotal:
					largestTotal = largest

		interpolPrec.append(largestTotal)

	return interpolPrec

def PlotInterpol (retrieved, relevant):
	interpolRecall = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
	interpolPrecision = InterpolatedValues (retrieved, relevant)
	#print (interpolPrecision)

	plt.plot (interpolRecall, interpolPrecision, marker = 'o')
	plt.xlabel ('Recall')
	plt.ylabel ('Precision')
	plt.grid()
	plt.legend()
	plt.savefig('Interpolated.png')
	plt.show()

def DCG (retrieved, relevant):
	dcg = retrieved[0][1]

	if len(retrieved) < len(relevant):
		length = len(retrieved)
	else:
		length = len(relevant)

	for i in range(length-1):
		i+=1
		dcg += retrieved[i][1] / math.log(i+1,2)

	return dcg

def IDCG (retrieved, relevant):
	idcg = relevant[0][1]

	if len(retrieved) < len(relevant):
		length = len(retrieved)
	else:
		length = len(relevant)

	for i in range(length-1):
		i+=1
		idcg += relevant[i][1] / math.log(i+1,2)
		
	return idcg

def NDCG (retrieved, relevant):
	return DCG(retrieved, relevant) / IDCG(retrieved, relevant)

def interpolated (retrieve1, query1, retrieve2, query2, retrieve3, query3): #Add more query variables here

	interpolRecall = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

	totalQueries = 3 #Set the number of total queries present in the argument.

	# Add another line for each query
	interpol_1 = InterpolatedValues(retrieve1, query1)
	interpol_2 = InterpolatedValues(retrieve2, query2)
	interpol_3 = InterpolatedValues(retrieve3, query3)

	numerator = [interpol_1[i] + interpol_2[i] + interpol_3[i] for i in range(len(interpol_1))] #Add a new interpol_X[i]
	averaged = [numerator[i] / totalQueries for i in range(len(interpol_1))]
	
	plt.plot (interpolRecall, averaged, marker = 'o')
	plt.xlabel ('Recall')
	plt.ylabel ('Precision')
	plt.title ('Averaged 11-point Precision/Recall Graph for Standard Analyzer')
	plt.grid()
	plt.legend()
	plt.savefig('AveragedInterpolated.png')
	plt.show()

	return averaged

def MAPTerm (retrieve1, query1):
	recTable1 = RecallTable(retrieve1, query1)
	precTable1 = PrecTable(retrieve1, query1)

	numer1 = 0
	incr1 = 0

	if recTable1[0] != 0:
		incr1 += 1
		numer1 += precTable1[0]
		for i in range(len(recTable1) -2):
			i+= 2
			if recTable1[i] > recTable1[i-1]:
				incr1 += 1
				numer1 += precTable1[i]

	else:
		for i in range(len(recTable1) -1):
			i+= 1
			if recTable1[i] > recTable1[i-1]:
				incr1 += 1
				numer1 += precTable1[i]

	term1 = numer1 / incr1
	return term1

def MAP (retrieve1, query1, retrieve2, query2):
	totalQueries = 2

	term1 = MAPTerm (retrieve1, query1)
	term2 = MAPTerm (retrieve2, query2)

	mapValue = (term1 + term2) / totalQueries
	print (f"MAP: {mapValue}")



## Don't Delete, this is for potential probelm debugging. 

#print(f"Recall: {basicRecall(retrieved, relevant)}")
#print(f"Precision: {basicPrecision(retrieved, relevant)}")
#print(f"F1: {F1(retrieved, relevant)}")

#print(f"Recall Table: {RecallTable(retrieved, relevant)}")
#print(f"Precision Table: {PrecTable(retrieved, relevant)}")
#print(len(PrecTable(retrieved,relevant)))

#PlotPrecRecall(retrieved, relevant)
#print(f"Interpolated Precision: {InterpolatedValues(retrieved2, relevant2)}")
#PlotInterpol(retrieved, relevant)

#print(f"DCG: {DCG(retrieved, relevant)}")
#print(f"IDCG: {IDCG(retrieved, relevant)}")
#print(f"NDCG: {NDCG(retrieved, relevant)}")

#print (RecallTable(retrieved, relevant))
MAP(retrieved, relevant, retrieved2, relevant2)

'''
## OUTPUT

#For Query1
print ('For Query1:')

print(f"NDCG: {NDCG(retrieved, relevant)}")
print(f"Recall: {basicRecall(retrieved, relevant)}")
print(f"Precision: {basicPrecision(retrieved, relevant)}")
print(f"F1: {F1(retrieved, relevant)}")
print('\n')

#For Query2
print ('For Query2:')

print(f"NDCG: {NDCG(retrieved2, relevant2)}")
print(f"Recall: {basicRecall(retrieved2, relevant2)}")
print(f"Precision: {basicPrecision(retrieved2, relevant2)}")
print(f"F1: {F1(retrieved2, relevant2)}")
print('\n')


interpolated(retrieved, relevant, retrieved2, relevant2, retrieve6, query6)
'''
