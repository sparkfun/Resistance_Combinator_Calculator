import math
import itertools

#5 Set values of resistors 
#Add a 6th value to resistor array if you add a custom resistor. You can then
#uncomment the code that is precluded by "Uncomment for sixth resistor" to
#calculate all combinations of values.
resistorArr = [11000, 2200, 2000, 4700, 170000]
letterEquiv = ["A", "B", "C", "D", "E"]

#Parallel resistance formula
def calculate_resistance(*args):
    totalResistance = 0 
    for arg in args:
        totalResistance += 1/arg 
    finalRes = (1/totalResistance)
    return finalRes

#Let's see the list of all combination of resistors. 
print("\n---------Lists of all combinations of Resistors-----------\n")
print("Combinations of 2:")
comboTwo = list(itertools.combinations(resistorArr, 2))
print(list(itertools.combinations(letterEquiv, 2)))
#print(comboTwo)

print("Combinations of 3:")
comboThree = list(itertools.combinations(resistorArr, 3))
print(list(itertools.combinations(letterEquiv, 3)))
#print(comboThree)

print("Combinations of 4:")
comboFour = list(itertools.combinations(resistorArr, 4))
print(list(itertools.combinations(letterEquiv, 4)))
#print(comboFour)

print("Combinations of 5:")
comboFive = list(itertools.combinations(resistorArr, 5))
print("{}\n".format(list(itertools.combinations(letterEquiv, 5))))
#print(comboFive)

#Uncomment for sixth resistor value
#print("Combinations of 6:")
#comboSix = list(itertools.combinations(resistorArr, 6))
#print(comboSix)
#print("")

print("------Calculated Resistance------\n")
print("Resistance for pairs of Resistors:")
total = 0
for res1, res2 in comboTwo:
    print("Res 1: {:<6} Res 2: {:<6}"
    " Combined Resistance {:<6} Ohms".format(res1, res2, calculate_resistance(res1, res2)))
    total += 1 
print("Print total combinations: {}\n".format(total))

total = 0
print("Resistance for trios of Resistors:")
for res1, res2, res3 in comboThree:
    print("Res 1: {:<6} Res 2: {:<6} Res 3: {:<6}"
    " Combined Resistance {:<6} Ohms".format(res1, res2, res3,\
                                         calculate_resistance(res1, res2, 
                                                              res3)))
    total += 1 
print("Print total combinations: {}\n".format(total))

total = 0
print("Resistance for quads of resistors:")
for res1, res2, res3, res4 in comboFour:
    print("Res 1: {:<6} Res 2: {:<6} Res 3: {:<6} Res 4: {:<6}"
    " Combined Resistance {:<6} Ohms".format(res1, res2, res3, res4,
                                         calculate_resistance(res1, res2, 
                                                              res3, res4)))
    total += 1 
print("Print total combinations: {}\n".format(total))

total = 0
print("Resistance when five are combined:")
for res1, res2, res3, res4, res5 in comboFive:
    print("Res 1: {:<6} Res 2: {:<6} Res 3: {:<6} Res 4: {:<6} Res 5: {:<6}"
    " Combined Resistance {:<6} Ohms".format(res1, res2, res3, res4, res5,
                                     calculate_resistance(res1, res2, 
                                                          res3, res4, res5)))
    total += 1 
print("Print total combinations: {}\n".format(total))

#Uncomment when sixth value is determined
#print("Resistance when all are combined:")
#for res1, res2, res3, res4, res5, res6 in comboSix:
#    print("Res 1: {:<6} Res 2: {:<6} Res 3: {:<6} Res 4: {:<6} Res 5: {:<6} Res 6: {:<6}"
#    " Combined Resistance {:<6}".format(res1, res2, res3, res4, res5,
#                                     calculate_resistance(res1, res2, 
#                                                          res3, res4, 
#                                                          res5, res6)))
#    total += 1 
#print("Print total combinations: {}\n".format(total))
