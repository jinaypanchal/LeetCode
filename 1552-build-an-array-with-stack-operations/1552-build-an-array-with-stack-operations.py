class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = ""
        st = []
        i = 1
        j = 0
        while i <= n and j < len(target):
            if i == target[j]:
                st.append("Push")
                j+=1

            else:
                st.append("Push")
                st.append("Pop")
            
            i+=1
            # j+=1
        
        return st




            
            

        