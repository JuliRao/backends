from app.models import ZhiDaoDoc, BaiKeDoc, WordIndex
from app.process import process
from app import db


def index_baike():
    ct = 0
    for page in BaiKeDoc.query.filter_by(is_indexed = False):
        words = process(page.title)
        for word, num in words.items():
            li = WordIndex.query.filter_by(word = word)
            if li.count() > 0:
                idx = li[0]
            else:
                idx = WordIndex(word=word, index={'baike_title':{}, 'baike_section':{}, 'zhidao_question':{}, 'zhidao_answer':{}})
                db.session.add(idx)
            saved = idx.index
            saved['baike_title'][page.doc_id] = num
            idx.index = saved

        section_words = {}
        for section in page.sections:
            section_words.update(process(section.text))
        for word, num in section_words.items():
            li = WordIndex.query.filter_by(word=word)
            if li.count() > 0:
                idx = li[0]
            else:
                idx = WordIndex(word=word, index={'baike_title': {}, 'baike_section': {}, 'zhidao_question': {}, 'zhidao_answer': {}})
                db.session.add(idx)
            saved = idx.index
            saved['baike_section'][page.doc_id] = num
            idx.index = saved

        page.is_indexed = True
        db.session.commit()
        if ct % 200==0:
            print('process file', ct)
        ct += 1
    return ct


def index_zhidao():
    ct = 0
    for page in ZhiDaoDoc.query.filter_by(is_indexed = False):
        words = process(page.question)
        for word, num in words.items():
            li = WordIndex.query.filter_by(word = word)
            if li.count() > 0:
                idx = li[0]
            else:
                idx = WordIndex(word=word, index={'baike_title':{}, 'baike_section':{}, 'zhidao_question':{}, 'zhidao_answer':{}})
                db.session.add(idx)
            saved = idx.index
            saved['zhidao_question'][page.doc_id] = num
            idx.index = saved

        section_words = {}
        for section in page.answers:
            section_words.update(process(section.answer))
        for word, num in section_words.items():
            li = WordIndex.query.filter_by(word=word)
            if li.count() > 0:
                idx = li[0]
            else:
                idx = WordIndex(word=word, index={'baike_title': {}, 'baike_section': {}, 'zhidao_question': {}, 'zhidao_answer': {}})
                db.session.add(idx)
            saved = idx.index
            saved['zhidao_answer'][page.doc_id] = num
            idx.index = saved

        page.is_indexed = True
        db.session.commit()
        if ct % 200 == 0:
            print('process file', ct)
        ct += 1
    return ct


if __name__ == '__main__':
    rows = db.session.query(WordIndex).delete()
    print('delete', rows, 'rows')

    for page in BaiKeDoc.query.filter_by(is_indexed=True):
        page.is_indexed = False

    for page in ZhiDaoDoc.query.filter_by(is_indexed=True):
        page.is_indexed = False

    db.session.commit()
    index_baike()

    db.session.commit()
    index_zhidao()
