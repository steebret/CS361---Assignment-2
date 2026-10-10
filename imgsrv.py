import time

while True:
    time.sleep(1)
    f = open('image-service.txt', 'r+', encoding="utf-8")
    file_data = f.read()
    if file_data.isnumeric():
        number = int(file_data)
        display_image = number % 5 # Five Images total
        display_link = f"U:/Oregon State/Fall 2026/CS 361/Assignment 1/{display_image}.jpg"
        f.seek(0)
        f.truncate(0)
        f.write(display_link)
    f.close()