from migrations import run_migrations
from functions import *


# Creating Database and tables
run_migrations()

# Scrapping from Twitter
print("Scrapping. please wait, this may take some minutes ...")

# limit
start_scrapping(limit_per_sub=3)

# Showing the results
print()
show_results()

# To show results in mysql workbench/shell, you can use the following
"""
SELECT c.title_chapter, sc.title_sub_chapter, l.url FROM Chapters c
	INNER JOIN SubChapters sc ON c.id_chapter = sc.chapter_id
    INNER JOIN Links l ON l.sub_chapter_id = sc.id_sub_chapter
    where sc.title_sub_chapter = "Django Framework"
    ORDER BY c.id_chapter, sc.id_sub_chapter;
"""

