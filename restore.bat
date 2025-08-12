@echo off
setlocal enabledelayedexpansion
set "base=LitBuddy.zip.part_"
set "output=LitBuddy.zip"
if exist "%output%" del "%output%"
for %%f in (%base%*) do (
    echo Adding %%f to %output%
    copy /b "%output%" + "%%f" "%output%" >nul
)
echo.
echo ✅ Rebuild complete: %output%
pause
