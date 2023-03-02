# AutoTranslatorGUI  
https://github.com/ThioJoe/Auto-Synced-Translated-Dubs  
をGUI化するために作成。  
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
- 'rubberband'というバイナリファイル  
  インストールする必要はなく、exeとdllファイルの両方をスクリプトと同じディレクトリに置くだけでよい

## 実行方法  
1. python AppGUI.pyを実行
2. 動画ファイルと字幕ファイルを選択
3. 翻訳する言語を選択(複数選択可)
4. 使う翻訳・読み上げサービスを選択し、API Keyを設定
5. 翻訳ボタンを押し、翻訳開始
6. '翻訳が完了しました。'と表示されたら翻訳完了
7. 翻訳された字幕ファイルと吹替音声トラックは'output'というフォルダに格納される

## 作成した機能  
- 動画ファイルと字幕ファイル
- 翻訳言語の設定  
- 使う翻訳サービスの設定
- 翻訳サービスのAPI Key設定
- 使う読み上げサービスの設定
- 読み上げサービスのAPI Key設定
- API Key設定時にメッセージを表示
- 翻訳完了時にメッセージを表示

## まだ実装できていない機能  
- Google Client Secret JSONファイルのパス指定
- 動画の元々の言語設定(現時点では日本語のみ)
- config.iniをアプリ側で設定
- 翻訳の進行状況をアプリ上で表示
