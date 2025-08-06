data = []

def insert(value):
    data.append(value)

def remove():
    if data:
        data.pop()

def get():
    return data
