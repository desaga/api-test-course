# src/db/dal/products_dal.py
from sqlalchemy import text
from src.db.database import Database
import logging
import pdb

logger = logging.getLogger(__name__)


def get_product_from_db(product_json):
    db = Database()
    session = db.get_session()
    sql_text = text("""
        SELECT 
            p.post_title AS name,
            p.post_content AS description,
            p.post_excerpt AS short_description,
            pm.meta_value AS regular_price
        FROM wp_posts p
        LEFT JOIN wp_postmeta pm
            ON p.ID = pm.post_id AND pm.meta_key = '_price'
        WHERE p.post_title = :title
        LIMIT 1;
    """)

    logger.info(sql_text)

    try:
        result = session.execute(
            sql_text, {'title': product_json['name']}
        ).mappings().all()
        logger.info(f"Found records {len(result)}: \n \
                    {result}")

        if result:
            return [dict(row) for row in result]
    except Exception as e:
        logger.error(e)
    finally:
        session.close()
