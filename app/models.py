from _datetime import datetime
from app import db
import json


class ZhiDaoDoc(db.Model):
    __tablename__ = "zhidao_doc"
    doc_id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=False)
    question = db.Column(db.Text)
    ask_time = db.Column(db.DateTime, default=datetime.utcnow)
    is_indexed = db.Column(db.Boolean, default=False)

    def __str__(self):
        return "<Question %r>" % self.question


class ZhiDaoAnswer(db.Model):
    __tablename__ = 'zhidao_answer'
    answer_id = db.Column(db.Integer, unique=True, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('zhidao_doc.doc_id'))
    answer = db.Column(db.Text)
    user_name = db.Column(db.String(255))
    answer_time = db.Column(db.DateTime, default=datetime.utcnow)
    likes = db.Column(db.Integer)
    dislikes = db.Column(db.Integer)
    accepted = db.Column(db.Boolean)
    picture_url = db.Column(db.Text)
    question = db.relationship('ZhiDaoDoc', backref=db.backref('answers'))

    def __str__(self):
        return "<Answer %d for question %d>" % self.answer_id, self.question_id


class BaiKeDoc(db.Model):
    __tablename__ = 'baike_doc'
    doc_id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=False)
    title = db.Column(db.String(255))
    description = db.Column(db.Text)
    is_indexed = db.Column(db.Boolean, default=False)

    def __str__(self):
        return "<BaiKe %r>" % self.title


class BaiKeSection(db.Model):
    __tablename__ = 'baike_section'
    section_id = db.Column(db.Integer, unique=True, primary_key=True)
    baike_id = db.Column(db.Integer, db.ForeignKey('baike_doc.doc_id'))
    section_title = db.Column(db.String(255))
    picture_url = db.Column(db.Text)
    text = db.Column(db.Text)
    page = db.relationship('BaiKeDoc', backref=db.backref('sections'))

    def __str__(self):
        return "<Section %r for BaiKe %d >" % self.section_title, self.baike_id


class WordIndex(db.Model):
    __tablename__ = 'word_index'
    word = db.Column(db.String(255), unique=True, primary_key=True)
    _index_list = db.Column(db.Text)

    @property
    def index(self):
        return json.loads(self._index_list)

    @index.setter
    def index(self, index_list):
        self._index_list = json.dumps(index_list)

    def __str__(self):
        return self.word


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
