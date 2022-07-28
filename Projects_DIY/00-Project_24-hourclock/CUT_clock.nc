
(======START============)
M3 S0
S0 
(G00 – Rapid Positioning------------Laser OFF)
S0 
G0 F1000 X0 Y0

(S1000 ------------------------------Laser 100% ON)
(S0    ------------------------------Laser 000% OFF)
(BEGIN Engrave)


G1 F500 X290 Y150 Z0
G1 F500 X290 Y150 Z-5
S1000
G3 F500 I-140 J0 K0 X290 Y150 Z-5
G1 F500 X290 Y150 Z0
S0

G1 F500 X225 Y150 Z0
G1 F500 X225 Y150 Z-5
S1000
G3 F500 I-75 J0 K0 X225 Y150 Z-5
G1 F500 X225 Y150 Z0
S0

G1 F500 X154 Y150 Z0
G1 F500 X154 Y150 Z-5
S1000
G3 F500 I-4 J0 K0 X154 Y150 Z-5
G1 F500 X154 Y150 Z0
S0

(END Engrave)
(======END============)
(G00 – Rapid Positioning------------Laser OFF)
S0 
G0 Z10
