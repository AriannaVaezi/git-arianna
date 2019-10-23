class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = ''
        for digit in str(x):
            y = digit + y
        return (int(y))