#!/usr/bin/env python3

import math
from math import ceil
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

#Add queries here, in this format:

query1 = [[486,1], [184,2], [29,2], [31,2], [12,3], [51,3], [102,3], [13,4], [14,4], [15,4], [57,2], [378,2], [859,2], [185,3], [30,3], [37,3], [52,4], [142,4], [195,4], [875,2], [56,3], [66,3], [95,3], [462,4], [497,3], [858,3], [876,3], [879,3], [880,3]]
query2 = [[12,1], [486,1], [15,2], [184,2], [858,2], [51,3], [102,3], [202,3], [14,4], [52,4], [380,4], [746,1], [859,2], [948,2], [285,3], [390,3], [391,3], [442,4], [497,3], [643,3], [856,3], [857,3], [877,3], [864,3], [658,3]]
query8 = [[488,1], [236,3], [166,3]]
query10 = [[491,1], [99,2], [115,3], [257,3], [258,3]]
query23 = [[624,1], [86,2], [194,2], [650,2], [649,4], [652,2]]
query29 = [[463,1], [497,1], [462,3]]
query39 = [[271,1], [501,1], [16,2], [413,2], [414,3]]
query40 = [[68,1], [502,1]]
query51 = [[145,1], [511,1], [611,1], [376,2], [406,2], [565,2], [1076,2]]
query53 = [[512,1], [224,3], [279,3]]
query157 = [[640,1], [725,2], [728,2], [729,3], [911,3], [720,4], [75,4], [909,4]]
query225 = [[1076,1], [1062,1], [1077,3], [569,3], [572,3], [687,4], [655,3]]

#Add retrievec here
retrieve1 = [[184,2], [13,2], [51,3], [12,3], [1268,3], [878,0], [486,0], [875,0], [1361,0], [588,0]]
retrieve1STOP = [[184,0], [13,0], [12,0], [878,0], [51,0], [875,0], [486,0], [1268,0], [429,0], [195,0]]
retrieve1WHITE = [[13,0], [51,0], [184,0], [878,0], [1361,0], [429,0], [875,0], [1268,0], [486,0], [792,0]]

retrieve2 = [[12,0], [792,0], [51,0], [746,0], [1158,0], [875,0], [884,0],[700,0], [1089,0], [726,0] ]
retrieve2STOP = [[12,0], [51,0], [875,0], [884,0], [726,0], [746,0], [792,0], [429,0], [700,0], [1169,0]]
retrieve2WHITE = [[12,0], [792,0], [1158,0], [746,0], [875,0], [51,0], [700,0], [884,0], [1089,0], [429,0]]

retrieve8 = [[166,0], [1275,0], [1085,0], [1189,0], [1312,0], [1252,0], [317,0], [236,0], [185,0], [575,0]]
retrieve8STOP = [[166,0], [1085,0], [1275,0], [1312,0], [1189,0], [236,0], [378,0], [317,0], [914,0], [575,0]]
retrieve8WHITE = [[166,0], [1085,0], [1312,0], [1189,0], [1275,0], [1252,0], [1255,0], [378,0], [317,0], [1224,0]]

retrieve10 = [[257,0], [491,0], [148,0], [544,0], [315,0], [386,0], [558,0], [121,0], [817,0], [344,0]]
retrieve10STOP = [[491,0], [385,0], [386,0], [257,0], [271,0], [610,0], [1374,0], [142,0], [137,0], [418,0]]
retrieve10WHITE = [[257,0], [491,0], [315,0], [544,0], [558,0], [121,0], [651,0], [817,0], [861,0], [228,0]]

retrieve23 = [[624,0], [650,0], [1232,0], [1223,0], [649,0], [543,0], [324,0], [678,0], [39,0], [982,0]]
retrieve23STOP = [[624,0], [650,0], [1223,0], [1232,0], [649,0], [1164,0], [324,0], [86,0], [245,0], [592,0]]
retrieve23WHITE = [[624,0], [1232,0], [1223,0], [543,0], [324,0], [39,0], [650,0], [982,0], [1305,0], [602,0]]

retrieve29 = [[1099,0], [463,0], [1117,0], [462,0], [1096,0], [1097,0], [817,0], [1340,0], [553,0], [1065,0]]
retrieve29STOP = [[463,0], [1099,0], [1117,0], [817,0], [462,0], [1097,0], [1340,0], [1096,0], [553,0]]
retrieve29WHITE = [[1099,0], [463,0], [1117,0], [462,0], [1096,0], [1097,0], [817,0], [1340,0], [553,0], [1065,0]]

retrieve39 = [[502,0], [302,0], [68,0], [96,0], [1007,0], [538,0], [1011,0], [628,0], [1199,0], [1230,0]]
retrieve39STOP = [[502,0], [68,0], [302,0], [96,0], [271,0], [343,0], [429,0], [686,0], [628,0], [1007,0] ]
retrieve39WHITE = [[502,0], [302,0], [68,0], [1007,0], [429,0], [628,0], [343,0],[96,0], [538,0], [16,0]]

retrieve40 = [[16,0], [560,0], [413,0], [125,0], [306,0], [61,0], [322,0], [260,0], [962,0], [1212,0]]
retrieve40STOP = [[413,0], [254,0], [560,0], [348,0], [50,0], [140,0], [306,0], [81,0], [55,0], [980,0]]
retrieve40WHITE = [[16,0], [560,0], [413,0], [61,0], [322,0], [125,0], [980,0], [140,0], [306,0], [254,0]]

retrieve51 = [[382,0], [4,0], [629,0], [180,0], [3,0], [664,0], [96,0], [611,0], [348,0], [21,0]]
retrieve51STOP = [[382,0], [629,0], [4,0], [3,0], [611,0], [307,0], [348,0], [180,0], [568,0], [1282,0]]
retrieve51WHITE = [[382,0], [629,0], [180,0], [4,0], [348,0], [96,0], [611,0], [664,0], [3,0], [21,0]]

retrieve53 =  [[251,0], [367,0], [250,0], [1050,0], [893,0], [1048,0], [521,0], [36,0], [633,0], [677,0]]
retrieve53STOP = [[367,0], [752,0], [1050,0], [1048,0], [677,0], [250,0], [1362,0], [981,0], [451,0], [1023,0]]
retrieve53WHITE = [[251,0], [250,0], [1050,0], [367,0], [1048,0], [893,0], [521,0], [633,0], [36,0], [1124,0]]

retrieve157 = [[640,0], [909,0], [220,0], [725,0], [722,0], [883,0], [29,0], [345,0], [1039,0], [1360,0]]
retrieve157STOP = [[640,0], [909,0], [725,0], [883,0], [29,0], [220,0], [415,0], [1051,0], [1039,0], [137,0]]
retrieve157WHITE = [[640,0], [909,0], [725,0], [220,0], [29,0], [722,0],[883,0], [345,0], [1039,0], [1360,0]]

retrieve225 = [[671,0], [1225,0], [94,0], [547,0], [1062,0], [42,0], [678,0], [255,0], [339,0], [610,0]]
retrieve225STOP = [[671,0], [1225,0], [3,0], [547,0], [339,0], [696,0], [333,0], [76,0], [335,0], [324,0]]
retrieve225WHITE = [[671,0], [94,0], [1074,0], [42,0], [1225,0], [547,0], [1362,0], [749,0], [291,0], [1062,0]]


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
	if (basicPrecision(retrieved, relevant) + basicRecall(retrieved, relevant)) == 0:
		return 0
	else:
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

def RelationFix (retrieve1, query1):
	for i in range(len(retrieve1)):
		totalNo = 0
		for j in range(len(query1)):
			if retrieve1[i][0] == query1[j][0]:
				retrieve1[i][1] = query1[j][1]
			else:
				totalNo+=1
		if totalNo == len(query1):
			retrieve1[i][1] = 0
	return retrieve1

def DCG (retrieved, relevant):
	retrieved = RelationFix(retrieved, relevant)
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
	retrieved = RelationFix(retrieved, relevant)
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

def interpolated (retrieve1, query1, retrieve2, query2, retrieve3, query3, retrieve4, query4, retrieve5, query5, retrieve6, query6, retrieve7, query7, retrieve8, query8, retrieve9, query9, retrieve10, query10, retrieve11, query11, retrieve12, query12): #Add more query variables here

	interpolRecall = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

	totalQueries = 12 #Set the number of total queries present in the argument.

	# Add another line for each query

	interpol_1 = InterpolatedValues (retrieve1, query1)
	interpol_2 = InterpolatedValues (retrieve2, query2)
	interpol_3 = InterpolatedValues (retrieve3, query3)
	interpol_4 = InterpolatedValues (retrieve4, query4)
	interpol_5 = InterpolatedValues (retrieve5, query5)
	interpol_6 = InterpolatedValues (retrieve6, query6)
	interpol_7 = InterpolatedValues (retrieve7, query7)
	interpol_8 = InterpolatedValues (retrieve8, query8)
	interpol_9 = InterpolatedValues (retrieve9, query9)
	interpol_10 = InterpolatedValues (retrieve10, query10)
	interpol_11 = InterpolatedValues (retrieve11, query11)
	interpol_12 = InterpolatedValues (retrieve12, query12)

	numerator = [interpol_1[i] + interpol_2[i] + interpol_3[i] + interpol_4[i] + interpol_5[i] + interpol_6[i] + interpol_7[i] + interpol_8[i] + interpol_9[i] + interpol_10[i] + interpol_11[i] + interpol_12[i] for i in range(len(interpol_1))] #Add a new interpol_X[i]
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

def CombinedInterpolated (array1, array2, array3):
	interpolRecall = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

	plt.plot (interpolRecall, array1, color ='red',marker = 'o', label = 'Standard')
	plt.plot (interpolRecall, array2, color ='blue',marker = 'o', label = 'NoStopWords')
	plt.plot (interpolRecall, array3, color ='black',marker = 'o', label = 'Whitespace')

	plt.xlabel ('Recall')
	plt.ylabel ('Precision')
	plt.title ('Averaged 11-point Precision/Recall Graph for All Analyzers')
	plt.grid()
	plt.legend()
	plt.savefig('CombinedInterpolated.png')
	plt.show()

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
	if incr1 ==0:
		term1 = 0
	else:
		term1 = numer1 / incr1
	return term1

def MAP (retrieve1, query1, retrieve2, query2, retrieve3, query3, retrieve4, query4, retrieve5, query5, retrieve6, query6, retrieve7, query7, retrieve8, query8, retrieve9, query9, retrieve10, query10, retrieve11, query11, retrieve12, query12):
	totalQueries = 12

	term1 = MAPTerm (retrieve1, query1)
	term2 = MAPTerm (retrieve2, query2)
	term3 = MAPTerm (retrieve3, query3)
	term4 = MAPTerm (retrieve4, query4)
	term5 = MAPTerm (retrieve5, query5)
	term6 = MAPTerm (retrieve6, query6)
	term7 = MAPTerm (retrieve7, query7)
	term8 = MAPTerm (retrieve8, query8)
	term9 = MAPTerm (retrieve9, query9)
	term10 = MAPTerm (retrieve10, query10)
	term11 = MAPTerm (retrieve11, query11)
	term12 = MAPTerm (retrieve12, query12)

	mapValue = (term1 + term2 + term3 + term4 + term5 + term6 +term7 + term8 + term9 +term10 + term11 + term12) / totalQueries
	print (f"MAP: {mapValue}")

def FirstCorrectRank (retrieve1, query1):
	for i in range(len(retrieve1)):
		for j in range(len(query1)):
			if retrieve1[i][0] == query1[j][0]:
				return (i+1)
	return 0

def ZeroCheck (retrieve1, query1):
	num1 = FirstCorrectRank(retrieve1, query1)
	if num1 !=0:
		term1 = 1 / FirstCorrectRank(retrieve1, query1)
	else:
		term1 = 0
	return term1

def MRR (retrieve1, query1, retrieve2, query2, retrieve3, query3, retrieve4, query4, retrieve5, query5, retrieve6, query6, retrieve7, query7, retrieve8, query8, retrieve9, query9, retrieve10, query10, retrieve11, query11, retrieve12, query12):
	totalQueries = 12
	term1 = ZeroCheck (retrieve1, query1)
	term2 = ZeroCheck (retrieve2, query2)
	term3 = ZeroCheck (retrieve3, query3)
	term4 = ZeroCheck (retrieve4, query4)
	term5 = ZeroCheck (retrieve5, query5)
	term6 = ZeroCheck (retrieve6, query6)
	term7 = ZeroCheck (retrieve7, query7)
	term8 = ZeroCheck (retrieve8, query8)
	term9 = ZeroCheck (retrieve9, query9)
	term10 = ZeroCheck (retrieve10, query10)
	term11 = ZeroCheck (retrieve11, query11)
	term12 = ZeroCheck (retrieve12, query12)

	mrr = (term1 + term2 + term3 + term4 + term5 + term6 +term7 + term8 + term9 +term10 + term11 + term12) / totalQueries

	print (f"MRR: {mrr}")



def EVALUATE (retrieve1, query1):
	print(f"NDCG: {NDCG(retrieve1, query1)}")
	print(f"Recall: {basicRecall(retrieve1, query1)}")
	print(f"Precision: {basicPrecision(retrieve1, query1)}")
	print(f"F1: {F1(retrieve1, query1)}")


## Don't Delete, this is for potential problem debugging. 

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

#OUTPUT

## OUTPUT

#FOR STANDARD ANALYZER

print('***** STANDARD: ******')

#For Query1
print ('For Query1:')
EVALUATE(retrieve1, query1)
print('\n')

#For Query2
print ('For Query2:')
EVALUATE(retrieve2, query2)
print('\n')

#For Query3
print ('For Query8:')
EVALUATE(retrieve8, query8)
print('\n')

#For Query4
print ('For Query10:')
EVALUATE(retrieve10, query10)
print('\n')

#For Query5
print ('For Query23:')
EVALUATE(retrieve23, query23)
print('\n')

#For Query6
print ('For Query29:')
EVALUATE(retrieve29, query29)
print('\n')

#For Query7
print ('For Query39:')
EVALUATE(retrieve39, query39)
print('\n')

#For Query8
print ('For Query40:')
EVALUATE(retrieve40, query40)
print('\n')

#For Query9
print ('For Query51:')
EVALUATE(retrieve51, query51)
print('\n')

#For Query10
print ('For Query53:')
EVALUATE(retrieve53, query53)
print('\n')

#For Query11
print ('For Query157:')
EVALUATE(retrieve157, query157)
print('\n')

#For Query12
print ('For Query225:')
EVALUATE(retrieve225, query225)
print('\n')

#FOR NO STOPWORD ANALYZER
print('***** NO STOPWORD: ******')

#For Query1
print ('For Query1:')
EVALUATE(retrieve1STOP, query1)
print('\n')

#For Query2
print ('For Query2:')
EVALUATE(retrieve2STOP, query2)
print('\n')

#For Query3
print ('For Query8:')
EVALUATE(retrieve8STOP, query8)
print('\n')

#For Query4
print ('For Query10:')
EVALUATE(retrieve10STOP, query10)
print('\n')

#For Query5
print ('For Query23:')
EVALUATE(retrieve23STOP, query23)
print('\n')

#For Query6
print ('For Query29:')
EVALUATE(retrieve29STOP, query29)
print('\n')

#For Query7
print ('For Query39:')
EVALUATE(retrieve39STOP, query39)
print('\n')

#For Query8
print ('For Query40:')
EVALUATE(retrieve40STOP, query40)
print('\n')

#For Query9
print ('For Query51:')
EVALUATE(retrieve51STOP, query51)
print('\n')

#For Query10
print ('For Query53:')
EVALUATE(retrieve53STOP, query53)
print('\n')

#For Query11
print ('For Query157:')
EVALUATE(retrieve157STOP, query157)
print('\n')

#For Query12
print ('For Query225:')
EVALUATE(retrieve225STOP, query225)
print('\n')

#FOR WHITESPACE ANALYZER
print('***** WHITESPACE: ******')

#For Query1
print ('For Query1:')
EVALUATE(retrieve1WHITE, query1)
print('\n')

#For Query2
print ('For Query2:')
EVALUATE(retrieve2WHITE, query2)
print('\n')

#For Query3
print ('For Query8:')
EVALUATE(retrieve8WHITE, query8)
print('\n')

#For Query4
print ('For Query10:')
EVALUATE(retrieve10WHITE, query10)
print('\n')

#For Query5
print ('For Query23:')
EVALUATE(retrieve23WHITE, query23)
print('\n')

#For Query6
print ('For Query29:')
EVALUATE(retrieve29WHITE, query29)
print('\n')

#For Query7
print ('For Query39:')
EVALUATE(retrieve39WHITE, query39)
print('\n')

#For Query8
print ('For Query40:')
EVALUATE(retrieve40WHITE, query40)
print('\n')

#For Query9
print ('For Query51:')
EVALUATE(retrieve51WHITE, query51)
print('\n')

#For Query10
print ('For Query53:')
EVALUATE(retrieve53WHITE, query53)
print('\n')

#For Query11
print ('For Query157:')
EVALUATE(retrieve157WHITE, query157)
print('\n')

#For Query12
print ('For Query225:')
EVALUATE(retrieve225WHITE, query225)
print('\n')

#For All Queries:
print("For Standard Analyzer")
MAP(retrieve1, query1, retrieve2, query2, retrieve8, query8, retrieve10, query10, retrieve23, query23, retrieve29, query29, retrieve39, query39, retrieve40, query40, retrieve51, query51, retrieve53, query53, retrieve157, query157, retrieve225, query225)
MRR(retrieve1, query1, retrieve2, query2, retrieve8, query8, retrieve10, query10, retrieve23, query23, retrieve29, query29, retrieve39, query39, retrieve40, query40, retrieve51, query51, retrieve53, query53, retrieve157, query157, retrieve225, query225)

print("For No Stop Word Analyzer")
MAP(retrieve1STOP, query1, retrieve2STOP, query2, retrieve8STOP, query8, retrieve10STOP, query10, retrieve23STOP, query23, retrieve29STOP, query29, retrieve39STOP, query39, retrieve40STOP, query40, retrieve51STOP, query51, retrieve53STOP, query53, retrieve157STOP, query157, retrieve225STOP, query225)
MRR(retrieve1STOP, query1, retrieve2STOP, query2, retrieve8STOP, query8, retrieve10STOP, query10, retrieve23STOP, query23, retrieve29STOP, query29, retrieve39STOP, query39, retrieve40STOP, query40, retrieve51STOP, query51, retrieve53STOP, query53, retrieve157STOP, query157, retrieve225STOP, query225)

print("For Whitespace Analyzer")
MAP(retrieve1WHITE, query1, retrieve2WHITE, query2, retrieve8WHITE, query8, retrieve10WHITE, query10, retrieve23WHITE, query23, retrieve29WHITE, query29, retrieve39WHITE, query39, retrieve40WHITE, query40, retrieve51WHITE, query51, retrieve53WHITE, query53, retrieve157WHITE, query157, retrieve225WHITE, query225)
MRR(retrieve1WHITE, query1, retrieve2WHITE, query2, retrieve8WHITE, query8, retrieve10WHITE, query10, retrieve23WHITE, query23, retrieve29WHITE, query29, retrieve39WHITE, query39, retrieve40WHITE, query40, retrieve51WHITE, query51, retrieve53WHITE, query53, retrieve157WHITE, query157, retrieve225WHITE, query225)


#interpolated(retrieved, relevant, retrieved2, relevant2, retrieve6, query6)
array1 = interpolated(retrieve1, query1, retrieve2, query2, retrieve8, query8, retrieve10, query10, retrieve23, query23, retrieve29, query29, retrieve39, query39, retrieve40, query40, retrieve51, query51, retrieve53, query53, retrieve157, query157, retrieve225, query225)
array2 = interpolated(retrieve1STOP, query1, retrieve2STOP, query2, retrieve8STOP, query8, retrieve10STOP, query10, retrieve23STOP, query23, retrieve29STOP, query29, retrieve39STOP, query39, retrieve40STOP, query40, retrieve51STOP, query51, retrieve53STOP, query53, retrieve157STOP, query157, retrieve225STOP, query225)
array3 = interpolated(retrieve1WHITE, query1, retrieve2WHITE, query2, retrieve8WHITE, query8, retrieve10WHITE, query10, retrieve23WHITE, query23, retrieve29WHITE, query29, retrieve39WHITE, query39, retrieve40WHITE, query40, retrieve51WHITE, query51, retrieve53WHITE, query53, retrieve157WHITE, query157, retrieve225WHITE, query225)

CombinedInterpolated(array1, array2, array3)

