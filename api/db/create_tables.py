import sqlite3
from .session import connect


def create_posts(con):
    cur = con.cursor()
    # Assuming that each post can only have 1 picture
    query = """
    CREATE TABLE POSTS(
        title varchar,
        description varchar,
        post_id varchar(32), 
        owner_id varchar,
        draft number(1)
    )
    """

    cur.execute(query)
    return True

def create_tables():
    con = connect()
    create_posts(con)


if __name__ == "__main__":
    create_tables()
