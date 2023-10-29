class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def feasibility(self, A, cows, distance):
        count = 1
        curr = 0
        for i in range(1, len(A)):
            if A[i] - A[curr] >= distance:
                count += 1
                curr = i
                if count >= cows:
                    return True
        return False

    def solve(self, A, B):
        A.sort()
        if len(A) == 2:
            return A[-1] - A[0]
        low, high = 1, A[-1] - A[0]
        ans = 1
        while low <= high:
            mid = (low + high) // 2
            result = self.feasibility(A, B, mid)
            if result:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    B = 3
    # A = [1, 2]
    # B = 2
    # A= [9380, 9909, 7518, 1909, 8619, 9215, 3314, 5035, 7356, 2568, 9255, 3340, 752, 8247, 2313, 8463, 9062, 6035, 5220,
    #     6702, 2682, 586, 2390, 1488, 4096, 8154, 9243, 3026, 4223, 6589, 3417, 541, 7147, 7164, 2959, 7672, 6358, 776,
    #     959, 6908, 7757, 409, 8286, 4731, 9457, 6325, 6107, 5103, 6139, 408, 7678, 5308, 6158, 1328, 4530, 4807, 2903,
    #     2717, 5647, 4695, 8025, 2480, 9454, 2671, 3039, 2478, 7522, 5989, 7571, 4357, 5811, 2757, 7013, 9095, 3908, 191,
    #     9760, 4945, 5278, 6924, 4317, 911, 1856, 5325, 9577, 594, 4423, 8941, 7342, 4353, 6183, 9610, 4781, 6057, 700,
    #     8608, 5911, 4403, 6940, 6235, 5437, 7769, 3518, 4690, 5324, 5857, 1505, 9767, 4315, 1045, 89, 7938, 3281, 7248,
    #     2265, 6738, 4788, 4354, 8322, 7996, 3514, 1881, 3375, 5441, 5300, 6323, 1436, 474, 6496, 2866, 2565, 2484, 2019,
    #     3657, 1582, 2994, 68, 1575, 6473, 6137, 3785, 622, 2136, 1469, 5350, 1444, 479, 9003, 5933, 3261, 940, 434,
    #     5761, 1521, 6528, 5074, 2114, 3999, 9189, 3698, 9535, 6678, 4889, 8681, 5704, 4823, 3203, 4115, 8547, 3905,
    #     8369, 5404, 4901, 9672, 8808, 3761, 8838, 6604, 9914, 7466, 8123, 9221, 544, 8306, 655, 1275, 7118, 8653, 8792,
    #     3721, 449, 1865, 8388, 3547, 9571, 6300, 1126, 2048, 3610, 1134, 3229, 2916, 7564, 388, 1018, 7640, 250, 78,
    #     3933, 8164, 3100, 2275, 8623, 4469, 6541, 8968, 3499, 7814, 6696, 8119, 1739, 8733, 8886, 4068, 2160, 2584,
    #     5958, 4518, 1602, 4413, 8906, 6748, 9499, 9226, 4395, 6415, 5172, 3370, 8833, 3309, 1059, 7662, 1462, 9800, 535,
    #     3137, 9559, 9323, 7316, 5858, 7294, 4255, 4510, 8088, 6056, 4768, 5316, 9318, 8117, 2874, 4064, 2121, 7398,
    #     8744, 5891, 4633, 807, 9606, 5636, 3548, 1104, 5071, 1751, 8993, 7589, 6543, 8979, 5331, 4046, 2542, 4343, 68,
    #     4316]
    # B= 252
    print(Solution().solve(A, B))

