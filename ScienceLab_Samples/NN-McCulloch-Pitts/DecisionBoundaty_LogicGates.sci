clf();
//=======================================================
// Truth Tables
TTand=[0,0,0;
            0,1,0;
            1,0,0
            1,1,1];

X1and=TTand(:,1);
X2and=TTand(:,2);
Yand=TTand(:,3);
            
//=======================================================

scatter3d(X1and,X2and,Yand,0.1,color("grey60"))  

Axes = gca();

title('Decision Boundary AND Gate')

Axes.title.text="Decision Boundary AND Gate"

