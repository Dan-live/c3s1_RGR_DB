# ModelClient
############################################################################
class ModelClient:
    def __init__(self, db_model):
        self.conn = db_model.conn  # Передаем атрибут conn из db_model

    def add_client(self, client_id, name, surname, email):
        c = self.conn.cursor()
        try:
            c.execute('INSERT INTO client (client_id, name, surname, email) VALUES (%s, %s, %s, %s)',
                      (client_id, name, surname, email))
            self.conn.commit()
            return True  # Возвращает True, если вставка прошла успешно
        except Exception as e:
            self.conn.rollback()
            print(f"Ошибка при добавлении клиента: {str(e)}")
            return False  # Возвращает False, если вставка не удалась

    def get_all_clients(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM client')
        return c.fetchall()

    def update_client(self, client_id, name, surname, email):
        c = self.conn.cursor()
        try:
            c.execute('UPDATE client SET name=%s, surname=%s, email=%s WHERE client_id=%s',
                      (name, surname, email, client_id))
            self.conn.commit()
            return True  # Возвращает True, если обновление прошло успешно
        except Exception as e:
            self.conn.rollback()
            print(f"Ошибка при обновлении клиента: {str(e)}")
            return False  # Возвращает False, если обновление не удалось

    def delete_client(self, client_id):
        c = self.conn.cursor()
        try:
            c.execute('DELETE FROM client WHERE client_id=%s', (client_id,))
            self.conn.commit()
            return True  # Возвращает True, если удаление прошло успешно
        except Exception as e:
            self.conn.rollback()
            print(f"Ошибка при удалении клиента: {str(e)}")
            return False  # Возвращает False, если удаление не удалось

    def check_client_existence(self, client_id):
        c = self.conn.cursor()
        c.execute("SELECT 1 FROM client WHERE client_id = %s", (client_id,))
        return bool(c.fetchone())

    def create_client_sequence(self):
        # Перевірка існування послідовності
        c = self.conn.cursor()
        c.execute("""
        DO $$
        BEGIN
            IF NOT EXISTS (SELECT 1 FROM pg_sequences WHERE schemaname = 'public' AND sequencename = 'client_id_seq') THEN
                -- Якщо послідовності не існує, створюємо її
                CREATE SEQUENCE client_id_seq;
            ELSE
                -- Якщо послідовність існує, видаляємо і створюємо нову
                DROP SEQUENCE client_id_seq;
                CREATE SEQUENCE client_id_seq;
            END IF;
        END $$;
        """)
        self.conn.commit()

    def generate_rand_client_data(self, number_of_operations):
        c = self.conn.cursor()
        try:
            # Вставка даних
            c.execute("""
            INSERT INTO client (client_id, name, surname, email)
            SELECT
                nextval('client_id_seq'), 
                (array['John', 'Alice', 'Bob', 'Emma', 'Michael'])[floor(random() * 5) + 1], 
                (array['Smith', 'Johnson', 'Brown', 'Davis', 'Wilson'])[floor(random() * 5) + 1],  
                (substr(md5(random()::text), 1, 10) || '@gmail.com') 
            FROM generate_series(1, %s);
            """, (number_of_operations,))
            self.conn.commit()
            return True  # Возвращает True, если вставка прошла успешно
        except Exception as e:
            self.conn.rollback()
            print(f"Ошибка при добавлении клиента: {str(e)}")
            return False  # Возвращает False, если вставка не удалась


    def truncate_client_table(self):
        c = self.conn.cursor()
        try:
            # Вставка даних
            c.execute("""DELETE FROM client""")
            self.conn.commit()
            return True  # Возвращает True, если вставка прошла успешно
        except Exception as e:
            self.conn.rollback()
            print(f"Ошибка при добавлении клиента: {str(e)}")
            return False  # Возвращает False, если вставка не удалась