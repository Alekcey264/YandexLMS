avg_height = 0


def changing_the_norm(arr):
    temp_list = [item for item in arr if item > avg_height]
    global avg_height
    avg_height = sum(arr) / len(arr)
    return len(temp_list)
