clc
lines(0) //Stops paging prompt
format(10) // number format
resethistory() // all history gone
clear // all mem gone
//===================================================================
//Functions 
//===================================================================
function [P]=Demand(Q)
   a= 100;
  P =a - Q;
  
 endfunction
 //===================================================================
 function [E]=Earnings(Q)
   a= 100;
  E =(a*Q - Q^2);  
  E=E / 100 ;

endfunction
//===================================================================
function [P]=ReactionFunctionFirmA(Q)
   a= 100;
   Qa=max(Q);
  
  P =a - Q;
  
 endfunction ;
//===================================================================
function [P]=ReactionFunctionFirmB(Q)
   a= 100;
  P =a - Q;
  
 endfunction
//===================================================================
// x initialisation
// P = a - Q
/*
Production of 100 at 300 SF each
*/
Q=[0:10:100]';
Qa=[0:10:100]';
Qb=100-Qa;

//simple plot
clf();
plot(Demand(Q));

xtitle( 'Demand Curve Product ', 'Q Units', 'P price', '' ) ;

Q2=[0:10:100];
plot(Earnings(Q2));
plot(max(Q2));

//===================================================================
//Graph Post Processing
//===================================================================
a=gca(); // Handle on axes entity
// Some operations on entities created by plot ...
isoview("on");
a.children // list the children of the axes : here it is an Compound child composed of 2 entities
poly1= a.children.children(2); //store polyline handle into poly1
poly1.foreground = 4; // another way to change the style...
poly1.thickness = 3;  // ...and the thickness of a curve.
poly1.clip_state='off' // clipping control
isoview("off");
//===================================================================
