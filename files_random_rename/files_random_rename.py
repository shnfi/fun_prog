import pathlib
import random
import os

names = ["hello", "shit", "dog", "fool", "hihi", "abc", "bye", "united", "new_shit", "aha", "noway", "trash", "new_trash", "efg", "hig"]


for fn in os.listdir('.') :
    if (fn[0] != '.') :
        random_name = random.choice(names)
        os.rename(fn, f"{random_name}{pathlib.Path(fn).suffix}")
