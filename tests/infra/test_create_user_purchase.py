import psycopg2
from beginner_data_project.infra.create_user_purchase import create_user_purchase

def test_create_user_purchase():
    conn = psycopg2.connect(dbname="test_db", user="pg", password="pwd")
    create_user_purchase(conn)

    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM information_schema.tables
        WHERE table_name = 'user_purchase';
    """)
    results = cur.fetchall()

    cur.execute("""
        DROP TABLE user_purchase;
    """)

    conn.commit()

    conn.close()
    cur.close()

    assert len(results) > 0