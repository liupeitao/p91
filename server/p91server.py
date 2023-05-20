from flask import Flask, jsonify
import pymysql
from flask_cors import CORS
app = Flask(__name__)

CORS(app, origins='*')

# MySQL连接信息
MYSQL_HOST = '106.15.10.74'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'root123456'
MYSQL_DATABASE = 'p91'


def get_mysql_connection():
    return pymysql.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )


@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        # 连接到MySQL数据库
        connection = get_mysql_connection()
        cursor = connection.cursor()

        # 执行查询
        sql = "SELECT * FROM p91videos order by add_time desc"
        cursor.execute(sql)

        # 获取查询结果
        result = cursor.fetchall()

        # 关闭数据库连接
        cursor.close()
        connection.close()

        # 返回结果
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run()
