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
 sPath_scilab="C:\Program Files\scilab-6.0.0\bin\Scilex.exe"
 ' does not work in non graphics windows
 sPath_scilab="X:\SYM_WINCHILL_Download\010_PortableApps\scilab-6.0.0\bin\Scilex.exe"
 sPath_scilab="X:\SYM_WINCHILL_Download\010_PortableApps\scilab-6.0.0\bin\wScilex.exe"
   
 sScript="X:\SYM_WINCHILL_Download\010-scilab\bar.sce"

' ====================================================================================

' call %sPath_scilab% -adv-cli  -f %sScript% -nb


sFileName=chr(34) & sPath_scilab & chr(34) &" -adv-cli  -f "& sScript &" -nb"

msgbox sFileName

Set poShell = CreateObject("WScript.Shell")

' Set poProcess = poShell.Exec(sFileName)  ' cant min a window with this command



Result = poShell.Run(sFileName,0,FALSE)


msgbox "Wait for SCILAB to start......."

' ====================================================================================
 
   