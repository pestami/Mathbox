//ANN_Toolbox set up :
//atomsSetConfig('Verbose','True');
//atomsInstall('ANN_Toolbox');

//https://www.scilab.org/artificial-neural-network-tutorial
// ensure the same starting point each time 
rand('seed',0);
// network def. neurons per Layer, including input 
//2 neurons in the input Layer, 2 in the hidden Layer and I in the ouput Layer 10 
          
// input training matrix x 

x = [0.8900,0.8544;
    0.8482,1.0000;
    0.0411,0.0746; 
    0.0247,0.0193;
    0.0086,0.0061;
    0.0044,0.7916;
    0.7470,0.7297;
    1.0000,0.0746;
    0.0240,0.0190;
    0.0102,0.0053;
    0.0026,0.0009;
    0.000,0.00001]'; 
    
 clf();

x1=x(1,:);
x2=x(2,:);

y1=x1-x2;

//plot2d(x1,x2,-1);

// desired output : I for class A and O for class B 
        
t1= [1 1 1 1 0 0 0 0 0 0 0 0]; 
t= [1 1 0 0 0 1 0 0 0 0 0 0]; 

N=[2,2,1]

Ip=[0.1,0]

// Learning rate and the thresrnzld for the error tolerated by the network 

  W= ann_FF_init(N); 

// training cyles 
 T=400;

  W = ann_FF_Std_online(x, t, N, W, Ip, T); 

//x is the training t 13 the Output W is the initialized weight, 
//N the architecture, Ip the Learning rate and 
//T is the number of iterations 

// full run 
x_test = [
1,1;
1,1;
0,0;
0,0;
0,0;
0,1;
1,1;
1,0;
0,0;
0,0;
0,0;
0,0;
]'; 
  
  Wtest=ann_FF_run(x_test, N,W) //the network N was tested using x as the test set, 

// and W as the weights of the connection 
