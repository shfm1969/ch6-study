"""記錄輸入視窗模組"""
import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
from utils import data_manager


class RecordWindow:
    def __init__(self, parent):
        try:
            self.parent = parent
            
            self.window = tk.Toplevel(parent)
            self.window.title("新增健康記錄")
            self.window.geometry("450x600")
            self.window.transient(parent)
            self.window.grab_set()
            
            # 居中顯示
            self.center_window()
            
            self.create_widgets()
            self.set_default_datetime()
            
            # 確保視窗顯示
            self.window.lift()
            self.window.focus_force()
        except Exception as e:
            import traceback
            traceback.print_exc()
            messagebox.showerror("錯誤", f"創建記錄視窗時發生錯誤：{e}")
            if hasattr(self, 'window'):
                self.window.destroy()
            raise
    
    def center_window(self):
        """將視窗居中顯示"""
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_widgets(self):
        """創建記錄輸入視窗組件"""
        # 標題
        title_label = tk.Label(
            self.window,
            text="新增健康記錄",
            font=("Microsoft YaHei", 16, "bold"),
            pady=15
        )
        title_label.pack()
        
        # 輸入框架（使用Frame，如果內容過多可以添加滾動條）
        input_frame = tk.Frame(self.window, padx=30, pady=20)
        input_frame.pack(fill="both", expand=True)
        
        # 日期
        tk.Label(
            input_frame,
            text="日期：",
            font=("Microsoft YaHei", 11)
        ).grid(row=0, column=0, sticky="w", pady=8)
        
        self.date_entry = tk.Entry(
            input_frame,
            font=("Microsoft YaHei", 11),
            width=25
        )
        self.date_entry.grid(row=0, column=1, pady=8, padx=10)
        tk.Label(
            input_frame,
            text="格式：YYYY-MM-DD",
            font=("Microsoft YaHei", 9),
            fg="gray"
        ).grid(row=0, column=2, sticky="w")
        
        # 時間
        tk.Label(
            input_frame,
            text="時間：",
            font=("Microsoft YaHei", 11)
        ).grid(row=1, column=0, sticky="w", pady=8)
        
        self.time_entry = tk.Entry(
            input_frame,
            font=("Microsoft YaHei", 11),
            width=25
        )
        self.time_entry.grid(row=1, column=1, pady=8, padx=10)
        tk.Label(
            input_frame,
            text="格式：HH:MM",
            font=("Microsoft YaHei", 9),
            fg="gray"
        ).grid(row=1, column=2, sticky="w")
        
        # 測量位置（下拉選單）
        tk.Label(
            input_frame,
            text="測量位置：",
            font=("Microsoft YaHei", 11)
        ).grid(row=2, column=0, sticky="w", pady=8)
        
        self.location_var = tk.StringVar(value="左臂")
        location_combo = ttk.Combobox(
            input_frame,
            textvariable=self.location_var,
            values=["左臂", "右臂"],
            state="readonly",
            font=("Microsoft YaHei", 11),
            width=22
        )
        location_combo.grid(row=2, column=1, pady=8, padx=10, sticky="w")
        
        # 收縮壓
        tk.Label(
            input_frame,
            text="收縮壓：",
            font=("Microsoft YaHei", 11)
        ).grid(row=3, column=0, sticky="w", pady=8)
        
        self.systolic_entry = tk.Entry(
            input_frame,
            font=("Microsoft YaHei", 11),
            width=25
        )
        self.systolic_entry.grid(row=3, column=1, pady=8, padx=10)
        tk.Label(
            input_frame,
            text="mmHg",
            font=("Microsoft YaHei", 9),
            fg="gray"
        ).grid(row=3, column=2, sticky="w")
        
        # 舒張壓
        tk.Label(
            input_frame,
            text="舒張壓：",
            font=("Microsoft YaHei", 11)
        ).grid(row=4, column=0, sticky="w", pady=8)
        
        self.diastolic_entry = tk.Entry(
            input_frame,
            font=("Microsoft YaHei", 11),
            width=25
        )
        self.diastolic_entry.grid(row=4, column=1, pady=8, padx=10)
        tk.Label(
            input_frame,
            text="mmHg",
            font=("Microsoft YaHei", 9),
            fg="gray"
        ).grid(row=4, column=2, sticky="w")
        
        # 脈搏
        tk.Label(
            input_frame,
            text="脈搏：",
            font=("Microsoft YaHei", 11)
        ).grid(row=5, column=0, sticky="w", pady=8)
        
        self.pulse_entry = tk.Entry(
            input_frame,
            font=("Microsoft YaHei", 11),
            width=25
        )
        self.pulse_entry.grid(row=5, column=1, pady=8, padx=10)
        tk.Label(
            input_frame,
            text="次/分",
            font=("Microsoft YaHei", 9),
            fg="gray"
        ).grid(row=5, column=2, sticky="w")
        
        # 體重
        tk.Label(
            input_frame,
            text="體重：",
            font=("Microsoft YaHei", 11)
        ).grid(row=6, column=0, sticky="w", pady=8)
        
        self.weight_entry = tk.Entry(
            input_frame,
            font=("Microsoft YaHei", 11),
            width=25
        )
        self.weight_entry.grid(row=6, column=1, pady=8, padx=10)
        tk.Label(
            input_frame,
            text="kg",
            font=("Microsoft YaHei", 9),
            fg="gray"
        ).grid(row=6, column=2, sticky="w")
        
        # 體脂率
        tk.Label(
            input_frame,
            text="體脂率：",
            font=("Microsoft YaHei", 11)
        ).grid(row=7, column=0, sticky="w", pady=8)
        
        self.body_fat_entry = tk.Entry(
            input_frame,
            font=("Microsoft YaHei", 11),
            width=25
        )
        self.body_fat_entry.grid(row=7, column=1, pady=8, padx=10)
        tk.Label(
            input_frame,
            text="%",
            font=("Microsoft YaHei", 9),
            fg="gray"
        ).grid(row=7, column=2, sticky="w")
        
        # 按鈕框架
        button_frame = tk.Frame(self.window, pady=20)
        button_frame.pack()
        
        # 保存按鈕
        save_btn = tk.Button(
            button_frame,
            text="保存",
            font=("Microsoft YaHei", 12),
            width=10,
            command=self.save_record
        )
        save_btn.pack(side="left", padx=10)
        
        # 取消按鈕
        cancel_btn = tk.Button(
            button_frame,
            text="取消",
            font=("Microsoft YaHei", 12),
            width=10,
            command=self.window.destroy
        )
        cancel_btn.pack(side="left", padx=10)
    
    def set_default_datetime(self):
        """自動填入當前日期時間"""
        now = datetime.now()
        self.date_entry.insert(0, now.strftime("%Y-%m-%d"))
        self.time_entry.insert(0, now.strftime("%H:%M"))
    
    def validate_number(self, value, field_name, min_val=None, max_val=None):
        """驗證數值輸入"""
        try:
            num = float(value)
            if min_val is not None and num < min_val:
                raise ValueError(f"{field_name}不能小於{min_val}")
            if max_val is not None and num > max_val:
                raise ValueError(f"{field_name}不能大於{max_val}")
            return num
        except ValueError as e:
            if "不能" in str(e):
                raise e
            raise ValueError(f"請輸入有效的{field_name}數值")
    
    def save_record(self):
        """保存記錄"""
        # 獲取輸入值
        date = self.date_entry.get().strip()
        time = self.time_entry.get().strip()
        location = self.location_var.get()
        
        # 驗證日期時間格式
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("錯誤", "請輸入正確的日期格式（YYYY-MM-DD）")
            return
        
        try:
            datetime.strptime(time, "%H:%M")
        except ValueError:
            messagebox.showerror("錯誤", "請輸入正確的時間格式（HH:MM）")
            return
        
        # 驗證數值輸入
        try:
            systolic = self.validate_number(
                self.systolic_entry.get().strip(),
                "收縮壓",
                min_val=0,
                max_val=300
            ) if self.systolic_entry.get().strip() else None
            
            diastolic = self.validate_number(
                self.diastolic_entry.get().strip(),
                "舒張壓",
                min_val=0,
                max_val=200
            ) if self.diastolic_entry.get().strip() else None
            
            pulse = self.validate_number(
                self.pulse_entry.get().strip(),
                "脈搏",
                min_val=0,
                max_val=300
            ) if self.pulse_entry.get().strip() else None
            
            weight = self.validate_number(
                self.weight_entry.get().strip(),
                "體重",
                min_val=0,
                max_val=500
            ) if self.weight_entry.get().strip() else None
            
            body_fat = self.validate_number(
                self.body_fat_entry.get().strip(),
                "體脂率",
                min_val=0,
                max_val=100
            ) if self.body_fat_entry.get().strip() else None
            
        except ValueError as e:
            messagebox.showerror("錯誤", str(e))
            return
        
        # 創建記錄
        record = {
            "date": date,
            "time": time,
            "location": location,
            "blood_pressure_systolic": systolic,
            "blood_pressure_diastolic": diastolic,
            "pulse": pulse,
            "weight": weight,
            "body_fat_percentage": body_fat
        }
        
        # 保存記錄
        if data_manager.add_health_record(record):
            messagebox.showinfo("成功", "記錄已保存")
            self.window.destroy()
        else:
            messagebox.showerror("錯誤", "保存記錄失敗")

