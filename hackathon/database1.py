from flask_sqlalchemy import SQLAlchemy
from hackathon.flask_app import app

# docker run -p 3306:3306 -e MYSQL_ROOT_PASSWORD=atom_pass -e MYSQL_DATABASE
# =atom_db -h 127.0.0.1 -d mysql
# docker ps
# docker exec -it pid bash
# mysql -u root -D atom_db -h 127.0.0.1 -p
# alter database atom_db character set=utf8mb4 collate utf8mb4_unicode_ci;
# --для кодировки нужной в бд
#  set names utf8mb4; -- чтобы в бд нормально отображалось всё
#
db = SQLAlchemy(app)


class history(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(2000), nullable=False)
    body = db.Column(db.String(2000), nullable=False)
    answer = db.Column(db.String(2000), nullable=False)


class account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    user_id = db.Column(db.Integer, primary_key=True)


# получить что то ############################################################


def get_account(user_id, name):
    if not account.query.filter_by(user_id=user_id, name=name).first():
        return add_account(user_id, name), False
    hh = account.query.filter_by(user_id=user_id).first()
    return hh.id, True


# добавить данные в таблицы###################################################

def add_account(user_id, name):
    db.session.add(account(user_id=user_id, name=name))
    db.session.commit()
    h = account.query.filter_by(user_id=user_id, name=name).first()
    return h.id


def add_history(id, user_id, title, body, answer):
    db.session.add(
        history(id=id, user_id=user_id, title=title, body=body, answer=answer))
    db.session.commit()
