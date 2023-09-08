def normalization(matrix):
    return (matrix - matrix.min()) / (matrix.max() - matrix.min())
