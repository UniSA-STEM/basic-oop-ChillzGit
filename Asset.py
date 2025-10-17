"""
File: Asset.py
Description: This class represents a digital asset that also includes a capability
of encryption. An asset contains a name, description and
whether or not the asset is encrypted.
Author: Patrick Williams
ID: 110465151
Username: wilpy031
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Asset:
    def __init__(self, name, description, encrypted=False):
        self.__name = name
        self.__description = description
        self.__encrypted = encrypted

    def __str__(self):
        if self.__encrypted:
            return f"{self.__name}: {self.__description} [Encrypted]"
        return f"{self.__name}: {self.__description}"

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def get_encrypted(self):
        return self.__encrypted

    def set_encrypted(self, encrypted):
        self.__encrypted = encrypted

    encrypted = property(get_encrypted, set_encrypted) #type: ignore
    description = property(get_description, set_description)  #type: ignore
    name = property(get_name) #type: ignore
