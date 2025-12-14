import tkinter as tk


def create_window():
    # 主視窗
    root = tk.Tk()
    root.title("Tkinter Grid")
    root.geometry("400x300")
    root.resizable(False, False)
    
    # Grid 配置
    root.rowconfigure(0, weight=0, minsize=60)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=0, minsize=30)
    root.columnconfigure(0, weight=0, minsize=40)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=0, minsize=40)
    
    # 左側欄
    left_frame = tk.Frame(root, bg='lightgreen')
    left_frame.grid(row=0, column=0, rowspan=3, sticky='nsew')
    
    # 右側欄
    right_frame = tk.Frame(root, bg='lightblue')
    right_frame.grid(row=0, column=2, rowspan=3, sticky='nsew')
    
    # 紅色區域
    top_frame = tk.Frame(root, bg='red')
    top_frame.grid(row=0, column=1, sticky='nsew')
    
    # 黃色區域
    middle_frame = tk.Frame(root, bg='yellow')
    middle_frame.grid(row=1, column=1, sticky='nsew')
    
    # 藍色區域
    bottom_frame = tk.Frame(root, bg='blue')
    bottom_frame.grid(row=2, column=1, sticky='nsew')
    
    # Labels
    top_frame.columnconfigure(0, weight=1)
    top_frame.columnconfigure(1, weight=1)
    top_frame.columnconfigure(2, weight=1)
    
    label_left = tk.Label(top_frame, text='left', bg='white', fg='black')
    label_left.grid(row=0, column=0, sticky='n', padx=5, pady=2)
    
    label_center = tk.Label(top_frame, text='center', bg='white', fg='black')
    label_center.grid(row=0, column=1, sticky='n', padx=5, pady=2)
    
    label_right = tk.Label(top_frame, text='Right', bg='white', fg='black')
    label_right.grid(row=0, column=2, sticky='n', padx=5, pady=2)
    
    # 主迴圈
    root.mainloop()


if __name__ == '__main__':
    create_window()
