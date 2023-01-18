// Default simulation parameters 
param = []; 
param.tau = 5e4; // Number of innovators per year (initiation) 
param.s = 0.61; // Annual rate at which light users attract non-users (initiation) 
param.q = 3.443; // Constant which measures the deterrent effect of heavy users (initiation) 
param.smax = 0.1; // Lower bound for s effective (initiation) 
param.a = 0.163; // Annual rate at which light users quit 
param.b = 0.024; // Annual rate at which light users escalate to heavy use 
param.g = 0.062; // Annual rate at which heavy users quit 
param.delta = 0.291; // Forgetting rate 
 
// Simulation data 
// Time variables 
sim = []; 
sim.Tbegin = 1970; // Initial time 
sim.Tend = 2020; // Final time 
sim.Tstep = 1/12; // Time step 
// Initial conditions 
sim.L0 = 1.4e6; // Light users at the initial time 
sim.H0 = 0.13e6; // Heavy users at the initial time 
sim.Y0 = 0.11e6; // Decaying heavy user at the initial time 

// Global window parameters 
global margin_x margin_y; 
global frame_w frame_h plot_w plot_h; 
 
// Window Parameters initialization 
frame_w = 300; frame_h = 550;// Frame width and height 
plot_w = 600; plot_h = frame_h;// Plot width and heigh 
margin_x = 15; margin_y = 15;// Horizontal and vertical margin for elements 
defaultfont = "arial"; // Default Font 
axes_w = 3*margin_x + frame_w + plot_w;// axes width 
axes_h = 2*margin_y + frame_h;          // axes height (100 => toolbar height) 
 
demo_lhy = scf(100001);// Create window with id=100001 and make 
it the current one 
 
 
// Background and text 
demo_lhy.background      = -2; 
demo_lhy.figure_position = [100 100]; 
demo_lhy.figure_name     = gettext("LHY solution"); 
 
// Change dimensions of the figure 
demo_lhy.axes_size = [axes_w axes_h]; 
