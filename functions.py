# For scrapping Twitter
import snscrape.modules.twitter as sntwitter
# Importing roadmap and sources for scrapping
from utils import *
from config import db


def start_scrapping(limit_per_sub=2):
    # Scrapping and populating the database
    chapter_id = 0
    sub_chapter_id = 0

    cursor = db.cursor()
    for chapter in ROADMAP.keys():
        chapter_name = ROADMAP[chapter]['name']
        chapter_id = chapter_id + 1
        print(f"{chapter}: {chapter_name}", end="")
        # Insert a new chapter in the database
        try:
            cursor.execute("INSERT INTO Chapters (id_chapter, title_chapter) values (%s, %s)", (chapter_id, chapter_name))
            db.commit()
        except:
            pass

        for sub_chapter in ROADMAP[chapter]["sub_chapters"]:
            # Insert a new sub_chapter in the DB
            sub_chapter_id = sub_chapter_id + 1
            try:
                cursor.execute(
                    "INSERT INTO SubChapters (id_sub_chapter, title_sub_chapter, chapter_id) values (%s, %s, %s)",
                    (sub_chapter_id, sub_chapter, chapter_id)
                )
            except:
                pass
            db.commit()
            for source in SOURCES:
                cpt = 0
                for tweet in sntwitter.TwitterSearchScraper(sub_chapter + " from:" + source).get_items():
                    print(".", end="")
                    if tweet.links is not None:
                        link = tweet.links[0].url
                        try:
                            cursor.execute("INSERT INTO Links (url, sub_chapter_id) VALUES (%s, %s)", (link, sub_chapter_id))
                            db.commit()
                        except:
                            pass
                    cpt += 1
                    if cpt == limit_per_sub:
                        break
        print()


def show_results():
    cursor = db.cursor()

    cursor.execute("SELECT * FROM Chapters ORDER BY id_chapter")
    chapters = cursor.fetchall()
    for (id_chapter, title_chapter) in chapters:
        print(f"Chapter {id_chapter} : {title_chapter}")
        cursor.execute("SELECT * FROM Subchapters WHERE chapter_id = %s ORDER BY id_sub_chapter", (id_chapter,))
        sub_chapters = cursor.fetchall()
        for (id_sub_chapter, title_sub_chapter, _) in sub_chapters:
            print(f"     Sub chapter: {title_sub_chapter}")
            cursor.execute("SELECT url FROM Links where sub_chapter_id = %s", (id_sub_chapter,))
            links = cursor.fetchall()
            for (link, ) in links:
                print(f"        - {link}")