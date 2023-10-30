from model import Model
from view import View
from view import ViewBookingTicket
from view import ViewClient
from view import ViewRoom
from model import ModelBookingTicket
from model import ModelClient
from model import ModelRoom


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()
        self.view_booking_ticket = ViewBookingTicket()
        self.view_client = ViewClient()
        self.view_room = ViewRoom()
        self.model_booking_ticket = ModelBookingTicket(self.model)
        self.model_client = ModelClient(self.model)
        self.model_room = ModelRoom(self.model)

        self.controller_booking = ControllerBooking(self.model_booking_ticket, self.view_booking_ticket)
        self.controller_client = ControllerClient(self.model_client, self.view_client)
        self.controller_room = ControllerRoom(self.model_room, self.view_room)

    def run(self):
        methods = {'1': self.add_task, '2': self.view_tasks, '3': self.update_task, '4': self.delete_task,
                   '5': self.controller_booking.add_booking_ticket,
                   '6': self.controller_booking.view_booking_tickets,
                   '7': self.controller_booking.update_booking_ticket,
                   '8': self.controller_booking.delete_booking_ticket,
                   '9': self.controller_client.add_client, '10': self.controller_client.view_clients,
                   '11': self.controller_client.update_client, '12': self.controller_client.delete_client,
                   '13': self.controller_room.add_room, '14': self.controller_room.view_rooms,
                   '15': self.controller_room.update_room, '16': self.controller_room.delete_room}

        while True:
            choice = self.show_menu()

            if choice in methods:
                methods[choice]()
            elif choice == '17':
                break

    def show_menu(self):
        self.view.show_message("\nMenu:")
        self.view.show_message("1. Add Task")
        self.view.show_message("2. View Tasks")
        self.view.show_message("3. Update Task")
        self.view.show_message("4. Delete Task")
        self.view.show_message("5. Add Booking Ticket")
        self.view.show_message("6. View Booking Tickets")
        self.view.show_message("7. Update Booking Ticket")
        self.view.show_message("8. Delete Booking Ticket")
        self.view.show_message("9. Add Client")
        self.view.show_message("10. View Clients")
        self.view.show_message("11. Update Client")
        self.view.show_message("12. Delete Client")
        self.view.show_message("13. Add Room")
        self.view.show_message("14. View Rooms")
        self.view.show_message("15. Update Room")
        self.view.show_message("16. Delete Room")
        self.view.show_message("17. Quit")
        return input("Enter your choice: ")

    def add_task(self):
        title, description = self.view.get_task_input()
        self.model.add_task(title, description)
        self.view.show_message("Task added successfully!")

    def view_tasks(self):
        tasks = self.model.get_all_tasks()
        self.view.show_tasks(tasks)

    def update_task(self):
        task_id = self.view.get_task_id()
        title, description = self.view.get_task_input()
        self.model.update_task(task_id, title, description)
        self.view.show_message("Task updated successfully!")

    def delete_task(self):
        task_id = self.view.get_task_id()
        self.model.delete_task(task_id)
        self.view.show_message("Task deleted successfully!")


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

# ControllerClient
############################################################################


class ControllerClient:
    def __init__(self, model_client, view_client):
        self.model_client = model_client
        self.view_client = view_client

    def add_client(self):
        client_id = self.view_client.get_client_id()
        name, surname, email = self.view_client.get_client_input()
        if self.model_client.add_client(client_id, name, surname, email):
            self.view_client.show_client_message("Client added successfully!")
        else:
            self.view_client.show_client_message("Failed to add client.")

    def view_clients(self):
        clients = self.model_client.get_all_clients()
        self.view_client.show_clients(clients)

    def update_client(self):
        # Запрос ID бронирования, которое нужно обновить
        client_id = self.view_client.get_client_id()

        # Проверка, существует ли бронирование с указанным ID
        client_exists = self.model_client.check_client_existence(client_id)

        if client_exists:
            # Запрос обновленных данных о client от пользователя
            name, surname, email = self.view_client.get_client_input()
            # Вызов метода из класса Model для обновления client
            success = (self.model_client.update_client(client_id, name, surname, email))

            # Отображение сообщения о результате операции
            if success:
                self.view_client.show_client_message("Client updated successfully!")
            else:
                self.view_client.show_client_message("Failed to update client.")
        else:
            self.view_client.show_client_message("Client with the specified ID does not exist.")

    def delete_client(self):
        client_id = self.view_client.get_client_id()
        if self.model_client.delete_client(client_id):
            self.view_client.show_client_message("Client deleted successfully!")
        else:
            self.view_client.show_client_message("Failed to delete client.")

# ControllerRoom
############################################################################


class ControllerRoom:
    def __init__(self, model_room, view_room):
        self.model_room = model_room
        self.view_room = view_room

    def add_room(self):
        # # Запрос данных о комнате от пользователя

        room_number = self.view_room.get_room_number()
        room_type = self.view_room.get_room_input()

        if self.model_room.add_room(room_number, room_type):
            self.view_room.show_room_message("Room added successfully!")
        else:
            self.view_room.show_room_message("Failed to add room.")

    def view_rooms(self):
        # Вызов метода из класса Model для получения всех комнат
        rooms = self.model_room.get_all_rooms()

        # Отображение комнат через метод из класса ViewRoom (подразумевая, что у вас есть такой класс)
        self.view_room.show_rooms(rooms)

    def update_room(self):
        # Запрос номера комнаты, которую нужно обновить
        room_number = self.view_room.get_room_number()

        # Проверка, существует ли комната с указанным номером
        room_exists = self.model_room.check_room_existence(room_number)

        if room_exists:
            # Запрос обновленных данных о комнате от пользователя
            room_type = self.view_room.get_room_input()

            # Вызов метода из класса Model для обновления комнаты
            success = self.model_room.update_room(room_number, room_type)

            # Отображение сообщения о результате операции
            if success:
                self.view_room.show_room_message("Room updated successfully!")
            else:
                self.view_room.show_room_message("Failed to update room.")
        else:
            self.view_room.show_room_message("Room with the specified number does not exist.")

    def delete_room(self):
        # Запрос номера комнаты, которую нужно удалить
        room_number = self.view_room.get_room_number()

        # Проверка, существует ли комната с указанным номером
        room_exists = self.model_room.check_room_existence(room_number)

        if room_exists:
            # Вызов метода из класса Model для удаления комнаты
            success = self.model_room.delete_room(room_number)

            # Отображение сообщения о результате операции
            if success:
                self.view_room.show_room_message("Room deleted successfully!")
            else:
                self.view_room.show_room_message("Failed to delete room.")
        else:
            self.view_room.show_room_message("Room with the specified number does not exist.")
