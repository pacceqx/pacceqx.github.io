#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess

if len(sys.argv) == 1 or not os.path.isdir(sys.argv[1]):
    print("Passe o nome da pasta por parametro")
    exit(1)

images = ["jpg", "jpeg", "png"]

def extension(x): return x.lower().split(".")[-1]

for pasta in sys.argv[1:]:
    if not os.path.isdir(pasta):
        continue
    files = os.listdir(pasta)
    files = [os.path.join(pasta, x) for x in files]  # construindo path completo
    files = [x for x in files if os.path.isfile(x)]  # obtendo apenas os arquivos
    files = [x for x in files if extension(x) in images]  # obtendo apenas os que são imagens
    for x in files:
        cmd = ["convert",  x, "-resize", "854x480^", "-gravity", "center", "-extent", "854x480", x]
        print(cmd)
        subprocess.run(cmd)
