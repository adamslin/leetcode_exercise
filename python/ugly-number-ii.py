#
# @lc app=leetcode id=264 lang=python3
# @lcpr version=30201
#
# [264] Ugly Number II
#
# https://leetcode.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (49.23%)
# Likes:    6681
# Dislikes: 423
# Total Accepted:    489.8K
# Total Submissions: 994.8K
# Testcase Example:  '10'
#
# An ugly number is a positive integer whose prime factors are limited to 2, 3,
# and 5.
# 
# Given an integer n, return the n^th ugly number.
# 
# 
# Example 1:
# 
# Input: n = 10
# Output: 12
# Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10
# ugly numbers.
# 
# 
# Example 2:
# 
# Input: n = 1
# Output: 1
# Explanation: 1 has no prime factors, therefore all of its prime factors are
# limited to 2, 3, and 5.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 1690
# 
# 
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# 10\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

