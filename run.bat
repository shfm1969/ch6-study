@echo off
echo 正在啟動健康記錄管理系統...
python main.py
if errorlevel 1 (
    echo.
    echo 程式執行出錯！
    pause
)

