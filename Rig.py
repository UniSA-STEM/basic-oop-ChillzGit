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
        self.__storage = [Asset("Data Spike", "Launch at other rigs to damage"), Asset("Data Spike", "Launch at other rigs to damage"),
                          Asset("Removable Drive", "Used to extract unsecured assets")]


    def get_condition(self):
        if self.__damage >= 2:
            self.__broken = True
            condition = "Broken"
        elif self.__damage == 1:
            condition = "Damaged"
        else:
            condition = "Broken"

        return f"{condition} (Level {self.__upgrade_level})"

    def __str__(self):
        condition = self.get_condition()
        asset_name = ""
        for asset in self.__storage:
            asset_name += asset.get_name() + ", "
        asset_name = asset_name[:-2]

        return f"{self.__name} | {condition} | Storage: {asset_name}"

