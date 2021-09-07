import unittest
from src.algorithms.bfs import *

class TestUM(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def assertEqualMatrices(self, matrix1, matrix2):
        self.assertTrue((matrix1 == matrix2).min())

    def testBFS(self):
        size = 7
        graph = Matrix.from_lists([3, 1, 0, 4, 4, 4, 5, 5, 5],
                                  [1, 4, 3, 3, 2, 6, 2, 0, 6],
                                  [1, 6, 2, 9, 7, 4, 3, 5, 8], size, size)
        vertices = [0, 1, 2, 3, 4, 5, 6]

        start_vertex = 0
        expected_1v = Matrix.sparse(UINT8, 1, size)
        expected_1v[0, 0:4] = start_vertex
        expected_1v[0, 6] = start_vertex
        print(bfs(graph, [start_vertex]))
        self.assertEqualMatrices(expected_1v, bfs(graph, [start_vertex]))

        expected_allV = Matrix.sparse(UINT8, size, size)
        expected_allV[0, 1:4] = 0
        expected_allV[0, 6] = 0
        expected_allV[1, 1:4] = 1
        expected_allV[1, 6] = 1
        expected_allV[3, 1:4] = 3
        expected_allV[3, 6] = 3
        expected_allV[4, 1:4] = 4
        expected_allV[4, 6] = 4
        expected_allV[5, :] = 5
        expected_allV[0, 0] = 0
        expected_allV[2, 2] = 2
        expected_allV[6, 6] = 6
        # Expected result:
        #  0 0 0 0 0   0
        #    1 1 1 1   1
        #      2
        #    3 3 3 3   3
        #    4 4 4 4   4
        #  5 5 5 5 5 5 5
        #              6
        print(bfs(graph, vertices))
        self.assertEqualMatrices(expected_allV, bfs(graph, vertices))

    def testException(self):
        size = 2
        self.assertRaises(IndexError, bfs, Matrix.sparse(INT8, size, size), [i for i in range(size + 1)])

if __name__ == '__main__':
    unittest.main()
