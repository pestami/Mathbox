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
(REPLACE F0.000000 ; F1000)
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

(New Coordinates---------------)
S0
G00 X10 Y10
G92 X0 Y0 (Shifts current G54)
(10,10)
(------------------------------)

(BEGIN SQUARE)
G00 X00 Y00
S1000
G01 X10 Y00
G01 X10 Y10
G01 X00 Y10
G01 X00 Y00
S0
(END SQUARE)
(BEGIN ARTWORK)
G00 X00 Y05
S1000
G03 X10 Y05 R5
S0
G00 X00 Y05
S1000
G02 X10 Y05 R5
(END ARTWORK)

(New Coordinates---------------)
S0
G00 X10 Y10
G92 X0 Y0 (Shifts current G54)
(10,10)(10,10)
(------------------------------)

(BEGIN SQUARE)
G00 X00 Y00
S1000
G01 X10 Y00
G01 X10 Y10
G01 X00 Y10
G01 X00 Y00
S0
(END SQUARE)
(BEGIN ARTWORK)
G00 X00 Y05
S1000
G03 X10 Y05 R5
S0
G00 X00 Y05
S1000
G02 X10 Y05 R5
(END ARTWORK)

(New Coordinates---------------)
S0
G00 X-20 Y-20
G92 X0 Y0 (Shifts current G54)
(10,10)(10,10)(-20-20)
(------------------------------)

(BEGIN SQUARE)
G00 X00 Y00
S1000
G01 X10 Y00
G01 X10 Y10
G01 X00 Y10
G01 X00 Y00
S0
(END SQUARE)
(BEGIN ARTWORK)
G00 X00 Y05
S1000
G03 X10 Y05 R5
S0
G00 X00 Y05
S1000
G02 X10 Y05 R5
(END ARTWORK)



(=END Engrave===========================)
(======END============)
(G00 – Rapid Positioning------------Laser OFF)
S0 
G0 Z10.000000
