"""
Q2: This file walks through different high level ways of implementing
correlate, slowly refactoring from a version that uses no
helper functions to a version that uses helper functions in a way that
reduces code complexity and repetition.

For each version, think about the pros and cons of implementing
correlate this way.

Then, for version 5, consider how you would implement
correlate_pixel given the different kernel representations described
in "q2_kernel_representations.py"
"""



# version 1: no helper functions
def correlate(image, kernel, boundary_behavior):
    result = {.... # make new image
              }
    if boundary_behavior == "zero":
        ... # 30 lines of correlation algorithm, but using zero boundary behavior
        """
        loop over each row in image
            loop over each col in image
                new_pixel = 0
                # apply kernel where (row, col) is at the center
                loop over kernel
                    find kernel val
                    find image coordinate that overlaps with kernel val
                    if coordinate is in bounds
                        get pixel val
                    else
                        get 0 (zero behavior)
                    new_pixel +=  kernel_val * pixel_val
                set row, col in image to new_pixel
        """
    elif boundary_behavior == "extend":
        ... # basically same 30 lines of correlation algorithm, but using extend boundary behavior
    elif boundary_behavior == "wrap":
        ... # basically same 30 lines of correlation algorithm, but using wrap boundary behavior











# version 2: make helper functions for each boundary behavior
def correlate(image, kernel, boundary_behavior):
    boundaries = {"zero": correlate_zero,
                  "extend": correlate_extend,
                  "wrap": correlate_wrap}
    if boundary_behavior not in boundaries:
        return None
    return boundaries[boundary_behavior](image, kernel)

def correlate_zero(image, kernel):
        ... # 30 lines of correlation algorithm, but using zero boundary behavior

def correlate_extend(image, kernel):
        ... # basically same 30 lines of correlation algorithm, but using extend boundary behavior

def correlate_wrap(image, kernel):
        ... # basically same 30 lines of correlation algorithm, but using wrap boundary behavior








# version 3: make image larger

def correlate(image, kernel, boundary_behavior):
    # first make bigger_image by extending image with len(kernel)/2+1 more pixels around each edge,
    # filled with appropriate pixel values for boundary behavior
    ...

    # then run correlation algorithm on bigger_image, keeping sliding window inside it
    ...

# it turns out that this approach takes more memory, and the logic to make the
# image larger and shift the row, col coordinates is quite complicated
# so let's go back to improving version 2








# version 4: move boundary behavior into get_pixel
def correlate(image, kernel, boundary_behavior="extend"):
    result = copy_image(image)
    for row in range(image["height"]):
        for col in range(image["width"]):
            new_pixel = 0
            for krow in range(kernel_height):
                 for kcol in range(kernel_width):
                    kval = ____
                    new_pixel += kval * get_pixel(image, row + __, col + __, boundary_behavior)
            set_pixel(result, row, col, new_pixel)
    return result

def get_pixel(image, row, col, behavior="extend"):
    if not in_bounds(image, row, col):
        if behavior == "extend":
            # extend: find the nearest in-bound coord using min / max
        elif behavior == "zero":
            # return 0
        elif behavior == "wrap":
            # wrap around image edge
    # in bounds get pixel as usual
    index = image["width"] * row + col
    return image["pixels"][index]











# version 5: make a helper function to apply the kernel
# to each (row, col) in the image

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

def get_pixel(image, row, col, behavior="extend"):
    if not in_bounds(image, row, col):
        if behavior == "extend":
            # extend: find the nearest in-bound coord using min / max
        elif behavior == "zero":
            # return 0
        elif behavior == "wrap":
            # wrap around image edge
    # in bounds get pixel as usual
    index = image["width"] * row + col
    return image["pixels"][index]