class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.friends = []

    def get_mutuals(self, new_contact):
        return [x.name for x in self.friends if x in new_contact.friends]

bob = Villager("Bob", "Cat", "pthhhpth")
marshal = Villager("Marshal", "Squirrel", "sulky")
ankha = Villager("Ankha", "Cat", "me meow")
fauna = Villager("Fauna", "Deer", "dearie")
raymond = Villager("Raymond", "Cat", "crisp")
stitches = Villager("Stitches", "Cub", "stuffin")

bob.friends = [stitches, raymond, fauna]
marshal.friends = [raymond, ankha, fauna]
# print(bob.get_mutuals(marshal))

ankha.friends = [marshal]
# print(bob.get_mutuals(ankha))


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

# Connect the provided node instances below to create the linked list kk_slider -> harriet -> saharah -> isabelle.

kk_slider = Node("K.K. Slider")
harriet = Node("Harriet")
saharah = Node("Saharah")
isabelle = Node("Isabelle")

# Add code here to link the above nodes

kk_slider.next = harriet
harriet.next = saharah
saharah.next = isabelle
# print_linked_list(kk_slider)


def add_first(head, task):
    added = Node(task)
    added.next = head
    return added

task_1 = Node("shake tree")
task_2 = Node("dig fossils")
task_3 = Node("catch bugs")
task_1.next = task_2
task_2.next = task_3

# Linked List: shake tree -> dig fossils -> catch bugs
# print_linked_list(add_first(task_1, "check turnip prices"))


def halve_list(head):
    curr = head
    while curr:
        curr.value = curr.value / 2
        curr = curr.next
    return head

node_one = Node(5)
node_two = Node(6)
node_three = Node(7)
node_one.next = node_two
node_two.next = node_three

# Input List: 5 -> 6 -> 7
# print_linked_list(halve_list(node_one))


def delete_tail(head):
    curr = head
    while curr:
        if not curr.next.next:
            curr.next = None
        curr = curr.next
    return head
    

butterfly = Node("Common Butterfly")
ladybug = Node("Ladybug")
beetle = Node("Scarab Beetle")
butterfly.next = ladybug
ladybug.next = beetle

# Input List: butterfly -> ladybug -> beetle
# print_linked_list(delete_tail(butterfly))

def find_min(head):
    curr = head
    mini = curr.value
    while curr:
        if curr.value < mini:
            mini = curr.value
        curr = curr.next
    return mini

head1 = Node(5, Node(6, Node(7, Node(8))))
head2 = Node(8, Node(5, Node(6, Node(7))))

# Linked List: 5 -> 6 -> 7 -> 8
# print(find_min(head1))

# Linked List: 8 -> 5 -> 6 -> 7
# print(find_min(head2))

# def tail_to_head(head):
#     curr = head
#     while curr:
#         if not curr.next.next:
#             tail = curr.next
#             curr.next = None
#         curr = curr.next
#     tail.next = head
#     return tail

# corrected:
def tail_to_head(head):
    curr = head
    while curr.next.next:
        curr = curr.next
    tail = curr.next
    curr.next = None
    tail.next = head
    return tail

daisy = Node("Daisy")
mario = Node("Mario")
toad = Node("Toad") 
peach = Node("Peach")
daisy.next = mario
mario.next = toad
toad.next = peach

# Linked List: Daisy -> Mario -> Toad -> Peach
# print_linked_list(tail_to_head(daisy))

class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

head = Node("Isabelle")
tail = Node("K.K. Slider")

head.next = tail
tail.prev = head

# print(head.value, "<->", head.next.value)
# print(tail.prev.value, "<->", tail.value)


def print_reverse(tail):
    current = tail
    while current:
        print(current.value, end=" " if current.prev else "\n")
        current = current.prev

isabelle = Node("Isabelle")
kk_slider = Node("K.K. Slider")
saharah = Node("Saharah")
isabelle.next = kk_slider
kk_slider.next = saharah
saharah.prev = kk_slider
kk_slider.prev = isabelle

# Linked List: Isabelle <-> K.K. Slider <-> Saharah
print_reverse(saharah)