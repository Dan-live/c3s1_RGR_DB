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

