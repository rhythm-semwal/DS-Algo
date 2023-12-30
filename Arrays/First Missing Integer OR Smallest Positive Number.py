class Solution1:
    def firstMissingPositive(self, nums) -> int:
        """
        Step 1 -> The main idea behind it is that the minimum number to be found will always be in the range [1....n]
        where 'n' is the length of list.
        So keep numbers in this range and mark others(here we are marking them with (n+1) value) in the list provided.
	    """

        n = len(nums)
        for i in range(n):
            if nums[i] < 1 or nums[i] > n:
                nums[i] = n + 1

        '''Step 2 -> Ignoring the values greater than 'n', mark the indexes of the numbers in the range [1...n]
					 so as to ensure that this values are present. To mark the indexes, 
					 I am negating the value present at that index.'''

        for i in range(n):
            val = abs(nums[i])
            if val > n:
                continue
            val -= 1  # since the list is zero indexed,so every value will be at position val - 1

            if nums[val] > 0:
                # For similar numbers, it will keep on fluctuating between negative and positive
                # which is not our motive here.

                nums[val] = -1 * nums[val]

        '''Step 3 -> Return the first occurence of the non-negative numbers from the list'''

        for i in range(n):
            if nums[i] >= 0:
                return (i + 1)  # bcoz list is zero indexed

        '''Step 4 -> We will encounter this if no positives were found. This means that all the 
			         numbers are in the range [1....n]. So the missing positive number will be n+1'''

        return (n + 1)


class Solution2:
    """
    @param A: An array of integers
    @return: An integer
    """

    def firstMissingPositive(self, A):
        # write your code here
        n = len(A)

        i = 0

        while i < n:
            while 0 < A[i] <= n and A[A[i] - 1] != A[i]:
                temp = A[A[i] - 1]
                A[A[i] - 1] = A[i]
                A[i] = temp

            i += 1

        for index, value in enumerate(A):
            if index + 1 != value:
                return index + 1

        return n + 1


# approach 1

def firstMissingPositive(A):
    contains_one = False
    n = len(A)
    for i in range(n):
        if A[i] == 1:
            contains_one = True

        elif A[i] <= 0 or A[i] > n:
            A[i] = 1

    if not contains_one:
        return 1

    i = 0
    while i < n:
        if A[i] != A[A[i] - 1]:
            temp = A[A[i] - 1]
            A[A[i] - 1] = A[i]
            A[i] = temp
        else:
            i += 1

    for i in range(n):
        if A[i] != i + 1:
            return i + 1

    return n + 1


if __name__ == "__main__":
    # arr = [1,2,3,4,-10]
    arr = [1, 2, 4, 3]
    # arr = [0, 2, 1]
    # arr = [3, 4, -1, 1]
    # arr = [2, 3, 1, 6]
    arr = [-163, -20]
    # arr = [ 699, 2, 690, 936, 319, 784, 562, 35, 151, 698, 126, 730, 587, 157, 201, 761, 956, 359, 198, 986, 915, 7, 703, 324, 814, 382, 294, 204, 120, 731, 615, 330, 486, 52, 223, 376, 649, 458, 564, 971, 72, 605, 177, 20, 461, 790, 872, 363, 916, 435, 991, 184, 410, 320, 16, 480, 768, 801, 117, 338, 650, 786, 17, 369, 979, 304, 445, 688, 862, 229, 311, 351, 985, 697, 135, 299, 310, 3, 643, 221, 831, 196, 887, 679, 484, 209, 824, 292, 588, 721, 140, 675, 827, 913, 271, 170, 812, 552, 334, 860, 981, 550, 308, 584, 442, 328, 251, 456, 976, 31, 507, 954, 982, 742, 45, 727, 794, 309, 527, 623, 56, 843, 436, 681, 143, 130, 689, 870, 362, 580, 560, 474, 385, 525, 881, 51, 890, 917, 820, 826, 139, 443, 978, 144, 512, 205, 682, 188, 344, 429, 497, 181, 749, 864, 664, 145, 621, 629, 886, 572, 89, 725, 945, 29, 553, 977, 783, 590, 236, 728, 125, 90, 492, 261, 543, 259, 662, 622, 285, 392, 561, 670, 200, 504, 246, 513, 910, 583, 460, 179, 207, 709, 127, 926, 816, 426, 520, 174, 464, 883, 780, 5, 268, 606, 1, 109, 704, 391, 661, 924, 516, 241, 477, 952, 405, 522, 247, 335, 356, 839, 423, 779, 4, 43, 720, 238, 965, 951, 914, 10, 496, 775, 651, 788, 373, 491, 746, 799, 518, 93, 86, 774, 652, 955, 494, 252, 781, 946, 412, 202, 741, 719, 612, 673, 896, 1000, 289, 554, 69, 424, 980, 506, 593, 889, 25, 959, 28, 736, 8, 969, 865, 657, 567, 434, 9, 167, 357, 929, 645, 250, 565, 94, 928, 473, 509, 823, 313, 762, -1, 208, 903, 922, 655, 948, 326, 485, 150, 73, 505, 225, 122, 129, 648, 838, 811, 972, 735, 78, 428, 740, 782, 632, 316, 440, 737, 297, 873, 281, 479, 654, 0, 633, 212, 152, 154, 470, 866, 79, 722, 958, 732, 900, 832, 278, 58, 842, 745, 540, 169, 347, 592, 438, 882, 462, 53, 34, 519, 489, 85, 757, 919, 701, 15, 211, 667, 637, 74, 573, 240, 559, -2, 472, 203, 112, 162, 776, -4, 155, 837, 99, 98, 64, 101, 983, 366, 853, 970, 482, 40, 921, 374, 758, 413, 339, 705, 771, 360, 734, 282, 219, 766, 535, 133, 532, 254 ]
    # print(firstMissingPositive(arr))
    print(Solution().firstMissingPositive(arr))
