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
(Engrave)
S0 		(--Laser 000% OFF)
S0 		(--Laser 000% OFF)
G0 F1000 X280.000000 Y140.000000
G0 F1000 Z4.000000
G1 F1000 X280.000000 Y140.000000 Z-5.000000
S1000	(---Laser 100% ON)
G3 F1000 I-140.000000 J0.000000 K0.000000 X280.000000 Y140.000000 Z-5.000000
S0 		(--Laser 000% OFF)
S0 		(--Laser 000% OFF)
G0 F1000 X215.000000 Y140.000000
G0 F1000 Z4.000000
G1 F1000 X215.000000 Y140.000000 Z-5.000000
S1000	(---Laser 100% ON)
G3 F1000 I-75.000000 J0.000000 K0.000000 X215.000000 Y140.000000 Z-5.000000
S0 		(--Laser 000% OFF)
S0 		(--Laser 000% OFF)
G0 F1000 X144.000000 Y140.000000
G0 F1000 Z4.000000
G1 F1000 X144.000000 Y140.000000 Z-5.000000
S1000	(---Laser 100% ON)
G3 F1000 I-4.000000 J0.000000 K0.000000 X144.000000 Y140.000000 Z-5.000000
G0 Z6.000000
S0 		(--Laser 000% OFF)
(=END Engrave===========================)
(======END============)
(G00 – Rapid Positioning------------Laser OFF)
S0 
G0 Z10.000000
