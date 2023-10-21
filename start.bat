@echo off

:: 파이썬 설치 확인
where python >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo Python is already installed.
) else (
    echo Installing Python...
    winget install Python.Python.3.11
    if %ERRORLEVEL% EQU 0 (
        echo Python installed successfully.
    ) else (
        echo Failed to install Python.
        exit /b 1
    )
)

:: 가상환경 설정
echo Setting up virtual environment...
python -m venv venv
if %ERRORLEVEL% EQU 0 (
    echo Virtual environment set up successfully.
) else (
    echo Failed to set up virtual environment.
    exit /b 1
)

:: 가상환경 활성화
call venv\Scripts\activate

:: requirements.txt 설치
echo Installing requirements...
pip install -r requirements.txt
if %ERRORLEVEL% EQU 0 (
    echo Requirements installed successfully.
) else (
    echo Failed to install requirements.
    exit /b 1
)

:: index.py 실행
echo Running index.py...
python index.py
if %ERRORLEVEL% EQU 0 (
    echo Successfully ran index.py.
) else (
    echo Failed to run index.py.
    exit /b 1
)