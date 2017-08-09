from flask import Flask, render_template, jsonify, request, Response
import sqlite3
import json
import os
array=[["121","Half Girlfriend","Chetan Bhagat", "135"],["123","Harry Potter Series","JK Rowling","200"],["124","One day at a call center","Chetan Bhagat","200"],["125","Best Day Ever","Random Author","100"]]
db=sqlite3.connect("yada.sqlite")
iterator = db.cursor()
try:
    iterator.execute("create table books(customerid , bookname , author, price)")
except sqlite3.OperationalError:
        pass
finally:
    print "Tables have been created"

def root_dir():  # Get root dir
    return os.path.abspath(os.path.dirname(__file__))

def get_file(filename):  # Get file name
    try:
        src = os.path.join(root_dir(), filename)
        return open(src).read()
    except IOError as exc:
        return str(exc)

def namesearch(query):
    iterator.execute("select * from books where bookname like '" + query+ "%' ;")
    return iterator.fetchall()
def authsearch(query):
    iterator.execute("select * from books where author like '" + query + "%' ;")
    return iterator.fetchall()

for i in range(0, len(array)):
    iterator.execute("""insert into books values(?,?,?,?)""",(array[i]))

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/<path:path>')
def get_resource(path):
    mimetypes = {
        ".css": "text/css",
        ".html": "text/html",
        ".js": "application/javascript",
    }
    complete_path = os.path.join(root_dir(), path)
    ext = os.path.splitext(path)[1]
    mimetype = mimetypes.get(ext, "text/html")
    content = get_file(complete_path)
    return Response(content, mimetype=mimetype)

@app.route('/books',methods=["POST"])
def search():
    if request.form['type'] == "name":
        result = namesearch(request.form['name']+'%')
        print result
        response = app.response_class(
            response=json.dumps(result),
            status=200,
            mimetype='application/json'
        )
        return response
    elif request.form['type'] == "author":
        result = authsearch(request.form['name']+'%')
        print result
        response = app.response_class(
            response=json.dumps(result),
            status=200,
            mimetype='application/json'
        )
        return response

    return "NULL"

if __name__ =="__main__":
    app.run()
