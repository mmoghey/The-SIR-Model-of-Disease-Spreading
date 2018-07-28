import snap
import numpy as np
import random
import matplotlib.pyplot as plt
import sets
from sets import Set
import scipy
from scipy import stats
from collections import Counter

iterations = 100

def SIR(Graph, I, beta, delta):
	n = Graph.GetNodes()
	S = set()
	for NI in Graph.Nodes():
		if NI.GetId() not in I:
			S.add( NI.GetId())
		
	R = set()
	
	
	while len(I)!= 0:
		# nodes no longer susceptible after current iteration
		Sprime = set()
		# newly infected nodes after current iteration
		Iprime = set()
		# nodes no longer infected after current iteration	
		Jprime = set()
		# newly recovered nodes after current iteration
		Rprime = set()

		for NI in Graph.Nodes():
			id = NI.GetId()
			if id in S:
				deg = NI.GetDeg()
				for i in range(deg):
					nbrId = NI.GetNbrNId(i)
					if nbrId in I:
						r = random.random()
						if r < beta:
							Sprime.add(id)
							Iprime.add(id)
		
			elif id in I:
				r = random.random()
				if r < delta:
					Jprime.add(id)
					Rprime.add(id)
					
		S.difference_update(Sprime)
		I.update(Iprime)
		I.difference_update(Jprime)
		R.update(Rprime)
	
	Ipercent = len(R) / (1.0* n)
	
	#print (len(R), n)
	return Ipercent
	 
				
def Q1_2(Graph1, Graph2):					   
	e1 = 0
	e2 = 0
	avg1 = 0
	avg2 = 0
	avg1_cond = 0
	avg2_cond = 0 

	n = Graph1.GetNodes()
	for i in range(iterations):
		I = set()
		# initialize infected node with randomnode number
		randNode = random.randint(1, n+1)
		I.add(randNode)
		ipercent1 = SIR(Graph1, I, 0.05, 0.5)
		avg1 += ipercent1
		if (ipercent1 >= 0.5):
			avg1_cond += ipercent1
			e1 += 1

		I = set()
		# initialize infected node with randomnode number
		I.add(randNode) 
		ipercent2 = SIR(Graph2, I, 0.05, 0.5)
		avg2 += ipercent2

		if (ipercent2 >= 0.5):
			avg2_cond += ipercent2
			e2 += 1
	
	print ("#################### Q1.2 #############################")
	print ("portion of simulation with infected atleast > 50%")
	print ("Event Epidemic Erdos Renyi Graph: ", e1/(1.0 * iterations))
	print ("Mean proportion infected for Erdos Renyi Graph (without condition) " , avg1 / (1.0 * iterations) )
	print ("Mean proportion infected for Erdos Renyi Graph (with condition) " , avg1_cond / (1.0 * e1) )
	print ("Event Epidemic Preferrential Attachment Graph: ", e2/(1.0 * iterations))
	print ("Mean proportion infected for Preferrential Attachment Graph (without condition) " , avg2 / (1.0 * iterations) )
	print ("Mean proportion infected for Preferrential Attachment Graph (with condition) " , avg2_cond / (1.0 * e2) )
	chi2, p, _, _ = scipy.stats.chi2_contingency([[e1, 100-e1],[e2, 100-e2]])
	print ("Chi square value: ", chi2, " p value: ", p)

	
def Q1_3(Graph1, Graph2):
	e1 = 0
	e2 = 0
	avg1_cond, avg1 = 0,0
	avg2, avg2_cond = 0, 0 

	n = Graph1.GetNodes()
	for i in range(iterations):
		I = set()
		# initialize infected node with randomnode number
		node =	snap.GetMxDegNId(Graph1)
		I.add(node)
   
		ipercent1 = SIR(Graph1, I, 0.05, 0.5)
		avg1 += ipercent1
		if (ipercent1 >= 0.5):
			avg1_cond += ipercent1
			e1 += 1

		I = set()
		# initialize infected node with randomnode number
		node =	snap.GetMxDegNId(Graph2)
		I.add(node)
		ipercent2 = SIR(Graph2, I, 0.05, 0.5)
		avg2 += ipercent2
		if (ipercent2 >= 0.5):
			avg2_cond += ipercent2
			e2 += 1
   
	print ("#################### Q1.3 #############################")
	print ("portion of simulation with infected with highest degree atleast > 50%")
	print ("Event Epidemic Erdos Renyi Graph: ", e1/(1.0 *iterations))
	print ("Mean proportion infected for Erdos Renyi Graph (without condition) " , avg1 / (1.0 * iterations) )
	print ("Mean proportion infected for Erdos Renyi Graph (with condition) " , avg1_cond / (1.0 * e1) )
	print ("Event Epidemic Preferrential Attachment Graph: ", e2/(1.0 * iterations))
	print ("Mean proportion infected for Preferrential Attachment Graph (without condition) " , avg2 / (1.0 * iterations) )
	print ("Mean proportion infected for Preferrential Attachment Graph (with condition) " , avg2_cond / (1.0 * e2) )




	
def Q1_5_1(Graph1, Graph2):
	e1 = 0
	e2 = 0
	avg1, avg1_cond = 0, 0 
	avg2, avg2_cond = 0, 0 

	n = Graph1.GetNodes()
	for i in range(iterations):
		I = set()
		# initialize infected node with 10 random nodes 
		cnt = 0
		while cnt < 10:
			randNode = random.randint(1, n+1)
			if randNode not in I:
				I.add(randNode)
				cnt+= 1		
   
		ipercent1 = SIR(Graph1, I, 0.05, 0.5)
		avg1 += ipercent1
		if (ipercent1 >= 0.5):
			e1 += 1
			avg1_cond += ipercent1

		I = set()
		# initialize infected node with 10 random nodes 
		cnt = 0
		while cnt < 10:
			randNode = random.randint(1, n+1)
			if randNode not in I:
				I.add(randNode)
				cnt+= 1	  
		ipercent2 = SIR(Graph2, I, 0.05, 0.5)
		avg2 += ipercent2
		if (ipercent2 >= 0.5):
			e2 += 1
			avg2_cond += ipercent2
	
  
	print ("#################### Q1.5 #############################")
	print ("portion of simulation atleast > 50% with infected set to be 10 random nodes ")
	print ("Event Epidemic Erdos Renyi Graph: ", e1/(1.0 * iterations))
	print ("Mean proportion infected for Erdos Renyi Graph (without condition) " , avg1 / (1.0 * iterations) )
	print ("Mean proportion infected for Erdos Renyi Graph (with condition) " , avg1_cond / (1.0 * e1) )
	print ("Event Epidemic Preferrential Attachment Graph: ", e2/(1.0 * iterations))
	print ("Mean proportion infected for Preferrential Attachment Graph (without condition) " , avg2 / (1.0 * iterations) )
	print ("Mean proportion infected for Preferrential Attachment Graph (with condition) " , avg2_cond / (1.0 * e2) )

def Q1_5_2(Graph1, Graph2):
	e1 = 0
	e2 = 0
	avg1, avg2 = 0,0
	avg1_cond, avg2_cond = 0,0 
	
	n = Graph1.GetNodes()
	for i in range(iterations):
		result_dict = dict()
		I = set()
		# initialize infected node with randomnode number
		for NI in Graph1.Nodes():
			result_dict[NI.GetId()] = NI.GetDeg()
			
		result = dict(Counter(result_dict).most_common(10))
				
		for key, value in result.iteritems():
			I.add(key)
			
		ipercent1 = SIR(Graph1, I, 0.05, 0.5)
		avg1 += ipercent1
		if (ipercent1 >= 0.5):
			avg1_cond += ipercent1
			e1 += 1

		I = set()
		# initialize infected node with randomnode number
		result_dict = dict()
		for NI in Graph2.Nodes():
			result_dict[NI.GetId()] = NI.GetDeg()
			
		result = dict(Counter(result_dict).most_common(10))
				
		for key, value in result.iteritems():
			I.add(key)
				
		ipercent2 = SIR(Graph2, I, 0.05, 0.5)
		avg2 += ipercent2	
		if (ipercent2 >= 0.5):
			avg2_cond += ipercent2
			e2 += 1
  
	print ("#################### Q1.5 #############################")
	print ("portion of simulation atleast > 50% with infected set to be 10 random nodes ")
	print ("Event Epidemic Erdos Renyi Graph: ", e1/(1.0 * iterations))
	print ("Mean proportion infected for Erdos Renyi Graph (without condition) " , avg1 / (1.0 * iterations) )
	print ("Mean proportion infected for Erdos Renyi Graph (with condition) " , avg1_cond / (1.0 * e1) )
	print ("Event Epidemic Preferrential Attachment Graph: ", e2/(1.0 * iterations))
	print ("Mean proportion infected for Preferrential Attachment Graph (without condition) " , avg2 / (1.0 * iterations) )
	print ("Mean proportion infected for Preferrential Attachment Graph (with condition) " , avg2_cond / (1.0 * e2) )

		
	

def main():
						
	Graph1 = snap.LoadEdgeList(snap.PUNGraph, "C:\Users\manas\Documents\eBooks\Advanced Databases\HomeWork4\SIR_erdos_renyi.txt", 0, 1)		
	Graph2 = snap.LoadEdgeList(snap.PUNGraph, "C:\Users\manas\Documents\eBooks\Advanced Databases\HomeWork4\SIR_preferential_attachment.txt", 0, 1)
	
	#Q1_2(Graph1, Graph2)

	#Q1_3(Graph1, Graph2)
	Q1_5_1(Graph1, Graph2)
	Q1_5_2(Graph1, Graph2)
	

main()
	
	