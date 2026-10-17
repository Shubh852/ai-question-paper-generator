@echo off
set "PATH=%~dp0..\tools\nodejs;%PATH%"
set "NEXT_TELEMETRY_DISABLED=1"
cd /d "%~dp0"
node.exe node_modules\next\dist\bin\next build
