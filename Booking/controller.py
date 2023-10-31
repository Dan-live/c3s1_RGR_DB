# ControllerBooking
############################################################################
class ControllerBooking:
    def __init__(self, model_booking_ticket, view_booking_ticket):
        self.model_booking_ticket = model_booking_ticket
        self.view_booking_ticket = view_booking_ticket

    def add_booking_ticket(self):
        # Запрос ID бронирования, которое нужно обновить
        booking_id = self.view_booking_ticket.get_booking_id()

        client_id, room_number, booking_start_date, booking_end_date, price = (
            self.view_booking_ticket.get_booking_ticket_input())
        # Вызов метода из класса Model для добавления бронирования
        success = (self.model_booking_ticket.add_booking_ticket
                   (booking_id, client_id, room_number, booking_start_date, booking_end_date, price))

        # Отображение сообщения о результате операции
        if success:
            self.view_booking_ticket.show_booking_ticket_message("Booking added successfully!")
        else:
            self.view_booking_ticket.show_booking_ticket_message("Failed to add booking.")

    def view_booking_tickets(self):
        # Вызов метода из класса Model для получения всех бронирований
        booking_tickets = self.model_booking_ticket.get_all_booking_tickets()

        # Отображение бронирований через метод из класса View
        self.view_booking_ticket.show_booking_tickets(booking_tickets)

    def update_booking_ticket(self):
        # Запрос ID бронирования, которое нужно обновить
        booking_id = self.view_booking_ticket.get_booking_id()

        # Проверка, существует ли бронирование с указанным ID
        booking_exists = self.model_booking_ticket.check_booking_existence(booking_id)

        if booking_exists:
            # Запрос обновленных данных о бронировании от пользователя
            client_id, room_number, booking_start_date, booking_end_date, price = (
                self.view_booking_ticket.get_booking_ticket_input())
            # Вызов метода из класса Model для обновления бронирования
            success = (self.model_booking_ticket.update_booking_ticket
                       (booking_id, client_id, room_number, booking_start_date, booking_end_date, price))

            # Отображение сообщения о результате операции
            if success:
                self.view_booking_ticket.show_booking_ticket_message("Booking updated successfully!")
            else:
                self.view_booking_ticket.show_booking_ticket_message("Failed to update booking.")
        else:
            self.view_booking_ticket.show_booking_ticket_message("Booking with the specified ID does not exist.")

    def delete_booking_ticket(self):
        # Запрос ID бронирования, которое нужно удалить
        booking_id = self.view_booking_ticket.get_booking_id()

        # Проверка, существует ли бронирование с указанным ID
        booking_exists = self.model_booking_ticket.check_booking_existence(booking_id)

        if booking_exists:
            # Вызов метода из класса Model для удаления бронирования
            success = self.model_booking_ticket.delete_booking_ticket(booking_id)

            # Отображение сообщения о результате операции
            if success:
                self.view_booking_ticket.show_booking_ticket_message("Booking deleted successfully!")
            else:
                self.view_booking_ticket.show_booking_ticket_message("Failed to delete booking.")
        else:
            self.view_booking_ticket.show_booking_ticket_message("Booking with the specified ID does not exist.")
