import sys
import time
import random
from math import sqrt, sin, cos,  log
import matplotlib.pyplot as plt


def arange(start, stop=None, step=None):
    if stop is None:
        stop = float(start)
        start = 0.0
    if step is None:
        step = 1.0
    cur = float(start)
    while cur < stop:
        yield cur
        cur += step

def cast_to_float(x):
    x = float(x)
    return float(x)

def euclidian_distance(p1, p2, p3):
    return (sqrt((p1[0] - p3[0])**2 + (p1[1] - p3[1])**2) + \
                        sqrt((p2[0] - p3[0])**2 + (p2[1] - p3[1])**2))


def vertical_distance(p1,  p2,  p3):    
    s = (p2[1] - p1[1])/(p2[0] - p1[0])
    distance = abs(p1[1] + (p2[1] - p1[1])*((p3[0] - p1[0]) / (p2[0] - p1[0])) - p3[1])
    return distance

def distance(p1,  p2,  p3):
    return vertical_distance(p1,  p2,  p3)

output = []  
def pip(input, n):
    #assumes input sorted
    #n = number of points to output, at least 2
    
    if (n >= len(input)):
        return input
   
    output.extend([input[0] + (0,), input[-1] + ((len(input) - 1),)])
    n = n - 2

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
                    dist = distance(pip_a, pip_b,  input[j])
                    if  dist > maximum:
                        maximum = dist
                        better = input[j]
                        better_position = j
                        temp_pip_a_index = pip_index
        output.insert(temp_pip_a_index + 1, better + (better_position,))               
    return map(lambda x: x[:2],  output)

n = 100
#values = [cos(x) for x in range(-n/2,   n/2)]
values = [1,  2,  4,  10,  20,  1,  3 ,  1,  10,  1,  10,  5, 30,  5,  1,  9,  13,  1,  0,  20,  1,  2,  4,  10,  5,  2,  50,  0,  7,  8, 5,  4,  3,  2,  20,  1,  3 ,  1,  10,  1,  10,  5, 30,  5,  1,  9,  13,  1,  0,  20,  1,  2,  4,  10,  20,  1,  3 ,  1,  10,  1,  10,  5, 30,  5,  1,  9,  13,  1,  0,  20,  1,  2,  4,  10,  5,  2,  50,  0,  7,  8, 5,  4,  3,  2,  20,  1,  3 ,  1,  10,  1,  10,  5, 30,  5,  1,  9,  13,  1,  0,  20]
#values = [random.random() for x in range(1000)]

original = zip(list(arange(0,  n+1,  1.0)), values)
start = time.time()
try:
    pip(original, int(sys.argv[1]))
except IndexError:
    print  "Missing number of points for output =("
    exit(1)
duration = time.time() - start
print "%s seconds elapsed." % duration

plt.plot([x[0] for x in original], [x[1] for x in original],  'k:')
plt.plot([x[0] for x in output], [x[1] for x in output])
plt.show()
