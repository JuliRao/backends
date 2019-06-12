from app import db
from sqlalchemy.dialects.mysql import LONGTEXT
import json


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
    text = db.Column(db.Text)
    page = db.relationship('BaiKeDoc', backref=db.backref('sections'))

    def __str__(self):
        return "<Section %r for BaiKe %d >" % self.section_title, self.baike_id


class BaiKeItem(db.Model):
    __tablename__ = 'baike_item'
    item_id = db.Column(db.Integer, unique=True, primary_key=True)
    baike_id = db.Column(db.Integer, db.ForeignKey('baike_doc.doc_id'))
    item_title = db.Column(db.String(255))
    text = db.Column(db.Text)
    page = db.relationship('BaiKeDoc', backref=db.backref('items'))

    def __str__(self):
        return "<Section %r for BaiKe %d >" % self.section_title, self.baike_id


class BaiKePicture(db.Model):
    __tablename__ = 'baike_pic'
    picture_id = db.Column(db.Integer, unique=True, primary_key=True)
    baike_id = db.Column(db.Integer, db.ForeignKey('baike_doc.doc_id'))
    picture_title = db.Column(db.Text)
    picture_url = db.Column(db.Text)
    page = db.relationship('BaiKeDoc', backref=db.backref('pictures'))


class ZhiDaoDoc(db.Model):
    __tablename__ = "zhidao_doc"
    doc_id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=False)
    question = db.Column(db.Text)
    description = db.Column(db.Text)
    ask_time = db.Column(db.String(255))
    is_indexed = db.Column(db.Boolean, default=False)

    def __str__(self):
        return "<Question %r>" % self.question


class ZhiDaoAnswer(db.Model):
    __tablename__ = 'zhidao_answer'
    answer_id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=False)
    question_id = db.Column(db.Integer, db.ForeignKey('zhidao_doc.doc_id'))
    answer = db.Column(db.Text)
    user_name = db.Column(db.String(255))
    answer_time = db.Column(db.String(255))
    likes = db.Column(db.Integer)
    dislikes = db.Column(db.Integer)
    accepted = db.Column(db.Boolean)
    question = db.relationship('ZhiDaoDoc', backref=db.backref('answers'))

    def __str__(self):
        return "<Answer %d for question %d>" % self.answer_id, self.question_id


class ZhiDaoPicture(db.Model):
    __tablename__ = 'zhidao_pic'
    picture_id = db.Column(db.Integer, unique=True, primary_key=True)
    answer_id = db.Column(db.Integer, db.ForeignKey('zhidao_answer.answer_id'))
    picture_url = db.Column(db.Text)
    answer = db.relationship('ZhiDaoAnswer', backref=db.backref('pictures'))


class WordIndex(db.Model):
    __tablename__ = 'word_index'
    word = db.Column(db.String(255), unique=True, primary_key=True)
    _index_list = db.Column(LONGTEXT)

    @property
    def index(self):
        return json.loads(self._index_list)

    @index.setter
    def index(self, index_list):
        self._index_list = json.dumps(index_list)

    def __str__(self):
        return self.word

#
# if __name__ == '__main__':
#     db.drop_all()
#     db.create_all()
