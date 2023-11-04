# import datetime
# import random


# ModelBookingTicket
#################################################################################
class ModelBookingTicket:
    def __init__(self, db_model):
        self.conn = db_model.conn  # Передаем атрибут conn из db_model

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
                    'INSERT INTO booking_ticket (booking_id, client_id, room_number, '
                    'booking_start_date, booking_end_date, price) VALUES (%s, %s, %s, %s, %s, %s)',
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
            c.execute('UPDATE booking_ticket SET client_id=%s, room_number=%s, booking_start_date=%s, '
                      'booking_end_date=%s, price=%s WHERE booking_id=%s',
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

    def create_booking_sequence(self):
        c = self.conn.cursor()
        c.execute("""
           DO $$
           BEGIN
               IF NOT EXISTS (SELECT 1 FROM pg_sequences WHERE schemaname = 'public' AND sequencename = 'booking_id_seq') THEN
                   CREATE SEQUENCE booking_id_seq;
               ELSE
                   DROP SEQUENCE booking_id_seq;
                   CREATE SEQUENCE booking_id_seq;
               END IF;
           END $$;
           """)
        self.conn.commit()

    def generate_rand_booking_ticket_data(self, number_of_operations):
        c = self.conn.cursor()
        try:
            c.execute("""
                    
            DO $$
            BEGIN
                IF NOT EXISTS (SELECT 1 FROM pg_sequences WHERE schemaname = 'public' AND sequencename = 'booking_id_seq') THEN
                    -- Якщо послідовності не існує, створюємо її
                    CREATE SEQUENCE booking_id_seq;
                ELSE
                    -- Якщо послідовність існує, видаляємо і створюємо нову
                    DROP SEQUENCE booking_id_seq;
                    CREATE SEQUENCE booking_id_seq;
                END IF;
            END $$;
            INSERT INTO booking_ticket (booking_id, client_id, room_number, booking_start_date, booking_end_date, price)
                SELECT
                    nextval('booking_id_seq'),
                    floor(random() * (SELECT max(client_id) FROM client) + 1),
                    floor(random() * (SELECT max(room_number) FROM room) + 1),
                    '2023-01-01'::date + floor(random() * (date '2023-11-05' - date '2023-01-01')) * interval '1 day',
    		        '2023-11-05'::date + floor(random() * (date '2025-01-01' - date '2023-11-05')) * interval '1 day',
    		        random() * 1000 
		        FROM generate_series(1, %s)
                  """, (number_of_operations,))

            self.conn.commit()
            return True
        except Exception as e:
            self.conn.rollback()
            print(f"Error while generating booking tickets: {str(e)}")
            return False

    # def generate_random_DateTime(self):
    #     start_date = datetime.date(2023, 1, 1)
    #     end_date = datetime.date(2023, 12, 31)
    #
    #     while True:
    #         random_days = datetime.timedelta(days=random.randint(0, (end_date - start_date).days))
    #         random_start_date = start_date + random_days
    #         random_end_date = random_start_date + datetime.timedelta(days=random.randint(1, 10))  # Ensure end_date > start_date
    #
    #         if random_end_date > random_start_date:
    #             return random_start_date, random_end_date

    def truncate_booking_table(self):
        c = self.conn.cursor()
        try:
            # Вставка даних
            c.execute("""DELETE FROM booking_ticket""")
            self.conn.commit()
            return True  # Возвращает True, если вставка прошла успешно
        except Exception as e:
            self.conn.rollback()
            print(f"Ошибка при добавлении клиента: {str(e)}")
            return False  # Возвращает False, если вставка не удалась

