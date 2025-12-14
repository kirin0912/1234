import tkinter as tk


def create_window():
    # 主視窗
    root = tk.Tk()
    root.title("Tkinter Pack")
    root.geometry("400x300")
    root.resizable(False, False)
    
    # 左側欄
    left_frame = tk.Frame(root, bg='lightgreen', width=40)
    left_frame.pack(side='left', fill='y')
    
    # 右側欄
    right_frame = tk.Frame(root, bg='lightblue', width=40)
    right_frame.pack(side='right', fill='y')
    
    # 紅色區域
    top_frame = tk.Frame(root, bg='red', height=60)
    top_frame.pack(side='top', fill='x')
    top_frame.pack_propagate(False)
    
    # 藍色區域
    bottom_frame = tk.Frame(root, bg='blue', height=30)
    bottom_frame.pack(side='bottom', fill='x')
    bottom_frame.pack_propagate(False)
    
    # 黃色區域
    middle_frame = tk.Frame(root, bg='yellow')
    middle_frame.pack(side='top', fill='both', expand=True)
    
    # Labels
    label_left = tk.Label(top_frame, text='left', bg='white', fg='black')
    label_left.pack(side='left', expand=True, anchor='n', padx=5, pady=2)
    
    label_center = tk.Label(top_frame, text='center', bg='white', fg='black')
    label_center.pack(side='left', expand=True, anchor='n', padx=5, pady=2)
    
    label_right = tk.Label(top_frame, text='Right', bg='white', fg='black')
    label_right.pack(side='left', expand=True, anchor='n', padx=5, pady=2)
    
    # 主迴圈
    root.mainloop()


if __name__ == '__main__':
    create_window()
