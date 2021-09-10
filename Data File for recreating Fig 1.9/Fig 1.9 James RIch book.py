# Fig 1.9 James RIch book

import math
import cmath
import sys
import numpy as np

sys.path.append('/home/ashmita/Desktop/ASHMITA/APanda_Lib')
# importing all files at once, now we just need to write function name to access it
from APanda_Lib import *


def RK4_first(F,x0,y0,h,N,name):
    x=x0
    y=y0
    if h<0 : handling_files.write_beginning(name, f'{x} {y}\n')
    else : handling_files.append_file(name, f'{x} {y}\n')
    for i in range(N):
        K1=F(x,y)
        #
        K2=F(x+h/2, y+(K1*h)/2)
        #
        K3=F(x+h/2, y+(K2*h)/2)
        #
        K4=F(x+h, y+(K3*h))
        #
        y=y+((K1+2*K2+2*K3+K4)*h)/6
        x=x+h
        if h<0 : handling_files.write_beginning(name, f'{x} {y}\n')
        else : handling_files.append_file(name, f'{x} {y}\n')
        #
    return(1)


#constants
O_M=0.5
O_L=0
O_T=O_M+O_L

t0=0
y0=1
h=0.1
tmax=3
tmin=-1
Nup=int((tmax-t0)/h)
Ndown=int((t0-tmin)/h)


Y=lambda t, y: (cmath.sqrt(O_M/y+(O_L)*math.pow(y, 2)+(1-O_T))).real
path="/home/ashmita/Desktop/ASHMITA/NISER Study/7th Semester/Cosmology/Week 4/"
n=f'Omega_M={O_M}, Omega_Lambda={O_L}.txt'
name=path+n
f=open(name, 'w')
f.close()
out1=RK4_first(Y,t0,y0,-h,Ndown,name) #for negative directions
out2=RK4_first(Y,t0,y0,h,Nup,name) #for positive
