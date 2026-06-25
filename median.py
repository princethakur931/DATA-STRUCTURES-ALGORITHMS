# merge the array and find the median of that array 


import numpy as np

nums1 = [1,3]
nums2 = [2]

nums1[:] = nums1 + nums2
np.array(nums1)
print(np.median(nums1))