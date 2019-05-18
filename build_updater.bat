@echo off

powershell -Command "Invoke-WebRequest https://raw.githubusercontent.com/Pi7on/C/master/build.bat -OutFile build_new.bat"

if exist "build_new.bat" (
	echo Downlaod succesful!
	del build.bat
	ren build_new.bat build.bat
	goto:END
)


echo download failed!


:END