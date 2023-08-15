import sqlite3
import pandas as pd
from loguru import logger
from app.posts.schemas import PostInDb, PostCreate

from ..session import connect



class CRUDPost():


    def create(self,obj:PostInDb):
        logger.info('Adding Post into Database')
        con = connect()
        cur = con.cursor()

        values = (obj.title, obj.description, obj.post_id, obj.owner_id, obj.draft) 
        query = """
        INSERT INTO POSTS(title, description, post_id, owner_id, draft)
        VALUES (?,?,?,?,?)
        """
        cur.execute(query, values)
        con.commit()
        con.close()
        logger.info('Completed Database Transaction')
    
    def publish(self, obj: PostInDb):
        #TODO: Need to update this
        logger.info('Publishing post')
        con = connect()
        cur = con.cursor()
        values = (obj.title, obj.description, obj.post_id, obj.owner_id, obj.draft) 
        post_id = obj.post_id
        query = """
        UPDATE POSTS
        SET WHERE post_id = 'post_id'
        """

    def get_all(self, limit: int = 10) -> pd.DataFrame:
        logger.info('Getting all Posts')
        # TODO: Need to have 
        con = connect()
        query = f'''SELECT * FROM POSTS LIMIT {limit};'''
        data = pd.read_sql(query, con).to_dict(orient='records')
        return data

    
post = CRUDPost()