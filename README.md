# Tkinter 佈局練習專案

本專案為 1141-Scripting 程式設計課程第 4 次小考作業。

## 專案說明

本專案實作了三種不同的 Tkinter 佈局管理方式：Pack、Grid 與 Place，展示如何使用不同的佈局方法實現相同的視窗介面。

## 檔案結構

```
tk-layout-quiz4/
├── tk_pack.py         # 使用 Pack 佈局管理器
├── tk_grid.py         # 使用 Grid 佈局管理器
├── tk_place.py        # 使用 Place 佈局管理器
├── .gitattributes     # Git 屬性設定
├── .gitignore         # Git 忽略檔案設定
├── LICENSE            # 授權檔案
└── README.md          # 專案說明文件
```

## 功能特色

### 共同特色
- 視窗大小：400x300 像素
- 包含五個色塊區域：
  - 左側欄（淺綠色，寬度 40px）
  - 右側欄（淺藍色，寬度 40px）
  - 上層區域（紅色，高度 60px）
  - 中層區域（黃色，填滿剩餘空間）
  - 下層區域（藍色，高度 30px）
- 在紅色區域內包含三個白底黑字的 Label：left、center、Right
- 支援視窗大小調整（RWD 自適應佈局）

### tk_pack.py
使用 Pack 佈局管理器實作，透過 `side`、`fill` 和 `expand` 參數控制元件排列。

### tk_grid.py
使用 Grid 佈局管理器實作，透過行列配置和權重設定實現佈局。

### tk_place.py
使用 Place 佈局管理器實作，透過相對位置和尺寸（relx、rely、relwidth、relheight）實現響應式佈局。

## 執行方式

### 環境需求
- Python 3.x
- Tkinter（Python 內建函式庫）

### 執行指令

```bash
# 執行 Pack 佈局版本
python tk_pack.py

# 執行 Grid 佈局版本
python tk_grid.py

# 執行 Place 佈局版本
python tk_place.py
```

## 技術重點

### Pack 佈局
- 使用 `pack_propagate(False)` 防止 Frame 被內容縮小
- 透過 `side` 參數控制元件排列方向
- 使用 `fill` 和 `expand` 實現空間填充

### Grid 佈局
- 使用 `rowconfigure` 和 `columnconfigure` 設定行列權重
- 透過 `rowspan` 和 `colspan` 控制跨越多個格子
- 使用 `sticky` 參數控制元件對齊方式

### Place 佈局
- 使用相對座標（relx、rely）和相對尺寸（relwidth、relheight）
- 實現完全響應式的佈局，所有元件隨視窗大小等比例縮放
- 透過 `anchor` 參數控制對齊方式

## 程式碼規範

- 符合 PEP8 編碼規範
- 包含完整的程式碼註解
- 使用有意義的變數命名

## 作者

學生作業專案

## 授權

MIT License
