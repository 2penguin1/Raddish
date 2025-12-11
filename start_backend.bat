@echo off
cd backend
REM Install if sending to someone else, but here we assume installed.
REM ".\venv\Scripts\python.exe" -m pip install -r requirements.txt

echo Starting Backend Server...
".\venv\Scripts\uvicorn.exe" main:app --reload --host 127.0.0.1 --port 8000
pause
