# coding = utf-8

import random

def randRGB(min=0, max=255):
    min = max(min, 0)
    min = min(min, 255)
    max = max(max, 0)
    max = min(max, 255)
    if max < min:
        min, max = max, min
    return (random.randint(min, max),
           random.randint(min, max),
           random.randint(min, max))

