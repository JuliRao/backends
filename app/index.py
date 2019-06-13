from app.models import ZhiDaoDoc, BaiKeDoc, WordIndex
from app.process import process
from app import db
import time


def index_baike():
    ct = 0
    for page in BaiKeDoc.query.filter_by(is_indexed = False):
        title_words = {}
        section_words = {}

        title_words.update(process(page.title))
        section_words.update(process(page.description))

        for section in page.sections:
            title_words.update(process(section.section_title))
            section_words.update(process(section.text))

        for item in page.items:
            section_words.update(process(item.item_title))
            section_words.update(process(item.text))

        for word, num in title_words.items():
            if len(word) > 255:
                continue
            li = WordIndex.query.filter_by(word = word)
            if li.count() > 0:
                idx = li[0]
            else:
                idx = WordIndex(word=word, index={'baike_title':{}, 'baike_section':{}, 'zhidao_question':{}, 'zhidao_answer':{}})
                db.session.add(idx)
            saved = idx.index
            saved['baike_title'][page.doc_id] = num
            idx.index = saved

        for word, num in section_words.items():
            if len(word) > 255:
                continue
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

        try:
            db.session.commit()
        except Exception as e:
            print(e)
            print(page.title)
            db.session.rollback()

        if ct % 200 == 0:
            print('process file', ct)
        ct += 1
    return ct


def index_zhidao():
    ct = 0
    for page in ZhiDaoDoc.query.filter_by(is_indexed = False):
        ques_words = process(page.question)
        section_words = {}
        for section in page.answers:
            section_words.update(process(section.answer))

        for word, num in ques_words.items():
            if len(word) > 255:
                continue
            li = WordIndex.query.filter_by(word = word)
            if li.count() > 0:
                idx = li[0]
            else:
                idx = WordIndex(word=word, index={'baike_title':{}, 'baike_section':{}, 'zhidao_question':{}, 'zhidao_answer':{}})
                db.session.add(idx)
            saved = idx.index
            saved['zhidao_question'][page.doc_id] = num
            idx.index = saved

        for word, num in section_words.items():
            if len(word) > 255:
                continue
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

        try:
            db.session.commit()
        except Exception as e:
            print(e)
            print(page.question)
            db.session.rollback()

        if ct % 200 == 0:
            print(time.ctime(), 'process file', ct)
        ct += 1
    return ct


if __name__ == '__main__':
    # rows = db.session.query(WordIndex).delete()
    # print('delete', rows, 'rows')
    #
    # for page in BaiKeDoc.query.filter_by(is_indexed=True):
    #     page.is_indexed = False
    #
    # db.session.commit()
    index_baike()

    # for page in ZhiDaoDoc.query.filter_by(is_indexed=True):
    #     page.is_indexed = False
    #
    # db.session.commit()
    # index_zhidao()
