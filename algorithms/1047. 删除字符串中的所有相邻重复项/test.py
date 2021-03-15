class Solution:
    def removeDuplicates(self, S: str) -> str:
        st = ['']
        for x in S:
            if x == st[-1]:
                st.pop()
            else:
                st.append(x)
        return ''.join(st)

object = Solution()
result = object.removeDuplicates('abbacd')
print(result)
