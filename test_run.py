"""測試腳本：檢查導入和運行"""
import sys
import traceback

print("開始測試...")
print(f"Python版本: {sys.version}")
print()

# 測試tkinter
try:
    import tkinter as tk
    print("✓ tkinter 導入成功")
except Exception as e:
    print(f"✗ tkinter 導入失敗: {e}")
    traceback.print_exc()
    sys.exit(1)

# 測試utils導入
try:
    from utils import data_manager
    print("✓ utils.data_manager 導入成功")
except Exception as e:
    print(f"✗ utils.data_manager 導入失敗: {e}")
    traceback.print_exc()
    sys.exit(1)

# 測試gui導入
try:
    from gui.main_window import MainWindow
    print("✓ gui.main_window 導入成功")
except Exception as e:
    print(f"✗ gui.main_window 導入失敗: {e}")
    traceback.print_exc()
    sys.exit(1)

# 測試創建視窗
try:
    print("\n嘗試創建視窗...")
    root = tk.Tk()
    root.withdraw()  # 先隱藏視窗
    app = MainWindow(root)
    print("✓ 視窗創建成功")
    print("\n顯示視窗...")
    root.deiconify()  # 顯示視窗
    root.update()
    print("✓ 視窗已顯示")
    print("\n請關閉視窗以繼續...")
    root.mainloop()
    print("✓ 程式正常結束")
except Exception as e:
    print(f"✗ 創建視窗失敗: {e}")
    traceback.print_exc()
    sys.exit(1)

