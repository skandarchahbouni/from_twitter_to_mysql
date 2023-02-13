from config import db


def run_migrations():
    # Creating a cursor
    cursor = db.cursor()

    # DATABASE NAME
    DB_NAME = "course_collector"

    # CREATING THE DATABASE IF IT DOESN'T EXISTS
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")

    # SELECTING THE DATABASE
    cursor.execute(f"USE {DB_NAME}")

    # Refreshing the database
    cursor.execute("DROP TABLE IF EXISTS Links")
    cursor.execute("DROP TABLE IF EXISTS SubChapters")
    cursor.execute("DROP TABLE IF EXISTS Chapters")

    # CREATING THE TABLES
    # --- Chapters table
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS Chapters (
            id_chapter int auto_increment,
            title_chapter varchar(100) not null,
            primary key(id_chapter)
        );"""
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS SubChapters (
            id_sub_chapter int auto_increment,
            title_sub_chapter varchar(100) not null,
            chapter_id int not null,
            primary key(id_sub_chapter),
            foreign key(chapter_id) references Chapters(id_chapter) on update cascade on delete cascade
        );"""
    )

    # --- Links table
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS Links (
            id_link int auto_increment,
            url varchar(512) unique not null,
            sub_chapter_id int not null,
            primary key(id_link),
            foreign key(sub_chapter_id) references SubChapters(id_sub_chapter) on update cascade on delete cascade
        );"""
    )

    print("\nMigrations executed succesfully. 03 tables has been created.\n")