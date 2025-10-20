"""
File: Hacker.py
Description: Hacker class which interacts with Rig and Asset objects
Author: Patrick Williams
ID: 110465151
Username: wilpy031
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
from Rig import Rig

THRESHOLD = 5

class Hacker:
    """
    Represents a Hacker object that interacts with
    both Rig and Asset classes. A Hacker can perform
    actions such as acquiring a rig, encrypting and decrypting
    assets, launching data spikes, upgrading or
    repairing their rig, and extracting assets from broken
     rigs. Hackers can also store and retrieve assets between
    their rig and inventory.
    """

    def __init__(self, name):
        self.__name = name
        self.__trace = 0
        self.__rig = None
        self.__inventory = [Asset("CryptoToken", "TBD")]

    def acquire_rig(self, rig_name):
        """
        This method is used for the hacker object to successfully acquire a rig.
        A hacker will need a CryptoToken in their inventory to purchase.
        Upon activation, a print message will appear.
        """
        for asset in self.__inventory:
            if asset.get_name() == "CryptoToken":
                self.__inventory.remove(asset)
                if isinstance(rig_name, Rig):
                    self.__rig = rig_name
                else:
                    self.__rig = Rig(rig_name)

                print(f"Successfully acquired Rig {self.__rig.get_name()}!")
                return
        if isinstance(rig_name, Rig):
            rig_n = rig_name.get_name()
        else:
            rig_n = rig_name

        print(f"Failed to acquire Rig {rig_n} due to insufficient CryptoToken!")

    def launch_data_spike(self, target):
        """
        This method is used to launch a data spike
        at a selected target rig. It checks if the
        hackers trace level is below the trace threshold.
        It then delivers damage to target rig as long
        as target rig is not broken. After successfully
        damaging target rig, a trace point is added
        to the hacker.
        """
        if not self.__rig:
            print("No Rig found!")
            return

        if self._trace_blocked("Launch a Data Spike"):
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
        """
        This method is used to encrypt
        an asset providing the hacker has a
        security chip in their inventory or
        rigs storage.
        """
        if not self.__rig:
            print("No Rig found!")
            return

        chip = self.find_asset_by_name("Security Chip")
        if chip:
            self.__inventory.remove(chip)
        else:
            chip = self.__rig.del_asset("Security Chip")
        if not chip:
            print(f"Failed to encrypt asset {asset_name}! No Security Chip found!")
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

    def decrypt_asset(self, asset_name):
        """
        This method is used to decrypt
        an asset providing the hacker has a
        security chip in their inventory or
        rigs storage.
        """
        if not self.__rig:
            print("No Rig found!")
            return

        chip = self.find_asset_by_name("Security Chip")
        if chip:
            self.__inventory.remove(chip)
        else:
            chip = self.__rig.del_asset("Security Chip")
        if not chip:
            print(f"Failed to decrypt asset {asset_name}! No Security Chip found!")
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
        """
        This method is used to upgrade the hackers
        rig providing they have a rig, the rig isn't
        broken and hacker has a hardware patch.
        The hardware patch is then removed from inventory
        and the rig is upgraded.
        """
        if not self.__rig:
            print("No Rig found!")
            return

        if self.__rig.is_broken():
            print(f"Rig cannot be upgraded as it is broken, please repair!")
            return

        patch = self.find_asset_by_name("Hardware Patch")

        if not patch:
            print("Failed to find a Hardware Patch asset! Unable to upgrade Rig!")
            return

        self.__inventory.remove(patch)
        self.__rig.upgrade()
        print(f"Successfully upgraded Rig: {self.__rig.get_name()} to {self.__rig.get_condition()}")

    def repair_rig(self):
        """
        This method is used to repair a rig
        providing that the hacker has a rig,
        the rig is broken and hacker has
        a CryptoToken.
        """
        if not self.__rig:
            print("No Rig found!")
            return
        if not self.__rig.is_broken():
            print("Rig is not broken! No repair needed!")
            return
        token = self.find_asset_by_name("CryptoToken")
        if not token:
            print("Failed to find a CryptoToken asset! Unable to repair!")
            return
        self.__inventory.remove(token)
        self.__rig.repair()
        print(f"Rig: {self.__rig.get_name()} is repaired!")

    def store_to_rig(self, asset_name):
        """
        This method is used to store a chosen
        asset from inventory to their rig.
        It then removes the chosen asset from inventory.
        """
        if not self.__rig:
            print("No Rig found!")
            return

        asset = self.find_asset_by_name(asset_name)

        if not asset:
            print(f"{asset_name} not found in inventory!")
            return

        stored = self.__rig.store_asset(asset)
        if stored:
            self.__inventory.remove(asset)
            print(f"{asset_name} removed from inventory and stored in rig!")

    def retrieve_from_rig(self, asset_name):
        """
        This method is used to store a chosen
        asset from their rig to their inventory.
        It then removes the chosen asset from their
        rig.
        """
        if not self.__rig:
            print("No Rig found!")
            return

        asset = self.__rig.del_asset(asset_name)
        if asset:
            self.__inventory.append(asset)
            print(f"{asset_name} added to inventory!")
        else:
            print(f"{asset_name} not found in Rig's storage!")

    def extract_from_broken_rig(self, target_rig):
        """
        This method is used to extract assets
        from a broken rig. It checks that the hacker
        has a rig, an acceptable trace level and
        if the target rig is broken. It also checks
        if the hacker has a removable drive so they
        can extract assets from the broken rig.
        It then extracts all unencrypted assets from
        target_rig and stores them in their inventory.
        """
        if not self.__rig:
            print("No Rig found!")
            return

        if not target_rig.is_broken():
            print(f"Rig {target_rig.get_name()} is not broken, mission aborted!")
            return

        if self._trace_blocked("Extract from a broken Rig"):
            return

        drive = self.__rig.del_asset("Removable Drive")

        if not drive:
            print("No removable drive found! Mission aborted!")
            return

        extracted_assets = ""
        while True:
            found = False
            for asset in target_rig.get_storage():
                if not asset.encrypted:
                    target_rig.del_asset(asset.get_name())
                    self.__inventory.append(asset)
                    if extracted_assets:
                        extracted_assets += ", " + asset.get_name()
                    else:
                        extracted_assets = asset.get_name()
                    found = True
                    break
            if not found:
                break

        if extracted_assets:
            self.__trace += 1
            print(f"Extracted assets: {extracted_assets}\nTrace: {self.__trace}")
        else:
            print(f"No unencrypted assets found for {target_rig.get_name()}!")

    def _trace_blocked(self, action):
        """
        Private method that checks if the trace is
        above the threshold and displays message
        to reduce trace.
        """
        if self.__trace >= THRESHOLD:
            print(f"Trace is too high to {action}! Reduce trace!")
            return True

        return False

    def reduce_trace(self, amount):
        """
        This method reduces trace by the amount
        put into the method. It assures the trace doesn't
        go below 0.
        """
        if amount < 0:
            print("Amount cannot be negative!")
            return self.__trace
        old = self.__trace
        if self.__trace - amount >= 0:
            self.__trace -= amount
        else:
            self.__trace = 0

        print(f"Trace reduced from {old} to {self.__trace}!")

        return self.__trace

    def find_asset_by_name(self, name):
        """
         This method finds an asset by
         their name and returns the asset
         """
        for asset in self.__inventory:
            if asset.get_name() == name:
                return asset

        return None

    def get_hacker_name(self):
        """
        Getter method that returns
        the hacker's name.
        """
        return self.__name

    def get_trace(self):
        """
        Getter method that returns
        hacker's trace level.
        """
        return self.__trace

    def get_rig(self):
        """
        Getter method that returns
        the hacker's rig.
        """
        return self.__rig

    def get_inventory(self):
        """
        Getter method that returns
        the hacker's inventory.
        """
        if not self.__inventory:
            return "Empty Inventory!"
        inventory = ""
        for asset in self.__inventory:
            inventory += str(asset) + "\n"

        return inventory

    def __str__(self):
        """
        String conversion method that returns
        the hackers name, trace level,
        rig and inventory.
        """
        string = ""
        string += "Name: "+ self.get_hacker_name() + "\n"
        string += "Trace Level: " + str(self.get_trace()) + "\n"
        if self.__rig:
            string += "Rig: "+ self.__rig.get_name() + "\n"
        else:
            string += "No rig acquired\n"
        string += "Inventory: " + self.get_inventory() + "\n"

        return string



