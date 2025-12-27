"""用戶設定視窗模組"""
import tkinter as tk
from tkinter import messagebox
from utils import data_manager


class SettingsWindow:
    def __init__(self, parent, main_window=None):
        self.parent = parent
        self.main_window = main_window
        
        self.window = tk.Toplevel(parent)
        self.window.title("用戶設定")
        self.window.geometry("450x380")
        self.window.transient(parent)
        self.window.grab_set()
        
        self.create_widgets()
        self.load_settings()
        
        # 在創建組件後居中顯示
        self.center_window()
    
    def center_window(self):
        """將視窗居中顯示"""
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_widgets(self):
        """創建設定視窗組件"""
        # 標題
        title_label = tk.Label(
            self.window,
            text="用戶設定",
            font=("Microsoft YaHei", 16, "bold"),
            pady=15
        )
        title_label.pack()
        
        # 輸入框架
        input_frame = tk.Frame(self.window, padx=30, pady=20)
        input_frame.pack(fill="x", padx=10, pady=10)
        
        # 姓名
        tk.Label(
            input_frame,
            text="姓名：",
            font=("Microsoft YaHei", 11)
        ).grid(row=0, column=0, sticky="w", pady=10)
        
        self.name_entry = tk.Entry(
            input_frame,
            font=("Microsoft YaHei", 11),
            width=25
        )
        self.name_entry.grid(row=0, column=1, pady=10, padx=10)
        
        # 身高
        tk.Label(
            input_frame,
            text="身高 (cm)：",
            font=("Microsoft YaHei", 11)
        ).grid(row=1, column=0, sticky="w", pady=10)
        
        self.height_entry = tk.Entry(
            input_frame,
            font=("Microsoft YaHei", 11),
            width=25
        )
        self.height_entry.grid(row=1, column=1, pady=10, padx=10)
        
        # 生日
        tk.Label(
            input_frame,
            text="生日：",
            font=("Microsoft YaHei", 11)
        ).grid(row=2, column=0, sticky="w", pady=10)
        
        self.birthday_entry = tk.Entry(
            input_frame,
            font=("Microsoft YaHei", 11),
            width=25
        )
        self.birthday_entry.grid(row=2, column=1, pady=10, padx=10)
        tk.Label(
            input_frame,
            text="格式：YYYY-MM-DD",
            font=("Microsoft YaHei", 9),
            fg="gray"
        ).grid(row=3, column=1, sticky="w", padx=10)
        
        # 按鈕框架
        button_frame = tk.Frame(self.window, pady=20)
        button_frame.pack(side="bottom", fill="x", padx=20, pady=10)
        
        # 保存按鈕
        save_btn = tk.Button(
            button_frame,
            text="保存",
            font=("Microsoft YaHei", 12),
            width=12,
            height=2,
            command=self.save_settings,
            bg="#4CAF50",
            fg="white"
        )
        save_btn.pack(side="left", padx=10, expand=True, fill="x")
        
        # 取消按鈕
        cancel_btn = tk.Button(
            button_frame,
            text="取消",
            font=("Microsoft YaHei", 12),
            width=12,
            height=2,
            command=self.window.destroy,
            bg="#f44336",
            fg="white"
        )
        cancel_btn.pack(side="left", padx=10, expand=True, fill="x")
    
    def load_settings(self):
        """載入現有設定"""
        settings = data_manager.load_user_settings()
        self.name_entry.insert(0, settings.get("name", ""))
        self.height_entry.insert(0, str(settings.get("height", "")) if settings.get("height") else "")
        self.birthday_entry.insert(0, settings.get("birthday", ""))
    
    def save_settings(self):
        """保存設定"""
        try:
            name = self.name_entry.get().strip()
            height_str = self.height_entry.get().strip()
            birthday = self.birthday_entry.get().strip()
            
            # 驗證身高
            try:
                height = float(height_str) if height_str else 0
                if height < 0:
                    raise ValueError("身高不能為負數")
            except ValueError as e:
                if "不能" in str(e):
                    messagebox.showerror("錯誤", str(e))
                else:
                    messagebox.showerror("錯誤", "請輸入有效的身高數值（cm）")
                return
            
            # 保存設定
            settings = {
                "name": name,
                "height": height,
                "birthday": birthday
            }
            
            print(f"嘗試保存設定: {settings}")
            if data_manager.save_user_settings(settings):
                messagebox.showinfo("成功", "設定已保存")
                if self.main_window:
                    self.main_window.refresh_user_info()
                self.window.destroy()
            else:
                messagebox.showerror("錯誤", "保存設定失敗，請檢查文件權限或磁盤空間")
        except Exception as e:
            import traceback
            traceback.print_exc()
            messagebox.showerror("錯誤", f"保存設定時發生錯誤：{e}")

