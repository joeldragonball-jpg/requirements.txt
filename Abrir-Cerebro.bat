@echo off
chcp 65001 >nul
title Panel informativo - app local
cd /d "%~dp0"

echo.
echo  ===============================================
echo    PANEL INFORMATIVO  (app local: Cerebro, Seguimiento,
echo    Privado)  -  http://localhost:8791
echo  ===============================================
echo.

where uv >nul 2>nul
if errorlevel 1 (
  echo  No encuentro "uv". Instalalo una vez con:
  echo      powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 ^| iex"
  echo  y vuelve a abrir este archivo.
  echo.
  pause
  exit /b 1
)

echo  Actualizando desde GitHub (los bots anaden cosas)...
git pull --ff-only >nul 2>nul && echo  Actualizado. || echo  No se pudo actualizar (sin internet o cambios locales): sigo con lo que hay.
echo.

rem Si ya esta abierta en el puerto 8791, solo abre el navegador
netstat -ano | findstr /R /C:":8791 .*LISTENING" >nul
if not errorlevel 1 (
  echo  La app ya esta en marcha. Abriendo el navegador...
  start "" http://localhost:8791
  ping -n 4 127.0.0.1 >nul
  exit /b 0
)

echo  Arrancando (la primera vez tarda un poco)... No cierres esta ventana mientras la uses.
echo  Para parar la app: cierra esta ventana o pulsa Ctrl+C.
echo.
start "" /b cmd /c "ping -n 9 127.0.0.1 >nul & start http://localhost:8791"
uv run --with-requirements requirements.txt --with tzdata streamlit run app.py --server.port 8791 --server.headless true --browser.gatherUsageStats false

echo.
echo  La app se ha cerrado.
pause
