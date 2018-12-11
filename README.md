# MySlackbot
botに投げた画像からテキストを抽出して保存、取得するslackbot

# 設定
slackbot_settings.pyに

API_TOKEN = '自身のslackbotのAPIトークン'

を追加してください

# 必要なモジュール、ツール
OCRツール(tesseract)をインストールする

https://github.com/tesseract-ocr/tesseract/wiki

CentOS7なら以下のような感じでOCRツールと言語パックを入れる
```
yum-config-manager --add-repo https://download.opensuse.org/repositories/home:/Alexander_Pozdnyakov/CentOS_7/
sudo rpm --import https://build.opensuse.org/projects/home:Alexander_Pozdnyakov/public_key
yum update
yum install tesseract 
yum install tesseract-langpack-jpn
```

以下のモジュールをインストールする(他はおそらく標準モジュール)

```
pip install pillow
pip install pyocr
```
