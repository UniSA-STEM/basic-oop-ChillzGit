"""
File: Rig.py
Description: Rig Class that represents a Rig Object which can store assets, take damage and be upgraded.
Author: Patrick Williams
ID: 110465151
Username: wilpy031
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset

"""
This class represents a computer rig and stores assets, takes damage 
and can be upgraded.
"""
class Rig:
    def __init__(self, name):
        self.__name = name
        self.__damage = 0
        self.__broken = False
        self.__upgrade_level = 0
        self.__storage = [Asset("Data Spike", "Launch at other rigs to damage"), Asset("Data Spike", "Launch at other rigs to damage"),
                          Asset("Removable Drive", "Used to extract unsecured assets")]

    """
    This method gets the current condition of the rig
    based on the damage and upgrade level.
    """
    def get_condition(self):
        if self.__broken or self.__damage >= 2:
            condition = "Broken"
        elif self.__damage == 1:
            condition = "Damaged"
        else:
            condition = "Pristine"

        return f"{condition} (Level {self.__upgrade_level})"

    """
    This method takes a hit and incurs damage onto
    the rig. There are some rules depending on the upgrade
    level of the rig. Initially, the threshold is 2, and
    if a rig takes 2 damage, the rig will become broken.
    """
    def take_hit(self):
        damage = 1
        if self.__upgrade_level == 0:
            threshold = 2
        elif self.__upgrade_level == 1:
            threshold = 3
        elif self.__upgrade_level == 2:
            threshold = 4
        else:
            threshold = 5
        new_damage = damage + self.__damage

        if new_damage >= threshold:
            self.__broken = True

        self.__damage = new_damage

    """
    This method will repair the rig and
    set damage to 0.
    """
    def repair(self):
        if self.__broken:
            self.__broken = False
        self.__damage = 0

    """
    This method will upgrade the rig
    by plus 1
    """
    def upgrade(self):
        self.__upgrade_level += 1


    """
    The method will store an asset
    if the asset is not encrypted.
    """
    def store_asset(self, asset):
        if not asset.encrypted:
            self.__storage.append(asset)


    """
    This method will check if asset
    is in storage and if it is,
    will return the asset.
    """
    def get_asset(self, asset_name):
        for asset in self.__storage:
            if asset.get_name() == asset_name:
                return asset
        return None


    """
    This method will check if asset
    is in storage and if it is, will
    delete the asset and return it.
    """
    def del_asset(self, asset_name):
        for asset in self.__storage:
            if asset.get_name() == asset_name:
                self.__storage.remove(asset)
                return asset
        return None


    """
    This method will return the storage
    in the rig.
    """
    def get_storage(self):
        return self.__storage

    """
    This method will return either
    True or False depending if the 
    rig is broken or not.
    """
    def is_broken(self):
        return self.__broken


    """
    String conversion method that prints 
    the rigs name, condition, upgrade level
    and stored assets.
    """
    def __str__(self):
        condition = self.get_condition()
        asset_name = ""
        for asset in self.__storage:
            asset_name += asset.get_name() + ", "
        if asset_name == "":
            asset_name = "(empty)"
        else:
            asset_name = asset_name[:-2]

        return f"{self.__name}\nCondition: {condition}\nUpgrade Level: {self.__upgrade_level}\nStorage: {asset_name}"

