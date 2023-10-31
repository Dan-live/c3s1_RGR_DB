
# ModelRoom
##############################################################################


class ModelRoom:
    def __init__(self, db_model):
        #self.db_manager = db_model
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
