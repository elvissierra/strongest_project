import psycopg2
import uuid
from connect import connect
from config import load_config
from webscrape import scrape_data

def insert_data(mon_data):
    config = load_config()
    conn = connect(config)
    if conn is not None:
        try:    
            cur = conn.cursor()

            for mon in mon_data:
                cur.execute(
                    """ 
                    INSERT INTO mon (id, name, type1, type2, hp, attack, defense, sp_attack, sp_defense, speed)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) 
                    """, (str(uuid.uuid4()), mon[0], mon[1], mon[2], *mon[3:]))
            conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

if __name__ == "__main__":
    mon_data = scrape_data()
    insert_data(mon_data)