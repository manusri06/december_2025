class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for i in range(len(tokens)):
            if tokens[i] not in "+-*/":
                st.append(int(tokens[i]))
            else:
                s = st.pop()
                f = st.pop()
                if tokens[i] == "+":
                    st.append(f+s)
                elif tokens[i] == "-":
                    st.append(f-s)
                elif tokens[i] == "*":
                    st.append(f*s)
                else:
                    st.append(int(f/s))
        return st[-1]