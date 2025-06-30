class Solution:
    def reverseArray(self, arr):
        # Get the number of elements in the array
        n = len(arr)
        
        # Create a temporary array of the same size
        temp = [0] * n
        
        # Copy elements from original array to temp in reverse order
        for i in range(n):
            temp[i] = arr[n - i - 1]
        
        # Copy reversed elements back into the original array
        for i in range(n):
            arr[i] = temp[i]

# Main block to run the function
if __name__ == "__main__":
    # Original array
    arr = [1, 9, 8, 2, 5, 6]
    
    # Create object of the class
    sol = Solution()
    
    # Call the function to reverse the array
    sol.reverseArray(arr)
    
    # Print the reversed array
    print(arr)
