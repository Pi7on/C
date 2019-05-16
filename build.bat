@echo off

rem -------variables-----------------------
set EXE_NAME="test.exe"
set MINGW_PATH="C:\MINGW\mingw64\bin"
set G_FLAGS="-g3"

set PATH=%MINGW_PATH%;%PATH%

rem ------paths check-----------------------
if NOT exist "build" (
	mkdir build
)


rem -------compile----------------------------
pushd build
if exist %EXE_NAME% (
    del %EXE_NAME%
)
cls
echo compiling...
g++ %G_FLAGS% ..\src\test.cpp -o %EXE_NAME%

rem ------launch exe-------------------------
rem note: /c flag closes the window as soon as the program finishes
rem note: deleting the exe after execution so it doesn't launch is compilation fails

if exist %EXE_NAME% (
    start cmd /C %EXE_NAME%
)
popd