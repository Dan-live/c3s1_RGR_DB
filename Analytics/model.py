# ModelAnalytics
#################################################################################
class ModelAnalytics:
    def __init__(self, db_model):
        self.conn = db_model.conn  # Передаем атрибут conn из db_model

    def room_occupancy(self):
        c = self.conn.cursor()
        try:
            c.execute("""
                    SELECT room_number, COUNT(*) AS occupancy_count
                    FROM booking_ticket
                    GROUP BY room_number
                    HAVING COUNT(*) >= 3
                    ORDER BY occupancy_count DESC;
               """)

            room_occupancy_data = c.fetchall()  # Отримати дані з запиту

            self.conn.commit()
            return room_occupancy_data  # Повернути дані
        except Exception as e:
            self.conn.rollback()
            print(f"Помилка при аналітиці зайнятості: {str(e)}")
            return None


    def number_of_orders(self):
        c = self.conn.cursor()
        try:
            c.execute("""
                        SELECT
                            room_number,
                            COUNT(*) AS orders_count
                        FROM
                            booking_ticket
                        WHERE
                            booking_start_date >= current_date - interval '14 days'
                        GROUP BY
                            room_number
                        ORDER BY
                        orders_count DESC;

                        """)

            number_of_orders_data = c.fetchall()  # Отримати дані з запиту

            self.conn.commit()
            return number_of_orders_data  # Повернути дані
        except Exception as e:
            self.conn.rollback()
            print(f"Помилка при аналітиці зайнятості: {str(e)}")
            return None

    def client_analytics(self):
        c = self.conn.cursor()
        try:
            c.execute("""SELECT
                            client.client_id,
                            client.name,
	                        client.surname,
	                        client.email,
                            COUNT(booking_ticket.booking_id) AS booking_count
                        FROM
                            client
                        JOIN
                            booking_ticket ON client.client_id = booking_ticket.client_id
                        GROUP BY
                            client.client_id, client.name, client.surname, client.email
                        HAVING
                            COUNT(booking_ticket.booking_id) > 3
                        ORDER BY
                            booking_count DESC;                                
                        """)

            number_of_orders_data = c.fetchall()  # Отримати дані з запиту

            self.conn.commit()
            return number_of_orders_data  # Повернути дані
        except Exception as e:
            self.conn.rollback()
            print(f"Помилка при аналітиці зайнятості: {str(e)}")
            return None