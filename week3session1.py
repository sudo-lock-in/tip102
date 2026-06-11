# A post is considered valid if:

#     Every opening tag has a corresponding closing tag of the same type.
#     Tags are closed in the correct order.


def is_valid_post_format(posts):
        stack = []
        for c in posts:
            if (c == '(' or c == '{' or c == '['):
                stack.append(c)

            elif (c == ')'): 
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False

            elif (c == ']'): 
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            
            elif (c == '}'): 
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False

        return len(stack) == 0

# print(is_valid_post_format("()"))
# print(is_valid_post_format("()[]{}")) 
# print(is_valid_post_format("(]"))


# On your platform, comments on posts are displayed in the order they are received.
#  However, for a special feature, you need to reverse the order of comments before displaying them.
#  Given a queue of comments represented as a list of strings, reverse the order using a stack.

def reverse_comments_queue(comments):
   # we want to start with an empty stack 
   # append each thing in order 
   # pop everything back onto the list
    stack = []
    for comment in comments:
        stack.append(comment)
    reverseCommments = []
    while stack:
        reverseCommments.append(stack.pop())
    return reverseCommments

# print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

# print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))


# As part of a new feature on your social media platform, you want to highlight post titles that are symmetrical, 
# meaning they read the same forwards and backwards when ignoring spaces, punctuation, and case. 
# Given a post title as a string, use a new algorithmic technique the two-pointer method to determine if the title is
#  symmetrical.

def is_symmetrical_title(title):
    # use two pointer to see if two ends are the same
    # 1st pointer starts at beginning and 2nd pointer at the end
    # ignore spaces, punctuation, and case
    # run lower on each character to save time complexity
    # we cna use is .alpha()
    l, r = 0, len(title) - 1
    while l < r:
        if not title[l].isalpha():
            l += 1
        if not title[r].isalpha():
            r -= 1
        if title[l].lower() != title[r].lower():
            return False
        l, r = l + 1, r -1
    return True


# print(is_symmetrical_title("A Santa at NASA"))
# print(is_symmetrical_title("Social Media")) 
    


# def engagement_boost(engagements):
#     squared_engagements = []
    
#     for i in range(len(engagements)):
#         squared_engagement = engagements[i] * engagements[i] # we are multiplying it by itself / squaring it
#         squared_engagements.append((squared_engagement, i))  #adding both the index and the squared result to the array
    
#     squared_engagements.sort(reverse=True) # reversing the order of the array
    
#     result = [0] * len(engagements) # creating a new array with spaces for every engagement
#     position = len(engagements) - 1 # a pointer starting at the end
    
#     for square, original_index in squared_engagements:
#         result[position] = square 
#         position -= 1 # bringing the position back
    
#     return result


# You track your daily engagement rates as a list of integers, sorted in non-decreasing order.
#  To analyze the impact of certain strategies, you decide to square each engagement rate and then sort the results 
# in non-decreasing order.

# Given an integer array engagements sorted in non-decreasing order, 
# return an array of the squares of each number sorted in non-decreasing order.

def engagement_boost(engagements):
   # the greatest value is either the leftmost or rightmost
   # we would append to a new list and put the largest value at the end
   # continue on looking for which value is larger on the left or the right
   # move the pointer based on which one is greater 
    for i  in range(len(engagements)):
       engagements[i] = engagements[i] * engagements[i]
    result = [0] * len(engagements)
    l, r = 0, len(engagements) - 1

    posiiton = len(engagements) - 1
    while l < r:
        if engagements[l] < engagements[r]:
            result[posiiton] = engagements[r]
            r -= 1 
        else:
            result[posiiton] = engagements[l]
            l += 1  
        # l, r = l + 1, r -1
        posiiton -= 1 
    return result

# print(engagement_boost([-4, -1, 0, 3, 10]))
# print(engagement_boost([-7, -3, 2, 3, 11]))


# You want to make sure your posts are clean and professional. Given a string post of lowercase and uppercase
#  English letters, you want to remove any pairs of adjacent characters where one is the lowercase version 
# of a letter and the other is the uppercase version of the same letter. Keep removing such pairs until the post is clean.

# A clean post does not have two adjacent characters post[i] and post[i + 1] where:
#     post[i] is a lowercase letter and post[i + 1] is the same letter in uppercase or vice-versa.

# Return the clean post.

# Note that an empty string is also considered clean.

def clean_post(post):
  # same logic as paranthesis problem w/ stack
    stack = []
    for char in post:
        if char.isupper():
            if stack and stack[-1] == char.lower():
                stack.pop()
            else:
                stack.append(char)
        elif char.islower():
            if stack and stack[-1] == char.upper():
                stack.pop()
            else:
                stack.append(char)
    return ''.join(stack)

# print(clean_post("poOost")) 
# print(clean_post("abBAcC")) 
# print(clean_post("s")) 

from collections import deque

# You want to add a creative twist to your posts by reversing the order of characters in each word within your 
# post while still preserving whitespace and the initial word order. 
# Given a string post, use a queue to reverse the order of characters in each word within the sentence.
def edit_post(post):
    new_post = ""
    arr = post.split()
    queue = deque()
    for word in arr:
        for char in word:
                queue.append(char)
        queue.append(" ")
        while queue:
            new_post += queue.pop()
        queue.clear()
    return new_post
  
# print(edit_post("Boost your engagement with these tips")) 
# print(edit_post("Check out my latest vlog")) 


# You often draft your posts and edit them before publishing. 
# Given two draft strings draft1 and draft2, return true if they are equal when both are typed into empty text editors. 
# '#' means a backspace character.

# Note that after backspacing an empty text, the text will remain empty.

def post_compare(draft1, draft2):
    stack = []
    stack2 = []
    for char in draft1:
        if char == "#":
            if stack:
                stack.pop()
        else:
            stack.append(char)
    for char in draft2:
        if char == "#":
            if stack2:
                stack2.pop()
        else:
            stack2.append(char)
    return stack == stack2

# print(post_compare("ab#c", "ad#c"))
# print(post_compare("ab##", "c#d#")) 
# print(post_compare("a#c", "b")) 