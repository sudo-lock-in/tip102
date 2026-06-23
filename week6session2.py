class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_circular(clues):
    curr = clues
    while curr.next:
        if curr.next == clues:
            return True # put statement in here to avoid infinite loop because the curr.next will point to the head if true
            # and continue endlessly
            # so if any nodes point to head that is the looping/tail part
            # if i did it like
            # while curr.next:
            #   curr = curr.next
            # if curr.next == clues:
            #   return True
            # it wouldnt work because the while loop will keep going since there will always be a curr.next if it points to head
            # so return inside the loop if it points to head to make it stop
        curr = curr.next 
    return False

clue1 = Node("The stolen goods are at an abandoned warehouse")
clue2 = Node("The mayor is accepting bribes")
clue3 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue1

# print(is_circular(clue1))


def collect_false_evidence(evidence):
    if not evidence:
        return []
    false = []
    slow = evidence
    fast = evidence # both start at evidence to keep the math in order. so we have to make them increment first before the condition in while
    while fast and fast.next: # floyd cycle detection algorithm
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else: # works with loops. if they break it will do this else block
        return []
    
    # floyd algorithm to get to start of cycle. so we can capture every value within it
    slow = evidence
    while slow != fast:
        slow = slow.next
        fast = fast.next 
        # visualize the pointers meeting up to a center point
    
    while fast: # will run inifnitely (its a cycle) until we find the cycle and break
        false.append(fast.value)
        fast = fast.next # incrememnt before checking again since both are equivalent from after cycle start check
        if fast == slow: # slow stays at the beginning of our cycle for comparison
            break
    return false
    

clue1 = Node("Unmarked sedan seen near the crime scene")
clue2 = Node("The stolen goods are at an abandoned warehouse")
clue3 = Node("The mayor is accepting bribes")
clue4 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue4
clue4.next = clue2

clue5 = Node("A masked figure was seen fleeing the scene")
clue6 = Node("Footprints lead to the nearby woods")
clue7 = Node("A broken window was found at the back")
clue5.next = clue6
clue6.next = clue7

# print(collect_false_evidence(clue1))
# print(collect_false_evidence(clue5))

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def partition(suspect_ratings, threshold):
    if not suspect_ratings:
        return None
    less_or_equal_head = Node(0)
    greater_head = Node(0)
    less_or_equal = less_or_equal_head
    greater = greater_head
    # temporary nodes to separate based on the nodes value in relation to threshold
    curr = suspect_ratings
    while curr:
        if curr.value > threshold:
            greater.next = curr
            greater = greater.next
        else:
            less_or_equal.next = curr
            less_or_equal = less_or_equal.next
        curr = curr.next
    
    greater.next = less_or_equal_head.next # the tail of greater head (where the greater pointer is) will link to head of less_or_equal

    if greater_head.next:
        return greater_head.next
    else:
        return less_or_equal_head.next

suspect_ratings = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))

# print_linked_list(partition(suspect_ratings, 3))


def merge_timelines(known_timeline, witness_timeline):
    known = known_timeline
    witness = witness_timeline
    temp_head = Node(0)
    temp = temp_head
    while known or witness:
        if not known:
            temp.next = witness
            witness = witness.next
        elif not witness:
            temp.next = known
            known = known.next
        elif known.value <= witness.value:
            temp.next = known
            known = known.next
        else:
            temp.next = witness
            witness = witness.next
        temp = temp.next
    return temp_head.next


known_timeline = Node(1, Node(2, Node(4)))
witness_timeline = Node(1, Node(3, Node(4)))

# print_linked_list(merge_timelines(known_timeline, witness_timeline))


# helper (fixed)
def tail_to_head(head):
    curr = head
    while curr.next.next:
        curr = curr.next
    tail = curr.next
    curr.next = None
    tail.next = head
    return tail

def rotate_right(evidence, k):
    rotated = evidence
    curr = evidence
    length = 0
    while curr:
        length += 1
        curr = curr.next

    k = k % length # makes it proportionate to array size

    for i in range(k):
        rotated = tail_to_head(rotated)
    return rotated

# evidence_list1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
# evidence_list2 = Node(0, Node(1, Node(2)))

print_linked_list(rotate_right(evidence_list1, 2))
print_linked_list(rotate_right(evidence_list2, 4))


def add_two_numbers(head_a, head_b):
    temp_head = Node(0)
    temp = temp_head
    while head_a or head_b:
        if not head_a:
            temp.next = Node(head_b.value)
            head_b =  head_b.next
        elif not head_b:
            temp.next = Node(head_a.value)
            head_a =  head_a.next
        else:
            if head_a.value + head_b.value == 10:
                temp.next = Node(0)
                temp.next.next = Node(1)
            else:
                if temp.next:
                    temp.next.value += head_a.value + head_b.value
                else:
                    temp.next = Node(head_a.value + head_b.value)
            head_a =  head_a.next
            head_b = head_b.next
        temp = temp.next
    return temp_head.next
    # i did proper solution on leetcode: https://leetcode.com/submissions/detail/2043443460/

head_a = Node(2, Node(4, Node(3))) # 342
head_b = Node(5, Node(6, Node(4))) # 465

print_linked_list(add_two_numbers(head_a, head_b))