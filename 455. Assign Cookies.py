class Solution:
    def findContentChildren(self, g, s):
        # Sort the arrays
        g.sort()
        s.sort()
        
        # Initialize count for tracking assignments of cookies
        count = 0
        # Initialize two pointers i and j to iterate on g and s
        i, j = 0, 0
        
        # Iterate through the arrays
        while i < len(g) and j < len(s):
            # If the size of the cookie is greater than or equal to the child's greed,
            # assign the cookie to the child and move both pointers
            if g[i] <= s[j]:
                count += 1
                i += 1
            # Move the cookie pointer to the next cookie, regardless of assignment
            j += 1
        
        return count
