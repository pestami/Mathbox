//===================================================================
//Pestami 20 June 2011
//  IN development not used
//===================================================================
clc
lines(0) //Stops paging prompt
format(10) // number format
resethistory() // all history gone
clear // all mem gone
//===================================================================
//Functions 
//===================================================================
function sLine= Get_Line(File,n)
  // used to read product attributes from file cfg
    sText=mgetl(File,n)
    FrtNr=sText(n)
    k1=strindex(sText(n),'=')+1
    k2=length(sText(n))
    sLine=part(FrtNr,k1:k2)
endfunction
//===================================================================
//Extract Data
//===================================================================
// fORWARD SLAAH FOR FILE NAMES
cd('G:/Technik/PROX3/Tooling/Programme/Imbach_01/')
chdir('G:/Technik/PROX3/Tooling/Programme/Imbach_01/')
PWD // LISTS CURRENT DIRECTORY  - dir is directory command
sFile01='G:\Technik\PROX3\Tooling\Programme\Imbach_01\ProX3SwissPcb_log.tdf'
//...read 

U=file('open',sFile01,'old')
A=read(U,-1,4)

file('close',U)

 //===================================================================
 
 exit
