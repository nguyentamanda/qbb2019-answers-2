#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Andrew Gordus
May, 2020
Quantitative Biology and Biophysics (AS.020.674/250.644)	Spring 2020
Gordus Lab #2

"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


#---------------#
# Set Variables #
#---------------#

S0 = 1 # Actual NYC population: 8*np.power(10,6)
I0 = 30 / (8*np.power(10,6))

R0 = 2.2
gamma = 0.44
beta = R0*gamma/S0


#-------------------#
# Current NYC Stats #
#-------------------#

# Current NYC Stats
# Shelter in Place occurred t = 12 days
# Confirmed cases was ~17644 at this point

Conf = 167000 #52 days from t0, Conf = Confirmed
Dead = 13000 #52 days from t0
Rec = 40000 #52 days from t0


f = Dead/Conf


#-------------#
# PHASE PLANE #
#-------------#

# Null Clines

Sn = gamma/beta
In = 0


Sspan = np.linspace(0,S0,10)
Ispan = np.linspace(0,S0,10)

# Grid of x & y values
S, I = np.meshgrid(Sspan, Ispan)

# Empty matrices to fill in with velocity data
dS = np.zeros(np.shape(S))
dI = np.zeros(np.shape(I))


# Fill velocities into grid.
for m in range(S.shape[0]):
    for n in range(I.shape[0]):
        dS[m,n] = -(beta)*(m)*(n)
        dI[m,n] = (beta)*(m)*(n)-(gamma)*(n) #m = S, n = I

#----------------------#
# NUMERICAL SIMULATION #
#----------------------#


# ODE

#intial conditions vector
# y0 = [1;(23/(8*10**6);0] #S0, I0, R0

def susceptible(t, s, i): 
    dSdt = -beta * s * i
    return dSdt

def infected(t, s, i): 
    dIdt = beta * s * i - gamma * i
    return dIdt

def recovered(t, i): 
    dRdt = (1 - f)*gamma * i #f being fraction that died
    return dRdt

def RK4SIR(t, y):
    # n = s0 + i0 + r0 #the population size
    for i in range(t+1):
        Si = s[i]
        Ii = i[i]
        Ii = r[i]
        
        s.k1 = susceptible(i, Si, Ii)
        i.k1 = infected(i, Si, Ii)
        r.k1 = recovered(i, Ii)

        s.k2 = susceptible(i+t/2, Si+t, Ii)
        i.k2 = 
        r.k2 = 
# def SIR(t,y):
#
#     return
#
#
#
#     tn1 = t + h
#
#     k1 = ( )/h
#
#     k2 = f( t + (h/2), y + h*(k1/2) )
#
#     k3 = f( t + (h/2), y + h*(k2/3) )
#
#     k4 = f( t + h, y + h*k3 )
#
#     yn1 = y + (1/6) * h * (k1 + 2*k2 + 2*k3 + k4)
#
#     y = yn1
#
#     return


# Integrators

# Runge-Kutta

# Scipy integrator

# sol = solve_ivp(SIR, [0,51],[S0,I0,0,0],max_step = 1)

# NOTE:
# sol.t = time vector
# sol.y = matrix of output. Rows are S, I, R, D; Columns are time

# Set up the matplotlib figure


X = np.arange(-10, 10, 1)
Y = np.arange(-10, 10, 1)
U, V = np.meshgrid(X, Y)

fig, ax = plt.subplots(3,2)
q = ax[0,0].quiver(S , I , dS, dI)
ax[0,0].quiverkey(q, X=0.3, Y=1.1, U=1,label='Quiver key, length = 1', labelpos='E')
ax[0,0].plot([Sn, Sn], [0,S0])
ax[0,0].set_xlabel('S')
ax[0,0].set_ylabel('I')

fig.savefig("quiver.png")
plt.close(fig)


