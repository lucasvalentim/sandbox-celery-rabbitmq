import time
import random
from tasks import add
from decouple import config


QNT_TASKS = config('QNT_TASKS', default=100, cast=int)
DURATION = config('DURATION', default=60, cast=int)
INTERVAL = config('INTERVAL', default=1, cast=int)

for m in range(DURATION):
    for n in range(QNT_TASKS):
        print(m, n)

        a = random.randint(1, 100)
        b = random.randint(-100, 1)
        
        add.delay(a, b)

    time.sleep(60 * INTERVAL)
