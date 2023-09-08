class ProcessedImage:

    def __init__(self, matrix, description, is_gray):
        self.matrix = matrix
        self.description = description
        self.isGray = is_gray

    def convert_to_json(self):
        return {
            'matrix': self.matrix.tolist(),
            'description': self.description,
            'isGray': self.isGray
        }
