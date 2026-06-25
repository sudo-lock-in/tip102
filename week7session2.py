def find_cruise_length(cruise_lengths, vacation_length):
    l = 0
    h = len(cruise_lengths) - 1
    while l <= h:
        mid = (l + h) // 2
        if cruise_lengths[mid] == vacation_length:
            return True
        elif cruise_lengths[mid] > vacation_length:
            h -= 1
        elif cruise_lengths[mid] < vacation_length:
            l += 1
    return False


    
# print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))

# print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))



# helper 
def search_cabin(cabins, preferred_deck, l, h):
    # l, h = 0, len(cabins) - 1
    if l > h:
        return l
    mid = (l + h)//2
    if cabins[mid] == preferred_deck:
        return mid
    elif cabins[mid] > preferred_deck:
        h -= 1
        return search_cabin(cabins, preferred_deck, l, h)
    else:
        l += 1
        return search_cabin(cabins, preferred_deck, l, h)
 


def find_cabin_index(cabins, preferred_deck):
    return search_cabin(cabins, preferred_deck, 0, len(cabins) - 1)
    
    
# print(find_cabin_index([1, 3, 5, 6], 5))
# print(find_cabin_index([1, 3, 5, 6], 2))
# print(find_cabin_index([1, 3, 5, 6], 7))

def count_checked_in_passengers(rooms):
    l, h = 0, len(rooms) - 1
    count  = 0
    while l <= h:
        mid = (l + h)//2
        if rooms[mid] == 1:
            count += 1
            h -= 1
        else:
            l += 1
    return count
    
rooms1 = [0, 0, 0, 1, 1, 1, 1]
rooms2 = [0, 0, 0, 0, 0, 1]
rooms3 = [0, 0, 0, 0, 0, 0]

# print(count_checked_in_passengers(rooms1)) 
# print(count_checked_in_passengers(rooms2))
# print(count_checked_in_passengers(rooms3))