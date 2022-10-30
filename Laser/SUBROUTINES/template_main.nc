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
(=BEGIN Engrave=========================)

(New Coordinates---------------)
S0
G00 X10 Y10
G92 X0 Y0 (Shifts current G54)
(10,10)
(------------------------------)
(SUB PROGRAM CALL 1 TIMES M98 = subprogram call)
#M97 "template_Coordinates_Subroutines_2022_10_07.nc"

(New Coordinates---------------)
S0
G00 X10 Y10
G92 X0 Y0 (Shifts current G54)
(10,10)
(------------------------------)
(SUB PROGRAM CALL 1 TIMES M98 = subprogram call)
#M97 "template_Coordinates_Subroutines_2022_10_07.nc"

(New Coordinates---------------)
S0
G00 X-20 Y-20
G92 X0 Y0 (Shifts current G54)
(10,10)(10,10)(-20-20)
(------------------------------)
(SUB PROGRAM CALL 1 TIMES M98 = subprogram call)
#M97 "template_Coordinates_Subroutines_2022_10_07.nc"

(=END Engrave===========================)
(======END============)
S0 		(--Laser 000% OFF)
