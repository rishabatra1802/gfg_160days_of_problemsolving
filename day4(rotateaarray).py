#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        #Your code here
        n=len(arr)
        temp=arr[:d]
        for i in range (n-d):
            arr[i]=arr[i+d]
        for i in range(d):
            arr[n-d+i]=temp[i]
            
if __name__ =="__main__":
    arr=[1,2,3,4,5,6,7,8,25,98]
    d=2
    sol=Solution()
    sol.rotateArr(arr,d)
   
