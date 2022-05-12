class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if s=='': 
            return 0
        else:
            max_len = 1
            for i in range(0, len(s)):
                for j in range (i+1, len(s)):
                    if s[j] in s[i:j]:
                        temp_len = j-i
                        if temp_len>max_len:
                            max_len = temp_len
                        break
                    else:
                        temp_len = j -i + 1
                        if temp_len>max_len:
                            max_len = temp_len
            return max_len
        """
        :type s: str
        :rtype: int
        """
        