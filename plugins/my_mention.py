# coding: utf-8

from slackbot.bot import respond_to  # メンションで反応
from slackbot.bot import listen_to  # チャンネル内発言で反応
from slackbot.bot import default_reply  # 該当する応答がない場合に反応

import slackbot_settings
from plugins.image_downloader import ImageDownloader
from plugins.image_to_text import ImageToText
from plugins import text_manager

# @respond_to('string')     bot宛のメッセージ
#                           stringは正規表現が可能 「r'string'」
# @listen_to('string')      チャンネル内のbot宛以外の投稿
#                           メンションでは反応しないことに注意
#                           他の人へのメンションでは反応する
#                           正規表現可能
# @default_reply()          DEFAULT_REPLY と同じ働き
#                           正規表現を指定すると、他のデコーダにヒットせず、
#                           正規表現にマッチするときに反応

# message.reply('string')   @発言者名: string でメッセージを送信
# message.send('string')    string を送信
# message.react('icon_emoji')  発言者のメッセージにリアクション(スタンプ)する


@default_reply()
def default(message):
    message.reply("画像を送るとテキストを記憶できます")

@listen_to('show')
def listen(message):
    # ランダムにテキストを1つ表示する
    text = text_manager.read_text()
    message.send(text)

@respond_to("反応語句")
def respond(message):
    message.reply("返事")

# 画像の読み取り
@listen_to('(.*)')
def read_img(message, something):
    if 'files' in message.body:
        slack_token = slackbot_settings.API_TOKEN
        downloader = ImageDownloader(slack_token)
        img_to_text = ImageToText(lang='jpn')
        for file in message.body['files']:
            if file['mimetype'].startswith('image/'):
                print(file)
                url = file['url_private_download']
                filename = file['title']
                img_path = downloader.download_image(url, filename, slack_token)
                text = img_to_text.image_to_text(img_path)
                print("image to text: ")
                print(text)
                msg = 'テキストを記憶しました\n %s' % text
                message.send(msg)

    # else:
    #     message.reply("画像をアップロードすると知識を蓄えることができます")
