@echo off
:: =======================================================
:: Auto Setup Script for Windows - LifeSync Report Project
:: =======================================================

title Installing LifeSync Report Dependencies (Windows)

echo =======================================================
echo   Installing All Required Tools for Windows
echo =======================================================
echo.

:: 1. Check Winget
where winget >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] winget is not available on your Windows system.
    echo Please install 'App Installer' from Microsoft Store first.
    pause
    exit /b 1
)

echo [1/4] Installing Hugo Extended...
winget install Hugo.Hugo.Extended --accept-source-agreements --accept-package-agreements

echo [2/4] Installing Pandoc...
winget install JohnMacFarlane.Pandoc --accept-source-agreements --accept-package-agreements

echo [3/4] Installing MiKTeX (LaTeX Engine)...
winget install MiKTeX.MiKTeX --accept-source-agreements --accept-package-agreements

echo [4/4] Installing Python 3 and PyYAML...
winget install Python.Python.3.11 --accept-source-agreements --accept-package-agreements
python -m pip install --upgrade pip
python -m pip install pyyaml

echo.
echo =======================================================
echo   SUCCESS: All requirements for Windows have been installed!
echo   NOTE: Please restart your terminal/cmd to apply PATH changes.
echo =======================================================
pause
