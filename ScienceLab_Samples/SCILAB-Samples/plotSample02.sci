// axis centered at (0,0)
clf();
x=[0:0.1:2*%pi]';
plot2d(x-4,sin(x),1,leg="sin(x)");
a=gca(); // Handle on axes entity
a.x_location = "origin";
a.y_location = "origin";
// Some operations on entities created by plot2d ...
isoview
a=gca();
a.children // list the children of the axes.
// There are a compound made of two polylines and a legend
poly1= a.children(1).children(1); //store polyline handle into poly1
poly1.foreground = 2; // another way to change the style...
poly1.thickness = 3;  // ...and the thickness of a curve.
poly1.clip_state='off'; // clipping control
leg = a.children(2); // store legend handle into leg
leg.font_style = 9;
leg.line_mode = "on";
isoview off
