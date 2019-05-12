from flask import Flask, request, abort
from hackathon.vk_api import messagehandler

app = Flask(__name__)

str1 = f"mysql+pymysql://bibliophagist:951753qw@bibliophagist.mysql." \
    f"pythonanywhere-services.com/bibliophagist$users"
app.config['SQLALCHEMY_DATABASE_URI'] = str1
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_RECORD_QUERIES'] = True
app.config['MYSQL_HOST'] = 'bibliophagist.mysql.pythonanywhere-services.com'
app.config['MYSQL_USER'] = 'bibliophagist'
app.config['MYSQL_PASSWORD'] = '951753qw'
app.config['MYSQL_DB'] = 'bibliophagist$users'

confirmation_token = '3a7afac8'
message_token = '4645c5e2f5d643d17ccf64f33ea8368ac407e41530919e5eaeb75c' \
                '17f65c6e7fa6ab13544cf0788f7757e'


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/', methods=['POST'])
def processing():
    data = request.json
    if 'type' not in data.keys():
        return abort(400)
    if data.get('type') == 'confirmation':
        return confirmation_token
    elif data.get('type') == 'message_new':
        messagehandler.create_answer(data['object'], message_token)
        return 'ok'
