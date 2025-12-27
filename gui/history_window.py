"""歷史記錄查看視窗模組"""
import tkinter as tk
from tkinter import ttk, messagebox
from utils import data_manager


class HistoryWindow:
    def __init__(self, parent):
        self.parent = parent
        
        self.window = tk.Toplevel(parent)
        self.window.title("歷史記錄")
        self.window.geometry("1000x600")
        self.window.transient(parent)
        
        self.create_widgets()
        self.load_records()
    
    def create_widgets(self):
        """創建歷史記錄視窗組件"""
        # 標題和刷新按鈕框架
        header_frame = tk.Frame(self.window, pady=10)
        header_frame.pack(fill="x", padx=10)
        
        title_label = tk.Label(
            header_frame,
            text="歷史記錄",
            font=("Microsoft YaHei", 16, "bold")
        )
        title_label.pack(side="left")
        
        refresh_btn = tk.Button(
            header_frame,
            text="刷新",
            font=("Microsoft YaHei", 10),
            command=self.load_records
        )
        refresh_btn.pack(side="right", padx=10)
        
        # 表格框架
        table_frame = tk.Frame(self.window)
        table_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # 創建表格
        columns = (
            "日期", "時間", "測量位置", "收縮壓", "舒張壓",
            "脈搏", "體重", "體脂率"
        )
        
        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=20
        )
        
        # 設定欄位標題和寬度
        column_widths = {
            "日期": 100,
            "時間": 80,
            "測量位置": 80,
            "收縮壓": 80,
            "舒張壓": 80,
            "脈搏": 80,
            "體重": 80,
            "體脂率": 80
        }
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=column_widths.get(col, 100), anchor="center")
        
        # 滾動條
        scrollbar_y = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.tree.yview
        )
        scrollbar_x = ttk.Scrollbar(
            table_frame,
            orient="horizontal",
            command=self.tree.xview
        )
        
        self.tree.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
        
        # 佈局
        self.tree.grid(row=0, column=0, sticky="nsew")
        scrollbar_y.grid(row=0, column=1, sticky="ns")
        scrollbar_x.grid(row=1, column=0, sticky="ew")
        
        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)
        
        # 按鈕框架
        button_frame = tk.Frame(self.window, pady=10)
        button_frame.pack()
        
        # 刪除按鈕
        delete_btn = tk.Button(
            button_frame,
            text="刪除選中記錄",
            font=("Microsoft YaHei", 11),
            command=self.delete_selected_record,
            bg="#ff6b6b",
            fg="white"
        )
        delete_btn.pack(side="left", padx=10)
        
        # 關閉按鈕
        close_btn = tk.Button(
            button_frame,
            text="關閉",
            font=("Microsoft YaHei", 11),
            command=self.window.destroy
        )
        close_btn.pack(side="left", padx=10)
    
    def load_records(self):
        """載入並顯示所有記錄"""
        # 清空現有數據
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # 初始化記錄映射
        self.record_map = {}  # 用於存儲item_id到記錄的映射
        
        # 載入記錄
        records = data_manager.get_all_records()
        
        # 按日期和時間排序（最新的在前）
        records.sort(key=lambda x: (x.get("date", ""), x.get("time", "")), reverse=True)
        
        # 插入數據，並存儲記錄的唯一標識
        for i, record in enumerate(records):
            values = (
                record.get("date", ""),
                record.get("time", ""),
                record.get("location", ""),
                self.format_value(record.get("blood_pressure_systolic")),
                self.format_value(record.get("blood_pressure_diastolic")),
                self.format_value(record.get("pulse")),
                self.format_value(record.get("weight")),
                self.format_value(record.get("body_fat_percentage"))
            )
            item_id = self.tree.insert("", "end", values=values)
            # 使用日期+時間+位置作為唯一標識
            record_key = (
                record.get("date", ""),
                record.get("time", ""),
                record.get("location", "")
            )
            self.record_map[item_id] = record_key
    
    def format_value(self, value):
        """格式化數值顯示"""
        if value is None:
            return "-"
        if isinstance(value, float):
            return f"{value:.1f}"
        return str(value)
    
    def delete_selected_record(self):
        """刪除選中的記錄"""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("警告", "請先選擇要刪除的記錄")
            return
        
        # 確認刪除
        if not messagebox.askyesno("確認", "確定要刪除選中的記錄嗎？"):
            return
        
        # 獲取選中項目的記錄標識
        item = selected_item[0]
        if item not in self.record_map:
            messagebox.showerror("錯誤", "無法找到對應的記錄")
            return
        
        record_key = self.record_map[item]
        date, time, location = record_key
        
        # 從所有記錄中找到並刪除
        all_records = data_manager.get_all_records()
        for i, record in enumerate(all_records):
            if (record.get("date") == date and
                record.get("time") == time and
                record.get("location") == location):
                if data_manager.delete_record(i):
                    messagebox.showinfo("成功", "記錄已刪除")
                    self.load_records()
                else:
                    messagebox.showerror("錯誤", "刪除記錄失敗")
                return
        
        messagebox.showerror("錯誤", "找不到要刪除的記錄")

