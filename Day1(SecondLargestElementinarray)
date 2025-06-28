class Solution:
    def getSecondLargest(self, arr):
        # Start by assuming the largest and second largest values are very, very small.
        # We'll update them as we look at each number in the array.
        first = second = float('-inf')

        # Go through every number in the array one by one
        for num in arr:
            # If this number is bigger than the current largest
            if num > first:
                # The old largest now becomes the second largest
                second = first
                # And this number becomes the new largest
                first = num
            # If this number is smaller than the largest,
            # but still bigger than the current second largest
            elif num > second and num != first:
                # Update the second largest
                second = num

        # After checking all numbers, if we never found a second largest (it's still -inf),
        # then return -1 to show it doesn't exist
        return second if second != float('-inf') else -1
