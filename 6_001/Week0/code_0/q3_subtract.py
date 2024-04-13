def subtract_lists(nums1, nums2):
    """
    Given lists of numbers nums1 and nums2, return a new list where each position is
    the difference between that position in nums1 and in nums2.
    """
    output = []
    for i in range(len(nums1)):
        output.append(nums1[i] - nums2[i])
    return output

def test_subtract_lists():
    assert subtract_lists([1, 2], [3, 5]) == [-2, -3]
    assert subtract_lists([325, 64, 66], [1, 2, 3]) == [324, 62, 63]
