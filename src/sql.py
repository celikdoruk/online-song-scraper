import psycopg

def connect_commit(query, params=None):
    with psycopg.connect(
        host="localhost",
        user="postgres",
        password="1234",
        dbname="postgres"   # don't forget this
    ) as conn:
        with conn.cursor() as cur:
            cur.execute(query, params)
        conn.commit()


def insert(values: list[str]) -> None:
    query = """
                INSERT INTO song_details
                (song_name, artist, tempo_bpm, song_key, duration)
                VALUES (%s, %s, %s, %s, %s)
            """
    
    params = (
        values[0],
        values[1],
        values[2],
        values[3],
        values[4],
    )

    connect_commit(query, params)