import tkinter as tk
from tkinter import ttk, filedialog
from tkinter.scrolledtext import ScrolledText
import threading
import os
from console import Console
from get_lyrics import GetLyrics
import configparser

class App(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master, borderwidth=3)
        self.root = master
        self.root.title('Lyrics')
        self.root.geometry('600x900')
        self.pack(fill=tk.BOTH, expand=True)

        # 左上メニューバー作成
        menubar = tk.Menu(self)

        # ファイルメニュー
        menu_file = tk.Menu(menubar, tearoff=0)    # tearoff=0で切り取り線非表示
        menu_file.add_command(label='ファイルを開く', command=self.menu_file_open_click, accelerator='Ctrl+O')
        menu_file.bind_all('<Control-o>', self.menu_file_open_click)
        menu_file.add_command(label='原文を保存', command=self.save_original_lyrics, accelerator='Ctrl+W')
        menu_file.add_command(label='翻訳文を保存', command=self.save_translated_lyrics, accelerator='Ctrl+S')
        menu_file.bind_all('<Control-w>', self.save_original_lyrics)
        menu_file.bind_all('<Control-s>', self.save_translated_lyrics)
        menu_file.add_separator()   # 仕切り線
        menu_file.add_command(label='終了', command=root.destroy)

        # オプションメニュー
        menu_option = tk.Menu(menubar, tearoff=0)
        menu_option.add_command(label='設定', command=self.open_option)

        # メニューバー表示
        menubar.add_cascade(label='ファイル', menu=menu_file)
        menubar.add_cascade(label='オプション', menu=menu_option)
        self.root.config(menu=menubar)

        # フラグ
        self.is_processing = False
        self.is_waiting_song_name = False

        # フィールド
        self.genius = GetLyrics()
        self.artist_name = ''
        self.config = configparser.ConfigParser()
        self.config_path = 'option.ini'

        self.pack_propagate(0)  # フレーム内のウィジェットサイズに合わせてフレームサイズが変化するの防ぐ
        self.create_widgets()

    def create_widgets(self):
        # 原文フレーム
        frame_left = ttk.Frame(self, width=280, height=500, borderwidth=3)
        frame_left.pack_propagate(0)
        frame_left.grid(column=0, row=0, padx=10, pady=5, sticky=tk.W+tk.E+tk.N+tk.S)
        topLabel_frame_left = ttk.Label(frame_left, text='原文')
        topLabel_frame_left.pack(side=tk.TOP)

        self.textbox_frame_left = ScrolledText(frame_left)
        self.textbox_frame_left.pack(fill=tk.BOTH, expand=True)

        # 翻訳文フレーム
        frame_right = ttk.Frame(self, width=280, height=500, borderwidth=3)
        frame_right.pack_propagate(0)

        frame_right.grid(column=1, row=0, padx=10, pady=5, sticky=tk.W+tk.E+tk.N+tk.S)
        topLabel_frame_right = ttk.Label(frame_right, text='翻訳文')
        topLabel_frame_right.pack(side=tk.TOP)

        self.textbox_frame_right = ScrolledText(frame_right)
        self.textbox_frame_right.pack(fill=tk.BOTH, expand=True)

        # コンソールフレーム
        frame_console = ttk.Frame(self, width=540, height=100, borderwidth=3, relief=tk.GROOVE)
        frame_console.pack_propagate(0)
        frame_console.grid(row=1, columnspan=2, padx=10, pady=5, sticky=tk.W+tk.E+tk.N+tk.S)

        self.console_frame_console = ScrolledText(frame_console)
        self.console_frame_console.configure(state='disabled')  # 書き込み禁止
        self.console_frame_console.grid(row=0, sticky=tk.W+tk.E+tk.N+tk.S)
        self.console = Console(self.console_frame_console)
        self.console.write('Enter artist name: ')

        # テキストボックス
        self.textboxvar_frame_console = tk.StringVar(frame_console)
        self.default_text = 'アーティスト名を入力してください...'
        self.textboxvar_frame_console.set(self.default_text)
        self.textbox_frame_console = ttk.Entry(frame_console, textvariable=self.textboxvar_frame_console)
        self.textbox_frame_console.config(foreground='gray')
        self.textbox_frame_console.bind('<Button-1>', self.click_textbox_frame_console)
        self.textbox_frame_console.bind('<Return>', self.enter_textbox_frame_console)

        self.textbox_frame_console.grid(row=1, pady=5, sticky=tk.W+tk.E)

        frame_console.columnconfigure(0, weight=1)
        frame_console.rowconfigure(0, weight=1)
        frame_console.rowconfigure(1, weight=1)

        # 各フレームグリッドの引き伸ばし設定
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        # クリック行のハイライト表示
        self.textbox_frame_left.tag_configure('clicked_line', background='#7cc7e8')
        self.textbox_frame_right.tag_configure('clicked_line', background='#7cc7e8')
        self.textbox_frame_left.bind('<Button-1>', self.highlight_current_line)
        self.textbox_frame_right.bind('<Button-1>', self.highlight_current_line)

        # 原文クリアボタン
        clear_origLyric_button = ttk.Button(frame_left, text='クリア', command=lambda:self.textbox_frame_left.delete(1.0, tk.END))
        clear_origLyric_button.pack(side=tk.BOTTOM, pady=5)

        # 原文保存ボタン
        save_original_button = ttk.Button(frame_left, text='保存', command=self.save_original_lyrics)
        save_original_button.pack(side=tk.BOTTOM, pady=5)

        # 翻訳文クリアボタン
        get_transLyric_button = ttk.Button(frame_right, text='クリア', command=lambda:self.textbox_frame_right.delete(1.0, tk.END))
        get_transLyric_button.pack(side=tk.BOTTOM, pady=5)

        # 翻訳文保存ボタン
        save_translated_button = ttk.Button(frame_right, text='保存', command=self.save_translated_lyrics)
        save_translated_button.pack(side=tk.BOTTOM, pady=5)

    def save_translated_lyrics(self, event=None):
        file = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('テキストファイル', '.txt')], initialdir='./')
        with open(file, 'w') as f:
            f.write(self.textbox_frame_right.get(1.0, tk.END))

    def save_original_lyrics(self, event=None):
        file = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('テキストファイル', '.txt')], initialdir='./')
        with open(file, 'w') as f:
            f.write(self.textbox_frame_left.get(1.0, tk.END))

    def menu_file_open_click(self, event=None):
        file = filedialog.askopenfilename(filetypes=[('テキストファイル', '.txt')], initialdir='./')
        with open(file, 'r') as f:
            self.textbox_frame_right.insert(tk.END, f.read())

    def open_option(self):
        self.option_window = tk.Toplevel(self.root)
        self.option_window.title('設定')
        self.option_window.geometry('450x100')
        self.option_window.resizable(False, False)

        if os.path.exists(self.config_path):
            self.config.read(self.config_path)
        else:
            self.config['CLIENT'] = {
                'CLIENT_ID' : 'default',
                'CLIENT_SECRET' : 'default',
                'CLIENT_ACCESS_TOKEN' : 'default'
            }
            self.config['DEFAULT']['Search'] = '0'
            with open(self.config_path, 'w') as configfile:
                self.config.write(configfile)

        ttk.Label(self.option_window, text='Client Access Token :').grid(row=0, column=0, padx=5, pady=5)
        self.textbox_token = ttk.Entry(self.option_window, width=50)
        self.textbox_token.insert(0, self.config['CLIENT']['CLIENT_ACCESS_TOKEN'])
        self.textbox_token.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.option_window, text='曲リストの検索数 :').grid(row=1, column=0, padx=5, pady=5)
        self.textbox_num = ttk.Entry(self.option_window, width=20)
        self.textbox_num.insert(0, self.config['DEFAULT']['Search'])
        self.textbox_num.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(self.option_window, text='保存', command=self.save_config).grid(row=2, column=0, pady=5)
        ttk.Button(self.option_window, text='キャンセル', command=self.option_window.destroy).grid(row=2, column=1, pady=5)

        self.option_window.mainloop()

    def save_config(self):
        self.config['CLIENT']['CLIENT_ACCESS_TOKEN'] = self.textbox_token.get()
        self.config['DEFAULT']['Search'] = self.textbox_num.get()
        with open(self.config_path, 'w') as configfile:
            self.config.write(configfile)
        self.option_window.destroy()

    def highlight_current_line(self, event):
        line_start = self.textbox_frame_left.index('@%s,%s linestart' % (event.x, event.y))
        line_left_end = self.textbox_frame_left.index('%s lineend' % line_start)
        line_right_end = self.textbox_frame_right.index('%s lineend' % line_start)

        self.textbox_frame_left.tag_remove('clicked_line', 1.0, 'end')
        self.textbox_frame_right.tag_remove('clicked_line', 1.0, 'end')
        self.textbox_frame_left.tag_add('clicked_line', line_start, line_left_end)
        self.textbox_frame_right.tag_add('clicked_line', line_start, line_right_end)

    def click_textbox_frame_console(self, event):
        self.textbox_frame_console.config(foreground='black')
        if self.textbox_frame_console.get() == self.default_text:
            event.widget.delete(0, tk.END)
        else:
            self.textbox_frame_console.config(foreground='black')

    def enter_textbox_frame_console(self, event):
        if threading.active_count() == 1:
            if (self.is_waiting_song_name == False) and (self.is_processing == True):
                self.is_processing = False

            self.config.read(self.config_path)
            self.genius.set_token(self.config['CLIENT']['CLIENT_ACCESS_TOKEN'])

            # アーティスト名の入力待ち
            if (artist_name:=self.textbox_frame_console.get()) != '' and not self.is_processing:
                self.artist_name = artist_name
                self.console.write(artist_name + '\n')
                self.console.write('Enter song name: ')
                self.textbox_frame_console.delete(0, tk.END)
                self.is_waiting_song_name = True
                self.is_processing = True

            # 曲名の入力待ち
            if (song_name:=self.textbox_frame_console.get()) != '' and self.is_waiting_song_name:
                self.is_waiting_song_name = False
                self.textbox_frame_console.delete(0, tk.END)
                self.console.write(song_name + '\n')
                thread = threading.Thread(target=lambda: self.genius.get_lyrics(self.console, self.artist_name, song_name, self.textbox_frame_left)).start()


if __name__  == '__main__':
    root = tk.Tk()
    app = App(master=root)
    app.mainloop()