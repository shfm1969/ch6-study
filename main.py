"""健康記錄管理系統主程式"""
import sys
import tkinter as tk
from gui.main_window import MainWindow


def main():
    """主函數：啟動應用程式"""
    try:
        print("正在啟動應用程式...")
        root = tk.Tk()
        print("主視窗已創建")
        
        # 設置視窗位置到屏幕中央
        width = 550
        height = 550
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        root.geometry(f"{width}x{height}+{x}+{y}")
        root.minsize(500, 500)  # 設置最小尺寸
        
        # 防止視窗被意外關閉時立即退出
        root.protocol("WM_DELETE_WINDOW", lambda: root.quit())
        
        app = MainWindow(root)
        print("應用程式初始化完成，顯示視窗...")
        
        # 確保視窗顯示
        root.deiconify()
        root.lift()
        root.focus_force()
        root.attributes('-topmost', True)
        root.update()
        root.after(100, lambda: root.attributes('-topmost', False))
        
        print("視窗應該已經顯示，請檢查屏幕...")
        print("如果看不到視窗，請嘗試 Alt+Tab 切換")
        
        root.mainloop()
        print("應用程式已關閉")
    except Exception as e:
        print(f"錯誤: {e}")
        import traceback
        traceback.print_exc()
        input("按Enter鍵退出...")
        sys.exit(1)


if __name__ == "__main__":
    main()
