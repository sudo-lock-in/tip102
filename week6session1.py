class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next
        
# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()


# Function with a bug!
def remove_song(playlist_head, song):
    if not playlist_head:
        return None
    # if playlist_head.next.song == song:
    #         playlist_head.next = playlist_head.next.next
    #     return playlist_head

    current = playlist_head
    while current:
        if current.next.song == song:
            current.next = current.next.next  
            return playlist_head 
        current = current.next

    return playlist_head

playlist = SongNode("SOS", "ABBA", 
                SongNode("Simple Twist of Fate", "Bob Dylan",
                    SongNode("Dreams", "Fleetwood Mac",
                        SongNode("Lovely Day", "Bill Withers"))))

# print_linked_list(remove_song(playlist, "Dreams"))




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

def count_critical_points(song_audio):
    curr = song_audio
    if not curr.next:
        return 0
    prev = curr
    curr = curr.next
    ahead = curr.next.next
    # compare curr
    # compare curr to curr.next and curr.next.next
    count = 0 
    while ahead:
        if prev.value > curr.value and ahead.value > curr.value:
            count += 1
        elif prev.value < curr.value and ahead.value < curr.value:
            count += 1
        prev = curr
        curr = prev.next
        ahead = curr.next.next
    return count

song_audio = Node(5, Node(3, Node(1, Node(2, Node(5, Node(1, Node(2)))))))

# print(count_critical_points(song_audio))




# problem set 2

head = Node("Jimin", Node("Taehyung", Node("Jungkook"))) # (im not doing h*rry p*tter lol... but ig for the rest i oughta)

# print_linked_list(head)

class Node:
    def __init__(self, house, score, next=None):
        self.house = house
        self.value = score
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print((current.house, current.value), end=" -> " if current.next else "\n")
        current = current.next


def count_element(house_points, score):
    count = 0
    curr = house_points
    while curr:
        if curr.value == score:
            count += 1
        curr = curr.next
    return count

house_points = Node("Gryffindor", 600, 
                Node("Ravenclaw", 300,
                    Node("Slytherin", 500,
                        Node("Hufflepuff", 600))))                  

# print(count_element(house_points, 600))



class Node:
    def __init__(self, potion, next=None):
        self.potion = potion
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.potion, end=" -> " if current.next else "\n")
        current = current.next

def find_middle_potion(potions):
    # curr = potions 
    # length = 0

    # while curr:
    #     length += 1
    #     curr = curr.next

    # slow = potions
    # fast = potions

    # while fast and fast.next:
    #     slow = slow.next
    #     fast = fast.next.next

    # if length % 2 == 1:
    #     return slow.potion
    # else:
    #     return slow.next.potion

    # more simple
    slow = potions
    fast = potions

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.potion
    
potions1 = Node("Poison Antidote", Node("Shrinking Solution", Node("Trollblood Tincture")))
potions2 = Node("Elixir of Life", Node("Sleeping Draught", Node("Babbling Beverage", Node("Aging Potion"))))

# print(find_middle_potion(potions1))
# print(find_middle_potion(potions2))

