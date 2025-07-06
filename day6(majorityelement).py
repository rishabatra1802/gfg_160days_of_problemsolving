day6.py
class Solution:
    def findMajority(self, arr):
        n = len(arr)
        
        # Step 1: Initialize two potential candidates and their counts
        candidate1 = candidate2 = None
        count1 = count2 = 0

        # Step 2: First pass to find potential candidates
        for num in arr:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        # Step 3: Second pass to verify actual counts
        count1 = count2 = 0
        for num in arr:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1

        # Step 4: Prepare the result
        result = []
        if count1 > n // 3:
            result.append(candidate1)
        if count2 > n // 3:
            result.append(candidate2)

        return sorted(result)  # Return in increasing order
