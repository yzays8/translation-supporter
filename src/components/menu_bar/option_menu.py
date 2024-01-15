import os
import sys

import tkinter as tk

from configparser import ConfigParser

from tkinter import ttk

class OptionMenu(tk.Menu):
    CONFIG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../option.ini'))
    sys.path.append(CONFIG_PATH)

    def __init__(self, parent, config: ConfigParser):
        super().__init__(parent, tearoff=0)
        self.parent = parent
        self.root = parent.root

        self.config = config
        self.add_command(label='設定', command=self.handle_open_option)

    def handle_open_option(self):
        self.option_window = tk.Toplevel(self.root)
        self.option_window.title('設定')
        self.option_window.geometry('800x100')
        self.option_window.resizable(False, False)

        if os.path.exists(self.CONFIG_PATH):
            self.config.read(self.CONFIG_PATH)
        else:
            self.config['CLIENT'] = {
                'CLIENT_ID' : 'default',
                'CLIENT_SECRET' : 'default',
                'CLIENT_ACCESS_TOKEN' : 'default'
            }
            self.config['DEFAULT']['Search'] = '0'
            with open(self.CONFIG_PATH, 'w') as configfile:
                self.config.write(configfile)

        ttk.Label(self.option_window, text='Client Access Token :').grid(row=0, column=0, padx=5, pady=5)
        self.textbox_token = ttk.Entry(self.option_window, width=70, show='*')
        self.textbox_token.insert(0, self.config['CLIENT']['CLIENT_ACCESS_TOKEN'])
        self.textbox_token.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.option_window, text='曲リストの検索数         :').grid(row=1, column=0, padx=5, pady=5)
        self.textbox_num = ttk.Entry(self.option_window, width=70)
        self.textbox_num.insert(0, self.config['DEFAULT']['Search'])
        self.textbox_num.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(self.option_window, text='保存', command=self.handle_save).grid(row=2, column=0, pady=5)
        ttk.Button(self.option_window, text='キャンセル', command=self.option_window.destroy).grid(row=2, column=1, pady=5)

        self.option_window.mainloop()

    # TODO Make another class for option window
    def handle_save(self):
        self.config['CLIENT']['CLIENT_ACCESS_TOKEN'] = self.textbox_token.get()
        self.config['DEFAULT']['Search'] = self.textbox_num.get()
        with open(self.CONFIG_PATH, 'w') as configfile:
            self.config.write(configfile)
        self.option_window.destroy()
