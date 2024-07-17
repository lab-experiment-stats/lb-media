import pyperclip,time
import random
# Output ryxay
for d in range(1000):
    a = ''.join((random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(random.randint(8,13))))
    pyperclip.copy(a)
    time.sleep(0.2) 