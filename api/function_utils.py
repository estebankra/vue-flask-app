from tasks import tasks


class FunctionUtils:
    @staticmethod
    def find_task(task_id):
        return [task for task in tasks if task['id'] == task_id]
