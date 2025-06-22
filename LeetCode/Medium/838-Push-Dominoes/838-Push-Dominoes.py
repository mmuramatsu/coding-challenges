class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        last_seen = None
        last_seen_index = 0

        ans = ""

        for i in range(len(dominoes)):
            aux = ""
            if dominoes[i] == "L":
                if last_seen != "R":
                    aux = "L" * (i - last_seen_index + 1 - (1 if last_seen else 0))
                else:
                    space = i - last_seen_index - 1
                    if space % 2 == 0:
                        aux = "R" * ((space // 2)) + "L" * ((space // 2) + 1)
                    else:
                        aux = "R" * ((space // 2)) + "." + "L" * ((space // 2) + 1)

                last_seen = dominoes[i]
                last_seen_index = i
            elif dominoes[i] == "R":
                if last_seen == "R":
                    aux = "R" * (i - last_seen_index + 1 - (1 if last_seen else 0))
                else:
                    aux = "." * (i - last_seen_index - (1 if last_seen else 0)) + "R"

                last_seen = dominoes[i]
                last_seen_index = i

            ans += aux

        if dominoes[-1] == ".":
            if last_seen == "R":
                ans += "R" * (len(dominoes) - last_seen_index - 1)
            elif last_seen == "L":
                ans += "." * (len(dominoes) - last_seen_index - 1)
            else:
                ans = dominoes

        return ans


a = Solution()
print("Input '.....', ans: ", a.pushDominoes("....."))
print("Input '....L', ans: ", a.pushDominoes("....L"))
print("Input '.L..L', ans: ", a.pushDominoes(".L..L"))
print("Input '.L.LL', ans: ", a.pushDominoes(".L.LL"))
print("Input 'R..L', ans: ", a.pushDominoes("R..L"))
print("Input 'R....', ans: ", a.pushDominoes("R...."))
print("Input 'RR.L', ans: ", a.pushDominoes("RR.L"))
print("Input '.L.R...LR..L..', ans: ", a.pushDominoes(".L.R...LR..L.."))
print("Input 'R.R.L', ans: ", a.pushDominoes("R.R.L"))
