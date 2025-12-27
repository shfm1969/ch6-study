"""數據管理模組：處理用戶設定和健康記錄的讀寫"""
import json
import os
from pathlib import Path
from typing import Dict, List, Optional

# 數據文件路徑
DATA_DIR = Path(__file__).parent.parent / "data"
SETTINGS_FILE = DATA_DIR / "user_settings.json"
RECORDS_FILE = DATA_DIR / "health_records.json"


def ensure_data_dir():
    """確保數據目錄存在"""
    DATA_DIR.mkdir(exist_ok=True)


def load_user_settings() -> Dict[str, any]:
    """載入用戶設定"""
    ensure_data_dir()
    if SETTINGS_FILE.exists():
        try:
            with open(SETTINGS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    
    # 返回默認設定
    return {
        "name": "",
        "height": 0,
        "birthday": ""
    }


def save_user_settings(settings: Dict[str, any]) -> bool:
    """保存用戶設定"""
    try:
        ensure_data_dir()
        with open(SETTINGS_FILE, 'w', encoding='utf-8') as f:
            json.dump(settings, f, ensure_ascii=False, indent=2)
        return True
    except IOError:
        return False


def load_health_records() -> List[Dict[str, any]]:
    """載入健康記錄列表"""
    ensure_data_dir()
    if RECORDS_FILE.exists():
        try:
            with open(RECORDS_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get("records", [])
        except (json.JSONDecodeError, IOError):
            pass
    
    return []


def save_health_records(records: List[Dict[str, any]]) -> bool:
    """保存健康記錄列表"""
    try:
        ensure_data_dir()
        data = {"records": records}
        with open(RECORDS_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except IOError:
        return False


def add_health_record(record: Dict[str, any]) -> bool:
    """添加新的健康記錄"""
    records = load_health_records()
    records.append(record)
    return save_health_records(records)


def get_all_records() -> List[Dict[str, any]]:
    """獲取所有健康記錄"""
    return load_health_records()


def delete_record(index: int) -> bool:
    """刪除指定索引的記錄"""
    records = load_health_records()
    if 0 <= index < len(records):
        records.pop(index)
        return save_health_records(records)
    return False

