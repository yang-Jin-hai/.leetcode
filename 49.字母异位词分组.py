#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
        groups = defaultdict(list)
        for str in strs:
            wordHash = 1
            for c in str:
                wordHash *= hash[ord(c)-ord('a')]
            groups[wordHash].append(str)
        return list(groups.values())
        # hashtab = defaultdict(list)
        # for str in strs:
        #     hashtab[tuple(sorted(str))].append(str)
        # return list(hashtab.values())
        # hashtab = defaultdict(list)
        # for str in strs:
        #     hashtab[''.join(sorted(str))].append(str)
        # return [value for value in  hashtab.values()]
# @lc code=end

