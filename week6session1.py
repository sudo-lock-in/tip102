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

# session 2 problem
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_circular(clues):
    curr = clues
    while curr.next:
        if curr.next == clues:
            return True # for some reason infinite loop if u check outside of it. lol.
            # ig in all cases here if next points back to head it is the tail pointing back
        curr = curr.next 
    return False

clue1 = Node("The stolen goods are at an abandoned warehouse")
clue2 = Node("The mayor is accepting bribes")
clue3 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue1

print(is_circular(clue1))
