# from flask import Flask, jsonify
# import pymysql
from flask_cors import CORS
from flask import request

# app = Flask(__name__)
#

#
# # MySQL连接信息
# MYSQL_HOST = '106.15.10.74'
# MYSQL_PORT = 3306
# MYSQL_USER = 'root'
# MYSQL_PASSWORD = 'root123456'
# MYSQL_DATABASE = 'p91'
#
#
# def get_mysql_connection():
#     return pymysql.connect(
#         host=MYSQL_HOST,
#         port=MYSQL_PORT,
#         user=MYSQL_USER,
#         password=MYSQL_PASSWORD,
#         database=MYSQL_DATABASE
#     )
#
#
# @app.route('/api/data', methods=['GET'])
# def get_data():
#     try:
#         # 连接到MySQL数据库
#         connection = get_mysql_connection()
#         cursor = connection.cursor()
#
#         # 执行查询
#         sql = "SELECT * FROM p91videos order by add_time desc"
#         cursor.execute(sql)
#
#         # 获取查询结果
#         result = cursor.fetchall()
#
#         # 关闭数据库连接
#         cursor.close()
#         connection.close()
#
#         # 返回结果
#         return jsonify(result)
#
#     except Exception as e:
#         return jsonify({'error': str(e)})
#
#
# if __name__ == '__main__':
#     app.run()
from flask import Flask, jsonify
from playhouse.pool import PooledMySQLDatabase
from playhouse.flask_utils import FlaskDB
from peewee import *
import datetime

app = Flask(__name__)
CORS(app, origins='*')
# MySQL连接信息
MYSQL_HOST = '106.15.10.74'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'root123456'
MYSQL_DATABASE = 'p91'

# 配置Peewee数据库连接
db = PooledMySQLDatabase(MYSQL_DATABASE, host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, password=MYSQL_PASSWORD)

# 配置Flask应用程序使用Peewee数据库连接
flask_db = FlaskDB(app, db)


class P91Videos(flask_db.Model):
    # 定义P91Videos模型
    id = IntegerField(primary_key=True)
    title = CharField()
    author = CharField(default='p91')
    m3u8_url = CharField()
    thumbnail = CharField(null=True)
    popularites = IntegerField(default=0)
    detail_url = CharField()
    duration = CharField()
    favorites = IntegerField(default=0, index=True)
    comments = IntegerField(default=0)
    likes = IntegerField(default=0, index=True)
    dislikes = IntegerField(default=0)
    add_time = DateTimeField(index=True, default=datetime.datetime.now)
    author_url = CharField(index=True)

    class Meta:
        table_name = 'p91videos'


# @app.route('/api/data', methods=['GET'])
# def get_data():
#     try:
#         # 查询数据
#         result = P91Videos.select().order_by(P91Videos.add_time.desc()).dicts()
#         page = request.args.get('page', default=1, type=int)
#         per_page = request.args.get('per_page', default=10, type=int)
#         print(page)
#         print(per_page)
#         # 返回结果
#         return jsonify(list(result))
#
#     except Exception as e:
#         return jsonify({'error': str(e)})

# http://127.0.0.1:5000/api/data?page=1&per_page=24

@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        # 获取分页参数
        page = request.args.get('page', default=1, type=int)
        per_page = request.args.get('per_page', default=10 , type=int)

        # 查询数据
        query = P91Videos.select().order_by(P91Videos.add_time.desc())
        paginated_query = query.paginate(page, per_page)

        # 构造分页结果
        result = {
            'data': list(paginated_query.dicts()),
            'total': query.count(),
            'page': page,
            'per_page': per_page,
        }
        # 返回结果
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)})
#

@app.route('/api/pages', methods=['GET'])
def get_pages():
    try:
        # 获取分页参数
#         page = request.args.get('page', default=1, type=int)
#         per_page = request.args.get('per_page', default=10, type=int)
        page =  2
        per_page = 24
        # 查询数据
        query = P91Videos.select().order_by(P91Videos.add_time.desc())
        paginated_query = query.paginate(page, per_page)

        # 构造分页结果
        result = {
            'data': list(paginated_query.dicts()),
            'total': query.count(),
            'page': page,
            'per_page': per_page,
        }


        # 返回结果
        return jsonify(result['data'])

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run()
