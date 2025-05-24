"""
Question 2:
What are the pros and cons of each kernel representation below?
What did you use for your kernel and why?
How would you implement correlate_pixel with each kernel representation?
"""

# a.	Image dictionary kernel
kernel = {
    "height": 3,
    "width": 3,
    "pixels": [0, 0, 0, 0, 0, 0, 0, 1, 0],
}

# b.	Flat-list kernel
kernel = [0, 0, 0, 0, 0, 0, 0, 1, 0]

# c.	Nested-list kernel
kernel = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 1, 0],
]

# d.	Image coordinate offsets to kernel value dictionary
kernel = {
    (-1, -1): 0,
    (-1, 0): 0,
    (-1, 1): 0,
    (0, -1): 1,
    (0, 0): 0,
    (0, 1): 0,
    (1, -1): 0,
    (1, 0): 0,
    (1, 1): 0,
}
# keys are (row, col) tuples for the corresponding
# kernel value, and the kernel is centered at (0, 0)


def correlate_pixel(image, row, col, kernel, behavior):
    color = 0
    k_length = _____
    for k_row in range(k_length):
        for k_col in range(k_length):
            im_row = row + _____
            im_col = col + _____
            k_val = _________
            color += k_val * get_pixel(image, im_row, im_col, behavior)
    return color


def correlate(image, kernel, boundary_behavior="extend"):
    result = copy_image(image)
    for row in range(image["height"]):
        for col in range(image["width"]):
            new_color = correlate_pixel(image, row, col, kernel, boundary_behavior)
            set_pixel(result, row, col, new_color)
    return result
