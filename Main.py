"""
File: main.py
Description: <A brief description of this Python module.>
Author: Patrick Williams
ID: 110465151
Username: wilpy031
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Hacker import Hacker
from Rig import Rig
from Asset import Asset

def intro():
    print("\n========== INTRODUCTION ==========")
    print("This test shows the interaction between hacker objects"
          ", rig objects and asset objects.")

player1 = Hacker("Player 1")
player2 = Hacker("Player 2")

def acquire_a_rig(hacker, name):
    hacker.acquire_rig(name)

def print_inventory_and_rig(hacker):
    print("Inventory:")
    inv = hacker.get_inventory()
    print(inv)
    r = hacker.get_rig()
    if r:
        print("Rig storage:")
        for asset in r.get_storage():
            print(" -", str(asset))
    else:
        print("Rig: None")

def data_spike(attacker, defender):
    if not defender.get_rig():
        print("Target has no rig!")
        return
    print(defender.get_rig().get_condition())
    attacker.launch_data_spike(defender)
    if defender.get_rig().is_broken():
        print("Rig successfully broken, ready for extraction!")

def extract_assets(attacker, defender):
    attacker.extract_from_broken_rig(defender.get_rig())

def encrypt(hacker, asset):
    hacker.encrypt_asset(asset)

def decrypt(hacker, asset):
    hacker.decrypt_asset(asset)

def store_rig(hacker, asset):
    hacker.store_to_rig(asset)

def retrieve_rig(hacker, asset):
    hacker.retrieve_from_rig(asset)

def upgrade(hacker):
    hacker.upgrade_rig()

def repair(hacker):
    hacker.repair_rig()

def generate(hacker):
    hacker.get_rig().generate_asset()

def reduce(hacker, amount):
    hacker.reduce_trace(amount)

intro()

print("\n========== ACQUIRE RIGS ==========")
acquire_a_rig(player1, "Rig1")
acquire_a_rig(player2, "Rig2")

print("\n========== DISPLAY INVENTORY AND STORAGE ==========")
print_inventory_and_rig(player1)
print_inventory_and_rig(player2)

print("\n========== LAUNCH DATA SPIKE ==========")
data_spike(player1, player2)
print("\n")
data_spike(player1, player2)

print("\n========== EXTRACT FROM BROKEN RIG ==========")
print("Player 1 inventory before:")
print(player1.get_inventory())
extract_assets(player1, player2)
print("\nPlayer 1 inventory after:")
print(player1.get_inventory())

print("\n========== Encrypt Assets ==========")
player1._Hacker__inventory.append(Asset("Security Chip", "Used to encrypt or decrypt assets"))
print("Player 1 inventory Before:")
print(player1.get_inventory())
encrypt(player1, "Data Spike")
print("\nPlayer 1 inventory After:")
print(player1.get_inventory())

print("\n========== DECRYPT ASSETS ==========")
player1._Hacker__inventory.append(Asset("Security Chip", "Used to encrypt or decrypt assets"))
print("Player 1 inventory Before:")
print(player1.get_inventory())
decrypt(player1, "Data Spike")
print("\nPlayer 1 inventory After:")
print(player1.get_inventory())

print("\n========== STORE TO RIG ==========")
print("Player 1 inventory and rig before:")
print_inventory_and_rig(player1)
store_rig(player1, "Data Spike")
print("Player 1 inventory and rig after:\n")
print_inventory_and_rig(player1)

print("\n========== RETRIEVE FROM RIG ==========")
print("Player 1 inventory and rig before:")
print_inventory_and_rig(player1)
retrieve_rig(player1, "Data Spike")
print("\nPlayer 1 inventory and rig after:")
print_inventory_and_rig(player1)

print("\n========== UPGRADE RIG ==========")
player1.upgrade_rig()
player1._Hacker__inventory.append(Asset("Hardware Patch", "Used to upgrade rigs"))
player1.upgrade_rig()

print("\n========== REPAIR RIG ==========")
print(player2.get_rig().get_condition())
player2._Hacker__inventory.append(Asset("CryptoToken", "Used to acquire or repair rigs"))
repair(player2)
print(player2.get_rig().get_condition())

print("\n========== TRACE LIMITER ==========")
store_rig(player1, "Data Spike")
store_rig(player1, "Data Spike")
print(player1)
data_spike(player1, player2)
print("\n")
data_spike(player1, player2)
print("\n")
player2._Hacker__inventory.append(Asset("CryptoToken", "Used to acquire or repair rigs"))
repair(player2)
print("\n")
data_spike(player1, player2)
print("\n")
reduce(player1, 5)
print(player1)

print("\n========== GENERATE ASSETS ==========")
print("Player 1 inventory and rig before:\n")
print_inventory_and_rig(player1)
generate(player1)
print("Player 1 inventory and rig after:\n")
print_inventory_and_rig(player1)