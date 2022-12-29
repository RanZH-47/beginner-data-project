import logging

import psycopg2


def create_user_purchase(conn):
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE user_purchase(
            invoice_number VARCHAR(255) PRIMARY KEY,
            stock_code VARCHAR(255),
            detail VARCHAR(255),
            quantity INT,
            invoice_date TIMESTAMP,
            unite_price NUMERIC,
            customer_id INT,
            country VARCHAR(255)
        );
        """
    )
    conn.commit()
    cur.close()


if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    conn = psycopg2.connect(dbname="mydb", user="pg", password="pwd")
    logger.info("Connection established")

    logger.info("Creating table: user_purchase")
    create_user_purchase(conn)

    conn.close()
