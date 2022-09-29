(======HEADER=====================)
(G00 – Rapid Positioning------------Laser OFF)
(G01 – Linear interpolation------------ )
(G02 – Circular interpolation CCW------------ )
(G02 – Circular interpolation CW------------ )
(Gcode G91 & Gcode G90: CNC Absolute and Incremental Programming)
(S00 - S1000 Spindle speed)
(M03 – Spindle on in a clockwise)
(======SEARCH REPLACE=====================)
(SEARCH (CUT) \r\n S1000	(---Laser 100% ON))
(REPLACE (CUT) \r\n S1000	(---Laser 100% ON))
(REPLACE F0.166667 F1000)
(REPLACE F8.333333 F1000)
(======START=====================)
(======CODE MANDATORY============)
M3 S0  (M03 – Spindle on in a clockwise)
(================================)
S0 		(--Laser 000% OFF)
G0 F1000 X0.000000 Y0.000000
S1000	(---Laser 100% ON)
S0 		(--Laser 000% OFF)
( GROUP=====================================)
(=BEGIN Engrave=========================)
(Engrave)

S0 		(--Laser 000% OFF)
( GROUP=====================================)
G0 F0.000000 X12.598400 Y58.274219
(CUT) 
S1000	(---Laser 100% ON)
G1 F0.166667 X12.598400 Y58.274219 Z-5.000000
G1 F8.333333 X60.598400 Y58.274219 Z-5.000000
G1 F8.333333 X108.598400 Y58.274219 Z-5.000000
G1 F8.333333 X102.279080 Y10.274219 Z-5.000000
G1 F8.333333 X60.598400 Y10.274219 Z-5.000000
G1 F8.333333 X18.917720 Y10.274219 Z-5.000000
G1 F8.333333 X12.598400 Y58.274219 Z-5.000000
S0 		(--Laser 000% OFF)

( GROUP=====================================)
G0 F0.000000 X123.680680 Y58.000000
(CUT) 
S1000	(---Laser 100% ON)
G1 F0.166667 X123.680680 Y58.000000 Z-5.000000
G1 F8.333333 X197.180680 Y58.000000 Z-5.000000
G1 F8.333333 X270.680680 Y58.000000 Z-5.000000
G1 F8.333333 X264.361360 Y10.000000 Z-5.000000
G1 F8.333333 X197.180680 Y10.000000 Z-5.000000
G1 F8.333333 X130.000000 Y10.000000 Z-5.000000
G1 F8.333333 X123.680680 Y58.000000 Z-5.000000
S0 		(--Laser 000% OFF)

(=END Engrave===========================)

(======END============)
(G00 – Rapid Positioning------------Laser OFF)
S0 
G0 Z10.000000
