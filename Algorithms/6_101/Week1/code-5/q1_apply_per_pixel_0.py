"""
Question 1: Given the two versions of inverted and round_and_clip_image below,
 discuss with a neighbor: How readable is each version (how easy is it to
 understand what the code is doing)? How extensible is each version
 (how hard would it be to change the image representation or add new behaviors)?
"""

# VERSION 1:
WIDTH, HEIGHT, PIXELS = "width", "height", "pixels"


def get_width(image):
    return image[WIDTH]


def get_height(image):
    return image[HEIGHT]


def get_index(image, row, col):
    return row * image[WIDTH] + col


def get_pixel(image, row, col):
    return image[PIXELS][get_index(image, row, col)]


def set_pixel(image, row, col, color):
    image[PIXELS][get_index(image, row, col)] = color


def blank_image(image):
    return {
        HEIGHT: image[HEIGHT],
        WIDTH: image[WIDTH],
        PIXELS: [0] * image[WIDTH] * image[HEIGHT],
    }


def apply_per_pixel(image, func):
    result = blank_image(image)
    for col in range(get_width(image)):
        for row in range(get_height(image)):
            color = get_pixel(image, row, col)
            new_color = func(color)
            set_pixel(result, row, col, new_color)
    return result


def inverted(image):
    return apply_per_pixel(image, lambda color: 255 - color)


def round_and_clip_image(image):
    clip = lambda pixel: max(0, min(255, round(pixel)))
    return apply_per_pixel(image, clip)


# VERSION 2:
w, h, p = "width", "height", "pixels"


def invertedV2(image):
    i = image
    out = {h: i[h], w: i[w], p: i[p].copy()}
    for r in range(i[h]):
        for c in range(i[w]):
            x = i[p][r * i[w] + c]
            x = 255 - x
            out[p][r * i[w] + c] = x
    return out


def round_and_clipV2(image):
    i = image
    out = {h: i[h], w: i[w], p: i[p].copy()}
    for r in range(i[h]):
        for c in range(i[w]):
            x = round(i[p][r * i[w] + c])
            if x > 255:
                x = 255
            elif x < 0:
                x = 0
            out[p][r * i[w] + c] = x
    return out
