"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: Patrick Williams
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Asset:
    def __init__(self, name, description, encrypted=False):
        self.__name = name
        self.__description =  description
        self.__encrypted = encrypted

    def __str__(self):
        if self.__encrypted:
            return f"{self.__name} {self.__description}[Encrypted]"
        return f"{self.__name} {self.__description}"
