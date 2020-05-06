class Solution:
    def openLock(self, deadends, target):
        visited = {}
        root = '0000'
        current = [root]
        step = 0
        while current !=[]:
            next = []
            for val in current:
                if val in deadends:
                    print(val)
                    continue
                elif val == target:
                    return step
                else:
                    for i in range(4):
                        change = self.up(val, i)
                        if change not in visited:
                            visited[change] = 1
                            next.append(change)
                        change = self.down(val, i)
                        if change not in visited:
                            visited[change] = 1
                            next.append(change)
            step += 1
            current = next
        return -1

    def up(self, s, i):
        if s[i] == '9':
            l = list(map(int, s))
            l[i] = 0
            return ''.join(map(str, l))
        else:
            l = list(map(int, s))
            l[i] = int(s[i]) + 1
            return ''.join(map(str, l))

    def down(self, s, i):
        if s[i] == '0':
            l = list(map(int, s))
            l[i] = 9
            return ''.join(map(str, l))
        else:
            l = list(map(int, s))
            l[i] = int(s[i]) - 1
            return ''.join(map(str, l))



if __name__ == "__main__":
    a = Solution()
    b = '1293'
    deadends = ["0201","0101","0102","1212","2002"]
    deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
    target = "0202"
    target = "8888"
    print(a.up(b,1)) 
    print(a.openLock(deadends, target))   