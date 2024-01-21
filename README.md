# openWeatherAPIから天気予報を取得してLINEに通知する
　通知対象は以下
- 天気
- 湿度
- 気温
- 気圧
- 最高気温
- 最低気温

# 環境構築について
## pythonのインストール(windows)
以下公式サイトからインストーラをダウンロードしてインストール

https://www.python.org/
## pythonのインストール(linux)
`sudo apt-get install python`


## ライブラリのインストール
`pip install requests`
※その他、必要なライブラリについては適宜インストール

## 環境変数の設定
.envファイルを作成して以下をローカルに追加
- LINE API endpoint
- LINE API key
- WEATHR API endpoint
- WEATHER API key
- location

例
```
LINE_NOTIFY_URL = "https://notify-api.line.me/api/notify"
LINE_API_KEY = "API　KEYを取得して追加"

WEATHER_NOTIFY_URL = "https://api.openweathermap.org/data/2.5/weather"
WEATHER_API_KEY = "API　KEYを取得して追加"

LOCATION = "tokyo" // ex.) osaka, fukuoka, naha ...etc
```

# その他
## バッチの実行間隔について
前回の取得結果と比較して、変化があれば通知するようにしている。１時間ごとが望ましい？
経度緯度を指定した方が良い気がする？
