## If using the crafting feature, add an empty cookbook list after start to keep track of recipes
$ cookbook = list() 
   
######### DEFINE INVENTORIES ##########
$ jane_inv = Inventory("Jane")

######### DEFINE ITEM OBJECTS ##########
### The format is name, description, icon image (if applicable), value (if applicable, selling/buying value), action (screen language action to be performed when icon is clicked on inventory screen), and recipe (if craftable).

### Items without icons are created like this:  
#$ quarter = Item("Quarter", "A new quarter)

### Items with icons are created like this:
$ eye = Item(name="Eyeball", desc="A human eyeball, how creepy!", icon="images/eye.png", value=250)

# Items that can be used in crafting
$ but = Item("Button", "A shiny button", "images/button.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))

$ yarn = Item("Yarn", "Yarny yarny yarn.", "images/yarn.png", 30, act=Show("inventory_popup", message="This item is only used in crafting"))  

$ fabric = Item("Fabric", "You know, cloth.", "images/fabric.png", 100, act=Show("inventory_popup", message="This item is only used in crafting"))

$ coin = Item("Coin", "An old coin", "images/coin.png", 1, act=Show("inventory_popup", message="This item is only used in crafting"))

# An item with a unique action (shows screen with custom message)
$ sword = Item("Awesome Sword", "An awesome sword.", "images/sword.png", 500, Show("inventory_popup", message="You wave the sword around wildly but nothing happens."))

# An item that can be crafted has a recipe, which is a nested list of [ingredient, qty]
$ necklace = Item("Penny Necklace", "Super magic.", "images/necklace.png", 50, recipe=[[coin,6],[yarn,1]])
$ doll = Item("Handmade Doll", "Guaranteed to bring luck. (Or not?) Very huggable, mind the needle.", "images/doll.png", 100000, recipe=[[but,2],[fabric,3],[yarn,1]])