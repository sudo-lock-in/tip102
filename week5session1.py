# Step 1: Copy the following code into your IDE.

# Step 2: Instantiate an instance of the class Villager, which represents characters in Animal Crossing. Store the instance in a variable named apollo.

#     The Villager object created should have the name "Apollo", the species "Eagle", and the catchphrase "pah".

class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

apollo = Villager("Apollo", "Eagle", "pah")

# print(apollo.name)  
# print(apollo.species)  
# print(apollo.catchphrase) 
# print(apollo.furniture) 

# Step 1: Using the Villager class from Problem 1, add the following greet_player() method to your existing code:



# Step 2: Create a second instance of Villager in a variable named bones.

bones = Villager("Bones", "Dog", "yip yip")
# print(bones.greet_player("AJ"))

#     The Villager object created should have name "Bones", species "Dog", and catchphrase "yip yip".

# Step 3: Call the method greet_player() with your name and print out "Bones: Hey there, <your name>! How's it going, yip yip!". 
# For example, if your name is Tram, "Bones: Hey there, Tram! How's it going, yip yip?" would be printed out to the console.



# In Animal Crossing, as players become friends with villagers, the villagers might ask the player to suggest a new catchphrase.

# Adding on to your existing code, update bones so that his catchphrase is "ruff it up" instead of its current value, "yip yip".

bones.catchphrase = "ruff it up"
# print(bones.greet_player("Samia"))


# The Villager class has been updated below to include the new string attribute personality representing the character's personality type.

# Outside of the Villager class, write a function of_personality_type(). Given a list of Villager instances townies and a string personality_type 
# as parameters, return a list containing the names of all villagers in townies with personality personality_type. Return the names in any order.

class Villager:
    def __init__(self, name, species, personality, catchphrase):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
    # ... methods from previous problems
    
def of_personality_type(townies, personality_type):
    # we would have to iterate through th elist of "townies" and for each villager that has a matching personality to the parameter we return thie rname
    # returned in an array
    out = []
    for villager in townies:
        if villager.personality == personality_type:
            out.append(villager.name)
    return out

isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

# print(of_personality_type([isabelle, bob, stitches], "Lazy"))
# print(of_personality_type([isabelle, bob, stitches], "Cranky"))


# The Villager constructor has been updated to include an additional attribute neighbor. A villager's neighbor is another Villager instance and 
# represents their closest neighbor. By default, a Villager's neighbor is set to None.

# Given two Villager instances start_villager and target_villager, write a function message_received() that returns True if you can pass a message 
# from the start_villager to the target_villager through a series of neighbors and False otherwise.

class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor
    # ... methods from previous problems
    
def message_received(start_villager, target_villager):
    curr = start_villager
    while curr.neighbor is not None:
        if curr.neighbor == target_villager:
            return True
        else:
            curr = curr.neighbor
    return False

isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
isabelle.neighbor = tom_nook
tom_nook.neighbor = kk_slider

# print(message_received(isabelle, kk_slider))
# print(message_received(kk_slider, isabelle))

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

tom_nook = Node("Tom Nook")
tommy = Node("Tommy") 
tom_nook.next = tommy 
# print(tom_nook.value) 
# print(tom_nook.next.value) 
# print(tommy.value) 
# print(tommy.next) 

# Using the linked list from Problem 9, create a new Node timmy with value "Timmy"
#  and place it between tom_nook and tommy so the new linked list is tom_nook -> timmy -> tommy.
timmy = Node("Timmy")
timmy.next = tommy
tom_nook.next = timmy
# print(tom_nook.value)
# print(tom_nook.next.value)
# print(timmy.value)
# print(timmy.next.value)
# print(tommy.value)
# print(tommy.next)

# Using the linked list from Problem 10, remove the tom_nook node and add in a node
#  saharah with value "Saharah" to the end of the list so that the resulting list is timmy -> tommy -> saharah.

tom_nook.next = None
timmy.next = tommy
saharah = Node("Saharah")
tommy.next = saharah
# print(tom_nook.next) 
# print(timmy.value) 
# print(timmy.next.value)  
# print(tommy.value) 
# print(tommy.next.value)
# print(saharah.value)  
# print(saharah.next) 



def print_list(head):
    curr = head
    tojoin = []
    while curr:
        tojoin.append(curr.value)
        curr = curr.next
    return " -> ".join(tojoin)

isabelle = Node("Isabelle")
saharah = Node("Saharah")
cj = Node("C.J.")

isabelle.next = saharah
saharah.next = cj

print(print_list(isabelle))


