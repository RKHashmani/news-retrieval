#!/usr/bin/env python3

import math
from math import ceil
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

#relevant = [[20,2], [56,3], [57,3], [58,3], [19,4]]
#retrieved = [[3,0], [20,2], [56,3], [57,3], [58,3], [19,4], [1,0], [300,0]]

# For testing Recall/Prec plots
#relevant = [[1,2], [4,3], [6,3], [9,3], [14,4], [17,0], [19,2], [21,3], [23,3], [29,3], [36,4], [37,0], [38,0]]
#retrieved = [[22,2], [4,3], [36,3], [39,3], [38,4], [6,0], [24,2], [15,3], [23,3], [14,3], [19,4], [18,0], [20,0], [8,0], [1,0]]

# For Testing NDCG:
relevant = [[1,3], [2,3], [3,3], [4,2], [5,2], [6,1], [7,1], [8,0], [9,0], [10,0]]
retrieved = [[5,2], [2,3], [1,3], [10,0], [6,1], [4,2], [7,1], [9,0], [3,3], [8,0]]


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
				largest = max(slicedPrec);
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




#print(f"Recall: {basicRecall(retrieved, relevant)}")
#print(f"Precision: {basicPrecision(retrieved, relevant)}")
#print(f"F1: {F1(retrieved, relevant)}")

#print(f"Recall Table: {RecallTable(retrieved, relevant)}")
#print(f"Precision Table: {PrecTable(retrieved, relevant)}")
#print(len(PrecTable(retrieved,relevant)))

#PlotPrecRecall(retrieved, relevant)
#InterpolatedValues(retrieved,relevant)
#PlotInterpol(retrieved, relevant)

print(f"DCG: {DCG(retrieved, relevant)}")
print(f"IDCG: {IDCG(retrieved, relevant)}")
print(f"NDCG: {NDCG(retrieved, relevant)}")
