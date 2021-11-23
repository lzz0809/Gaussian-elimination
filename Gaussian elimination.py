import numpy as np

def solve(A, B):
    #matrix A has m rows and n columns
    m = A.shape[0]
    n = A.shape[1]
    #to horizontally stack A and B
    C = np.hstack((A, B))
    
    row = 0
    col = 0
    while row < m and col < n:
        #to make sure C[row, col] is the largest along the col column.
        max_row = row
        max_element = abs(C[row][col])
        for j in range(row+1, m):
            if(abs(C[j][col]) > max_element):
                max_element = abs(C[j][col])
                max_row = j
        if max_row != row:
            C[[row,max_row],:] = C[[max_row, row],:]

        #if all elements in col column equal zero, then skip this col.
        if C[row][col] == 0:
            col += 1
            continue
        
        #Gaussian elimination
        for j in range(row+1, m):
            ratio = C[j][col] / C[row][col]
            C[j] -= C[row] * ratio

        col += 1
        row += 1
        #print(C)
        #print('-'*30)

    #no solution
    for i in range(row, m):
        if C[i][col] != 0:
            return -1

    #infinite solutions, return the number of free variables
    if row <  n:
        return n - row

    #one solution, calculate and return it
    res = np.zeros(n)
    for i in range(n-1, -1, -1):
        temp = C[i][-1]
        for j in range(n-1, i, -1):
            temp -= res[j] * C[i][j]
        res[i] = temp / C[i][i]
    return res


if __name__ == '__main__':
    #test the case of one solution
    '''
    A = np.array([[2., 23., 5., 1.], [2., 5., 9., 12.], [4., 2., 34., 2.], [1., 5., 3., 61.]])
    B = np.array([[59.], [-16.], [126.], [-284.]])
    '''
    '''
    #test the case of infinite solutions
    A = np.array([[1., 1.]])
    B = np.array([[3.]])
    '''
    #test the case of no solution
    A = np.array([[1., 1.], [3., -1.], [1., 1.]])
    B = np.array([[3.], [1.], [5.]])

    print('A and B are: ')
    print(A)
    print(B)
    res = solve(A, B)
    if isinstance(res, int):
        if res == -1:
            print('No solution.')
        else:
            print('Infinite solutions! There are %d free variables.' %res)
    else:
        print('One solution:')
        print(res)
