
(======START============)
M3 S0
S0 
(G00 – Rapid Positioning------------Laser OFF)
(G1 - CUT      G1 F1000 X51 Y248 Z-5 )  
S0 
G0 F1000 X0.000000 Y0.000000

(S1000 ------------------------------Laser 100% ON)
(S0    ------------------------------Laser 000% OFF)
(BEGIN Engrave)
S0
G0 F1000 X0.000000 Y0.000000

S1000 
G1 F1000 X74 Y00 Z-5
G1 F1000 X74 Y52 Z-5
G1 F1000 X00 Y52 Z-5
G1 F1000 X00 Y00 Z-5
S0 

(END Engrave)
(======END============)
(G00 – Rapid Positioning------------Laser OFF)
S0 
G0 Z10.000000
