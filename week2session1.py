# Given two lists of strings artists and set_times of length n, write a function lineup() that maps each artist to their set time.

# An artist artists[i] has set time set_times[i]. Assume i <= 0 < n and len(artists) == len(set_times).

def lineup(artists, set_times):
    n = len(artists)
    lineup = {}
    for i in range(n):
        lineup[artists[i]] = set_times[i]
    return lineup

artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

# print(lineup(artists1, set_times1))
# print(lineup(artists2, set_times2))


# You are designing an app for your festival to help attendees have the best experience possible! As part of the application, 
# users will be able to easily search their favorite artist and find out the day, time, and stage the artist is playing at. 
# Write a function get_artist_info() that accepts a string artist and a dictionary festival_schedule mapping artist's names 
# to dictionaries containing the day, time, and stage they are playing on. Return the dictionary containing the information about 
# the given artist.
# If the artist searched for does not exist in festival_schedule, return the dictionary {"message": "Artist not found"}.

def get_artist_info(artist, festival_schedule):
    # we want to start with creating the default dictionary if artist not in festival
    # that could be a first line to check before we start working on the rest of the problem
    # we find the artist key in the nested dictionary and return the value of the dictionary that is the value
    not_exist = {
        "message": "Artist not found"
    }
    if artist not in festival_schedule:
        return not_exist
    else:
        return festival_schedule[artist]


festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}
# print(get_artist_info("Taylor Swift", festival_schedule))  # works
# print(get_artist_info("Blood Orange", festival_schedule)) 

# A dictionary ticket_sales is used to map ticket type to number of tickets sold. 
# Return the total number of tickets of all types sold.

def total_sales(ticket_sales):
    # we could either use sum() or iterate through the dictionary
    return sum(ticket_sales.values())
ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

# print(total_sales(ticket_sales))


# Demand for your festival has exceeded expectations, 
# so you're expanding the festival to span two different venues. Some artists will perform both venues, 
# while others will perform at just one. To ensure that there are no scheduling conflicts,
# implement a function identify_conflicts() that accepts two dictionaries venue1_schedule 
# and venue2_schedule each mapping the artists playing at the venue to their set times. 
# Return a dictionary containing the key-value pairs that are the same in each schedule.

def identify_conflicts(venue1_schedule, venue2_schedule):
    # we are looking for conflicts across two different dictionaries
    # and if there are a key-value pair that are the same in both dictionaries
    # we return a dictionary containing just those
    
    # we can loop through venue1 and if the artist (key) is in venue2 we can check if the value is the same
    # make a new dictionary containing the conflicts
    
    conflicts = {}
    
    for artist in venue1_schedule:
        if artist in venue2_schedule:
            if venue2_schedule[artist] == venue1_schedule[artist]:
                conflicts[artist] = venue1_schedule[artist]
    return conflicts

venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

# print(identify_conflicts(venue1_schedule, venue2_schedule))

# As part of the festival, attendees cast votes for their favorite set. 
# Given a dictionary votes that maps attendees id numbers to the artist they voted for, 
# return the artist that had the highest number of votes. If there is a tie, return any artist with the top number of votes.

from collections import Counter

def best_set(votes):
    # use python counter/count
    freq = Counter(votes.values())
    return freq.most_common(1)[0][0]

votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

# print(best_set(votes1))
# print(best_set(votes2))


# You are given an array audiences consisting of positive integers representing the audience size for different performances
# at a music festival.

# Return the combined size of every audience that had the maxmium size.

# The audience size of a performance is the number of people who attended that performance.

# def max_audience_performances(audiences):
# #    # do a frequency count
#      # multiply the max value by its frequency
#      maximum = max(audiences) # 200
#      freq = Counter(audiences) # keys + the freqs as values
#      return maximum * freq[maximum]

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

# print(max_audience_performances(audiences1))
# print(max_audience_performances(audiences2))

# If you used a dictionary as part of your solution to max_audience_performances() in the previous problem, 
# try reimplementing the function without using a dictionary. If you implemented max_audience_performances() 
# without using a dictionary, try solving the problem with a dictionary.
# Once you've come up with your second solution, compare the two. Is one solution better than the other? Why or why not?

def max_audience_performances(audiences):
    # keep a count and iterate through for the maximum
    maximum = max(audiences)
    count = 0
    for num in audiences:
        if num == maximum:
            count += 1
    return count * maximum

# print(max_audience_performances(audiences1))
# print(max_audience_performances(audiences2))


# Given an array of integers popularity_scores representing the popularity scores of songs in a music festival playlist,
# return the number of popular song pairs.

# A pair (i, j) is called popular if the songs have the same popularity score and i < j.

# Hint: number of pairs = (n x n-1)/2

def num_popular_pairs(popularity_scores):
    # return number of popular songs
    # considered popular if they have the same value and the index of the first one is before the next one
    
    # possibly: nested for loop or frequency map
    
    # we go through and then sum for each score and its frequency using the (n x n-1)/2 
    # add each of these to return
    
    total = 0
    
    freq = Counter(popularity_scores)
    for score in freq:
        total += (freq[score] * (freq[score] - 1))/2
    return int(total)

popularity_scores1 = [1, 2, 3, 1, 1, 3]
popularity_scores2 = [1, 1, 1, 1]
popularity_scores3 = [1, 2, 3]

# print(num_popular_pairs(popularity_scores1))
# print(num_popular_pairs(popularity_scores2))
# print(num_popular_pairs(popularity_scores3)) 
                
# You are given two lists of strings s and t representing the stage arrangements of performers in two different performances at a 
# music festival, such that every performer occurs at most once in s and t, and t is a permutation of s.

# The stage arrangement difference between s and t is defined as the sum of the absolute difference between the index of the 
# occurrence of each performer in s and the index of the occurrence of the same performer in t.

# Return the stage arrangement difference between s and t.

# A permutation is a rearrangement of a sequence. For example, [3, 1, 2] and [2, 1 , 3] are both permutations of the list [1, 2, 3].

def find_stage_arrangement_difference(s, t):
    # we have to find the abs() value of the difference between index of the value in t1 s1
    # we must find the index() of when it occurs in the other function
    differences = 0
    for i in range(len(s)):
        differences += abs(i - t.index(s[i]))
    return differences
    
    """
    :type s: List[str]
    :type t: List[str]
    :rtype: int
    """


s1 = ["Alice", "Bob", "Charlie"]
t1 = ["Bob", "Alice", "Charlie"]
s2 = ["Alice", "Bob", "Charlie", "David", "Eve"]
t2 = ["Eve", "David", "Bob", "Alice", "Charlie"]

# print(find_stage_arrangement_difference(s1, t1))
# print(find_stage_arrangement_difference(s2, t2))

# You're given strings vip_passes representing the types of guests that have VIP passes, and guests representing 
# the guests you have at the music festival. Each character in guests is a type of guest you have. 
# You want to know how many of the guests you have are also VIP pass holders.

# Letters are case sensitive, so "a" is considered a different type of guest from "A".

# Here is the pseudocode for the problem. Implement this in Python and explain your implementation step-by-step.

# 1. Create an empty set called vip_set.
# 2. For each character in vip_passes, add it to vip_set.
# 3. Initialize a counter variable to 0.
# 4. For each character in guests:
#    * If the character is in vip_set, increment the count by 1.
# 5. Return the count.

def num_VIP_guests(vip_passes, guests):
    vip_set = set(vip_passes)
    count = 0
    for char in guests:
        if char is in vip_set:
            count += 1
    return count

vip_passes1 = "aA"
guests1 = "aAAbbbb"

vip_passes2 = "z"
guests2 = "ZZ"

print(num_VIP_guests(vip_passes1, guests1))
print(num_VIP_guests(vip_passes2, guests2))
