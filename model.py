import psycopg2


class Model:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password='1',
            host='localhost',
            port=5432
        )
        self.create_tables()

    def create_tables(self):
        c = self.conn.cursor()
        # Проверка наличия таблиц
        c.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'booking_ticket')")
        booking_ticket_table_exists = c.fetchone()[0]

        c.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'client')")
        client_table_exists = c.fetchone()[0]

        c.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'room')")
        room_table_exists = c.fetchone()[0]

        if not booking_ticket_table_exists:
            c.execute('''
                        CREATE TABLE booking_ticket (
                            booking_id SERIAL PRIMARY KEY,
                            client_id INTEGER NOT NULL,
                            room_number INTEGER NOT NULL,
                            booking_start_date DATE NOT NULL,
                            booking_end_date DATE NOT NULL,
                            price DECIMAL(10, 2) NOT NULL
                        )
                    ''')
        if not client_table_exists:
            c.execute('''
                        CREATE TABLE client (
                            client_id SERIAL PRIMARY KEY,
                            name TEXT NOT NULL,
                            surname TEXT NOT NULL,
                            email TEXT
                        )
                    ''')
        if not room_table_exists:
            c.execute('''
                        CREATE TABLE room (
                            room_number SERIAL PRIMARY KEY,
                            room_type TEXT NOT NULL
                        )
                    ''')

        self.conn.commit()


#booking_ticket
#################################################################################
    # def add_booking_ticket(self, client_id, room_number, booking_start_date, booking_end_date, price):
    #     c = self.conn.cursor()
    #     c.execute(
    #         'INSERT INTO booking_ticket (client_id, room_number, booking_start_date, booking_end_date, price) VALUES (%s, %s, %s, %s, %s)',
    #         (client_id, room_number, booking_start_date, booking_end_date, price))
    #     self.conn.commit()
    def add_booking_ticket(self, booking_id, client_id, room_number, booking_start_date, booking_end_date, price):
        c = self.conn.cursor()
        try:
            # Проверяем наличие client_id и room_number в соответствующих родительских таблицах
            c.execute('SELECT 1 FROM client WHERE client_id = %s', (client_id,))
            client_exists = c.fetchone()

            c.execute('SELECT 1 FROM room WHERE room_number = %s', (room_number,))
            room_exists = c.fetchone()

            if not client_exists or not room_exists:
                # Возвращаем сообщение об ошибке или бросаем исключение
                return False  # Или вызываем исключение, чтобы обработать его далее
            else:
                # Все проверки прошли, выполняем вставку в booking_ticket
                c.execute(
                    'INSERT INTO booking_ticket (booking_id, client_id, room_number, booking_start_date, booking_end_date, price) VALUES (%s, %s, %s, %s, %s, %s)',
                    (booking_id, client_id, room_number, booking_start_date, booking_end_date, price))
                self.conn.commit()
                return True
        except Exception as e:
            # Обработка ошибок
            self.conn.rollback()
            print(f"Ошибка при добавлении бронирования: {str(e)}")
            return False

    def get_all_booking_tickets(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM booking_ticket')
        return c.fetchall()

    def update_booking_ticket(self, booking_id, client_id, room_number, booking_start_date, booking_end_date, price):
        c = self.conn.cursor()
        try:
            # Попытка выполнить обновление записи
            c.execute('UPDATE booking_ticket SET client_id=%s, room_number=%s, booking_start_date=%s, booking_end_date=%s, price=%s WHERE booking_id=%s',
                (client_id, room_number, booking_start_date, booking_end_date, price, booking_id))
            self.conn.commit()
            return True  # Возвращает True, если обновление прошло успешно
        except Exception as e:
            # Обработка ошибки в случае, если обновление не удалось
            self.conn.rollback()
            print(f"Ошибка при обновлении бронирования: {str(e)}")
            return False  # Возвращает False, если обновление не удалось

    def delete_booking_ticket(self, booking_id):
        c = self.conn.cursor()
        try:
            # Попытка выполнить удаление записи
            c.execute('DELETE FROM booking_ticket WHERE booking_id=%s', (booking_id,))
            self.conn.commit()
            return True  # Возвращает True, если удаление прошло успешно
        except Exception as e:
            # Обработка ошибки в случае, если удаление не удалось
            self.conn.rollback()
            print(f"Ошибка при удалении бронирования: {str(e)}")
            return False  # Возвращает False, если удаление не удалось

    def check_booking_existence(self, booking_id):
        c = self.conn.cursor()
        c.execute("SELECT 1 FROM booking_ticket WHERE booking_id = %s", (booking_id,))
        return bool(c.fetchone())


#client
############################################################################
    def add_client(self, client_id, name, surname, email):
        c = self.conn.cursor()
        try:
            c.execute('INSERT INTO client (client_id, name, surname, email) VALUES (%s, %s, %s, %s)', (client_id, name, surname, email))
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

############################################################################

#room
##############################################################################
    def add_room(self, room_number, room_type):
        c = self.conn.cursor()
        try:
            c.execute('INSERT INTO room (room_number ,room_type) VALUES (%s, %s)', (room_number ,room_type,))
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

##############################################################################
    def add_task(self, title, description):
        c = self.conn.cursor()
        c.execute('INSERT INTO tasks (title, description) VALUES (%s, %s)', (title, description))
        self.conn.commit()

    def get_all_tasks(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM tasks')
        return c.fetchall()

    def update_task(self, task_id, title, description):
        c = self.conn.cursor()
        c.execute('UPDATE tasks SET title=%s, description=%s WHERE id=%s', (title, description, task_id))
        self.conn.commit()

    def delete_task(self, task_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM tasks WHERE id=%s', (task_id,))
        self.conn.commit()
