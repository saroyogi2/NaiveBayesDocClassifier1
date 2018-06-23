# -*- coding: utf-8 -*-

from __future__ import division
import sys
import pdb
from collections import defaultdict
import pandas as pd


#Step 1
#Calculate Prior Probabilities

class Prior():
    def __init__(self,labels):
        self.labels = labels
    def calcPrior(self):
        labels = self.labels
        classLabels = list(set(labels))
        probLabels ={}
        for i in classLabels:
            prob = labels.count(i)/len(labels)
            probLabels[i] =  prob            
        return probLabels

#Step 2
#Calculate Likelihood
class Likely():
    def __init__(self,Docs,labels,train_Content,prob):
        self.prob = prob
        self.train_Content = train_Content
        self.Docs = Docs
        self.labels = labels

    # Number of Total Unique Words in All Documents    

    def totwordcount(self):
        train_Content = self.train_Content
        totwordcnt = len(list(set(" ".join(train_Content).split(" "))))
        return totwordcnt

    # Total Words in each Document Class

    def labwordcount(self):
        ilist=[]
        clist = []
        train_Content = self.train_Content
        prob = self.prob
        labels = self.labels
        dataset = zip(train_Content,labels)
        classLabels = list(set(labels))
        for i in classLabels:
            klist=[]            
            for k,v in dataset:
                if i == v:
                    if klist != []:
                        klist += len(k.split(" "))                        
                    else:
                        klist = len(k.split(" "))                        
            ilist.append(i)
            clist.append(klist)
        return ilist,clist        

    
class createDF():
    def __init__(self,train_Content,test_Content,Labels):
        self.train_Content = train_Content
        self.test_Content = test_Content
        self.Labels = Labels
    
    #Calculate the number of words on each documents classes

    def termFreq(self):
        train_Content = self.train_Content
        test_Content = self.test_Content
        Labels = self.Labels
        corpus = " ".join(train_Content+test_Content)
        uniWords = list(set(corpus.split(" ")))
        result= {}
        for i in range (0, len(uniWords)):
            presdict = zip(train_Content,Labels)
            for k,v in presdict:
                if uniWords[i] in k:
                    if result.has_key((v,uniWords[i])):
                        cnt = k.count(uniWords[i])
                        result[v,uniWords[i]] += cnt                        
                    else:
                        cnt = k.count(uniWords[i])
                        result[v,uniWords[i]] = cnt                        
                else:
                    if result.has_key((v,uniWords[i])):
                        if uniWords[i] in k:
                            result[v,uniWords[i]] += 1
                        else:
                            result
                    else:
                        result[v,uniWords[i]] = 0                    
        return result

    
#Calculate Conditional Probability for words on Documents

class Conditional:
    def __init__(self,termfreqdict):
        self.termfreqdict = termfreqdict


    def condProb(self):
        termfreqdict = self.termfreqdict
        countComputer = []
        countAuto = []
        countSports = []
        compute= {}
        for k,v in termfreqdict.iteritems():
            if k[0] == 'Computer':
                for e,f in LabWordCnt.iteritems():
                    if e == 'Computer':
                        lab1cnt = f
                countComputer.append((k,v))
                if compute.has_key(k):
                    pass
                else:
                    compute[k] = (v + 1)/(lab1cnt+totWordCnt)
            elif k[0] == 'Auto':
                for e,f in LabWordCnt.iteritems():
                    if e == 'Auto':
                        lab1cnt = f
                countAuto.append((k,v))
                if compute.has_key(k):
                    pass
                else:
                    compute[k] = (v + 1)/(lab1cnt+totWordCnt)
            elif k[0] == 'Sports':
                for e,f in LabWordCnt.iteritems():
                    if e == 'Sports':
                        lab1cnt = f
                countSports.append((k,v))
                if compute.has_key(k):
                    pass
                else:
                    compute[k] = (v + 1)/(lab1cnt+totWordCnt)
            else:
                pass
        return compute


    def docScore(self,MBdict):
        Docscore = {}
        for m in Labelsset:        
            for x,y in PriorProb.iteritems():
                if m == x:
                    problist = []
                    testtext = D6.split(" ")
                    for u in testtext:
                        problist.append(MBdict[m,u])
                    score = reduce((lambda x, y: x * y), problist)*y
                    if Docscore.has_key((D6,m)):
                        pass
                    else:
                        Docscore[D6,m] =  score    
        return Docscore

        

if __name__ == '__main__':
    

    Docs = ['D1','D2','D3','D4','D5']
    Labels = ['Auto','Auto','Sports','Sports','Computer']
    Labelsset = list(set(Labels))
    train_Content = ['Saturn Dealer\'s Car', 
                'Toyota Car Tercel',
                'Baseball Game Play',
                'Pulled Muscle Game',
                'Colored GIFs Root']

    test_Content = ['Home Runs Game',
                    'Car Engine Noises']

    
    P1 = Prior(Labels)
    PriorProb = P1.calcPrior()
    P2 = Likely(Docs,Labels,train_Content,PriorProb)
    totWordCnt = P2.totwordcount()
    Ilist,Klist = P2.labwordcount()
    LabWordCnt = dict(zip(Ilist,Klist))
    
   

    C1 = createDF(train_Content,test_Content,Labels)
    TermFreqDict = C1.termFreq()


    C2 = Conditional(TermFreqDict)
    MultiBayes = C2.condProb()    

    # step 3: Evaluation of the Document
    # D6 = 'Car Engine Noises'
    # D6 = 'Home Runs Game'
    D6 = input("Enter a Document:")
    DocSqore = C2.docScore(MultiBayes)
    print DocSqore
    

    