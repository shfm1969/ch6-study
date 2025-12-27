"""簡單的tkinter測試"""
import tkinter as tk

print("測試1: 導入tkinter...")
try:
    root = tk.Tk()
    print("✓ tkinter視窗創建成功")
    
    root.title("測試視窗")
    root.geometry("300x200")
    
    label = tk.Label(root, text="如果您看到這個視窗，\n說明tkinter正常工作！", font=("Microsoft YaHei", 12))
    label.pack(expand=True)
    
    print("顯示視窗...")
    root.lift()
    root.attributes('-topmost', True)
    root.update()
    root.after(100, lambda: root.attributes('-topmost', False))
    
    print("進入主循環...")
    root.mainloop()
    print("視窗已關閉")
except Exception as e:
    print(f"錯誤: {e}")
    import traceback
    traceback.print_exc()
    input("按Enter鍵退出...")

