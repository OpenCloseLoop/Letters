
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BaseMixin(object):
    @classmethod
    def create(cls, **kw):
        obj = cls(**kw)
        db.session.add(obj)
        db.session.commit()
        
    @classmethod
    def delete(cls, **kw):
        obj = cls.query.filter_by(**kw).first()
        db.session.delete(obj)
        db.session.commit()

class Letter(BaseMixin, db.Model):
    __tablename__ = 'letters'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(6))
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'<Letter: {self.id}, {self.code}, {self.name}>'

class Content(BaseMixin, db.Model):
    __tablename__ = 'content'
    id = db.Column(db.Integer, primary_key=True)
    letter_id = db.Column(db.Integer, nullable=False)
    paragraph_no = db.Column(db.Integer)
    option = db.Column(db.Integer)
    paragraph_text = db.Column(db.Text)

    def update(id, p_no=None, opt=None, p_text=None):
        obj = Content.query.filter_by(id=row).first()
        if p_no:
            obj.paragraph_no = p_no
        if opt:
            obj.option = opt
        if p_text:
            obj.paragraph_text = p_text
        db.session.commit() 

class Case(BaseMixin, db.Model):
    __tablename__ = 'case'
    id = db.Column(db.Integer, primary_key=True)
    IRN = db.Column(db.String(9), unique=True, nullable=False)
    status = db.Column(db.String(64), nullable=False)
    country = db.Column(db.String(2), nullable=False)
    appno = db.Column(db.String(12), nullable=True)
    regno = db.Column(db.String(12), nullable=True)
    appdate = db.Column(db.DateTime, nullable=True)
    regdate = db.Column(db.DateTime, nullable=True)

class LetterTable(BaseMixin, db.Model):
    __tablename__ = 'lettertable'
    id = db.Column(db.Integer, primary_key=True)
    letter_id = db.Column(db.Integer, nullable=False)
    table_no = db.Column(db.Integer, nullable=False)
    row = db.Column(db.Integer, nullable=False)
    col = db.Column(db.Integer, nullable=False)
    detail = db.Column(db.Text)
    db.UniqueConstraint(letter_id, table_no, row, col)

    def update(id, t_no,row, col, detail=None):
        obj = LetterTable.query.filter_by(letter_id=id, table_no=t_no, row=row, col=col).first()
        if detail:
            obj.detail = detail
        db.session.commit() 
