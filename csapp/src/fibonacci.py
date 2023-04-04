# print("Full Pyramid Pattern of Stars (*), : ")
# abc = 20
# for i in range(abc):
#        # print(-i)
#        for s in range(-abc+1, -i):
#               print("-", end="")
#        print("* "*i, end = "" )
#        print()       


class Solution:
    def rotate(self, matrix) -> None:
       """
        Do not return anything, modify matrix in-place instead.
       """
       # return_list = []
       # for i in range(len(matrix)):
       #        test_list = []
       #        for j in matrix[::-1]:
       #               test_list.append(j[i])
       #        return_list.append(test_list)
       
       # return return_list
#        matrix1 = matrix.copy()
#        for i in range(len(matrix1)):
#               test_list = []
#               for j in matrix1[::-1]:
#                      test_list.append(j[i])
#               matrix[i] = test_list
#        return matrix



# a =  Solution()
# # matrix = [[1,2,3],[4,5,6],[7,8,9]]
# matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# print(a.rotate(matrix))



class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        _sum = 0 
        _count = 0
        end_neg = False
        sor_neg = False
        if divisor < 0 or dividend:
              neg = True
              divisor = abs(divisor)
        for i in range(0, dividend, divisor):
            if _sum <= dividend and _sum+divisor<=dividend :
                _sum = _sum+divisor
                _count += 1
        if neg:
              return int("-"+str(_count))
        return _count


a= Solution()
print(a.divide(-1,1))
