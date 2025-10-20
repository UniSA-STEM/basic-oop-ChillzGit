"""
File: Rig.py
Description: Rig Class that represents a Rig Object which can store assets, take damage and be upgraded.
Author: Patrick Williams
ID: 110465151
Username: wilpy031
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
import random

class Rig:
    """
    Represents a Rig that stores and manages Asset objects.
    A Rig can take damage, be repaired, upgraded, and generate new assets.
    Its storage capacity increases with each upgrade level, and only unencrypted
    assets can be stored or extracted. Broken rigs can no longer perform operations
    until repaired.
    """

    def __init__(self, name):
        self.__name = name
        self.__damage = 0
        self.__broken = False
        self.__upgrade_level = 0
        self.__storage = [Asset("Data Spike", "Launch at other rigs to damage"), Asset("Data Spike", "Launch at other rigs to damage"),
                          Asset("Removable Drive", "Used to extract unsecured assets")]

    def get_condition(self):
        """
        This method gets the current condition of the rig
        based on the damage and upgrade level.
        """
        if self.__upgrade_level == 0:
            threshold = 2
        elif self.__upgrade_level == 1:
            threshold = 3
        elif self.__upgrade_level == 2:
            threshold = 4
        else:
            threshold = 5

        if self.__broken or self.__damage >= threshold:
            condition = "Broken"
        elif self.__damage == 1:
            condition = "Damaged"
        else:
            condition = "Pristine"

        return f"{condition} (Level {self.__upgrade_level})"

    def take_hit(self):
        """
        This method takes a hit and incurs damage onto
        the rig. There are some rules depending on the upgrade
        level of the rig. Initially, the threshold is 2, and
        if a rig takes 2 damage, the rig will become broken.
        """
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

    def repair(self):
        """
        This method will repair the rig and
        set damage to 0.
        """
        if self.__broken:
            self.__broken = False
        self.__damage = 0

    def upgrade(self):
        """
        This method will upgrade the rig
        by plus 1
        """
        self.__upgrade_level += 1

    def store_asset(self, asset):
        """
        The method will store an asset
        if the asset is not encrypted.
        """
        capacity = 3 + self.__upgrade_level
        if len(self.__storage) >= capacity:
            print("No storage room to store " + asset.get_name() + "! Capacity: " + str(capacity))
            return False

        if not asset.encrypted:
            self.__storage.append(asset)
            return True
        else:
            print(f"Cannot store encrypted asset {asset.get_name()}!")
            return False

    def get_asset(self, asset_name):
        """
        This method will check if asset
        is in storage and if it is,
        will return the asset.
        """
        for asset in self.__storage:
            if asset.get_name() == asset_name:
                return asset
        return None

    def del_asset(self, asset_name):
        """
        This method will check if asset
        is in storage and if it is, will
        delete the asset and return it.
        """
        for asset in self.__storage:
            if asset.get_name() == asset_name:
                if asset.encrypted:
                    return None
                self.__storage.remove(asset)
                return asset
        return None

    def get_storage(self):
        """
        This method will return the storage
        in the rig.
        """
        return self.__storage

    def is_broken(self):
        """
        This method will return either
        True or False depending if the
        rig is broken or not.
        """
        return self.__broken

    def get_name(self):
        """
        Getter method that returns the
        name of the rig.
        """
        return self.__name

    def generate_asset(self):
        """
        This method generates a random asset.
        It checks that the rig has enough storage
        depending on upgrade level. Then a random
        asset is chosen and stored in rigs
        storage.
        """
        capacity = 3 + self.__upgrade_level
        if len(self.__storage) >= capacity:
            print("No storage room to generate new asset! Capacity: " + str(capacity))
            return None

        choices = ["Data Spike", "CryptoToken", "Removable Drive", "Security Chip", "Hardware Patch"]
        asset_name = random.choice(choices)

        if asset_name == "Data Spike":
            desc = "Launch at other rigs to damage"
        elif asset_name == "CryptoToken":
            desc = "Used to acquire or repair rigs"
        elif asset_name == "Removable Drive":
            desc = "Used to extract unsecured assets"
        elif asset_name == "Security Chip":
            desc = "Used to encrypt or decrypt assets"
        else:
            desc = "Used to upgrade rigs"

        new_asset = Asset(asset_name, desc)
        self.__storage.append(new_asset)
        print("Generated asset: " + str(new_asset))
        return new_asset

    def __str__(self):
        """
        String conversion method that prints
        the rigs name, condition, upgrade level
        and stored assets.
        """
        condition = self.get_condition()
        asset_list_str = ""
        for asset in self.__storage:
            asset_list_str += str(asset) + ", "
        if asset_list_str == "":
            asset_list_str = "(empty)"
        else:
            asset_list_str = asset_list_str[:-2]

        return (self.__name + "\n"
                "Condition: " + condition + "\n"
                "Upgrade Level: " + str(self.__upgrade_level) + "\n"
                "Storage: " + asset_list_str)

