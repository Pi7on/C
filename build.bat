@echo off
rem todo: check se un file è già presente in src, se si, salva il nome e fai set NAME=nome

rem -------variables-----------------------
set NAME=main
set MINGW_PATH=C:\MINGW\mingw64\bin
set NOTEPAD_PATH=D:\PROGRAMMI\NOTEPAD++\notepad++
set G_FLAGS=-g3
set PATH=%MINGW_PATH%;%PATH%

rem ------paths check-----------------------
if NOT exist "src" (
	mkdir src
	pushd src
	echo. >> %NAME%.cpp
	%NOTEPAD_PATH% %NAME%.cpp
	popd
)
else (
	pushd src
	if NOT exist "*.cpp" (
		echo. >> %NAME%.cpp
		%NOTEPAD_PATH% %NAME%.cpp
	)
	popd
)
if NOT exist "build" (
	mkdir build
)

rem -------compile----------------------------
pushd build
if exist "%NAME%.exe" (
    del %NAME%.exe
)
popd 

cls
echo compiling...
g++ %G_FLAGS% src\%NAME%.cpp -o build\%NAME%.exe

rem ------launch exe-------------------------
rem note: /c flag closes the window as soon as the program finishes
rem note: deleting the exe after execution so it doesn't launch is compilation fails
pushd build
if exist "%NAME%.exe" (
    start cmd /C %NAME%.exe
)
popd
