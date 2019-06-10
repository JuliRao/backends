import json
from app.models import BaiKeDoc, BaiKeSection, BaiKeItem, BaiKePicture, ZhiDaoDoc, ZhiDaoAnswer
from app import db
import os


def single():
    f = open('baike/燕山君.json', 'r')
    content = json.loads(f.readline())
    print(content)
    title = content['title']
    print(title)
    description = content['description']
    print(description)

    for item in content['items']:
        for title in item:
            print(title, item[title])

    details = content['content']
    for title in details:
        print(title, details[title])

    pictures = content['pictures']
    for title in pictures:
        print(title)
        print(pictures[title])


def add_one(json_path, id):
    f = open(json_path, 'r')
    content = json.loads(f.readline())

    title = content['title']
    description = content['description']

    baike_doc = BaiKeDoc(
        title=title,
        description=description,
        doc_id=id
    )
    db.session.add(baike_doc)
    db.session.commit()

    for item in content['items']:
        for title in item:
            baike_item = BaiKeItem(
                baike_id=id,
                item_title=title,
                text=item[title]
            )
            db.session.add(baike_item)

    details = content['content']
    for title in details:
        baike_section = BaiKeSection(
            baike_id=id,
            section_title=title,
            text=details[title]
        )
        db.session.add(baike_section)

    pictures = content['pictures']
    for title in pictures:
        baike_pic = BaiKePicture(
            baike_id=id,
            picture_title=title,
            picture_url=pictures[title]
        )
        db.session.add(baike_pic)

    baike_pic = BaiKePicture(
        baike_id=id,
        picture_title='summary_pic',
        picture_url=content['summary_pic']
    )
    db.session.add(baike_pic)

    db.session.commit()


def add_all():
    files = os.listdir('baike')
    cnt = 100000
    for file in files:
        if file.endswith('.json'):
            json_path = os.path.join('baike', file)
            try:
                add_one(json_path, cnt)
            except Exception as e:
                print(e)
                print(json_path)
                db.session.rollback()
                cnt += 1
                continue
        cnt += 1


if __name__ == '__main__':
    db.session.query(BaiKeItem).delete()
    db.session.query(BaiKeSection).delete()
    db.session.query(BaiKePicture).delete()
    db.session.commit()
    db.session.query(BaiKeDoc).delete()
    db.session.commit()

    add_all()
