//===================================================================
//Pestami 20 June 2011
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
  // used to read product attributes from the file "cfg"
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
F='G:/Technik/PROX3/Tooling/Programme/Imbach_01/ProX3SwissPcb.tdf'
//...read atributes
F2='G:/Technik/PROX3/Tooling/Programme/Imbach_01/ProX3SwissPcb.cfg'

//......read points
U=file('open',F,'old')
A=read(U,6,4)
//--------------------------------------
// Data Matrix Format
//P1  Xist  Xsoll Yist  Ysoll
//P2
//X1
//X2
//X3
//X4 
//---------------------------------------
file('close',U)
//===================================================================
//Manipulate data into Data structures suitible for processing
// X1 6 element column vector with points p2 X1...X4  x-coordinate
//Y1 .....
//===================================================================
// ------Ist
Ax1=[1 0 0 0 ]
Ay1=[0 0 1 0 ]

// Ist Werte in Vectors X and Y
X1=A*Ax1'  
Y1=A*Ay1'
// ------Soll
Ax2=[0 1 0 0 ]
Ay2=[0 0 0 1 ]


A_sign=[-1 0 0 0 0 0;
0 1 0 0 0 0;
0 0 1 0 0 0;
0 0 0 1 0 0;
0 0 0 0 1 0;
0 0 0 0 0 1;]

// Soll Werte
X2=A*Ax2'
Y2=A*Ay2'

X2=(X2'*A_sign)'
Y2=(Y2'*A_sign)'
// Vectors Ist:  X1 Y1    and  Soll:  X2 Y2    X1[1...6]
//
//Making X1 the origin
D_X=[ X2(3);
X2(3);
X2(3);
X2(3);
X2(3);
X2(3);
]
 
 D_Y=[ Y2(3);
Y2(3);
Y2(3);
Y2(3);
Y2(3);
Y2(3);
]
 
X1_=X1-D_X
X2_=X2-D_X
Y1_=Y1-D_Y
Y2_=Y2-D_Y

//===================================================================
//-------Scale the errror
//  used for ploting grqaphs
//===================================================================

Scale_Error = abs(X1(5)/(X2(5)-X1(5))*0.2)
Scale_Error = 400

Dx=(-X1+X2)*Scale_Error
Dy=(-Y1+Y2)*Scale_Error

// Ist X values with scaled error
X3=X1+ Dx+0
Y3=Y1+ Dy+0
X3(1)=0 +0 // initial position of coordinate origin
Y3(1)=0

//clc
//===================================================================
//Solving Transformation equations
// 
//===================================================================
// using points X2/X3
i=4
j=5
P=[X1_(i) Y1_(i) X1_(j) Y1_(j)] 
M=[X2_(i) Y2_(i) 0 0;
0 0 X2_(i) Y2_(i);
X2_(j) Y2_(j) 0 0 ;
0 0 X2_(j) Y2_(j)]

B=inv(M)
TR=B*P'
TR=matrix(TR,2,2)
// using points X3/X4
i=5
j=6
P=[X1_(i) Y1_(i) X1_(j) Y1_(j)] 

M=[X2_(i) Y2_(i) 0 0;
0 0 X2_(i) Y2_(i);
X2_(j) Y2_(j) 0 0 ;
0 0 X2_(j) Y2_(j)]

B=inv(M)
TR2=B*P'
 TR2=matrix(TR2,2,2)
//average transformation
TR3=(TR2*1+TR)/2

X(1)=0; Y(1)=0


X4=X1
Y4=Y1

[evecs,evals]= spec(TR3)

//===================================================================
//Plot Graph
//===================================================================
  scf(1) // set graph hanle
   //clf()  // clear the graph
   lines(0) //Stops paging prompt
   //---------------------------------------------------------------
   // SETUP of graph
   a=get("current_axes")//get the handle of the newly created axes
   sTilte='Streching Plot (V02) (Error Scale=' + string(Scale_Error) + ') ' 
   xtitle( sTilte,"X Axis","Y Axis") ;
   a.data_bounds=[-300,-150;200,500];
   //---------------------------------------------------------------
 
  
   xpoly(X1,Y1,"lines",0)   // Plots ist
   p=get("hdl"); //get handle on current entity (here the polyline entity)
    p.polyline_style=4
    p.foreground=3;
    p.mark_style=5;
   
   xpoly(X3,Y3,"lines",0) // Plots Soll
   p=get("hdl"); //get handle on current entity (here the polyline entity)
    p.polyline_style=4
    p.foreground=2;
    p.mark_style=11;
   
   //...........Graph Points........................
   //...........Graph Decorations........................
        xstring(X2(3),Y2(3),'X1' )
        xstring(X2(4),Y2(4),'X2' )
        xstring(X2(5),Y2(5),'X3' )
        xstring(X2(6),Y2(6),'X4' )
   
        xstring(0,0-50,'P1(0,0)' )
        xstring(X2(2),Y2(2),'P2' )
        
   
        KaNr=Get_Line(F2,3)
        FrtNr=Get_Line(F2,2)
        Lage=Get_Line(F2,5)
        
        sText=KaNr + '_' + FrtNr+ '_' + Lage
        xstring(150,200,sText)
        
         offset=400
        xstring(-300,offset+10,"Scale as 1 =100%:")
        sText=" Xscale= " + string(TR3(1,1))
        xstring(-300,offset-20,sText)
        sText=" Yscale= " + string(TR3(2,2))
        xstring(-300,offset-40,sText)
        sText="XYscale= " + string(TR3(1,2))
        xstring(-300,offset-60,sText)
        sText="YXscale= " + string(TR3(2,1))
        xstring(-300,offset-80,sText)
        
        offset=250
        xstring(-300,offset+10,"Scale as PPM:")
       sText=" Xscale= " + string(1000000*(TR3(1,1)-1))
        xstring(-300,offset-20,sText)
        sText=" Yscale= " + string(1000000*(TR3(2,2)-1))
        xstring(-300,offset-40,sText)
        sText="XYscale= " + string(1000000*TR3(1,2))
        xstring(-300,offset-60,sText)
        sText="YXscale= " + string(1000000*TR3(2,1))
        xstring(-300,offset-80,sText)
                
        sT="P1 X2 X3 used to calc [Scale M 1]"
        sT=sT +"P1 X3 X4 used to calc [Scale M 2]"
        sT=sT +"[Scale Matrix] = ([M1]+[M2])/2"
          xstring(-300,-150,sT)
 //===================================================================
 // //JPG export
 //===================================================================
    F3='G:/Technik/PROX3/Tooling/Programme/Imbach_01/jpg/counter.dat'
    nCounter=0
    load(F3) // contains variable nCounter
    nCounter=nCounter+1
    save(F3,nCounter)
    sCounter=string(nCounter)
    cd('G:/Technik/PROX3/Tooling/Programme/Imbach_01/jpg')
    chdir('G:/Technik/PROX3/Tooling/Programme/Imbach_01/jpg')
    KaNr=Get_Line(F2,3)
    FrtNr=Get_Line(F2,2)
    Lage=Get_Line(F2,5)
    sGraphName=KaNr+'_'+FrtNr+'_' +Lage+'_' +  sCounter +'.jpg'
    
    xs2jpg(1,sGraphName);
   
 //.................................................................
  // clc
 //---------------------------------------------------------------
 //===================================================================
 // Log graph name in log file
 // list of graphs created
 //===================================================================
 //clc
  sPathName='G:\Technik\PROX3\Tooling\Programme\Imbach_01\jpg\index_scaling_graphs.dat'
  f=mopen(sPathName,'at');
  sLine=KaNr + ascii(9) + FrtNr + ascii(9) + Lage + ascii(9) + sGraphName
  //printf ("%s \n", "A string");  c reference
  mfprintf(f,'%s \n',sLine);
  //mprintf(f,sLine,'');
  mclose(f);

 //===================================================================
 // Print result in scilab console
 //===================================================================
 
 write(%io(2),'=====Transformation matrix Points x1 X2 X3======================')
 write(%io(2),TR)
 
 write(%io(2),'=====Transformation matrix Points x1 X3 X4======================')
write(%io(2),TR2)
 
 write(%io(2),'=====Transformation matrix Points AVERAGE======================')
 write(%io(2),TR3)
write(%io(2),'=========================================================')
write(%io(2),'=====Eigenvalues======================')
write(%io(2),"In Work.......... ")
// evecs
 //evals*1000
 //Orthagonality= atan(evecs(1,1)/evecs(2,1))/%pi*180 - atan(evecs(1,2)/evecs(2,2))/%pi*180
 //write(%io(2),Orthagonality)
write(%io(2),'=========================================================')
 //===================================================================
 
 exit
