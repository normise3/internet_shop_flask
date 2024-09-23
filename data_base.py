import sqlite3


def create_table():
    try:
        sqlite_connection = sqlite3.connect('game.db')
        sqlite_create_table_query = '''CREATE TABLE game_store (
                                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                                   name TEXT NOT NULL,
                                   description TEXT NOT NULL,
                                   price INTEGER NOT NULL,
                                   img TEXT NOT NULL,
                                   metascore INTEGER NOT NULL);'''

        cursor = sqlite_connection.cursor()
        print("База даних підключена до SQLite")
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()
        print("Таблиця SQLite створена")

        cursor.close()

    except sqlite3.Error as error:
        print("Помилка підключення до SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("З’єднання з SQLite закрите")


def insert_variable_into_table(name, description, price, img, metascore):
    try:
        sqlite_connection = sqlite3.connect('game.db')
        cursor = sqlite_connection.cursor()
        print("Підключено до SQLite")

        sqlite_insert_with_param = """INSERT INTO game_store
                             (name, description, price, img, metascore)
                             VALUES (?, ?, ?, ?, ?);"""

        data_tuple = (name, description, price, img, metascore)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqlite_connection.commit()
        print("Змінні успішно вставлені в таблицю game_store")

        cursor.close()

    except sqlite3.Error as error:
        print("Помилка при роботі з SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("З'єднання з SQLite закрите")


def delete_record_by_id(record_id):
    try:
        sqlite_connection = sqlite3.connect('game.db')
        cursor = sqlite_connection.cursor()
        print("Підключено до SQLite")

        sqlite_delete_query = """DELETE FROM game_store WHERE id = ?"""

        cursor.execute(sqlite_delete_query, (record_id,))
        sqlite_connection.commit()
        print("Запис успішно видалений")

        cursor.close()

    except sqlite3.Error as error:
        print("Помилка при роботі з SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("З'єднання з SQLite закрите")


def select_random_records():
    try:
        with sqlite3.connect('game.db') as sqlite_connection:
            cursor = sqlite_connection.cursor()
            print("Підключено до SQLite")

            sqlite_select_query = """ 
            SELECT * FROM game_store WHERE metascore BETWEEN 90 AND 96 ORDER BY RANDOM() LIMIT 6 """

            cursor.execute(sqlite_select_query)
            rows = cursor.fetchall()

            column_names = [description[0] for description in cursor.description]

            records = [dict(zip(column_names, row)) for row in rows]

            return records

    except sqlite3.Error as error:
        print("Помилка при роботі з SQLite", error)
        return []


def select_game_name_for_url(name):
    try:
        with sqlite3.connect('game.db') as sqlite_connection:
            cursor = sqlite_connection.cursor()
            print("Підключено до SQLite")

            sqlite_select_query = "SELECT * FROM game_store WHERE name_for_url = ?"

            cursor.execute(sqlite_select_query, (name,))
            rows = cursor.fetchall()

            column_names = [description[0] for description in cursor.description]

            records = [dict(zip(column_names, row)) for row in rows]

            return records

    except sqlite3.Error as error:
        print("Помилка при роботі з SQLite", error)
        return []


def select_game_name(name):
    try:
        with sqlite3.connect('game.db') as sqlite_connection:
            cursor = sqlite_connection.cursor()
            print("Підключено до SQLite")

            sqlite_select_query = "SELECT * FROM game_store WHERE name = ?"

            cursor.execute(sqlite_select_query, (name,))
            rows = cursor.fetchall()

            column_names = [description[0] for description in cursor.description]

            records = [dict(zip(column_names, row)) for row in rows]

            return records

    except sqlite3.Error as error:
        print("Помилка при роботі з SQLite", error)
        return []


def select_all_games():
    try:
        with sqlite3.connect('game.db') as sqlite_connection:
            cursor = sqlite_connection.cursor()
            print("Підключено до SQLite")

            sqlite_select_query = """SELECT * FROM game_store"""

            cursor.execute(sqlite_select_query)
            rows = cursor.fetchall()

            column_names = [description[0] for description in cursor.description]

            records = [dict(zip(column_names, row)) for row in rows]

            return records

    except sqlite3.Error as error:
        print("Помилка при роботі з SQLite", error)
        return []


def add_column_to_game_store(column_name, column_type):
    try:
        with sqlite3.connect('game.db') as sqlite_connection:
            cursor = sqlite_connection.cursor()
            print("Підключено до SQLite")

            sqlite_add_column_query = f"""ALTER TABLE game_store ADD COLUMN {column_name} {column_type}"""

            cursor.execute(sqlite_add_column_query)
            print(f"Колонка '{column_name}' з типом '{column_type}' була успішно додана.")

    except sqlite3.Error as error:
        print("Помилка при роботі з SQLite:", error)


def update_image_by_id(image_url, game_id):
    try:
        with sqlite3.connect('game.db') as sqlite_connection:
            cursor = sqlite_connection.cursor()
            print("Підключено до SQLite")

            sqlite_update_query = """UPDATE game_store SET about_game = ? WHERE id = ?"""

            cursor.execute(sqlite_update_query, (image_url, game_id))

            if cursor.rowcount == 0:
                print(f"Нічого не було оновлено. Перевірте ID гри: {game_id}")
            else:
                print(f"Зображення для гри з ID {game_id} було успішно оновлено.")

            sqlite_connection.commit()

    except sqlite3.Error as error:
        print("Помилка при роботі з SQLite:", error)


def filter_games_by_price(games, sort_by):
    if sort_by == 'price-asc':
        return sorted(games, key=lambda x: x['price'])
    elif sort_by == 'price-desc':
        return sorted(games, key=lambda x: x['price'], reverse=True)
    return games
