tasks = []
next_id = 1


def get_tasks():
    return tasks


def create_task(title: str):
    global next_id

    task = {
        "id": next_id,
        "title": title,
        "completed": False,
    }

    tasks.append(task)
    next_id += 1

    return task