(======HEADER=====================)
(G00 – Rapid Positioning------------Laser OFF)
(G01 – Linear interpolation------------ )
(G02 – Circular interpolation CCW------------ )
(G02 – Circular interpolation CW------------ )
(Gcode G91 & Gcode G90: CNC Absolute and Incremental Programming)
(S00 - S1000 Spindle speed)
(M03 – Spindle on in a clockwise)
(======POST PROCESSING===========)
(REPLACE (CUT); (CUT) \r\n S1000	(---Laser 100% ON))
(REPLACE F0.166667 ; F1000)
(REPLACE F8.333333 ; F1000)
(REPLACE F1000 ; F1000)
(REPLACE Z-5.000000 ;  )
(REPLACE Z-5.000000 ; \r\n S1000	(---Laser 100% ON))
(======START=====================)
(======CODE MANDATORY============)
M3 S0  (M03 – Spindle on in a clockwise)
(================================)
S0 		(--Laser 000% OFF)
G0 F1000 X0.000000 Y0.000000
S1000	(---Laser 100% ON)
S0 		(--Laser 000% OFF)
(=BEGIN Engrave=========================)
(Engrave004)
(Engrave007)

G0 F1000 Z6 
S0 		(--Laser 000% OFF)
G0 F1000 X19.888963 Y50.188310
G0 F1000 Z4 
 S1000	(---LaserOn 100% ON)
G1 F1000 X19.888963 Y50.188310 Z-5.000000
G1 F1000 X129.888963 Y50.188310 Z-5.000000
G1 F1000 X129.888963 Y5.188310 Z-5.000000
G1 F1000 X19.888963 Y5.188310 Z-5.000000
G1 F1000 X19.888963 Y50.188310 Z-5.000000
G0 F1000 Z6 
S0 		(--Laser 000% OFF)
G0 F1000 Z6 
S0 		(--Laser 000% OFF)
G0 F1000 X37.171707 Y45.455119
G0 F1000 Z4 
 S1000	(---LaserOn 100% ON)
G1 F1000 X37.171707 Y45.455119 Z-5.000000
G3 F1000 I-1.000000 J0.000000 K0.000000 X37.171707 Y45.455119 Z-5.000000
G0 F1000 Z6 
S0 		(--Laser 000% OFF)
G0 F1000 Z6 
S0 		(--Laser 000% OFF)
G0 F1000 X117.171707 Y45.455119
G0 F1000 Z4 
 S1000	(---LaserOn 100% ON)
G1 F1000 X117.171707 Y45.455119 Z-5.000000
G3 F1000 I-1.000000 J0.000000 K0.000000 X117.171707 Y45.455119 Z-5.000000
G0 F1000 Z6 
S0 		(--Laser 000% OFF)
G0 F1000 Z6 
S0 		(--Laser 000% OFF)
G0 F1000 X117.171707 Y15.455119
G0 F1000 Z4 
 S1000	(---LaserOn 100% ON)
G1 F1000 X117.171707 Y15.455119 Z-5.000000
G3 F1000 I-1.000000 J0.000000 K0.000000 X117.171707 Y15.455119 Z-5.000000
G0 F1000 Z6 
S0 		(--Laser 000% OFF)
G0 F1000 Z6 
S0 		(--Laser 000% OFF)
G0 F1000 X37.171707 Y15.455119
G0 F1000 Z4 
 S1000	(---LaserOn 100% ON)
G1 F1000 X37.171707 Y15.455119 Z-5.000000
G3 F1000 I-1.000000 J0.000000 K0.000000 X37.171707 Y15.455119 Z-5.000000
G0 Z6.000000


(=END Engrave===========================)
(======END============)
(G00 – Rapid Positioning------------Laser OFF)
S0 
G0 Z10.000000
