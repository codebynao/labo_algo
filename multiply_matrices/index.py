import unittest


def multiply(size, matrixA, matrixB):
    matrixC = []
    # As they are square matrices, the size of both matrices is the same, we can use size for every loop instead of len() of matrix/row/column
    # loop through the length of matrixA
    for i in range(size):
        # Add a new row to the result matrix
        matrixC.append([])
        # loop through matrixB rows
        for j in range(size):
            # add the initial value to the result matrix for position [i][j]
            matrixC[i].append(0)
            # loop through matrixB columns
            for k in range(size):
                # increment the result value with the multiplication of matrixA and matrixB values
                matrixC[i][j] += matrixA[i][k] * matrixB[k][j]

    return matrixC


class TestMultiply(unittest.TestCase):
    def test1(self):
        self.assertEqual(multiply(2, [[17, 4], [17, 16]], [[9, 2], [7, 1]]), [[181, 38], [265, 50]])

    def test2(self):
        self.assertEqual(multiply(2, [[7, 18], [2, 9]], [[14, 5], [5, 18]]), [[188, 359], [73, 172]])

    def test3(self):
        self.assertEqual(multiply(3, [[15, 3, 18], [12, 9, 2], [14, 12, 1]], [[5, 10, 15], [15, 18, 4], [2, 6, 11]]), [[156, 312, 435], [199, 294, 238], [252, 362, 269]])


if __name__ == "__main__":
    unittest.main()
