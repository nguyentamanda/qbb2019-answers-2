#!/usr/bin/env python3

"""
./01-WF-Model.py <population size> <generations> 
"""

import sys
import numpy as np
import numpy.random as npr
import scipy.stats as scs
import matplotlib.pyplot as plt

# n = int(sys.argv[1]) #population size
# generations = int(sys.argv[2]) #generations


def WrightFisher(n, freq, generations):
    gen_list = []
    for gen in range(generations):
        freq = 0.5
        gen_counter = 0
        while True: 
            output = npr.binomial(n= (n*2), p = freq) #n is the number of trials which is the number of alleles you want to pick, p is the probability of success which is the allele frequencys 
            freq = (output/(2*n))
            gen_counter += 1
            # print(freq)
    #         print (gen_counter)
            if (freq == 0) or (freq == 1):
                break
        gen_list.append(int(gen_counter))
    return(gen_list)


    # fig, ax = plt.subplots()
    # histogram = ax.hist(gen_list)
    # fig.savefig("histogram.png")
    # plt.close(fig)
    #
# WrightFisher(100, 0.5, 1000)
#
# pop_size = [100,1000,10000,100000,1000000,10000000]
# gen_counter2 = []
#
# for size in pop_size:
#     a = WrightFisher(size, 0.5, 1)
#     gen_counter2.append(a)
#
# fig, ax = plt.subplots()
# line = ax.plot(gen_counter2)
# fig.savefig("line.png")
# plt.close(fig)
#
#
# allele_freq = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
# allele_dict = {}
#
# for allele in allele_freq:
#     a = WrightFisher(100, allele, 100)
#     allele_dict[allele] = a
#
# fig, ax = plt.subplots()
#
# for key in allele_freq:  #this is magic
#     for j in allele_dict[key]:
#         # print(key, j)
#         plt.scatter(x = key, y = j, alpha = 0.3, color = "blue")
#
# fig.savefig("scatter.png")
# plt.close(fig)
#

def Selection(n, f, generations, s):
    for gen in range(generations):
        freq = f
        gen_counter = 0
        while True: 
            output = npr.binomial(n= (n*2), p = freq) 

            freq = (output*(1+s)) / ((2*n) - output + (output*(1+s)))
            gen_counter += 1

            if (freq == 0) or (freq == 1):
                break
        return (gen_counter)

select = [0.01, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.7]

select_list = []

for value in select: 
    a = Selection(1000, 0.5, 10, value)
    select_list.append(a)


fig, ax = plt.subplots()
plt.scatter(x = select, y = select_list, alpha = 0.3, color = "blue")
fig.savefig("Selection.png")
plt.close(fig)
