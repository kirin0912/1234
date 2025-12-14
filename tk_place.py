import tkinter as tk


def create_window():
    # 主視窗
    root = tk.Tk()
    root.title("Tkinter Place")
    root.geometry("400x300")
    root.resizable(False, False)
    
    # 左側欄
    left_frame = tk.Frame(root, bg='lightgreen')
    left_frame.place(relx=0, rely=0, relwidth=0.1, relheight=1.0)
    
    # 右側欄
    right_frame = tk.Frame(root, bg='lightblue')
    right_frame.place(relx=0.9, rely=0, relwidth=0.1, relheight=1.0)
    
    # 紅色區域
    top_frame = tk.Frame(root, bg='red')
    top_frame.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.2)
    
    # 黃色區域
    middle_frame = tk.Frame(root, bg='yellow')
    middle_frame.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.7)
    
    # 藍色區域
    bottom_frame = tk.Frame(root, bg='blue')
    bottom_frame.place(relx=0.1, rely=0.9, relwidth=0.8, relheight=0.1)
    
    # Labels
    label_left = tk.Label(top_frame, text='left', bg='white', fg='black')
    label_left.place(relx=0.17, rely=0, anchor='n')
    
    label_center = tk.Label(top_frame, text='center', bg='white', fg='black')
    label_center.place(relx=0.5, rely=0, anchor='n')
    
    label_right = tk.Label(top_frame, text='Right', bg='white', fg='black')
    label_right.place(relx=0.83, rely=0, anchor='n')
    
    # 主迴圈
    root.mainloop()


if __name__ == '__main__':
    create_window()
