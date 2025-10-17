"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: Patrick Williams
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset

class Rig:
    def __init__(self, name):
        self.__name = name
        self.__damage = 0
        self.__broken = False
        self.__upgrade_level = 0
        self.__storage = [Asset("Data Spike", "tbd"), Asset("Data Spike", "tbd"),
                          Asset("Removable Drive", "tbd")]

