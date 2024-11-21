class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        toBan = 0

        while len(senate) > abs(toBan):

            if toBan < 0 and senate[0] == 'R':
                senate.pop(0)
                toBan += 1
            
            elif toBan > 0 and senate[0] == 'D':
                senate.pop(0)
                toBan -= 1

            else:
                toBan += 1 if senate[0] == 'R' else -1
                senate.append(senate.pop(0))

        return 'Radiant' if toBan > 0 else 'Dire'