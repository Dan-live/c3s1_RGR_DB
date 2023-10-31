

class ControllerTask:
    def __init__(self, model_task, view_task):
        self.model_task = model_task
        self.view_task = view_task

    def add_task(self):
        title, description = self.view_task.get_task_input()
        self.model_task.add_task(title, description)
        self.view_task.show_message("Task added successfully!")

    def view_tasks(self):
        tasks = self.model_task.get_all_tasks()
        self.view_task.show_tasks(tasks)

    def update_task(self):
        task_id = self.view_task.get_task_id()
        title, description = self.view_task.get_task_input()
        self.model_task.update_task(task_id, title, description)
        self.view_task.show_message("Task updated successfully!")

    def delete_task(self):
        task_id = self.view_task.get_task_id()
        self.model_task.delete_task(task_id)
        self.view_task.show_message("Task deleted successfully!")
