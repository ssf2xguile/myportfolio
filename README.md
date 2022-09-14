# ポートフォリオアプリ  
A.M.RによるDjango個人開発アプリその3です。こちらのソースはローカルのみでの動作となっております。

## 概要
A.M.RがPhotoshopやIllustratorで作成したサークル・同好会宣伝用ポスターやPinteresetで見つけて真似してみた広告等を置いています。もちろん作成したプログラムの画像もあります。

## デプロイ版のURL
http://amrs-portfolio.herokuapp.com/

## 環境構築
1. 必要パッケージの用意
```
pip install -r requirements.txt
```

2. manage.pyが置いてあるディレクトリ(myportfolio)に入りサーバを立ち上げます。
```
cd myportfolio
python manage.py runserver
```
※今回はこのソースを見ていただいている方のために`db.sqlite3`を用意しているので`makemigrations`や`migrate`を行う必要はありません。  

3. スーパーユーザーの編集・閲覧  
スーパーユーザーの編集・閲覧を行いたい場合は`admin/`から以下の情報を使ってログインすることができます。
```
name : hogepiyo
password : myportfolio
```

## 参考サイト
* [djangoでポートフォリオサイトを作成する](https://qiita.com/Tett/items/3d7d63a95a9935cc200c)
* [【Django】クラスベースビュー(Class-based View)の操作入門](https://qiita.com/ryuunosuke0905/items/1134eb4ed29cc249a74d)
* [【django-cleanup】画像等のファイルを自動的に削除する](https://noauto-nolife.com/post/django-cleanup/)
* [クラスベースビューで複数の変数をテンプレートに渡す](https://chuna.tech/detail/46/)
* [Djangoでお問い合わせフォームを作成する](https://medium.com/@kjmczk/django-contact-form-5a35d43b00a6)
* [Django本番環境でメディアファイル公開に必要な設定](https://sinyblog.com/django/media_file_001/)
* [『flexbox』だけでフッターを一番下（最下部）に固定する](https://www.tipdip.jp/tips_posts/production/2213/)




