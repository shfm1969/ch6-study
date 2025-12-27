"""測試視窗顯示"""
import tkinter as tk
import sys

print("創建測試視窗...")
root = tk.Tk()
root.title("測試視窗 - 如果您看到這個，說明視窗正常顯示")

# 設置視窗大小和位置
root.geometry("400x300")
root.update_idletasks()

# 居中顯示
width = root.winfo_width()
height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - width) // 2
y = (screen_height - height) // 2
root.geometry(f"{width}x{height}+{x}+{y}")

# 添加標籤
label = tk.Label(
    root,
    text="這是測試視窗\n\n如果您能看到這個視窗，\n說明tkinter正常工作！\n\n請關閉此視窗以繼續...",
    font=("Microsoft YaHei", 14),
    justify="center"
)
label.pack(expand=True, fill="both")

# 確保視窗顯示在最前面
root.lift()
root.attributes('-topmost', True)
root.update()
root.after(200, lambda: root.attributes('-topmost', False))

print("視窗已創建並應該顯示在屏幕中央")
print("如果看不到視窗，請：")
print("1. 檢查任務欄")
print("2. 按 Alt+Tab 切換視窗")
print("3. 檢查是否有其他屏幕")
print("\n等待視窗關閉...")

try:
    root.mainloop()
    print("視窗已關閉")
except KeyboardInterrupt:
    print("\n程式被中斷")
    root.destroy()

print("測試完成")

