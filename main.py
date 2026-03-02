from flask import Flask, render_template, redirect, request, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)  # Flaskアプリ（Webサーバーの本体）を作成

# データベース設定------------------------------------------------------------------------------------------------------------------------------------
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://urara2438@localhost/postgres"
# DBに接続するための設定をFlaskに登録．"SQLALCHEMY_DATABASE_URI"はFlask-SQLAlchemyが読むための決まり名．
# postgresql:// … DBの種類（PostgreSQL）
# urara2438@localhost … DBに接続するユーザー名とホスト名（ユーザー名が urara2438、ホスト名が localhost）
# /postgres … DB名（データベース名が postgres）


app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy()  # SQLAlchemyオブジェクトを作成．これがDB操作の中心になる．
migrate = Migrate()  # Migrationオブジェクトを作成．これがDBの構造変更を管理する．

db.init_app(app)
# dbとappを接続し，このFlaskアプリで使うDBを確定．
migrate.init_app(app, db)
# Flask-Migrateをappとdbに接続．これでFlask-MigrateがDBの構造変更を管理できるようになる．


# モデル定義------------------------------------------------------------------------------------------------------------------------------------
class Ingredient(db.Model):
    __tablename__ = "ingredient"
    ing_id = db.Column(db.Integer, primary_key=True)
    ing_name = db.Column(db.String(20), unique=True, nullable=False)
    cat_id = db.Column(db.Integer, db.ForeignKey("category.cat_id"), nullable=False)


class Category(db.Model):
    __tablename__ = "category"
    cat_id = db.Column(db.Integer, primary_key=True)
    cat_name = db.Column(db.String(20), unique=True, nullable=False)


class Dish(db.Model):
    __tablename__ = "dish"
    dish_id = db.Column(db.Integer, primary_key=True)
    dish_name = db.Column(db.String(20), unique=True, nullable=False)


class Ing_Dish_Set(db.Model):
    __tablename__ = "ing_dish_set"
    dish_id = db.Column(db.Integer, db.ForeignKey("dish.dish_id"), primary_key=True)
    ing_id = db.Column(db.Integer, db.ForeignKey("ingredient.ing_id"), primary_key=True)


# ルーティング------------------------------------------------------------------------------------------------------------------------------------
# トップページ
@app.route("/")
def index():
    return render_template("menu/index.html")


@app.route("/index_new")
def index_new():
    return render_template("menu/index_new.html")


# 材料登録ページ
@app.route("/new_ing", methods=["GET", "POST"])
def new_ing():
    if request.method == "POST":
        new_ing_name = request.form.get("new_ing_name")
        if not new_ing_name:
            flash("名前を入力してください")
            return redirect("/new_ing")
        cat_id = request.form.get("cat_id")
        # request.form = ImmutableMultiDict([('new_ing_name', 'トマト'), ('cat_id', '1')])． 辞書と似てる．
        # new_ing_name = request.form["new_ing_name"]でも動くが， []内が空のときにエラーを吐く． .get(キー)ならNoneを返す．
        new_ing = Ingredient(ing_name=new_ing_name, cat_id=int(cat_id))
        db.session.add(new_ing)
        db.session.commit()
        return redirect("/new_ing")
    else:
        cat_list = Category.query.all()
        # cat_list = [
        #    Category(cat_id=1, cat_name="野菜"),
        #    Category(cat_id=2, cat_name="肉"),
        #    Category(cat_id=3, cat_name="魚") ・・・
        #   ] 各要素がCategoryクラスから作られたインスタンスであるリスト
        return render_template("menu/new_ing.html", cat_list=cat_list)


# 料理登録ページ
@app.route("/new_dish", methods=["GET", "POST"])
def new_dish():
    cat_list = Category.query.all()
    ing_list = Ingredient.query.all()
    # ing_list = [
    #    Ingredient(ing_id=1, ing_name="野菜", cat_id=1),
    #    Ingredient(ing_id=2, ing_name="肉", cat_id=2),
    #    Ingredient(ing_id=3, ing_name="魚", cat_id=3) ・・・
    #   ]
    if request.method == "POST":
        new_dish_name = request.form.get("new_dish_name")
        if not new_dish_name:
            flash("料理名を入力してください．")
            return redirect("/new_dish")

        ing_id_needed_list = request.form.getlist("ing_id_needed_list")
        if not ing_id_needed_list:
            flash("材料を選択してください．")
            return redirect("/new_dish")

        new_dish = Dish(dish_name=new_dish_name)
        db.session.add(new_dish)
        db.session.flush()  # <- 料理名を一時保存

        try:
            for ing_id_needed in ing_id_needed_list:
                new_ing_dish_set = Ing_Dish_Set(
                    dish_id=new_dish.dish_id,
                    ing_id=int(ing_id_needed),
                )  # htmlからrequest.formで取得したidはstr型なのでint型に変換．
                db.session.add(new_ing_dish_set)
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise

        return redirect("/new_dish")

    elif request.method == "GET":
        return render_template(
            "menu/new_dish.html", ing_list=ing_list, cat_list=cat_list
        )


# 編集メニューページ
@app.route("/index_edit")
def index_edit():
    return render_template("menu/index_edit.html")


# カテゴリー別材料リスト
@app.route("/list_ing")
def list_ing():
    cat_list = Category.query.all()
    ing_list = Ingredient.query.all()
    return render_template("menu/list_ing.html", cat_list=cat_list, ing_list=ing_list)


# 材料編集ページ
@app.route("/edit_ing/<int:ing_id>", methods=["GET", "POST"])
def edit_ing(ing_id):
    now_ing = Ingredient.query.filter_by(ing_id=ing_id).first_or_404()
    cat_list = Category.query.all()

    if request.method == "POST":
        now_ing.ing_name = request.form.get("edited_ing_name")
        now_ing.cat_id = int(request.form.get("edited_cat_id"))
        db.session.commit()
        return redirect("/list_ing")

    elif request.method == "GET":
        return render_template("menu/edit_ing.html", now_ing=now_ing, cat_list=cat_list)


# 料理リスト
@app.route("/list_dish")
def list_dish():
    dish_list = Dish.query.all()
    return render_template("menu/list_dish.html", dish_list=dish_list)


# 料理編集ページ
@app.route("/edit_dish/<int:dish_id>", methods=["GET", "POST"])
def edit_dish(dish_id):
    now_dish = Dish.query.filter_by(dish_id=dish_id).first_or_404()
    cat_list = Category.query.all()
    ing_list = Ingredient.query.all()

    if request.method == "POST":
        edited_dish_name = request.form.get("edited_dish_name")
        if not edited_dish_name:
            flash("新しい料理の名前を入力してください．")
            return redirect(
                url_for("edit_dish", dish_id=dish_id)
            )  # redirectはカッコの中身が文字列で飛ぶので，引数がある場合はurl_forで関数を指定．

        edited_ing_id_needed_list = request.form.getlist("edited_ing_id_needed_list")
        if not edited_ing_id_needed_list:
            flash("材料を選択してください")
            return redirect(url_for("edit_dish", dish_id=dish_id))

        try:
            now_dish.dish_name = edited_dish_name
            Ing_Dish_Set.query.filter_by(dish_id=dish_id).delete(
                synchronize_session=False
            )
            for edited_ing_id_needed in edited_ing_id_needed_list:
                edited_ing_dish_set = Ing_Dish_Set(
                    dish_id=now_dish.dish_id, ing_id=int(edited_ing_id_needed)
                )

                db.session.add(edited_ing_dish_set)
            db.session.commit()

        except Exception:
            db.session.rollback()
            raise

        return redirect("/list_dish")

    elif request.method == "GET":
        return render_template(
            "menu/edit_dish.html",
            now_dish=now_dish,
            cat_list=cat_list,
            ing_list=ing_list,
        )


@app.route("/search", methods=["GET", "POST"])
def search():
    ing_list = Ingredient.query.all()
    cat_list = Category.query.all()
    dish_list = Dish.query.all()

    if request.method == "POST":
        # 指定された材料idのリスト
        searched_ing_id_list = request.form.getlist("searched_ing_id_list")
        searched_ing_id_list_int = list(map(int, searched_ing_id_list))

        # 結果保存用リスト
        result_list = []

        for dish in dish_list:
            match_score = 0
            ing_dish_set_list = Ing_Dish_Set.query.filter_by(
                dish_id=dish.dish_id
            ).all()  # <-対象の料理idとそれに必要な材料のリスト = [(dish_id = ?, ing_id = ?), (dish_id = ?, ing_id = ?), ...]

            for ing_dish_set in ing_dish_set_list:
                for searched_ing_id in searched_ing_id_list_int:
                    if searched_ing_id == ing_dish_set.ing_id:
                        match_score += 1  # <-各料理ごとにseached_ing_idと料理に一致するidがあると+1
                        break
            if match_score > 0:
                ing_needed = len(ing_dish_set_list)  # <-必要な材料の個数
                lack = ing_needed - match_score  # <-不足数

                # 不足材料の表示--------------------------------------------------------------------------------------------
                # 不足材料id検索用に対象の料理に必要な材料idだけのリスト
                ing_id_needed_list_for_search = []
                for ing_dish_set in ing_dish_set_list:
                    ing_id_needed_list_for_search.append(ing_dish_set.ing_id)

                lack_ing_id_list = []

                for ing_id_needed in ing_id_needed_list_for_search:
                    if ing_id_needed not in searched_ing_id_list_int:
                        lack_ing_id_list.append(
                            ing_id_needed
                        )  # <-不足材料idのリスト(int)

                lack_ing_name_list = []
                for lack_ing_id in lack_ing_id_list:
                    lack_ing_name = Ingredient.query.filter_by(
                        ing_id=lack_ing_id
                    ).first()
                    if lack_ing_name:
                        lack_ing_name_list.append(lack_ing_name.ing_name)

                result_list.append(
                    [dish.dish_name, match_score, lack, lack_ing_name_list]
                )

        result_list.sort(key=lambda result: result[1], reverse=True)

        return render_template("menu/result.html", result_list=result_list)

    elif request.method == "GET":
        return render_template("menu/search.html", ing_list=ing_list, cat_list=cat_list)
