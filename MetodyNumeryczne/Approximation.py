

class Approximation:

    def __init__ (self,polynominalDegree, data):
        self.pd = polynominalDegree
        self.xy = data
        self.s = (self.pd*2 + 1) * [0]
        self.t = (self.pd+1) * [0]
        self.count_st()

    def count_st (self):
        for xy in self.xy:
            for i in range(len(self.s)):
                self.s[i] += xy[0]**i
            for i in range(len(self.t)):
                self.t[i] += xy[1] * xy[0]**i
    
    def get_matrix(self):
        matrix = [[0] * (self.pd+1)] * (self.pd+1)
        matrixDimension = len(matrix)
        for i in range(matrixDimension):
            matrixRow = [0]*(self.pd+1)
            for j in range(matrixDimension):
                matrixRow[j] = self.s[i+j]
            matrix[i]=matrixRow
        return matrix

    def get_t(self):
        return self.t