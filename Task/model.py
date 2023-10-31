

class ModelTask:
    def __init__(self, db_model):
        #self.db_manager = db_model
        self.conn = db_model.conn  # Передаем атрибут conn из db_model

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
