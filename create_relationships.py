"""
Description:
 Creates the relationships table in the Social Network database
 and populates it with 100 fake relationships.

Usage:
 python create_relationships.py
"""
import os
import sqlite3
from faker import Faker
from random import randint, choice
# Determine the path of the database
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'social_network.db')

def main():
    create_relationships_table()
    populate_relationships_table()

def create_relationships_table():
    """Creates the relationships table in the DB"""
    # TODO: Function body
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    create_relationships_tbl_query = """
        CREATE TABLE IF NOT EXISTS relationships
        (
        id INTEGER PRIMARY KEY,
        person1_id INTEGER NOT NULL,
        person2_id INTEGER NOT NULL,
        type TEXT NOT NULL,
        start_date DATE NOT NULL,
        FOREIGN KEY (person1_id) REFERENCES people (id),
        FOREIGN KEY (person2_id) REFERENCES people (id)
        );
    """
    cur.execute(create_relationships_tbl_query)
    con.commit()
    con.close()
    return

def populate_relationships_table():
    """Adds 100 random relationships to the DB"""
    # TODO: Function body
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    # SQL query that inserts a row of data in the relationships table.
    add_relationship_query = """
    INSERT INTO relationships
    (
    person1_id,
    person2_id,
    type,
    start_date
    )
    VALUES (?, ?, ?, ?);
    """
    fake = Faker()

    for _ in range(100):
        rel_type = choice(('friend', 'spouse', 'partner', 'relative'))
        start_date = fake.date_between(start_date='-50y', end_date='today' )
        new_relationshpis = ( randint(1,200),
                              randint(1,200),
                              rel_type,
                              start_date

        )
        cur.execute(add_relationship_query, new_relationshpis)
    con.commit()
    con.close()
    return 

if __name__ == '__main__':
   main()