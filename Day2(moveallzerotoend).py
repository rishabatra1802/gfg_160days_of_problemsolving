class Solution:
    def pushZerosToEnd(self, arr):
        # idx will track the position where the next non-zero element should go
        idx = 0

        # Loop through the entire array
        for i in range(len(arr)):
            # If current element is not zero
            if arr[i] != 0:
                # Swap current element with the element at idx
                arr[i], arr[idx] = arr[idx], arr[i]
                # Move idx to next position
                idx += 1

        # Finally return the modified array (optional in some platforms)
        return arr
