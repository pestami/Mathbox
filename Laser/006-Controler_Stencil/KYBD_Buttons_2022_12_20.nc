(Changes==========================)
(template_2022_09_02.nc)
(template_2022_11_15.nc Gimp post processing, LaserOn LaserOff keywords easier to select and highlight)
(template_2022_11_18.nc Gimp post processing F500 S250 for size font 18)
(======HEADER=====================)
(G00 – Rapid Positioning------------Laser OFF)
(G01 – Linear interpolation------------ )
(G02 – Circular interpolation CCW------------ )
(G02 – Circular interpolation CW------------ )
(Gcode G91 & Gcode G90: CNC Absolute and Incremental Programming)
(S00 - S1000 Spindle speed)
(M03 – Spindle on in a clockwise)
(======POST PROCESSING====FREECAD=======)
(REPLACE (CUT); (CUT) \r\n S1000	(---LaserOn 100% ON))
(Penetrate)
(REPLACE F0.166667 ; F1000)
(REPLACE F8.333333 ; F1000)
(REPLACE F1000 ; F1000)
(REPLACE Z-5 ;  )
(REPLACE Z-5 ; \r\n S1000	(---LaserOff 100% ON))
(======POST PROCESSING====GIMP=======)
(REPLACE (Penetrate); (Penetrate) \r\n S1000	(---LaserOn 100% ON))
(REPLACE G00 Z 0.0000 G00 Z 0.0000\n\rS000	(---LaserOff 000%))
(REPLACE (Penetrate); (Penetrate) \r\n S250	(---LaserOn 100% ON))
(REPLACE G01 G01 F1000 )
(REPLACE G02 G01 F1000 )
(REPLACE G03 G01 F1000 )
(======START=====================)
(======CODE MANDATORY============)
M3 S0  (M03 – Spindle on in a clockwise)
(================================)
S0 		(--LaserOff 000% OFF)
G0 F1000 X0 Y0

S0 		(---LaserOff 000% OFF)
(=BEGIN Engrave=========================)
(Engrave)
G0 F1000 Z6
S000	(---LaserOff 000%) 
 
G0 F1000 X63.284271 Y104.852814
G0 F1000 Z4
S1000	(---LaserOn 100% ON)
G1 F1000 X63.284271 Y104.852814 Z-5
G3 F1000 I-15 J0 K0 X63.284271 Y104.852814 Z-5
G0 F1000 Z6
S000	(---LaserOff 000%) 
 
G0 F1000 X91.568542 Y76.568542
G0 F1000 Z4
S1000	(---LaserOn 100% ON)
G1 F1000 X91.568542 Y76.568542 Z-5
G3 F1000 I-15 J0 K0 X91.568542 Y76.568542 Z-5
G0 F1000 Z6
S000	(---LaserOff 000%) 
 
G0 F1000 X63.284271 Y48.284271
G0 F1000 Z4
S1000	(---LaserOn 100% ON)
G1 F1000 X63.284271 Y48.284271 Z-5
G3 F1000 I-15 J0 K0 X63.284271 Y48.284271 Z-5
G0 F1000 Z6
S000	(---LaserOff 000%) 
 
G0 F1000 X35 Y76.568542
G0 F1000 Z4
S1000	(---LaserOn 100% ON)
G1 F1000 X35 Y76.568542 Z-5
G3 F1000 I-15 J0 K0 X35 Y76.568542 Z-5
G0 F1000 Z6
S000	(---LaserOff 000%) 
 
G0 F1000 X91.568542 Y133.137085
G0 F1000 Z4
S1000	(---LaserOn 100% ON)
G1 F1000 X91.568542 Y133.137085 Z-5
G3 F1000 I-15 J0 K0 X91.568542 Y133.137085 Z-5
G0 F1000 Z6
S000	(---LaserOff 000%) 
 
G0 F1000 X119.852814 Y104.852814
G0 F1000 Z4
S1000	(---LaserOn 100% ON)
G1 F1000 X119.852814 Y104.852814 Z-5
G3 F1000 I-15 J0 K0 X119.852814 Y104.852814 Z-5
G0 F1000 Z6
S000	(---LaserOff 000%) 
 
G0 F1000 X119.852814 Y48.284271
G0 F1000 Z4
S1000	(---LaserOn 100% ON)
G1 F1000 X119.852814 Y48.284271 Z-5
G3 F1000 I-15 J0 K0 X119.852814 Y48.284271 Z-5
G0 F1000 Z6
S000	(---LaserOff 000%) 
 
G0 F1000 X91.568542 Y20
G0 F1000 Z4
S1000	(---LaserOn 100% ON)
G1 F1000 X91.568542 Y20 Z-5
G3 F1000 I-15 J0 K0 X91.568542 Y20 Z-5
G0 F1000 Z6
S000	(---LaserOff 000%) 
 
G0 F1000 X0 Y153.137085
G0 F1000 Z4
S1000	(---LaserOn 100% ON)
G1 F1000 X0 Y153.137085 Z-5
G1 F1000 X124.852814 Y153.137085 Z-5
G1 F1000 X124.852814 Y0 Z-5
G1 F1000 X0 Y0 Z-5
G1 F1000 X0 Y153.137085 Z-5
G0 Z6


(=END Engrave===========================)
(======END============)
(G00 – Rapid Positioning------------Laser OFF)
S0 
G0 Z10
