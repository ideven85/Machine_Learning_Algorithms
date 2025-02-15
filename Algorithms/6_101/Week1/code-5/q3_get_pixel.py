"""
Question 3: Given the implementation of get_pixel below, write a few bullet 
points answering the following questions: What does the code do well? How 
easy is it to understand what the code is doing? How would you refactor the 
code to reduce repetition or make it simpler?
"""


def get_pixel(image, row, col, boundary_behavior):
    if boundary_behavior == "zero":
        if row < 0 and col < 0:
            return 0
        elif row < 0 and col <= image["width"] - 1:
            return 0
        elif row < 0 and col > image["width"] - 1:
            return 0
        elif row <= image["height"] - 1 and col < 0:
            return 0
        elif row <= image["height"] - 1 and col <= image["width"] - 1:
            return image["pixels"][row * image["width"] + col]
        elif row <= image["height"] - 1 and col > image["width"] - 1:
            return 0
        elif row > image["height"] - 1 and col < 0:
            return 0
        elif row > image["height"] - 1 and col <= image["width"] - 1:
            return 0
        elif row > image["height"] - 1 and col > image["width"] - 1:
            return 0
    elif boundary_behavior == "extend":
        if row < 0 and col < 0:
            return image["pixels"][0 * image["width"] + 0]
        elif row < 0 and col <= image["width"] - 1:
            return image["pixels"][0 * image["width"] + col]
        elif row < 0 and col > image["width"] - 1:
            return image["pixels"][0 * image["width"] + (image["width"] - 1)]
        elif row <= image["height"] - 1 and col < 0:
            return image["pixels"][row * image["width"] + 0]
        elif row <= image["height"] - 1 and col <= image["width"] - 1:
            return image["pixels"][row * image["width"] + col]
        elif row <= image["height"] - 1 and col > image["width"] - 1:
            return image["pixels"][row * image["width"] + (image["width"] - 1)]
        elif row > image["height"] - 1 and col < 0:
            return image["pixels"][(image["height"] - 1) * image["width"] + 0]
        elif row > image["height"] - 1 and col <= image["width"] - 1:
            return image["pixels"][(image["height"] - 1) * image["width"] + col]
        elif row > image["height"] - 1 and col > image["width"] - 1:
            return image["pixels"][
                (image["height"] - 1) * image["width"] + (image["width"] - 1)
            ]
    elif boundary_behavior == "wrap":
        while row < 0:
            row += image["height"]
        while row > 0:
            row -= image["height"]
        while col < 0:
            col += image["width"]
        while col > 0:
            col -= image["width"]
        return image["pixels"][row * image["width"] + col]
