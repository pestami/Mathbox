'========================================================
'VBS run Python
'========================================================

if wscript.arguments.count > 0 then 
	sExportFolder = WScript.Arguments.Item(0)
	sLevels= WScript.Arguments.Item(1)
end if

'fDEBUG=TRUE

'sR=msgbox(sScriptdir,1,"debug in Tool_BOM: " ) 

sApplication="C:\Users\sesa237770\Documents\Mathbox\Python_Samples\01-ParabolicMirror\math_plot_parabolic_mirror.py"
sPython="C:\ProgrammeApps\python3\python.exe"
'=========================================================================================================================

sPathFile1=sPython &" "&sApplication 
cmd1=sPathFile1
sR=InputBox("cmd:", "DEBUG", sPathFile1)

Set WshShell = WScript.CreateObject("WScript.Shell")   
WshShell.Run cmd1,1,true
'=========================================================================================================================

'=========================================================================================================================
