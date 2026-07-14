@echo off
REM ============================================================
REM  Build portable de Tiempo y Clima (.exe para Windows)
REM  Requisito: tener Python instalado SOLO en esta PC que compila.
REM  El .exe resultante NO necesita Python en la PC que lo use.
REM ============================================================

echo.
echo === Tiempo y Clima - Generador de portable ===
echo.

where python >nul 2>nul
if errorlevel 1 (
    echo [ERROR] No se encontro Python en el PATH.
    echo Instalalo desde https://www.python.org/downloads/ y volve a intentar.
    pause
    exit /b 1
)

echo [1/3] Instalando dependencias necesarias...
python -m pip install --upgrade pyinstaller requests certifi tzdata -q

echo [2/3] Limpiando builds anteriores...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist TiempoYClima.spec del TiempoYClima.spec

echo [3/3] Compilando el .exe portable...
python -m PyInstaller --onefile --windowed --name TiempoYClima --collect-all certifi --collect-all tzdata weather_time_gui.py

echo.
echo ============================================================
echo  LISTO. Tu portable esta en la carpeta "dist":
echo    dist\TiempoYClima.exe
echo.
echo  Es un unico archivo, lo podes mover a cualquier PC con
echo  Windows y funciona sin instalar nada mas (necesita conexion
echo  a internet para traer el clima y la ubicacion).
echo ============================================================
echo.
pause
