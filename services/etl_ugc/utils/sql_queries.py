MOVIE_PROGRESS_QUERY = {
    "create_table": """
        CREATE TABLE IF NOT EXISTS default.movie_progress (
            user_id UUID,
            movie_id UUID,
            progress Float32,
            status Enum8('in_progress' = 1, 'completed' = 2),
            last_watched DateTime
        ) ENGINE = ReplacingMergeTree(last_watched)
        PRIMARY KEY (user_id, movie_id);
    """,
    "insert_data": """
        INSERT INTO default.movie_progress (user_id, movie_id, progress, status, last_watched)
        VALUES (%(user_id)s, %(movie_id)s, %(progress)s, %(status)s, %(last_watched)s);
    """,
}

MOVIE_FILTERS_QUERY = {
    "create_table": """
        CREATE TABLE IF NOT EXISTS default.movie_filters (
            user_id UUID,
            query String,
            page UInt32,
            size UInt32,
            date_event DateTime
        ) ENGINE = ReplacingMergeTree(date_event)
        PRIMARY KEY (user_id, query, date_event);
    """,
    "insert_data": """
        INSERT INTO default.movie_filters (user_id, query, page, size, date_event)
        VALUES (%(user_id)s, %(query)s, %(page)s, %(size)s, %(date_event)s);
    """,
}

MOVIE_DETAILS_QUERY = {
    "create_table": """
        CREATE TABLE IF NOT EXISTS default.movie_details (
            user_id UUID,
            uuid UUID,
            title String,
            imdb_rating Float32,
            description String,
            genres Array(String),
            actors Array(String),
            writers Array(String),
            directors Array(String),
            date_event DateTime
        ) ENGINE = ReplacingMergeTree(date_event)
        PRIMARY KEY (user_id, uuid);
    """,
    "insert_data": """
        INSERT INTO default.movie_details (user_id, uuid, title, imdb_rating, description, genres, actors, writers, directors, date_event)
        VALUES (%(user_id)s, %(uuid)s, %(title)s, %(imdb_rating)s, %(description)s,
                %(genres)s, %(actors)s, %(writers)s, %(directors)s, %(date_event)s);
    """,
}
