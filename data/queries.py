from data import data_manager
from psycopg2 import sql


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')

def display_shows(order_by="rating", order_direction="DESC", limit=0, offset=0):
    return data_manager.execute_select(sql.SQL("""SELECT id, title, year, runtime,
    to_char(rating:: float, '99.9') AS rating
    FROM shows 
    ORDER BY
        CASE WHEN %(order_direction)s = 'ASC' THEN {order_by} END ASC,
        CASE WHEN %(order_direction)s = 'DESC' THEN {order_by} END DESC
    LIMIT %(limit)s OFFSET %(offset)s;""").format(order_by=sql.Identifier(order_by)),
                                       {'order_direction':order_direction, 'limit': limit, "offset":offset}, fetchall=True)
