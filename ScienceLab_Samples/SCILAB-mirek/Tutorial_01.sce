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
function sLine= myADD(X,Y)
    sLine=X + Y
endfunction
//===================================================================
//===================================================================
//===================================================================
/*
============================================================================
Basic Mathamatical Functions
============================================================================
*/
x=25
y=25
z=myADD(x,y)


mprintf('X + Y =',z)