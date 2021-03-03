from flask import Flask, render_template, request, redirect, url_for
from models import *
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///letters.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/", methods=['GET'])
def main():
    """index"""
    db.create_all()
    return render_template('index.html')

@app.route("/letters", methods=['GET'])
def lettersget():
    """Show list of letters"""
    global letters
    letters = Letter.query.all()
    return render_template('letters.html', letters=letters)

@app.route("/letters", methods=['Post'])
def letterspost():
    """Add/Update/Delete Letters"""
    code = request.form.get('lettercode')
    name = request.form.get('lettername')
    Letter.create(code=code, name=name)
    return redirect(url_for('lettersget'))

@app.route("/letters/<int:letterid>", methods=['GET'])
def letterget(letterid):
    """Show Letter Template"""
    letter = Letter.query.filter_by(id=letterid).first()
    contents = Content.query.filter_by(letter_id=letterid).order_by(Content.paragraph_no,Content.option).all()
    tables = LetterTable.query.filter_by(letter_id=letterid).order_by(LetterTable.table_no, LetterTable.row, LetterTable.col).all()
    t_no = set()
    row = set()
    col = set()
    for x in range(len(tables)):
        t_no.add(tables[x].table_no)
        row.add(tables[x].row)
        col.add(tables[x].col)
    table_nos = {  "table_no": t_no, "row": row, "col": col  }
    if letter is None:
        return render_template('error.html', letters=letters)
    return render_template('letter.html',letter=letter,contents=contents,tables=tables,table_nos=table_nos)

@app.route("/letters/<int:letterid>", methods=['POST'])
def letterpost(letterid):
    """Add/Update/Delete Letter Template"""
    if 'create' in request.form:
        p_no = int(request.form.get('paragraphno'))
        option = int(request.form.get('option'))
        p_text = request.form.get('paragraphtext')
        Content.create(letter_id=letterid, paragraph_no=p_no, option=option, paragraph_text=p_text)
    if 'delete' in request.form:
        contentid = int(request.form.get('delete'))
        Content.delete(id=contentid)
    if 'update' in request.form:
        contentid = int(request.form.get('update'))
        p_no = int(request.form.get('newno'))
        opt = int(request.form.get('newoption'))
        p_text = request.form.get('newtext')
        Content.update(row=contentid, p_no=p_no, opt=opt, p_text=p_text)
    if 'createTable' in request.form:
        t_no = int(request.form.get('tableno'))
        rows = int(request.form.get('tablerow'))
        cols = int(request.form.get('tablecol'))
        if LetterTable.query.filter_by(letter_id=letterid, table_no=t_no) is None:
            for row in range(rows):
                for col in range(cols):
                    LetterTable.create(letter_id=letterid, table_no=t_no, row=row, col=col)
    if 'deleteRow' in request.form:
        tableno = int(request.form.get('tableno'))
        rowno = int(request.form.get('rowno'))
        cols = request.form.get('cols').replace("{","").replace(", ","").replace("}","")
        for col in cols:
            LetterTable.delete(table_no=tableno, row=rowno, col=col) 
    return redirect(url_for('letterget', letterid=letterid))

@app.route("/letters/<int:letterid>", methods=['POST'])
def tablepost(letterid):
    """Add/Update/Delete Letter Tables"""
    if 'create' in request.form:
        t_no = int(request.form.get('tableno'))
        rows = int(request.form.get('tablerow'))
        cols = int(request.form.get('tablecol'))
        if LetterTable.query.filter_by(letter_id=letterid, table_no=t_no) is None:
            for row in range(rows):
                for col in range(cols):
                    LetterTable.create(letter_id=letterid, table_no=t_no, row=row, col=col)
    if 'delete' in request.form:
        tableno = int(request.form.get('delete'))
        rows = len(LetterTable.query.filter_by(letter_id=letterid, table_no=tableno).all())
        for row in rows:
            LetterTable.delete(table_no=tableno) 
    return redirect(url_for('letterget', letterid=letterid))

@app.route("/letters/<int:letterid>", methods=['POST'])
def tablerowpost(letterid):
    """Add/Update/Delete Letter Tables"""
    if 'create' in request.form:
        t_no = int(request.form.get('tableno'))
        rows = int(request.form.get('tablerow'))
        cols = int(request.form.get('tablecol'))
        if LetterTable.query.filter_by(letter_id=letterid, table_no=t_no) is None:
            for row in range(rows):
                for col in range(cols):
                    LetterTable.create(letter_id=letterid, table_no=t_no, row=row, col=col)
    if 'delete' in request.form:
        tableno = int(request.form.get('tableno'))
        rowno = int(request.form.get('rowno'))
        cols = request.form.get('cols').replace("{","").replace(", ","").replace("}","")
        for col in cols:
            LetterTable.delete(table_no=tableno, row=rowno, col=col) 
    return redirect(url_for('letterget', letterid=letterid))
