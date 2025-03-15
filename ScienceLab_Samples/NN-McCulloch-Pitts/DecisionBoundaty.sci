clf();
//=======================================================

W1 = 2;
W2 = 2;

// W1*X1 +W2*X2 = 1;

X2 = (1- W1*12)/W2

L=[1,1;
    -1,-2;
    0,0]';
L1= L(1,:);
L2=L(2,:);

//=======================================================

X1=[-10:0.1:10]';  // [start incremet end]

X1=linspace(-10,10,5);  // [start end , ]

X2 =1/W2- W1*X1/W2;


plot2d(X1,X2);

//plot2d(L1,L2,style=-1);   // works
plot2d(L1,L2,style=-1);   //'r','LineWidth',3,     

a=get("current_axes") //get the handle of the newly created axes

xgrid
xlabel('Synapsis X1')
ylabel('Synapsis X2 ')
title('McCulloch-Pitts Model 2 Synaps')
legend('Decision Plane','Inputs X1 X2',3)
a.x_label.text="Synapsis X1"

poly1= a.children(1).children(1); //store polyline handle into poly1
poly1.foreground = 6; 
