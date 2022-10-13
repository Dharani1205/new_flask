from flask import Flask, jsonify,request
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL(app)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'newmicro'

mysql.init_app(app)

@app.route('/users', methods=['POST'])
def get():
    cur = mysql.connect().cursor()
    json_dict = request.get_json()

    json_dict = request.get_json()
    for login in json_dict["users"]:
        name = str(json_dict["name"])
        password = str(json_dict["password"])
    #with cur.cursor() as cursor:
    values = 'INSERT INTO login(name,password) VALUES(%s,%s)'
    cur.execute(values, (name,password))
    mysql.connect().commit()

    #cur.close()

    return jsonify()

if __name__ == '__main__':
    app.run(debug=True,port=4022)