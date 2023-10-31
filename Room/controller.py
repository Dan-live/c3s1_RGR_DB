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
