queue_data = []

def insert(value):
    queue_data.append(value)
    return queue_data

def remove():
    if queue_data:
        queue_data.pop(0)
    return queue_data

def get():
    return queue_data
