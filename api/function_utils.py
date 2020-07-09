from tasks import tasks


class FunctionUtils:
    @staticmethod
    def find_task(task_id):
        """
        Return a task by the id provided
        :param task_id:
        :return:
        """
        return [task for task in tasks if task['id'] == task_id]
