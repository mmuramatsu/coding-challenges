class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        n = len(players)
        m = len(trainers)
        players.sort()
        trainers.sort()

        j = 0
        count = 0

        for i in range(n):
            while j < m and players[i] > trainers[j]:
                j += 1

            if j < m:
                count += 1
                j += 1
            else:
                break

        return count


a = Solution()
print(a.matchPlayersAndTrainers(players=[4, 7, 9], trainers=[8, 2, 5, 8]))
print(a.matchPlayersAndTrainers(players=[1, 1, 1], trainers=[10]))
