#!/usr/bin/python
# -*- coding: utf-8 -*-

R1 = raw_input("Was ist das Ergebnis des Tests? \n>>")
C1 = raw_input("Was war die Voraussetzung, deren Wahrscheinlichkeit du willst? \n>>")

p_a = input("Wahrscheinlichkeit fuer %r, bevor du testest? \n>>" %C1)
p_b_a = input("Wahrscheinlichkeit fuer %r wenn %r ? \n" %(R1,C1))
p_b_a2 = input("Wahrscheinlichkeit fuer %r wenn %r NICHT vorliegt? \n>>" %(R1,C1))
p_a2 = 1.0-p_a
p_b =  (p_b_a*p_a)+(p_b_a2*p_a2) #Die Summe aller Ergebnisse X.
p_b2 = 1 - p_b

def Bayes(p_a, p_b, p_b_a):
	p_a_b = (float(p_b_a) * float(p_a)) / float(p_b) # hier passiert die Magie ;)
	return p_a_b

print "Wahrscheinlichkeit fuer \n%r\nbei\n%r\n: %r. \n" %(C1,R1,Bayes(p_a,p_b,p_b_a))
