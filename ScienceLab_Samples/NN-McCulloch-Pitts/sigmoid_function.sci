//u1=100
//out=(1-exp(-u1))/(1+exp(-u1))
//sigmoid_function.sci

clf();
//=======================================================
function [z] = sigmoid(x)
    
    A =   (1-exp(-x*10))
  
    B =(1+exp(-x*10))
    
    [r,q] = pdiv(A, B)

    z=q
  
  //(1-exp(-u1))/(1+exp(-u1))
   
endfunction

function [z] = test(x)
    
  z =  2*x
  //(1-exp(-u1))/(1+exp(-u1))
   
endfunction
//=======================================================

u1=[-10:0.1:10]';  // [start incremet end]

u1=linspace(-10,10,40);  // [start end , ]

z=sigmoid(u1);


plot2d(u1,z);




