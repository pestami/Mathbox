' ====================================================================================
' -adv-cli
' ====================================================================================
Dim poShell
Dim poProcess
Dim iStatus

' ====================================================================================
sPath_scilab="G:\Technik\PROX3\scilab-5.1.1\bin\wScilex.exe"
sScript="G:\Technik\PROX3\Tooling\Programme\Imbach_01\scilab\Plot_Stretch_no_log.sce"

' ====================================================================================

' call %sPath_scilab% -adv-cli  -f %sScript% -nb


sFileName=sPath_scilab &" -adv-cli  -f "& sScript &" -nb"

'msgbox sFileName

Set poShell = CreateObject("WScript.Shell")

 'Set poProcess = poShell.Exec(sFileName)  ' cant min a window with this command
 
 Set poProcess = poShell.Exec("explorer.exe G:\Technik\PROX3\Tooling\Programme\Imbach_01\jpg\")

'Result = poShell.Run(sFileName,0,TRUE)

' ====================================================================================
 
  