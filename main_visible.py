"""健康記錄管理系統主程式 - 增強可見性版本"""
import sys
import tkinter as tk
from gui.main_window import MainWindow


def main():
    """主函數：啟動應用程式"""
    try:
        print("=" * 60)
        print("正在啟動健康記錄管理系統...")
        print("=" * 60)
        
        root = tk.Tk()
        print("✓ 主視窗已創建")
        
        # 設置視窗位置到屏幕中央
        root.update_idletasks()
        width = 500
        height = 400
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        root.geometry(f"{width}x{height}+{x}+{y}")
        print(f"✓ 視窗位置設置: {width}x{height} 在 ({x}, {y})")
        
        # 防止視窗被意外關閉時立即退出
        root.protocol("WM_DELETE_WINDOW", lambda: (print("視窗關閉請求..."), root.quit()))
        
        print("✓ 正在初始化應用程式界面...")
        app = MainWindow(root)
        print("✓ 應用程式初始化完成")
        
        # 確保視窗顯示
        print("✓ 正在顯示視窗...")
        root.deiconify()
        root.lift()
        root.focus_force()
        
        # 強制置頂一段時間，確保用戶能看到
        root.attributes('-topmost', True)
        root.update()
        print("✓ 視窗已置頂")
        
        # 3秒後取消置頂
        root.after(3000, lambda: root.attributes('-topmost', False))
        
        print("=" * 60)
        print("視窗應該已經顯示在屏幕中央！")
        print("如果看不到視窗，請：")
        print("1. 檢查任務欄是否有應用程式圖標")
        print("2. 按 Alt+Tab 切換到該視窗")
        print("3. 檢查是否有其他顯示器")
        print("4. 視窗會在3秒後取消置頂")
        print("=" * 60)
        print("\n程式正在運行中，請關閉視窗以退出...\n")
        
        root.mainloop()
        print("\n應用程式已關閉")
        
    except Exception as e:
        print(f"\n✗ 錯誤: {e}")
        import traceback
        traceback.print_exc()
        input("\n按Enter鍵退出...")
        sys.exit(1)


if __name__ == "__main__":
    main()

