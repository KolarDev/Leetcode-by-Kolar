class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        # Edge case: If there is only 1 row, no zigzag happens
        if numRows == 1 or numRows >= len(s):
            return s

        # Create a list of strings, one for each row
        rows = [""] * numRows
        curr_row = 0
        step = 1  # 1 means moving down, -1 means moving up

        for char in s:
            rows[curr_row] += char
            
            # If we hit the top row, we must go down
            if curr_row == 0:
                step = 1
            # If we hit the bottom row, we must go up
            elif curr_row == numRows - 1:
                step = -1
                
            curr_row += step

        # Join all rows together to get the final result
        return "".join(rows)

            