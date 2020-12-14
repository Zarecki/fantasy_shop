import pdb
from models.item import Item
from models.manufacturer import Manufacturer

import repositories.item_repository as item_repository
import repositories.manufacturer_repository as manufacturer_repository

item_repository.delete_all()
manufacturer_repository.delete_all()

man_1 = Manufacturer("Lonely Mountain's Lost Halls", "Treasures raised from the roots of Lonely Mountain", "Gemstones")
manufacturer_repository.save(man_1)

man_2 = Manufacturer("Iron Hills Forge", "The finest Dwarven armours, sealed with Dain Ironfoot's personal mark of approval", "Armour")
manufacturer_repository.save(man_2)

man_3 = Manufacturer("Murkwood's Ironbark Armoury", "The finest Elven steel and woodland weaponry", "Weapons")
manufacturer_repository.save(man_3)

man_4 = Manufacturer("Nasty Bitza Kit", "Stabbas, choppas, cuttas! Nocked togevva by da Goblins ov Misty Mountain.", "Weapons")
manufacturer_repository.save(man_4)

item_1 = Item("The Arkenstone", "Found by Thror, Lost by Thrain, Recovered by Thorin", "Gemstones", 0, 1000000, man_1, 1)
item_repository.save(item_1)

item_2 = Item("Heart of the Mountain", "Blood red and shining through the darkness", "Gemstones", 10, 50, man_1, 13)
item_repository.save(item_2)

item_3 = Item("Dwalin's Schnozz", "As garnet a colour as ever was seen on the face of Dwalin the Drinker", "Gemstones", 5, 30, man_1, 10)
item_repository.save(item_3)

item_4 = Item("Laketown Lapis", "The rich blue of Laketown Lake on a cold spring morning", "Gemstones", 3, 25, man_1, 15)
item_repository.save(item_4)

item_5 = Item("Mountain shield", "Twice that of a tower shield, three Dwarves can stand atop each other and barely see over the rim!", "Armour", 8, 80, man_2, 10)
item_repository.save(item_5)

item_6 = Item("Iron maiden", "An all-encompasing suite of solid plate armour. Not for claustrophobes.", "Armour", 15, 100, man_2, 5)
item_repository.save(item_6)

item_7 = Item("Mithril Pyjamas", "Unstabbable P.J.'s! Sleep soundly!", "Armour", 6, 60, man_2, 5)
item_repository.save(item_7)

item_8 = Item("Steel Sabatons", "Ironfoot's Iron Boots! Currently available in Steel", "Amour", 3, 30, man_2, 10)
item_repository.save(item_8)

item_9 = Item("Murkwood scout bow", "An item as immortal as the hands that built it. The classic bow", "Weapons", 4, 20, man_3, 20)
item_repository.save(item_9)

item_10 = Item("Tea Tree Tonfa", "Give your foes an delicately-scented thrashing", "Weapons", 6, 30, man_3, 15)
item_repository.save(item_10)

item_11 = Item("Deadwood Dirk", "Elegantly crafted, forged with finesse, a true joy to shank with", "Weapons", 5, 30, man_3, 10)
item_repository.save(item_11)

item_12 = Item("Tharanduil's Glory", "A gorgeous piece, sumptuous inlays, decadent engraving, delicious decoration. Display only.", "Weapons", 15, 200, man_3, 3)
item_repository.save(item_12)

item_13 = Item("Stabbin' Stick", "It's a stick wot yoo stab wiv. Stick at one end, pointy bit at t'ova.", "Weapons", 1, 3, man_4, 10)
item_repository.save(item_13)

item_14 = Item("Big Cutta", "Issa real big cutta, for sure! Takes two Gobbo gits ta swing!", "Weapons", 3, 10, man_4, 8)
item_repository.save(item_14)

item_15 = Item("DeffPogo", "Dis is, get this, a pogo stick wivva spike at da bottom! A personal favorit!", "Weapons", 8, 80, man_4, 5)
item_repository.save(item_15)

item_16 = Item("Fang Shiv", "A real narsty bit ov kit. A good owld shiv made from a spida fang. Leefal.", "Weapons", 8, 40, man_4, 12)
item_repository.save(item_16)

pdb.set_trace()