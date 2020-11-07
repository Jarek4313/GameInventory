import os
import csv
from pathlib import Path
class GameInventory:
    def __init__(self, dictionary):
        self.__dictionary = dictionary

    
    @property
    def Dictionary(self):
        return self.__dictionary
    
    @Dictionary.setter
    def Dictionary(self, dictionary):
        self.__dictionary = dictionary

    
    
    def display_inventory(self):      
        if not self.__dictionary == {} or not self.__dictionary == None:
            for key,value in self.__dictionary.items():
                print("{:<30} | {:>20}".format(key,value))
        input()
    

    def add__to_inventory(self, added_items):
        os.system("cls || clear") 
        if not self.__dictionary == {} or not self.__dictionary == None:
            for key_dic in self.__dictionary.keys():
                for key_item in added_items.keys():
                    if key_dic == key_item:
                        self.__dictionary[key_dic] += added_items[key_item]
            
            for key_item in added_items.keys():
                if not key_item in self.__dictionary.keys():
                        self.__dictionary[key_item] = added_items[key_item]

    def remove_from_inventory(self, removed_items):
        if not self.__dictionary == {} or not self.__dictionary == None:
            for key_remove_items in removed_items.keys():
                if key_remove_items in self.__dictionary.keys():
                    self.__dictionary[key_remove_items] -= removed_items[key_remove_items]                      
                    if self.__dictionary[key_remove_items] <= 0:
                        self.__dictionary.pop(key_remove_items)

    def __add(self, item):
        if item in self.__dictionary.keys():
            self.__dictionary[item] += 1
        else:
            self.__dictionary[item] = 1
            
    def import_inventory(self, filename="import_inventory.csv"):
        path = Path(__file__).parent
        with open(f'{path}\\{filename}') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                for item in row:
                    self.__add(item)


dictionary = {
    "gold coin": 45,
    "arrow": 12,
    "torch": 6
}

game_inventory = GameInventory(dictionary)
game_inventory.import_inventory("file.csv")
game_inventory.display_inventory()
game_inventory.add__to_inventory({"mana potion": 100})
game_inventory.display_inventory()
game_inventory.add__to_inventory({"gold coin": 100, "magic staff": 1})
game_inventory.display_inventory()
game_inventory.remove_from_inventory({"mana potion": 50})
game_inventory.display_inventory()
game_inventory.remove_from_inventory({"magic staff": 1})
game_inventory.display_inventory()



