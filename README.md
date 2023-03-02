# AutoTranslatorGUI  
https://github.com/ThioJoe/Auto-Synced-Translated-Dubs  
をGUI化するために作成。  
動画ファイルと字幕ファイルを準備すれば自動で翻訳された字幕ファイルと吹き替え音声を作成できる。  
AppGUI.pyから起動できる。  

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
- Google Cloud 用 token.pickleファイルのパス指定
- client secret file のパス指定
- 動画の元々の言語設定(現時点では日本語のみ)
- config.iniをアプリ側で設定
- 翻訳の進行状況をアプリ上で表示
