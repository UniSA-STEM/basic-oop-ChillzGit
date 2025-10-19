"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: Patrick Williams
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
from Rig import Rig

class Hacker:
    def __init__(self, name):
        self.__name = name
        self.__trace = 0
        self.__rig = None
        self.__inventory = [Asset("CryptoToken", "TBD")]

    """
    This method is used for the hacker object to successfully acquire a rig.
    A hacker will need a CryptoToken in their inventory to purchase.
    Upon activation, a print message will appear.
    """
    def acquire_rig(self, rig_name):
        for asset in self.__inventory:
            if asset.get_name() == "CryptoToken":
                self.__inventory.remove(asset)
                if isinstance(rig_name, Rig):
                    self.__rig = rig_name
                    print(f"Successfully acquired rig {rig_name}!")
                else:
                    self.__rig = Rig(rig_name)
                    print(f"Successfully acquired rig {rig_name}!")
                return
        print(f"Failed to acquire rig {rig_name} due to insufficient CryptoToken!")

    def launch_data_spike(self, target):
        if not self.__rig:
            print("No Rig found!")
            return

        target_rig = None
        if isinstance(target, Rig):
            target_rig = target
        else:
            target_rig = target.get_rig()

        if not target_rig:
            print("Target has no rig!")
            return

        if target_rig.is_broken():
            print("Rig broken, mission aborted! No spike consumed.")
            return

        spike_in_rig = self.__rig.del_asset("Data Spike")

        if not spike_in_rig:
            print("No data spike in storage!")
            return

        target_rig.take_hit()
        self.__trace += 1
        print(f"{self.__name} launched a Data Spike at {target_rig.get_name()}! (Trace: {self.__trace})")
        print(f"Target rig condition: {target_rig.get_condition()}")

    def encrypt_asset(self, asset_name):
        if not self.__rig:
            print("No Rig found!")
            return

        chip = self.find_asset_by_name("Security Chip")
        if chip:
            self.__inventory.remove(chip)
        else:
            chip = self.__rig.del_asset("Security Chip")
        if not chip:
            print(f"Failed to encrypt asset {asset_name}! No security chip found!")
            return

        for asset in self.__inventory:
            if asset.get_name() == asset_name:
                asset.set_encrypted(True)
                print(f"Successfully encrypted asset {asset_name}!")
                return

        asset_in_rig = self.__rig.get_asset(asset_name)
        if asset_in_rig:
            asset_in_rig.set_encrypted(True)
            print(f"Successfully encrypted asset {asset_name}!")
            return

        print(f"Failed to encrypt asset {asset_name}!")
        return

    def decrypt_asset(self, asset_name):
        if not self.__rig:
            print("No Rig found!")
            return

        chip = self.find_asset_by_name("Security Chip")
        if chip:
            self.__inventory.remove(chip)
        else:
            self.__rig.del_asset("Security Chip")
        if not chip:
            print(f"Failed to decrypt asset {asset_name}! No security chip found!")
            return

        for asset in self.__inventory:
            if asset.get_name() == asset_name:
                asset.set_encrypted(False)
                print(f"Successfully decrypted asset {asset_name}!")
                return

        asset_in_rig = self.__rig.get_asset(asset_name)
        if asset_in_rig:
            asset_in_rig.set_encrypted(False)
            print(f"Successfully decrypted asset {asset_name}!")
            return

        print(f"Failed to decrypt asset {asset_name}!")

    def upgrade_rig(self):
        pass

    def store_to_rig(self, asset_name):
        if not self.__rig:
            print("No Rig found!")
            return

        asset = self.find_asset_by_name(asset_name)

        if not asset:
            print(f"{asset_name} not found in inventory!")
            return
        self.__rig.store_asset(asset)
        if asset in self.__rig.get_storage():
            self.__inventory.remove(asset)
            print(f"{asset_name} removed from inventory and stored in rig!")

    def retrieve_from_rig(self, asset_name):
        if not self.__rig:
            print("No Rig found!")
            return

        asset = self.__rig.del_asset(asset_name)
        if asset:
            self.__inventory.append(asset)
            print(f"{asset_name} added to inventory!")
        else:
            print(f"{asset_name} not found in rigs storage!")

    def find_asset_by_name(self, name):
        for asset in self.__inventory:
            if asset.get_name() == name:
                return asset
        return None

    def get_hacker_name(self):
        return self.__name

    def get_trace(self):
        return self.__trace

    def get_rig(self):
        return self.__rig

    def get_inventory(self):
        inventory = ""
        for asset in self.__inventory:
            inventory += asset.get_name()
            inventory += "\n"
        return inventory

    def __str__(self):
        return self.__name



