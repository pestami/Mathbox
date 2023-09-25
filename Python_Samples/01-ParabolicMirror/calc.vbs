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
sDirectory="C:\Users\sesa237770\Documents\Mathbox\Python_Samples\01-ParabolicMirror"
sPython="C:\ProgrammeApps\python3\python.exe"
'=========================================================================================================================

sPathFile1=sPython &" "&sApplication 
cmd1=sPathFile1


scriptdir = CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName)
sR=InputBox(scriptdir+ " cmd:", "DEBUG", sPathFile1)

Set WshShell = WScript.CreateObject("WScript.Shell")   

'WshShell.Run cmd1,1,true    ' not work from shell in open office


Set objShell = CreateObject("Shell.Application")
'Syntax
'      .ShellExecute "application", "parameters", "dir", "verb", window

'      .ShellExecute 'some program.exe', '"some parameters with spaces"', , "runas", 1

'Key
'   application   The file to execute (required)
'   parameters    Arguments for the executable
'   dir           Working directory
'  verb          The operation to execute (runas/open/edit/print)
'   window        View mode application window (normal=1, hide=0, 2=Min, 3=max, 4=restore, 5=current, 7=min/inactive, 10=default)

objShell.ShellExecute sPython, sApplication, sDirectory, "runas", 1


'=========================================================================================================================

'=========================================================================================================================
