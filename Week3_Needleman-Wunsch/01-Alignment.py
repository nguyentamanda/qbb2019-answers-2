#!/usr/bin/env python3

"""
./01-Alignment.py 
"""

import numpy as np 


# HoxD70 matrix of Chiaromonte, Yap, Miller 2002,
#              A     C     G     T
sigma = [ [   91, -114,  -31, -123 ],
          [ -114,  100, -125,  -31 ],
          [  -31, -125,  100, -114 ],
          [ -123,  -31, -114,   91 ] ]

gap = 300

def score(a,b): 
    if a == "A":
        if b == "A": 
            return 91  
        if b == "C": 
            return -114
        if b == "G": 
            return -31 
        if b == "T": 
            return -123
    if a == "C": 
        if b == "A": 
            return -114 
        if b == "C": 
            return 100
        if b == "G": 
            return -125
        if b == "T": 
            return -31 
    if a == "G": 
        if b == "A": 
            return -31 
        if b == "C": 
            return -125
        if b == "G": 
            return 100
        if b == "T": 
            return -114
    if a == "T": 
        if b == "A": 
            return -123 
        if b == "C": 
            return -31
        if b == "G": 
            return -114
        if b == "T": 
            return 91
        
seq1 = 'CATAAACCCTGGCGCGCTCGCGGCCCGGCACTCTTCTGGTCCCCACAGACTCAGAGAGAACCCACCATGGTGCTGTCTCCTGCCGACAAGACCAACGTCAAGGCCGCCTGGGGTAAGGTCGGCGCGCACGCTGGCGAGTATGGTGCGGAGGCCCTGGAGAGGATGTTCCTGTCCTTCCCCACCACCAAGACCTACTTCCCGCACTTCGACCTGAGCCACGGCTCTGCCCAGGTTAAGGGCCACGGCAAGAAGGTGGCCGACGCGCTGACCAACGCCGTGGCGCACGTGGACGACATGCCCAACGCGCTGTCCGCCCTGAGCGACCTGCACGCGCACAAGCTTCGGGTGGACCCGGTCAACTTCAAGCTCCTAAGCCACTGCCTGCTGGTGACCCTGGCCGCCCACCTCCCCGCCGAGTTCACCCCTGCGGTGCACGCCTCCCTGGACAAGTTCCTGGCTTCTGTGAGCACCGTGCTGACCTCCAAATACCGTTAAGCTGGAGCCTCGGTGGCCATGCTTCTTGCCCCTTGGGCCTCCCCCCAGCCCCTCCTCCCCTTCCTGCACCCGTACCCCCGTGGTCTTTGAATAAAGTCTGAGTGGGCGGCAAAAAAAAAAAAAAAAAAAAAA'
seq2 = 'GGGGCTGCCAACACAGAGGTGCAACCATGGTGCTGTCCGCTGCTGACAAGAACAACGTCAAGGGCATCTTCACCAAAATCGCCGGCCATGCTGAGGAGTATGGCGCCGAGACCCTGGAAAGGATGTTCACCACCTACCCCCCAACCAAGACCTACTTCCCCCACTTCGATCTGTCACACGGCTCCGCTCAGATCAAGGGGCACGGCAAGAAGGTAGTGGCTGCCTTGATCGAGGCTGCCAACCACATTGATGACATCGCCGGCACCCTCTCCAAGCTCAGCGACCTCCATGCCCACAAGCTCCGCGTGGACCCTGTCAACTTCAAACTCCTGGGCCAATGCTTCCTGGTGGTGGTGGCCATCCACCACCCTGCTGCCCTGACCCCGGAGGTCCATGCTTCCCTGGACAAGTTCTTGTGCGCCGTGGGCACTGTGCTGACCGCCAAGTACCGTTAAGACGGCACGGTGGCTAGAGCTGGGGCCAACCCATCGCCAGCCCTCCGACAGCGAGCAGCCAAATGAGATGAAATAAAATCTGTTGCATTTGTGCTCCAG'

len_seq1 = len(seq1)
len_seq2 = len(seq2)

matrix = np.zeros((len_seq1+1, len_seq2+1))

#Fill out first row and first column
for i in range(0, len_seq1+1): #the +1 makes it include the last letter
    matrix[i][0] = gap * -i
for j in range(0, len_seq2+1):
    matrix[0][j] = gap * -j

#fill out table
for i in range(1, len_seq1+1): #1 because u want to skip [0], which was our initialization, and the +1 is to include the last base
    for j in range(1, len_seq2+1):
        match = matrix[i-1][j-1] + score(seq1[i-1], seq2[j-1]) #the -1 is for the diagonal 
        delete = matrix[i-1][j] - gap 
        insert = matrix[i][j-1] - gap 
        matrix[i][j] = max(match, delete, insert)
        
    # if max(match, delete, insert) == match:
    #     traceback[i][j] = match
    # elif max(match, delete, insert) == delete:
    #     traceback[i][j] = delete
    # elif max(match, delete, insert) == insert:
    #     traceback[i][j] = insert


align1 = ""
align2 = ""

i = len_seq1
j = len_seq2


# print(matrix)

while i > 0 and j > 0:
    score_current = matrix[i][j]
    score_diagonal = matrix[i-1][j-1]
    score_up = matrix[i][j-1]
    score_left = matrix[i-1][j]

    # print (score_current)
    # print (score_diagonal)
    # print(score_up)
    # print(score_left)
    # print(align1[::-1])
    # print(align2[::-1])
    # print(j, i)
    if score_current == score_diagonal + score(seq1[i-1], seq2[j-1]):
        align1 += seq1[i-1]
        align2 += seq2[j-1]
        i -= 1
        j -= 1

    elif score_current == score_up - gap:
        align1 += '-'
        align2 += seq2[j-1]
        j -= 1

    elif score_current == score_left - gap:
        align1 += seq1[i-1]
        align2 += '-'
        i -= 1
    # else:
    #     break


while i > 0:
    align1 += seq1[i-1]
    align2 += '-'
    i -= 1

while j >0:
    align1 += '-'
    align2 += seq2[j-1]
    j -= 1
    



align1 = align1[::-1]
align2 = align2[::-1]

print(align1)
print(align2)





