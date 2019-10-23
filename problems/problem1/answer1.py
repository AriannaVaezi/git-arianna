class Solution(object):
    def reverse(self, x):
<<<<<<< HEAD
        int xr = x
        for i in x:
            xr = i + xr
        return xr
=======
        """
        :type x: int
        :rtype: int
        """
        y = ''
        for digit in str(x):
            y = digit + y
        return (int(y))
>>>>>>> 4213d27761807b61dc857e6c89fcf89cddf85c0c
