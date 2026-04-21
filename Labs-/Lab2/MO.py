from logic import *

P = Symbol("P") 
Q = Symbol("Q")

knowledge = Implication(
            And(P, Q), Or(P, Not(Q)))

print(model_check(knowledge, knowledge))