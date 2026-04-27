from sqlalchemy import create_engine, text


db_url = "postgresql://postgres:Dayana@localhost:5432/QA"
db = create_engine(db_url)


def test_add_subject():
    with db.connect() as conn:
        query = "INSERT INTO subject (subject_title) VALUES ('Python')"
        conn.execute(text(query))
        conn.commit()

        res_query = "SELECT * FROM subject WHERE subject_title = 'Python'"
        res = conn.execute(text(res_query)).fetchone()
        assert res is not None

        del_query = "DELETE FROM subject WHERE subject_title = 'Python'"
        conn.execute(text(del_query))
        conn.commit()


def test_update_subject():
    with db.connect() as conn:
        conn.execute(text("INSERT INTO subject (subject_title) VALUES ('A')"))
        conn.commit()

        upd = ("UPDATE subject SET subject_title = 'B' "
               "WHERE subject_title = 'A'")
        conn.execute(text(upd))
        conn.commit()

        res = conn.execute(text("SELECT * FROM subject")).fetchone()
        assert res is not None

        conn.execute(text("DELETE FROM subject WHERE subject_title = 'B'"))
        conn.commit()


def test_delete_subject():
    with db.connect() as conn:
        ins = "INSERT INTO subject (subject_title) VALUES ('Temp')"
        conn.execute(text(ins))
        conn.commit()

        conn.execute(text("DELETE FROM subject WHERE subject_title = 'Temp'"))
        conn.commit()

        sel = "SELECT * FROM subject WHERE subject_title = 'Temp'"
        res = conn.execute(text(sel)).fetchone()
        assert res is None
