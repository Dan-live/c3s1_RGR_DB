# ModelRoom
##############################################################################
class ModelRoom:
    def __init__(self, db_model):
        self.conn = db_model.conn  # Передаем атрибут conn из db_model

    def add_room(self, room_number, room_type):
        c = self.conn.cursor()
        try:
            c.execute('INSERT INTO room (room_number ,room_type) VALUES (%s, %s)', (room_number, room_type,))
            self.conn.commit()
            return True  # Возвращает True, если вставка прошла успешно
        except Exception as e:
            self.conn.rollback()
            print(f"Ошибка при добавлении комнаты: {str(e)}")
            return False  # Возвращает False, если вставка не удалась

    def get_all_rooms(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM room')
        return c.fetchall()

    def update_room(self, room_number, room_type):
        c = self.conn.cursor()
        try:
            c.execute('UPDATE room SET room_type=%s WHERE room_number=%s', (room_type, room_number))
            self.conn.commit()
            return True  # Возвращает True, если обновление прошло успешно
        except Exception as e:
            self.conn.rollback()
            print(f"Ошибка при обновлении комнаты: {str(e)}")
            return False  # Возвращает False, если обновление не удалось

    def delete_room(self, room_number):
        c = self.conn.cursor()
        try:
            c.execute('DELETE FROM room WHERE room_number=%s', (room_number,))
            self.conn.commit()
            return True  # Возвращает True, если удаление прошло успешно
        except Exception as e:
            self.conn.rollback()
            print(f"Ошибка при удалении комнаты: {str(e)}")
            return False  # Возвращает False, если удаление не удалось

    def check_room_existence(self, room_number):
        c = self.conn.cursor()
        c.execute('SELECT 1 FROM room WHERE room_number = %s', (room_number,))
        return c.fetchone() is not None

    def create_room_sequence(self):
        # Перевірка існування послідовності
        c = self.conn.cursor()
        c.execute("""
        DO $$
        BEGIN
            IF NOT EXISTS (SELECT 1 FROM pg_sequences WHERE schemaname = 'public' AND sequencename = 'room_number_seq') THEN
                -- Якщо послідовності не існує, створюємо її
                CREATE SEQUENCE room_number_seq;
            ELSE
                -- Якщо послідовність існує, видаляємо і створюємо нову
                DROP SEQUENCE room_number_seq;
                CREATE SEQUENCE room_number_seq;
            END IF;
        END $$;
        """)
        self.conn.commit()
    def generate_rand_room_data(self, number_of_operations):
        c = self.conn.cursor()
        try:
            # Вставка даних
            c.execute("""
            INSERT INTO room (room_number, room_type)
            SELECT
                nextval('room_number_seq'), 
                (array['Single', 'Double', 'Suite'])[floor(random() * 3) + 1]
            FROM generate_series(1, %s);
            """, (number_of_operations,))
            self.conn.commit()
            return True  # Возвращает True, если вставка прошла успешно
        except Exception as e:
            self.conn.rollback()
            print(f"Ошибка при добавлении комнаты: {str(e)}")
            return False  # Возвращает False, если вставка не удалась

    def truncate_room_table(self):
        c = self.conn.cursor()
        try:
            # Вставка даних
            c.execute("""DELETE FROM room""")
            self.conn.commit()
            return True  # Возвращает True, если вставка прошла успешно
        except Exception as e:
            self.conn.rollback()
            print(f"Ошибка при добавлении клиента: {str(e)}")
            return False  # Возвращает False, если вставка не удалась