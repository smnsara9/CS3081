from logic import *

rain = Symbol("rain") # it is reining
hagrid = Symbol("hagrid")
dumbledore = Symbol("dumbledore")

stentence = And(rain,hagrid)

print(stentence.formula())

knowledge = And(
Implication(Not(rain), hagrid),
Or(hagrid,dumbledore),
Not(And(hagrid,dumbledore)),
dumbledore)
print(knowledge.formula())