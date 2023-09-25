#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      SESA237770
#
# Created:     04.08.2023
# Copyright:   (c) SESA237770 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

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
    print(f'{sCellName} has Cell Address scalar: {cellAddress} and value= {sValue}')

    return sValue
#-------------------------------------------------------------------------------


from openpyxl import load_workbook
wb = load_workbook("ParabolicMirror.xlsx")
ws = wb.active
sheet = wb.active

## print(f'The value of A2 is {sheet["B4"].value}')

address = list(wb.defined_names["rngMirrorWidth"].destinations)
#[('Sheet1', '$B$7:$E$10')]
#removing the $ from the address
#------------------------------------------------------
for sheetname, cellAddress in address:
    cellAddress = cellAddress.replace('$','')
    #'B7:E10'

print(f'Cell Address scalar: {cellAddress}')

address = list(wb.defined_names["rngMatrix"].destinations)
# address = [('Sheet1', '$B$7:$C$11')]
#removing the $ from the address
#------------------------------------------------------
for sheetname, cellAddress in address:
    cellAddress = cellAddress.replace('$','')
    #'B7:E10'

sValue=GetNamedCellValue('rngMirrorWidth',wb, sheet)
print(f'Cell Address Matrix: {cellAddress}')
print(f' value= {sValue}')

sValue=GetNamedCellValue('rngMatrix',wb, sheet)
print(f'Cell Address Matrix: {cellAddress}')
print(f' value= {sValue}')




