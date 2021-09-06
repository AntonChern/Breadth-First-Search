
from pygraphblas import *

def bfs(matrix, start_vertices):
    """Gets a matrix and a list of starting vertices.
    Returns a matrix in which the columns are the vertices,
    and the rows show where the vertices are reachable from"""

    num_starts = len(start_vertices)
    if num_starts > matrix.nrows or max(start_vertices) > num_starts or min(start_vertices) < 0:
        raise IndexError()

    # matrix in which each row is responsible for its start vertex
    result = Matrix.sparse(UINT8, num_starts, matrix.nrows)

    # matrix in which each row is responsible for keeping track of known nodes of the current start vertex
    mask = Matrix.sparse(BOOL, num_starts, matrix.nrows)
    for i in range(num_starts):
        mask[i, start_vertices[i]] = True

    for i in range(matrix.nrows):
        for j in range(num_starts):
            result.assign_scalar(start_vertices[j] + 1, row_slice=j, mask=mask)
        result.mxm(matrix, mask=result, out=mask, desc=descriptor.RC)
        if not mask.reduce_bool():
            break
    return result - 1
