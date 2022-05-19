#Given a m x n matrix grid which is sorted in non-increasing 
#order both row-wise and column-wise, return the number of negative numbers in grid.


#Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
#Output: 8
#Explanation: There are 8 negatives number in the matrix.


class Solution(object):
    def countNegatives(self, grid):
        negcounter = 0              #counter to count negative number
        for i in grid:              #outer loop to iterate over the list of the array
            for j in i:             #inner loop to iterate over each array
                if j < 0:
                    negcounter +=1
        return negcounter

