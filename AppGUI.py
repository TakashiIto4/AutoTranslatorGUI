# -*- coding:utf-8 -*-
import tkinter as tk
from tkinter import filedialog
# import customtkinter as ctk
import subprocess
from main import translator
import configparser
import time

# iniファイルの読み込み
batchConfig = configparser.ConfigParser() 
batchConfig.read('batch.ini')
cloudConfig = configparser.ConfigParser()
cloudConfig.read('cloud_service_settings.ini')

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master.title("動画・字幕翻訳ツール")  # ウィンドウタイトル
        self.master.geometry("600x400")  # ウィンドウサイズ(幅x高さ)
        
        self.video_file_path = ''  # 動画ファイルパスを格納する変数
        self.subtitle_file_path = ''  # 字幕ファイルパスを格納する変数

        self.create_widgets()

    def create_widgets(self):
        #---------------------------------------
        #  ファイル選択
        # --------------------------------------------------------
        # ファイル選択用Frame
        self.frame_file = tk.Frame(self.master)
        self.frame_file.pack()

        lbl_movie = tk.Label(self.frame_file, text="動画ファイル")
        lbl_sub = tk.Label(self.frame_file, text="字幕ファイル")

        self.entry1 = tk.Entry(self.frame_file, width=70)
        self.entry2 = tk.Entry(self.frame_file, width=70)

        button_mov = tk.Button(self.frame_file, text="選択", command=self.select_mov_path)
        button_sub = tk.Button(self.frame_file, text="選択", command=self.select_sub_path)

        # --------------------------------------------------------
        # 配置
        lbl_movie.grid(row=0, column=0)
        lbl_sub.grid(row=1, column=0)

        self.entry1.grid(row=0, column=1)
        self.entry2.grid(row=1, column=1)

        button_mov.grid(row=0, column=2)
        button_sub.grid(row=1, column=2)

        #---------------------------------------
        #  言語選択
        # --------------------------------------------------------
        # 言語選択用Frame
        self.frame_lang = tk.Frame(self.master)
        self.frame_lang.pack()

        # --------------------------------------------------------
        # 言語選択ボタン
        self.lang_dict = {'en' : [0, tk.BooleanVar()], 
                         'es' : [1, tk.BooleanVar()], 
                         'hi' : [2, tk.BooleanVar()],
                         'ar' : [3, tk.BooleanVar()],
                         'ru' : [4, tk.BooleanVar()],
                         'pt' : [5, tk.BooleanVar()],
                         'it' : [6, tk.BooleanVar()],
                         'id' : [7, tk.BooleanVar()],
                         'ja' : [8, tk.BooleanVar()],
                         'ko' : [9, tk.BooleanVar()],
                         'de' : [10, tk.BooleanVar()],
                         'zh' : [11, tk.BooleanVar()],
                         'tr' : [12, tk.BooleanVar()]}
        chk_en = tk.Checkbutton(self.frame_lang, text='英語', variable=self.lang_dict['en'][1])
        chk_es = tk.Checkbutton(self.frame_lang, text='スペイン語', variable=self.lang_dict['es'][1])
        chk_hi = tk.Checkbutton(self.frame_lang, text='ヒンディー語', variable=self.lang_dict['hi'][1])
        chk_ar = tk.Checkbutton(self.frame_lang, text='アラビア語', variable=self.lang_dict['ar'][1])
        chk_ru = tk.Checkbutton(self.frame_lang, text='ロシア語', variable=self.lang_dict['ru'][1])
        chk_pt = tk.Checkbutton(self.frame_lang, text='ポルトガル語', variable=self.lang_dict['pt'][1])
        chk_it = tk.Checkbutton(self.frame_lang, text='イタリア語', variable=self.lang_dict['it'][1])
        chk_id = tk.Checkbutton(self.frame_lang, text='インドネシア語', variable=self.lang_dict['id'][1])
        chk_ja = tk.Checkbutton(self.frame_lang, text='日本語', variable=self.lang_dict['ja'][1])
        chk_ko = tk.Checkbutton(self.frame_lang, text='韓国語', variable=self.lang_dict['ko'][1])
        chk_de = tk.Checkbutton(self.frame_lang, text='ドイツ語', variable=self.lang_dict['de'][1])
        chk_zh = tk.Checkbutton(self.frame_lang, text='中国語', variable=self.lang_dict['zh'][1])
        chk_tr = tk.Checkbutton(self.frame_lang, text='トルコ語', variable=self.lang_dict['tr'][1])

        # --------------------------------------------------------
        # 配置
        chk_en.grid(row=5, column=0, sticky=tk.W)
        chk_es.grid(row=5, column=1, sticky=tk.W)
        chk_hi.grid(row=5, column=2, sticky=tk.W)
        chk_ar.grid(row=5, column=3, sticky=tk.W)
        chk_ru.grid(row=6, column=0, sticky=tk.W)
        chk_pt.grid(row=6, column=1, sticky=tk.W)
        chk_it.grid(row=6, column=2, sticky=tk.W)
        chk_id.grid(row=6, column=3, sticky=tk.W)
        chk_ko.grid(row=7, column=0, sticky=tk.W)
        chk_de.grid(row=7, column=1, sticky=tk.W)
        chk_zh.grid(row=7, column=2, sticky=tk.W)
        chk_tr.grid(row=7, column=3, sticky=tk.W)


        #---------------------------------------
        #  設定
        # --------------------------------------------------------
        # 設定用Frame
        self.frame_setting = tk.Frame(self.master)
        self.frame_setting.pack()

        #---------------------------------------
        #  認証
        # --------------------------------------------------------
        # 認証用Frame
        self.frame_auth = tk.Frame(self.master)
        self.frame_auth.pack()

        # --------------------------------------------------------
        # 翻訳クラウドサービス
        self.frame_auth_tr = tk.Frame(self.frame_auth)
        self.frame_auth_tr.pack()
        lbl_translator = tk.Label(self.frame_auth_tr, text="翻訳サービス")
        self.preferredTranslateService = tk.StringVar()
        try:
            self.preferredTranslateService.set(cloudConfig['CLOUD']['translate_service']) #前回選択されたサービスを初期値に選択
        except:
            self.preferredTranslateService.set(None)

        radio_translator_google = tk.Radiobutton(self.frame_auth_tr, text='google', value='google', variable=self.preferredTranslateService, command=self.set_TranslateService)
        radio_translator_deepl = tk.Radiobutton(self.frame_auth_tr, text='deepl', value='deepl', variable=self.preferredTranslateService, command=self.set_TranslateService)

        lbl_google_project_id = tk.Label(self.frame_auth_tr, text="Google Project ID")
        self.entry_google_project_id = tk.Entry(self.frame_auth_tr, width=50)
        try:
            self.entry_google_project_id.insert(tk.END, cloudConfig['CLOUD']['google_project_id']) #Keyを設定済の場合はそれを表示
        except:
            pass
        button_google_project_id = tk.Button(self.frame_auth_tr, 
                                             text='更新', 
                                             command=lambda:self.update_cloud_ini('google_project_id', self.entry_google_project_id, 'Google Project ID'))

        lbl_deepl_api_key = tk.Label(self.frame_auth_tr, text='DeepL API Key')
        self.entry_deepl_api_key = tk.Entry(self.frame_auth_tr, width=50)
        try:
            self.entry_deepl_api_key.insert(tk.END, cloudConfig['CLOUD']['deepl_api_key']) #Keyを設定済の場合はそれを表示
        except:
            pass
        button_deepl_api_key = tk.Button(self.frame_auth_tr, 
                                         text='更新', 
                                         command=lambda:self.update_cloud_ini('deepl_api_key', self.entry_deepl_api_key, 'DeepL API Key'))

        lbl_translator.grid(row=0, column=0)

        radio_translator_google.grid(row=1, column=1)
        lbl_google_project_id.grid(row=1, column=2)
        self.entry_google_project_id.grid(row=1, column=3)
        button_google_project_id.grid(row=1, column=4)

        radio_translator_deepl.grid(row=2, column=1)
        lbl_deepl_api_key.grid(row=2, column=2)
        self.entry_deepl_api_key.grid(row=2, column=3)
        button_deepl_api_key.grid(row=2, column=4)



        # --------------------------------------------------------
        # 読み上げクラウドサービス
        self.frame_auth_sp = tk.Frame(self.frame_auth)
        self.frame_auth_sp.pack()
        lbl_speech = tk.Label(self.frame_auth_sp, text="読み上げサービス")
        self.ttsService = tk.StringVar()
        try:
            self.ttsService.set(cloudConfig['CLOUD']['tts_service']) #前回選択されたサービスを初期値に選択
        except:
            self.ttsService.set(None)

        radio_speech_google = tk.Radiobutton(self.frame_auth_sp, text='google', value='google', variable=self.ttsService, command=self.set_ttsService)
        radio_speech_azure = tk.Radiobutton(self.frame_auth_sp, text='azure', value='azure', variable=self.ttsService, command=self.set_ttsService)

        lbl_google_project_id_sp = tk.Label(self.frame_auth_sp, text="Google Project ID")
        self.entry_google_project_id_sp = tk.Entry(self.frame_auth_sp, width=50)
        try:
            self.entry_google_project_id_sp.insert(tk.END, cloudConfig['CLOUD']['google_project_id']) #Keyを設定済の場合はそれを表示
        except:
            pass
        button_google_project_id_sp = tk.Button(self.frame_auth_sp, 
                                                text='更新', 
                                                command=lambda:self.update_cloud_ini('google_project_id', self.entry_google_project_id_sp, 'Google Project ID'))

        lbl_azure_speech_key = tk.Label(self.frame_auth_sp, text="Azure API Key")
        self.entry_azure_speech_key = tk.Entry(self.frame_auth_sp, width=50)
        try:
            self.entry_azure_speech_key.insert(tk.END, cloudConfig['CLOUD']['azure_speech_key']) #Keyを設定済の場合はそれを表示
        except:
            pass
        button_azure_speech_key = tk.Button(self.frame_auth_sp, 
                                            text='更新', 
                                            command=lambda:self.update_cloud_ini('azure_speech_key', self.entry_azure_speech_key, 'Azure API Key'))

        lbl_speech.grid(row=0, column=0)

        radio_speech_google.grid(row=1, column=1)
        lbl_google_project_id_sp.grid(row=1, column=2)
        self.entry_google_project_id_sp.grid(row=1, column=3)
        button_google_project_id_sp.grid(row=1, column=4)

        radio_speech_azure.grid(row=2, column=1)
        lbl_azure_speech_key.grid(row=2, column=2)
        self.entry_azure_speech_key.grid(row=2, column=3)
        button_azure_speech_key.grid(row=2, column=4)

        #---------------------------------------
        #  実行ボタン
        # --------------------------------------------------------
        # 実行ボタン用Frame
        self.frame_exe = tk.Frame(self.master)
        self.frame_exe.pack()
        button_exe = tk.Button(self.frame_exe, text="翻訳", command=self.translate)
        button_exe.pack()
        self.message_label = tk.Label(self.frame_exe, text="")
        self.message_label.pack()

    def select_mov_path(self):
        '動画ファイル選択ボタンが押された時の処理'
        self.video_file_path = filedialog.askopenfilename()
        self.entry1.delete(0, tk.END)  # Entryウィジェットの中身を削除
        self.entry1.insert(tk.END, self.video_file_path)  # Entryウィジェットにファイルパスを表示
        batchConfig['SETTINGS']['original_video_file_path'] = self.video_file_path # 動画ファイルのパスを編集

    def select_sub_path(self):
        '字幕ファイル選択ボタンが押された時の処理'
        self.subtitle_file_path = filedialog.askopenfilename()
        self.entry2.delete(0, tk.END)  # Entryウィジェットの中身を削除
        self.entry2.insert(tk.END, self.subtitle_file_path)  # Entryウィジェットにファイルパスを表示
        batchConfig['SETTINGS']['srt_file_path'] = self.subtitle_file_path # 字幕ファイルのパスをiniファイルに書き込む

    def set_TranslateService(self):
        cloudConfig['CLOUD']['translate_service'] = self.preferredTranslateService.get()

    def set_ttsService(self):
        cloudConfig['CLOUD']['tts_service'] = self.ttsService.get()

    def update_cloud_ini(self, ini_var, val, text):
        cloudConfig['CLOUD'][ini_var] = val.get()
        with open('cloud_service_settings.ini', 'w') as configfile:
                cloudConfig.write(configfile)
        self.message_label.configure(text=f"{text} を更新しました。")
        self.master.update()
        time.sleep(1.5)
        self.message_label.configure(text="")

    def translate(self):
        def config():
            # INIファイルの更新 ----------------------------------
            with open('batch.ini', 'w') as configfile:
                batchConfig.write(configfile)
            with open('cloud_service_settings.ini', 'w') as configfile:
                cloudConfig.write(configfile)

        def langconfig():
            langNum = []
            for k in self.lang_dict:
                if self.lang_dict[k][1].get():
                    langNum.append(self.lang_dict[k][0])
            batchConfig['SETTINGS']['enabled_languages'] = ','.join(map(str, langNum))
        
        self.message_label.configure(text="")
        langconfig()
        config()
            # 翻訳を実行 ------------------------------------------
        try:
            translator()
            self.message_label.configure(text="翻訳が完了しました。")
        except Exception as e:
            self.message_label.configure(text="翻訳中にエラーが発生しました。詳細：" + str(e))


if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(width=False, height=False)
    app = Application(master=root)
    app.mainloop()
