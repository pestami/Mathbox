(======HEADER=====================)
(G00 – Rapid Positioning------------Laser OFF)
(G01 – Linear interpolation------------ )
(G02 – Circular interpolation CCW--X-Y-I-J-------)
(G02 – Circular interpolation CW---X-Y-I-J-------)
(Gcode G91 & Gcode G90: CNC Absolute and Incremental Programming)
(S00 - S1000 Spindle speed)
(M03 – Spindle on in a clockwise direction.)
(======START=====================)
(======CODE MANDATORY============)
M3 S0
(================================)
S1000	(---Laser 100% ON)
S0 		(--Laser 000% OFF)
(=BEGIN Engrave=========================)

S0 		(--Laser 000% OFF)
G1 X100 Y100 F1000
G1 X110 Y100 F1000
S1000	(---Laser 100% ON)
G3 I-10 J0 X100 Y110 F1000
S0 		(--Laser 000% OFF)

S0 		(--Laser 000% OFF)
G1 X150 Y150 F1000
S1000	(---Laser 100% ON)
G3 I-10 J0 F1000
S0 		(--Laser 000% OFF)




(=END Engrave===========================)
S0 		(--Laser 000% OFF)
(======END============)


