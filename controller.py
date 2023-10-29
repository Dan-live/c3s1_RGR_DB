from model import Model
from view import View
from view import ViewBookingTicket
from view import ViewClient
from view import ViewRoom

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()
        self.view_booking_ticket = ViewBookingTicket()
        self.view_client = ViewClient()
        self.view_room = ViewRoom()

    def run(self):
        while True:
            choice = self.show_menu()
            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                self.update_task()
            elif choice == '4':
                self.delete_task()
            elif choice == '5':
                self.add_booking_ticket()  # Опция для добавления бронирования
            elif choice == '6':
                self.view_booking_tickets()  # Опция для просмотра бронирований
            elif choice == '7':
                self.update_booking_ticket()  # Опция для обновления бронирования
            elif choice == '8':
                self.delete_booking_ticket()  # Опция для удаления бронирования
            elif choice == '9':
                self.add_client()  # Опция для добавления клиента
            elif choice == '10':
                self.view_clients()  # Опция для просмотра клиентов
            elif choice == '11':
                self.update_client()  # Опция для обновления клиента
            elif choice == '12':
                self.delete_client()  # Опция для удаления клиента
            elif choice == '13':
                self.add_room()  # Опция для добавления комнаты
            elif choice == '14':
                self.view_rooms()  # Опция для просмотра комнат
            elif choice == '15':
                self.update_room()  # Опция для обновления комнаты
            elif choice == '16':
                self.delete_room()  # Опция для удаления комнаты
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

    #################################################
    def add_booking_ticket(self):
        # Запрос данных о бронировании от пользователя
        # booking_id = int(input("Enter booking_id: "))
        # client_id = int(input("Enter client ID: "))
        # room_number = int(input("Enter room number: "))
        # booking_start_date = input("Enter booking start date (YYYY-MM-DD): ")
        # booking_end_date = input("Enter booking end date (YYYY-MM-DD): ")
        # price = float(input("Enter price: "))

        booking_id, client_id, room_number, booking_start_date, booking_end_date, price = self.view_booking_ticket.get_booking_ticket_input()
        # Вызов метода из класса Model для добавления бронирования
        success = self.model.add_booking_ticket(booking_id, client_id, room_number, booking_start_date, booking_end_date, price)

        # Отображение сообщения о результате операции
        if success:
            self.view.show_message("Booking added successfully!")
        else:
            self.view.show_message("Failed to add booking.")

    def view_booking_tickets(self):
        # Вызов метода из класса Model для получения всех бронирований
        booking_tickets = self.model.get_all_booking_tickets()

        # Отображение бронирований через метод из класса View
        self.view_booking_ticket.show_booking_tickets(booking_tickets)

    def update_booking_ticket(self):
        # Запрос ID бронирования, которое нужно обновить
        #booking_id = int(input("Enter booking ID: "))
        booking_id = self.view_booking_ticket.get_booking_id()

        # Проверка, существует ли бронирование с указанным ID
        booking_exists = self.model.check_booking_existence(booking_id)

        if booking_exists:
            # Запрос обновленных данных о бронировании от пользователя
            # client_id = int(input("Enter new client ID: "))
            # room_number = int(input("Enter new room number: "))
            # booking_start_date = input("Enter new booking start date (YYYY-MM-DD): ")
            # booking_end_date = input("Enter new booking end date (YYYY-MM-DD): ")
            # price = float(input("Enter new price: "))
            #
            # client_id, name, surname, email = self.view_client.get_client_input()
            booking_id, client_id, room_number, booking_start_date, booking_end_date, price = self.view_booking_ticket.get_booking_ticket_input()
            # Вызов метода из класса Model для обновления бронирования
            success = self.model.update_booking_ticket(booking_id, client_id, room_number, booking_start_date,
                                                       booking_end_date, price)

            # Отображение сообщения о результате операции
            if success:
                self.view.show_message("Booking updated successfully!")
            else:
                self.view.show_message("Failed to update booking.")
        else:
            self.view.show_message("Booking with the specified ID does not exist.")

    def delete_booking_ticket(self):
        # Запрос ID бронирования, которое нужно удалить
        #booking_id = int(input("Enter booking ID: "))
        booking_id = self.view_booking_ticket.get_booking_id()

        # Проверка, существует ли бронирование с указанным ID
        booking_exists = self.model.check_booking_existence(booking_id)

        if booking_exists:
            # Вызов метода из класса Model для удаления бронирования
            success = self.model.delete_booking_ticket(booking_id)

            # Отображение сообщения о результате операции
            if success:
                self.view.show_message("Booking deleted successfully!")
            else:
                self.view.show_message("Failed to delete booking.")
        else:
            self.view.show_message("Booking with the specified ID does not exist.")
#################################################

    def add_client(self):
        client_id, name, surname, email = self.view_client.get_client_input()
        if self.model.add_client(client_id, name, surname, email):
            self.view_client.show_client_message("Client added successfully!")
        else:
            self.view_client.show_client_message("Failed to add client.")

    def view_clients(self):
        clients = self.model.get_all_clients()
        self.view_client.show_clients(clients)

    def update_client(self):
        #client_id = self.view_client.get_client_id()
        client_id, name, surname, email = self.view_client.get_client_input()
        if self.model.update_client(client_id, name, surname, email):
            self.view_client.show_client_message("Client updated successfully!")
        else:
            self.view_client.show_client_message("Failed to update client.")

    def delete_client(self):
        client_id = self.view_client.get_client_id()
        if self.model.delete_client(client_id):
            self.view_client.show_client_message("Client deleted successfully!")
        else:
            self.view_client.show_client_message("Failed to delete client.")

#################################################

    def add_room(self):
        # # Запрос данных о комнате от пользователя
        # room_number = int(input("Enter room number: "))
        # room_type = input("Enter room type: ")
        #
        # # Вызов метода из класса Model для добавления комнаты
        # success = self.model.add_room(room_number, room_type)
        #
        # # Отображение сообщения о результате операции
        # if success:
        #     self.view.show_message("Room added successfully!")
        # else:
        #     self.view.show_message("Failed to add room.")

        room_number = self.view_room.get_room_number()
        room_type = self.view_room.get_room_input()

        if self.model.add_room(room_number, room_type):
            self.view_room.show_room_message("Room added successfully!")
        else:
            self.view_room.show_room_message("Failed to add room.")

    def view_rooms(self):
        # Вызов метода из класса Model для получения всех комнат
        rooms = self.model.get_all_rooms()

        # Отображение комнат через метод из класса ViewRoom (подразумевая, что у вас есть такой класс)
        self.view_room.show_rooms(rooms)

    def update_room(self):
        # Запрос номера комнаты, которую нужно обновить
        room_number = self.view_room.get_room_number()

        # Проверка, существует ли комната с указанным номером
        room_exists = self.model.check_room_existence(room_number)

        if room_exists:
            # Запрос обновленных данных о комнате от пользователя
            room_type = self.view_room.get_room_input()

            # Вызов метода из класса Model для обновления комнаты
            success = self.model.update_room(room_number, room_type)

            # Отображение сообщения о результате операции
            if success:
                self.view.show_message("Room updated successfully!")
            else:
                self.view.show_message("Failed to update room.")
        else:
            self.view.show_message("Room with the specified number does not exist.")

    def delete_room(self):
        # Запрос номера комнаты, которую нужно удалить
        room_number = self.view_room.get_room_number()

        # Проверка, существует ли комната с указанным номером
        room_exists = self.model.check_room_existence(room_number)

        if room_exists:
            # Вызов метода из класса Model для удаления комнаты
            success = self.model.delete_room(room_number)

            # Отображение сообщения о результате операции
            if success:
                self.view.show_message("Room deleted successfully!")
            else:
                self.view.show_message("Failed to delete room.")
        else:
            self.view.show_message("Room with the specified number does not exist.")

#################################################
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
