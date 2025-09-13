# import pandas as pd
class Solution(object):
    def __init__(self, data=None):
        if data:
            self.s1 = data["s1"]
            self.s2 = data["s2"]
            self.baseStr = data["baseStr"]
        else:
            self.s1 = None
            self.s2 = None
            self.baseStr = None

    def smallestEquivalentString(self, s1, s2, baseStr):
        # """
        # :type s1: str
        # :type s2: str
        # :type baseStr: str
        # :rtype: str
        # """
        # Create initial groups
        s1s2groups = []
        for i in range(len(s1)):
            s1s2groups.append(s1[i] + s2[i])
        print("Original groups:", s1s2groups)
        
        # Create a dictionary to track which groups share letters
        shared_letters = {}
        for i, group in enumerate(s1s2groups):
            for letter in group:
                if letter not in shared_letters:
                    shared_letters[letter] = set()
                shared_letters[letter].add(i)
        
        # Find connected groups
        connected_groups = []
        used_indices = set()
        
        for i, group in enumerate(s1s2groups):
            if i in used_indices:
                continue
                
            current_group = set(group)
            to_process = {i}
            
            while to_process:
                idx = to_process.pop()
                if idx in used_indices:
                    continue
                    
                used_indices.add(idx)
                current_group.update(s1s2groups[idx])
                
                # Find all groups that share letters with current group
                for letter in s1s2groups[idx]:
                    for other_idx in shared_letters[letter]:
                        if other_idx not in used_indices:
                            to_process.add(other_idx)
            
            connected_groups.append(current_group)
        
        # Create mapping from each letter to its group's smallest letter
        letter_to_smallest = {}
        for group in connected_groups:
            smallest = min(group)
            for letter in group:
                letter_to_smallest[letter] = smallest
        
        # Create result string
        result = ""
        for char in baseStr:
            if char in letter_to_smallest:
                result += letter_to_smallest[char]
            else:
                result += char
        
        print("\nResult:", result)
        return result

# Test with data object
dataobj = {
    "s1" : "leetcode",
    "s2" : "programs",
    "baseStr" : "sourcecode",
}
sol = Solution(dataobj)
result = sol.smallestEquivalentString(sol.s1, sol.s2, sol.baseStr)

# Test without data object
sol2 = Solution()
result2 = sol2.smallestEquivalentString("leetcode", "programs", "sourcecode")