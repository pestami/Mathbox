
(======START============)
(======CODE MANDATORY============)
M3 S0
(================================)
S0 
(G00 – Rapid Positioning------------Laser OFF)
(G01 – Linear interpolation------------ )
(G02 – Circular interpolation CCW------------ )
(G02 – Circular interpolation CW------------ )
(S00 - S1000 Spindle speed)
S0 
G0 F1000 X0.000000 Y0.000000

(S1000 ------------------------------Laser 100% ON)
(S0    ------------------------------Laser 000% OFF)
(BEGIN Engrave)


(END Engrave)
(======END============)
(G00 – Rapid Positioning------------Laser OFF)
S0 
G0 Z10.000000
