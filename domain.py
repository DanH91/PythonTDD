#!/usr/bin/env python
#classes file 

class MathFunction: 
        
    def __init__(self, lbd = 0): 
        self.fct = lbd;
        self.action = "calcul";
        
    def applyAction(self):
        return self.action;

    def execute(self, v):
        return self.fct(v);

#raw_input()
