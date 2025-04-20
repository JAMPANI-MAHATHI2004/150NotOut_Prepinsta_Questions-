##---Program for checking if two strings are Anagram of each other – Is Anagram?
##---Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
"""An anagram is a word or phrase that can be rearranged to form another word or phrase by using 
all the original letters exactly once. For example, “listen” and “silent” are 
anagrams because they have the same letters, even though they are arranged differently."""
"""
#Example 1
Input: s = "racecar", t = "carrace"
Output: true
#Example 2
Input: s = "jar", t = "jam"
Output: false
Note - s and t consist of lowercase English letters.
"""

# Method 1: Sorting 
def Anagram(s,t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)
s = input("S: ")
t = input("T: ")
print(Anagram(s,t))

#Method 2: Hash Table
def anagram(s,t):
    if len(s) != len(t):
        return False
    
    scount = {}
    tcount = {}

    for c in s:
        if c in scount:
            scount[c] += 1
        scount[c] = 1
    for c in t:
        if c in tcount:
            tcount[c] += 1
        tcount[c] = 1
    
    return scount == tcount

s = input("S: ")
t = input("T: ")
print(anagram(s,t))