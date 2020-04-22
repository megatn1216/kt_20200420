from flask import Flask
from flask import request, redirect, abort
import os
import time

# app = Flask("flask")
app = Flask(__name__, static_folder="static")

def get_menu():
    menu=[e for e in os.listdir('content') if e[0] != '.']
    menu_temp = "<li><a href='/{0}'>{0}</a></li>"
    return "\n".join([menu_temp.format(m) for m in menu])

def get_template(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        return f.read()



@app.route('/')
def index():
    title ='야구 게임을 하고, 결과와 코멘트를 게시할 수 있습니다.' 
    content = '\'게시글 생성\' 버튼을 클릭하면, 게임이 시작됩니다.<br><br>\'게시글 검색\' 버튼을 클릭하면, 원하는 결과를 확인 할 수 있습니다.'
    menu = get_menu()
    return get_template("main.html").format(title, content, menu)

@app.route('/<title>')
def html(title):
    template = get_template("template.html")
    menu = get_menu()
    with open(f'content/{title}', 'r') as f:
        content = f.read()
        # mytext = "<br />".join(content.split("\n"))
    # return template.format(title, mytext, menu)
    return template.format(title, content, menu)

@app.route('/search')
def search():
    template = get_template("search.html")
    q = request.args.get('q', '')
    result = [filename for filename in os.listdir('content') if q in filename]
    menu_temp = "<li><a href='/{0}'>{0}</a></li>"
    menu = "\n".join([menu_temp.format(m) for m in result if m[0] != '.'])

    return template.format(menu)

@app.route("/create", methods=['GET', 'POST'])
def create():
    template = get_template('create.html')
    menu= get_menu()
    if request.method=="GET":
        return template.format(menu)
    elif request.method=="POST":
        title = request.form["title"]
        if title == "":
            title = time.strftime("%Y%m%d-%I.%M.%S",time.localtime(time.time()))          
        with open(f'content/{title}','w') as f:
            f.write(request.form['desc'])
        return redirect('/')

@app.route('/modify/<title>')
def modify(title):
    template = get_template("modify.html")
    menu = get_menu()
    with open(f'content/{title}', 'r') as f:
        content = f.read()
    return template.format(title, content, menu)
        
@app.route('/delete/<path>')
def delete(path):
    os.remove(f"content/{path}")
    return redirect("/")

@app.route("/favicon.ico")
def favicon():
    return abort(404)