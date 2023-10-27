#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      SESA237770
#
# Created:     18.07.2023
# Copyright:   (c) SESA237770 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass


## For most practical purposes, you can think of the conditional block that you open
## with if __name__ == "__main__"
## as a way to store code that should only run when your file is executed as a script.

if __name__ == '__main__':
    main()

#-------------------------------------------------------------------------------

def GetNamedCellValue(sCellName,workbook,sheet):

    address = list(workbook.defined_names[sCellName].destinations)
    #[('Sheet1', '$B$7:$E$10')]
    #removing the $ from the address
    #------------------------------------------------------
    for sheetname, cellAddress in address:
        cellAddress = cellAddress.replace('$','')
        #'B7:E10'

    sValue=sheet[cellAddress].value
##    sValue=sheet[cellAddress][0][0].value
    print(f'Named Range {sCellName} has Cell Address scalar: {cellAddress} and value= {sValue}')

    return sValue
#-------------------------------------------------------------------------------
import sys
sys.path.append('C:\\ProgrammeApps\\python3')
sys.path.append('C:\\ProgrammeApps\\python3\\Lib\\site-packages')

import matplotlib.pyplot as plt
import numpy as np
import os
#-------------------------------------------------------------------------------
# open workbook and load all variables
#-------------------------------------------------------------------------------
from openpyxl import load_workbook
from scipy import integrate
from scipy.integrate import quad
print('=====================================================')
print('=====ARGUMENTS========================================')
print( 'Arguments:', len(sys.argv), 'arguments.')
print('Argument:', str(sys.argv[0]))
if len(sys.argv) == 3:
    print('Argument:', str(sys.argv[1]))
    print('Argument:', str(sys.argv[2]))
if len(sys.argv) == 2:
    print('Argument:', str(sys.argv[1]))
    WBname=str(sys.argv[1])
else:
    WBname='NULL.XLSX'

print('=====================================================')
print('< Loading Ranges fron XLSX >')
print('=====================================================')

##WBname='ParabolicMirror_OoCalc_02.xlsx'
WBpath='C:\\Users\\sesa237770\\Documents\\Mathbox\\Python_Samples\\02-BeadOnWire'
if WBname=='NULL.XLSX':
    WBname='BeadOnWire_OoCalc.xlsx'
WBpath=os.path.dirname(__file__)
WBpathname=WBpath +'\\'+ WBname

##WBname='ParabolicMirror.ods'

wb = load_workbook(WBpathname,data_only=True) # otherwise formula is displayed
ws = wb.active  # work sheet
#-------------------------------------------------------------------------------
A=1  #
B=-95  #
L1=90  #
L2=90  #

A=float(GetNamedCellValue('rng_A',wb,ws))
B=float(GetNamedCellValue('rng_B',wb,ws) )
L1=GetNamedCellValue('rng_L1',wb,ws)
L2=GetNamedCellValue('rng_L2',wb,ws)


print('<---ECHO RANDES FRON XLS-----')
print('\n A==' + str(A))
print('\n B==' + str(B))
print('\n L1==' + str(L1))
print('\n L2==' + str(L2))


print('=====================================================')
print('</ Loading Ranges fron XLSX >')
print('=====================================================')
#-------------------------------------------------------------------------------
# open workbook and load all variables
#-------------------------------------------------------------------------------
print('=====================================================')
print('<Ploting Path of wireX >')
print('=====================================================')

x = np.linspace(0, -L1, 20)

y = A*(x)**2 + B*x

fig, ax = plt.subplots()
ax.plot(x, y,'r')

ax.set_xlim([-L1, 0])
ax.set_ylim([-L2, L2])

plt.savefig(WBpath+'\\'+'wirepath.jpg')
##plt.show()

print('=====================================================')
print('</Ploting Path of wireX >')
print('=====================================================')