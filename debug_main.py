"""調試版本的主程式"""
import sys
import os

print("=" * 50)
print("健康記錄管理系統 - 調試模式")
print("=" * 50)
print(f"Python版本: {sys.version}")
print(f"工作目錄: {os.getcwd()}")
print()

# 測試導入
print("步驟1: 測試tkinter導入...")
try:
    import tkinter as tk
    print("  ✓ tkinter導入成功")
except Exception as e:
    print(f"  ✗ tkinter導入失敗: {e}")
    import traceback
    traceback.print_exc()
    input("\n按Enter鍵退出...")
    sys.exit(1)

print("\n步驟2: 測試utils模組導入...")
try:
    from utils import data_manager
    print("  ✓ utils.data_manager導入成功")
except Exception as e:
    print(f"  ✗ utils.data_manager導入失敗: {e}")
    import traceback
    traceback.print_exc()
    input("\n按Enter鍵退出...")
    sys.exit(1)

print("\n步驟3: 測試gui模組導入...")
try:
    from gui.main_window import MainWindow
    print("  ✓ gui.main_window導入成功")
except Exception as e:
    print(f"  ✗ gui.main_window導入失敗: {e}")
    import traceback
    traceback.print_exc()
    input("\n按Enter鍵退出...")
    sys.exit(1)

print("\n步驟4: 創建主視窗...")
try:
    root = tk.Tk()
    print("  ✓ Tk根視窗創建成功")
    
    app = MainWindow(root)
    print("  ✓ MainWindow初始化成功")
    
    print("\n步驟5: 顯示視窗...")
    root.lift()
    root.attributes('-topmost', True)
    root.update()
    root.after(100, lambda: root.attributes('-topmost', False))
    print("  ✓ 視窗應該已經顯示")
    print("\n" + "=" * 50)
    print("如果視窗沒有出現，請檢查：")
    print("1. 視窗是否在另一個屏幕或桌面")
    print("2. 任務欄是否有應用程式圖標")
    print("3. Alt+Tab是否可以切換到該視窗")
    print("=" * 50)
    print("\n進入主循環...")
    root.mainloop()
    print("\n程式正常結束")
    
except Exception as e:
    print(f"  ✗ 創建視窗失敗: {e}")
    import traceback
    traceback.print_exc()
    input("\n按Enter鍵退出...")
    sys.exit(1)

