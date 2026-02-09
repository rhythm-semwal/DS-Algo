class Solution1:
    # TC = O(N* K log K)
    def groupAnagrams(self, strs):
        hash_map = dict()
        for str in strs:
            new_str = list(str)
            new_str.sort()
            key = "".join(new_str)
            if key not in hash_map:
                hash_map[key] = [str]
            else:
                hash_map[key].append(str)

        result = []
        for key, value in hash_map.items():
            result.append(value)
        return result

strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs))


class Solution2:
    # TC = O(N . K)
    # SC = O(N · K)
    # Anagrams have the same character counts
	# Since strings are lowercase English letters (a–z), we can represent each word using a 26-length frequency tuple
	# Tuples are hashable → can be dictionary keys
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_word_dict = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for each in word:
                count[ord(each) - ord('a')] += 1

            sorted_word_dict[tuple(count)].append(word)

        print(sorted_word_dict)
        return list(sorted_word_dict.values())
