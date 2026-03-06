# 一人暮らしの味方

一人暮らしの方向けに．毎日の献立を考える手間を減らすアプリを開発しました．

私自身も一人暮らしをしており．毎晩「今日は何を作ろうか」と献立を考えることを面倒に感じていました．
また．冷蔵庫にある材料をうまく使い切れず．食材を余らせてしまうことも多くありました．

そこで．手元にある材料から作れる料理を簡単に見つけられるアプリを作ろうと考え．本アプリを開発しました．

ユーザーは手元にある材料を入力するだけで．その材料で作れる料理を検索でき．
不足している材料も確認することができます．

---

## スクリーンショット

### ホーム画面

<img src="/static/screenshot/index.png" width="600">
<img src="/static/screenshot/index-1.png" width="600">
<img src="/static/screenshot/index-2.png" width="600">

### さがす

カテゴリーごとに材料を選択し．「さがす」ボタンを押すと検索結果画面に遷移します．  
選択した材料から作れる料理と，不足している材料を確認することができます．
<img src="/static/screenshot/search.png" width="600">
<img src="/static/screenshot/result.png" width="600">

### ふやす

名前とカテゴリを選択して，材料をふやすことができます．
<img src="/static/screenshot/new_ing.png" width="600">

名前と必要な材料を選択して，料理をふやすことができます．
<img src="/static/screenshot/new_dish.png" width="600">

---

## 機能一覧

### 材料管理機能

- 材料一覧表示
- 材料の追加
- 材料の編集

### 料理管理機能

- 料理一覧表示
- 料理の追加
- 料理の編集
- 料理に使用する材料の登録

### 料理検索機能

- 手元にある材料を選択して料理を検索
- 選択した材料から作れる料理の表示
- 不足している材料の表示

### レシピ補助機能

- 外部サイトへのレシピ検索リンク

---

## 使用技術

### バックエンド

- Python 3.x
- Flask
- SQLAlchemy

### フロントエンド

- HTML
- CSS
- JavaScript（DOM操作）

### データベース

- PostgreSQL

### インフラ

- Heroku

### その他

- Git / GitHub

---

## 工夫した点

### 材料と料理の多対多関係を考慮したデータベース設計

料理と材料は多対多の関係にあるため，中間テーブルを作成して管理しています．
これにより，1つの料理に複数の材料を登録できるだけでなく，同じ材料を複数の料理で共有できる設計にしました．

### 不足材料の自動算出機能

ユーザーが手元にある材料を選択すると，その材料で作れる料理を検索できるようにしました．
また，料理を作るために不足している材料を自動的に算出し，ユーザーが確認できるようにしています．
これにより，料理を作る際に追加で購入する必要のある材料を簡単に把握できるようにしました．

### 直感的で親しみやすいUI設計

JavaScriptを利用してメニュー画面を動的にし．ユーザーが直感的に操作できるUIを実装しました．  
また．イラストを多用したデザインにすることで．鮮やかで親しみやすいアプリになるよう工夫しました．

---

## 環境構築

1. リポジトリをクローン

```bash
git clone https://github.com/xxxx/menu-app.git
```

2. 仮想環境を作成

```bash
python -m venv venv
```

3. 仮想環境を有効化

```bash
source venv/bin/activate
```

4. 必要なライブラリをインストール

```bash
pip install -r requirements.txt
```

5. アプリ起動

```bash
flask run
```

---

## ER図

category テーブルと ingredient テーブルは 1対多 の関係です．また，dish テーブルと ingredient テーブルは多対多の関係にあるため，中間テーブルとして ing_dish_set を設けています．
これにより，1つの料理に複数の材料を登録でき，同じ材料を複数の料理で共有できる設計にしました．

```text
+-------------------+
| category |
+-------------------+
| cat_id (PK) |
| cat_name |
+-------------------+
          |
          | 1 : N
          |
+-------------------+
| ingredient |
+-------------------+
| ing_id (PK) |
| ing_name |
| cat_id (FK) |
+-------------------+

+-------------------+
| dish |
+-------------------+
| dish_id (PK) |
| dish_name |
+-------------------+
          |
          | 1 : N
          |
+-------------------+
| ing_dish_set |
+-------------------+
| id (PK) |
| dish_id (FK) |
| ing_id (FK) |
+-------------------+
```

## ルーティング一覧

| URL               | 内容                     |
| ----------------- | ------------------------ |
| `/`               | ホーム画面               |
| `/search`         | 材料を選択して料理を検索 |
| `/result`         | 検索結果表示             |
| `/list_ing`       | 材料一覧                 |
| `/new_ing`        | 材料追加                 |
| `/edit_ing/<id>`  | 材料編集                 |
| `/list_dish`      | 料理一覧                 |
| `/new_dish`       | 料理追加                 |
| `/edit_dish/<id>` | 料理編集                 |

---

## ディレクトリ構成

```bash

Menu
├── main.py
├── .gitignore
├── templates
│   └── menu
│       ├── index.html
│       ├── search.html
│       ├── result.html
│       ├── list_dish.html
│       ├── list_ing.html
│       ├── new_dish.html
│       ├── new_ing.html
│       ├── edit_dish.html
│       └── edit_ing.html
│
├── static
│   ├── css
│   │   └── menu
│   │       ├── base.css
│   │       ├── index.css
│   │       ├── list_dish.css
│   │       ├── list_ing.css
│   │       ├── new_ing.css
│   │       ├── result.css
│   │       └── search + new_dish + edit_dish.css
│   │
│   ├── img
│   │
│   ├── javascript
│   │
│   └── screenshot
│       ├── index.png
│       ├── index-1.png
│       ├── index-2.png
│       ├── new_ing.png
│       ├── result.png
│       └── search.png

```

main.py
Flaskアプリのエントリーポイント．ルーティングやアプリケーションの処理を定義している．

templates/
HTMLテンプレートを格納しているディレクトリ．Jinja2を使用して画面を描画する．

static/css/
アプリのスタイルシートを格納している．画面ごとにCSSを分割して管理している．

static/img/
アプリ内で使用する画像ファイルを格納している．

static/javascript/
フロントエンドのJavaScriptファイルを格納している．

static/screenshot/
READMEに掲載するアプリ画面のスクリーンショットを保存している．

---

## 今後の改善点

### ユーザーごとの材料管理機能

現在は材料を都度選択する形式ですが，将来的にはユーザーごとに所持している材料を保存できる機能を追加し，毎回入力しなくても料理を検索できるようにする予定です．

### 買い物リスト機能

料理を作るために不足している材料をまとめて表示し，買い物リストとして利用できる機能を実装することで，より実用的なアプリに改善したいと考えています．
