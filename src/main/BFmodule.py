# -*- coding:utf-8 -*-
'''
Created on 8 de dez de 2017

@author: Israël & Renan
'''
from parsers.parsing import *
class BF:
    def __init__(self,graph,origin):
        self.G=graph
        self.d={}
        self.p={}
        self.o=origin
        self.caminho=[]
    
    def relax(self,u,v,p):
        if self.d[v]>self.d[u]+p:
            self.d[v]=self.d[u]+p
            self.p[v]=u
    
    def encontrado(self,i):
        if i in self.p:
            return self.encontrado(self.p[i])+[i]
        return []
       
    def single_source(self):
        for g in self.G.keys():
            if g!=self.o:
                self.d[g]=1000
            else:
                self.d[g]=0
    
    def begin(self):
        self.single_source()
        for _ in range(len(self.G.keys())-1):
            for u,adj in self.G.items():
                for v,p in adj.items():
                    self.relax(u, v, p)
        for u,adj in self.G.items():
            for v,p in adj.items():
                if self.d[v]>self.d[u]+p:
                    return False
        return True
 
filename=input("Escolha o arquivo do grafo:")   
p=Parser("../../"+filename)
g=p.get_list()
inicial=input("Vértice inicial")
b=BF(g,inicial)
v=[x for x in g.keys()]
if b.begin():
    print("Tem solução: ",b.begin())
    print([inicial]+b.encontrado(v[-1]))
else:
    print("Sem solução")