from datetime import datetime
import json

def hello_world(event, context):
    output = []
    rows = ["Проверка 1",
        "Проверка 2",
        "Проверка 3",
        "Проверка 1",
        "Проверка 3",
        "Проверка 2",
        "Hello",
        "world",
        "Hello world",
        "!Hello world!",
        "Hey",
        "Hello world!",
        "New day",
        "Hello world!"]


    blocks_number = len(rows) // 3
    if len(rows) % 3 != 0:
        blocks_number += 1

    block_index = datetime.now().second % blocks_number
    i = block_index * 3

    output.append(rows[i])

    if i + 1 < len(rows):
        output.append(rows[i+1])

    if i + 2 <  len(rows):
        output.append(rows[i+2])

    response = {
        "statusCode": 200,
        "body": json.dumps(output)
    }
    return response

