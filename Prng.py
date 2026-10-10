import random
import time

while True:
    time.sleep(1)
    f = open('prng-service.txt', 'r+', encoding="utf-8")
    file_data = f.read()
    if "run" in file_data:
        integer = random.randint(1, 1000)
        f.seek(0)
        f.truncate(0)
        f.write(str(integer))
    f.close()
