"""健康記錄管理系統主程式"""
import tkinter as tk
from gui.main_window import MainWindow


def main():
    """主函數：啟動應用程式"""
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
