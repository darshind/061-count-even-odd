def solution(list_of_nums):
            c1 = 0
            c2 = 0
            c = dict()
            for i in list_of_nums:
                if i % 2 == 0:
                    c1+=1
                    c['EVEN'] = c1

                else:
                    c2+=1
                    c['ODD'] = c2
            return c
print solution([1, 2, 3, 5, 8, 9])
