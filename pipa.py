import sys
import time
import random
from math import sqrt, sin, cos,  log
import matplotlib.pyplot as plt


def euclidian_distance(p1, p2, p3):
 return float(sqrt((p1[0] - p3[0])**2 + (p1[1] - p3[1])**2) + \
                        sqrt((p2[0] - p3[0])**2 + (p2[1] - p3[1])**2))


def vertical_distance(p1,  p2,  p3):
    s = float((p2[1] - p1[0])/(p2[0] - p1[0]))
    xc = float((p3[0] + s*p3[1] + s*p2[1] - (s*s)*p2[0])/(1 + s*s))    
    return float(abs(p1[1] + (p2[1] - p1[1])*((xc - p1[0]) / (p2[0] - p1[0])) + p3[1]))
   
output = []  
def pip(input, n):
    #assumes input sorted
    #n = number of points to output, at least 2
    
    if (n >= len(input)):
        return input
   
    output.extend([input[0] + (0,), input[-1] + ((len(input) - 1),)])
    n = n - 2

    count = 0
    for i in range(n):        
        maximum = 0
        for pip_index, pip in zip(range(len(output)), output):
            if pip_index < (len(output) - 1):
                pip_a = pip
                pip_b = output[pip_index + 1]
                pip_a_input_index = pip[2]
                pip_b_input_index = output[pip_index + 1][2]

                input_interval = range(pip_a_input_index + 1, pip_b_input_index)
               
                if len(input_interval) == 0: continue
                
                for j in input_interval:
                    distance = euclidian_distance(pip_a, pip_b,  input[j])
                    if  distance > maximum:
                        maximum = distance
                        better = input[j]
                        better_position = j
                        temp_pip_a_index = pip_index
        output.insert(temp_pip_a_index + 1, better + (better_position,))               
    output.sort()
    return output

n = 1000
values = [x*x for x in range(-n/2,  n/2)]
original = zip(range(0, n + 1), values)
start = time.time()
try:
    pip(original, int(sys.argv[1]))
except IndexError:
    print  "Missing number of points for output =("
    exit(1)
duration = time.time() - start
print "%s seconds elapsed." % duration

plt.plot([x[0] for x in original], [x[1] for x in original])
plt.plot([x[0] for x in output], [x[1] for x in output])
plt.show()
