// This is written by Zhiyang Ong
// For his "BibTeX Analytics" project

// Size of the figure
size(20cm,0,false);

// Importing packages from the Aysymptote Library
import graph;
import geometry;

// Set the limits of the x- and y- axis
xlimits(-2, 10);
ylimits(-2, 10);
// Draw the x- and y- axis with ticks
yaxis("$x_{2}$", RightTicks());
xaxis("$x_{1}$", Ticks());


// Maximize -x_1 + x_2

// Subject to:
// x1 - x2 <= 2
point c1A=(2,0), c1B=(0,-2);
line c1=line(c1A, c1B);
draw(c1,red);
label("$x1 - x2 \leq 2$",(8,6));
//real f(real x1, real x2) {return x}

// x1 + x2 <= 6
point c2A=(6,0), c2B=(0,6);
line c2=line(c2A, c2B);
draw(c2,red);
label("$x1 + x2 \leq 6$",(3,4));

// Draw initial solution
//	point fs1=(0,0);
//	real R=0.2;
//	circle c=circle(fs1, R);
//	draw(c);

// Draw final solution
point fs1=(0,6);
real R=0.2;
circle c=circle(fs1, R);
draw(c);


// real f(real x, real y) {return x*y;}
//draw(contour(f,(-3,-3),(3,3),new real[] {1}));
