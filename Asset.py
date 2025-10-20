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
    """
    Represents an Asset object that can
    belong to a Hacker or be stored in a Rig.
    Each asset has a name, description, and
    an encryption state that determines whether
    it can be accessed or transferred.
    Assets can be encrypted or decrypted
    through hacker actions.
    """

    def __init__(self, name, description, encrypted=False):
        self.__name = name
        self.__description = description
        self.__encrypted = encrypted

    def __str__(self):
        """
        String conversion method that returns
        the Asset name, description and if
        Asset is encrypted, will return "[Encrypted]"
        """
        if self.__encrypted:
            return f"{self.__name}: {self.__description} [Encrypted]"
        return f"{self.__name}: {self.__description}"

    def get_name(self):
        """
        Getter method that returns
        the Asset name
        """
        return self.__name

    def get_description(self):
        """
        Getter method that returns
        the Asset description
        """
        return self.__description

    def set_description(self, description):
        """
        Setter method that sets
        the Asset description
        """
        self.__description = description

    def get_encrypted(self):
        """
         Getter method that returns
         the Asset encryption
         """
        return self.__encrypted

    def set_encrypted(self, encrypted):
        """
        Setter method that sets
        the asset encryption
        """
        self.__encrypted = encrypted

    encrypted = property(get_encrypted, set_encrypted) #type: ignore
    description = property(get_description, set_description)  #type: ignore
    name = property(get_name) #type: ignore
