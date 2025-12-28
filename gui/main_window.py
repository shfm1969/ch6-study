"""主視窗模組"""
import tkinter as tk
from tkinter import ttk
from utils import data_manager


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("健康記錄管理系統")
        # 不在此處設置geometry，讓main.py處理位置
        
        # 存儲其他視窗的引用
        self.settings_window = None
        self.record_window = None
        self.history_window = None
        
        self.create_widgets()
        self.refresh_user_info()
        
        # 確保視窗內容已更新
        self.root.update_idletasks()
    
    def create_widgets(self):
        """創建主視窗組件"""
        # 標題
        title_label = tk.Label(
            self.root,
            text="健康記錄管理系統",
            font=("Microsoft YaHei", 20, "bold"),
            pady=20
        )
        title_label.pack()
        
        # 用戶資訊框架
        info_frame = tk.LabelFrame(
            self.root,
            text="用戶資訊",
            font=("Microsoft YaHei", 12),
            padx=20,
            pady=15
        )
        info_frame.pack(pady=10, padx=20, fill="x", anchor="n")
        
        self.name_label = tk.Label(
            info_frame,
            text="姓名：未設定",
            font=("Microsoft YaHei", 11),
            anchor="w"
        )
        self.name_label.pack(fill="x", pady=5)
        
        self.height_label = tk.Label(
            info_frame,
            text="身高：未設定",
            font=("Microsoft YaHei", 11),
            anchor="w"
        )
        self.height_label.pack(fill="x", pady=5)
        
        self.birthday_label = tk.Label(
            info_frame,
            text="生日：未設定",
            font=("Microsoft YaHei", 11),
            anchor="w"
        )
        self.birthday_label.pack(fill="x", pady=5)
        
        # 功能按鈕框架
        button_frame = tk.Frame(self.root)
        button_frame.pack(fill="x", padx=20, pady=20)
        
        # 設定按鈕
        settings_btn = tk.Button(
            button_frame,
            text="用戶設定",
            font=("Microsoft YaHei", 12),
            width=15,
            height=2,
            command=self.open_settings,
            bg="#2196F3",
            fg="white"
        )
        settings_btn.pack(side="left", padx=5, expand=True, fill="both")
        
        # 新增記錄按鈕
        record_btn = tk.Button(
            button_frame,
            text="新增記錄",
            font=("Microsoft YaHei", 12),
            width=15,
            height=2,
            command=self.open_record,
            bg="#4CAF50",
            fg="white"
        )
        record_btn.pack(side="left", padx=5, expand=True, fill="both")
        
        # 查看歷史按鈕
        history_btn = tk.Button(
            button_frame,
            text="查看歷史",
            font=("Microsoft YaHei", 12),
            width=15,
            height=2,
            command=self.open_history,
            bg="#FF9800",
            fg="white"
        )
        history_btn.pack(side="left", padx=5, expand=True, fill="both")
    
    def refresh_user_info(self):
        """刷新用戶資訊顯示"""
        settings = data_manager.load_user_settings()
        
        name = settings.get("name", "")
        height = settings.get("height", 0)
        birthday = settings.get("birthday", "")
        
        self.name_label.config(text=f"姓名：{name if name else '未設定'}")
        self.height_label.config(text=f"身高：{height if height else '未設定'} cm")
        self.birthday_label.config(text=f"生日：{birthday if birthday else '未設定'}")
    
    def open_settings(self):
        """打開設定視窗"""
        if self.settings_window is None or not self.settings_window.window.winfo_exists():
            from .settings_window import SettingsWindow
            self.settings_window = SettingsWindow(self.root, self)
        else:
            self.settings_window.window.lift()
    
    def open_record(self):
        """打開記錄輸入視窗"""
        try:
            if self.record_window is None or not self.record_window.window.winfo_exists():
                from .record_window import RecordWindow
                self.record_window = RecordWindow(self.root)
            else:
                self.record_window.window.lift()
        except Exception as e:
            import traceback
            traceback.print_exc()
            from tkinter import messagebox
            messagebox.showerror("錯誤", f"無法打開記錄輸入視窗：{e}")
    
    def open_history(self):
        """打開歷史記錄視窗"""
        if self.history_window is None or not self.history_window.window.winfo_exists():
            from .history_window import HistoryWindow
            self.history_window = HistoryWindow(self.root)
        else:
            self.history_window.window.lift()

