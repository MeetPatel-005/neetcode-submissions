class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for x in operations:
            if x.isdigit() or x[1:].isdigit():
                record.append(int(x))
            elif x == '+':
                record.append(record[-1]+record[-2])
            elif x == 'C':
                record.pop()
            else:
                record.append(2*record[-1])
            print(record)
        return sum(record)