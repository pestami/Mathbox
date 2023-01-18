@prompt $n$g
@cls
@color 1A
@Echo 0n

@Echo ========================================================
@Echo Start SCILAB and display scaling of fiducial points
@Echo 2011/06/14 Pestami
@Echo Path: G:\Technik\PROX3\Tooling\Programme\Imbach_01\scilab\
@Echo Script: Plot_Stretch.sce
@Echo ========================================================
@Echo Scilab script starting.....
@Echo off

set sPath_scilab=G:\Technik\PROX3\scilab-5.1.1\bin\wScilex.exe
set sScript=G:\Technik\PROX3\Tooling\Programme\Imbach_01\scilab\Plot_Stretch.sce
set Para= 

call %sPath_scilab% -adv-cli  -f %sScript% -nb

:  taskkill /IM wScilex.exe
:  taskkill /IM wScilex.exe
 pause

REM  =======================================================