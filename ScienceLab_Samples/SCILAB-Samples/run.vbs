' ====================================================================================
' -adv-cli
' Program called by XLS for IMPEX machine
' ====================================================================================
Dim poShell
Dim poProcess
Dim iStatus

' ====================================================================================
' sPath_scilab="G:\Technik\PROX3\scilab-5.1.1\bin\Scilex.exe"
' Run non graphics version of scilab
 sPath_scilab="G:\Technik\PROX3\PortableApps\scilab-5.3.2\bin\Scilex.exe"
 sScript="G:\Technik\PROX3\Tooling\Programme\Imbach_01\scilab\Plot_Stretch.sce"

' ====================================================================================

' call %sPath_scilab% -adv-cli  -f %sScript% -nb


sFileName=sPath_scilab &" -adv-cli  -f "& sScript &" -nb"

'msgbox sFileName

Set poShell = CreateObject("WScript.Shell")

' Set poProcess = poShell.Exec(sFileName)  ' cant min a window with this command

Result = poShell.Run(sFileName,0,TRUE)

' ====================================================================================
 
   