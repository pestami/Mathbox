(======START=====================)
(======CODE MANDATORY============)
M3 S0  (M03 – Spindle on in a clockwise)
(================================)
S0 		(--Laser 000% OFF)
G0 F1000 X0.000000 Y0.000000
S1000	(---Laser 100% ON)
S0 		(--Laser 000% OFF)
(=BEGIN Engrave=========================)
	(BEGIN SQUARE)
	G00 X00 Y00
	S1000	(---Laser 100% ON)
	G01 X10 Y00
	G01 X10 Y10
	G01 X00 Y10
	G01 X00 Y00
	S0 		(--Laser 000% OFF)
	(END SQUARE)
	(BEGIN ARTWORK)
	G00 X00 Y05
	S1000	(---Laser 100% ON)
	G03 X10 Y05 R5
	S0 		(--Laser 000% OFF)
	G00 X00 Y05
	S1000
	G02 X10 Y05 R5
	(END ARTWORK)
(=END Engrave===========================)
(======END============)

