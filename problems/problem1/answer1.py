class Solution(object):
    def reverse(self, x):
        int xr = x
        for i in x:
            xr = i + xr
        return xr
