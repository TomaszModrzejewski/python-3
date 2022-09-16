# -*- coding: utf-8 -*-
__author__ = 'PatchLion'
import uuid

def createSN(count):
    if count <= 0:
        return


    return [uuid.uuid4().hex.upper() for _ in range(count)]

def createSNAndSaveToFile(count, filepath):
    sns = createSN(count)

    with open(filepath, 'wt') as f:
        for sn in sns:
            f.write(sn+"\n");

print(createSN(200))
createSNAndSaveToFile(200, 'sns.txt')