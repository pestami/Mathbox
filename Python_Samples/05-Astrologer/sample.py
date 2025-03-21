#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      SESA237770
#
# Created:     18.04.2024
# Copyright:   (c) SESA237770 2024 import swisseph as swe
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import swisseph as swe
from kerykeion import AstrologicalSubject

import sys


##=======================================================
if __name__ == '__main__':

    print("===========================================================")
    print("=====ASTROLOGY SANDBOX=====================================")
    print("===========================================================")

    print(sys.path)

    kanye = AstrologicalSubject("Kanye", 1977, 6, 8, 8, 45, "Atlanta")
    
    #kanye = AstrologicalSubject("Kanye", 1977, 6, 8, 8, 45, lng=50, lat=50, tz_str="Europe/Rome", city="Rome")
    
    from kerykeion import Report, AstrologicalSubject

    kanye = AstrologicalSubject("Kanye", 1977, 6, 8, 8, 45, "Atlanta")
    report = Report(kanye)
    report.print_report()
