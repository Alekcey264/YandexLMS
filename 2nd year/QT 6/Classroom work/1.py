with open('input.bmp', 'br') as f:
    lines = f.read()

header = lines[:54]
data = lines[54:]
negative_data = bytes([255 - item for item in data])

with open('res.bmp', 'wb') as f:
    f.write(header)
    f.write(negative_data)
