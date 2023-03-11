# AutoTranslatorGUI  
https://github.com/ThioJoe/Auto-Synced-Translated-Dubs  
をデスクトップアプリ化するために作成。  
動画ファイルと字幕ファイルを準備すれば自動で翻訳された字幕ファイルと吹き替え音声を作成できる。  
デスクトップアプリはAppGUI.pyから起動できる。  
CUIで使いたい場合はmain.pyを実行すれば自動翻訳・吹替ができる。  

## 現状必要な事前準備
- リポジトリ内のすべてのファイルをダウンロードし、一つのディレクトリに保存
- pip install -r requirements.txtを使って必要なものをインストール
- config.iniの設定。詳しくはhttps://github.com/ThioJoe/Auto-Synced-Translated-Dubs を参照
- 翻訳サービス(google translate or deepl)と読み上げサービス(google tts or azure tts)のAPI Keyを取得
- googleを使用する場合はクライアントIDに関連付けられたclient secretを含むJSONファイルをダウンロードし、auth.pyにパスを入力

### 外部の必要ツール
- ffmpegのインストール(https://ffmpeg.org/download.html)
- 'rubberband'というバイナリファイル (https://breakfastquay.com/rubberband/)  
  インストールする必要はなく、exeとdllファイルの両方をスクリプトと同じディレクトリに置くだけでよい

## 実行方法  
1. python AppGUI.pyを実行しアプリを立ち上げる
2. 動画ファイルと字幕ファイルを選択
3. 翻訳する言語を選択(複数選択可)
4. 使う翻訳・読み上げサービスを選択
5. API Keyを入力し更新ボタンを押す
6. 翻訳ボタンを押し、翻訳開始
7. '翻訳が完了しました。'と表示されたら翻訳完了
8. 翻訳された字幕ファイルと吹替音声トラックは'output'というフォルダに格納される

**必要に応じて以下の処理を実行(アプリでは未実装)**
- python TrackAdder.pyで吹替音声トラックを動画の音声トラックに追加
- TitleTranslator.pyの中に動画タイトルと説明文を入力し、python TitleTranslator.pyで翻訳

## 作成した機能  
- 翻訳する動画ファイルと字幕ファイルを選択
- 翻訳言語の設定  
- 使う翻訳サービスの設定
- 翻訳サービスのAPI Key設定
- 使う読み上げサービスの設定
- 読み上げサービスのAPI Key設定
- API Key設定時にメッセージを表示
- 翻訳完了時にメッセージを表示
- Google Client Secret JSONファイルのパス指定

## まだ実装できていない機能  
- 動画の元々の言語設定(現時点では日本語のみ)
- config.iniをアプリ側で設定
- 翻訳の進行状況をアプリ上で表示
