## FRONT MATTER FOR DRAWING/SAVING IMAGES, ETC

from PIL import Image as PILImage

# some test colors
COLORS = {
    "red": (255, 0, 0),
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "green": (0, 100, 0),
    "lime": (0, 255, 0),
    "blue": (0, 0, 255),
    "cyan": (0, 255, 255),
    "yellow": (255, 230, 0),
    "purple": (179, 0, 199),
    "pink": (255, 0, 255),
    "orange": (255, 77, 0),
    "brown": (66, 52, 0),
    "grey": (152, 152, 152),
}


def new_image(width, height, fill=(240, 240, 240)):
    return {
        "height": height,
        "width": width,
        "pixels": [fill for r in range(height) for c in range(width)],
    }


def flat_index(image, x, y):
    assert 0 <= x < image["width"] and 0 <= y < image["height"]
    return (image["height"] - 1 - y) * image["width"] + x


def get_pixel(image, x, y):
    return image["pixels"][flat_index(image, x, y)]


def set_pixel(image, x, y, c):
    assert (
        isinstance(c, tuple)
        and len(c) == 3
        and all((isinstance(i, int) and 0 <= i <= 255) for i in c)
    )
    if 0 <= x < image["width"] and 0 <= y < image["height"]:
        image["pixels"][flat_index(image, x, y)] = c


def save_color_image(image, filename, mode="PNG"):
    out = PILImage.new(mode="RGB", size=(image["width"], image["height"]))
    out.putdata(image["pixels"])
    if isinstance(filename, str):
        out.save(filename)
    else:
        out.save(filename, mode)
    out.close()


## SHAPES!


class Shape:
    # Shape s = new Rectangle();
    # Point p = new Point(s.center[0],s.center[1]);
    # s.center= p
    # All subclasses MUST implement the following:
    #
    # __contains__(self, p) returns True if point p is inside the shape
    # represented by self
    #
    # note that "(x, y) in s" for some instance of Shape
    # will be translated automatically to "s.__contains__((x, y))"
    #
    # s.center should give the (x,y) center point of the shape
    #
    # draw(self, image, color) should mutate the given image to draw the shape
    # represented by self on the given image in the given color
    #
    def __contains__(self, p):
        raise NotImplementedError("SubClass  of shape did not  implement this method")

    def draw(self, image, color):
        for x in range(image["width"]):
            for y in range(image["height"]):
                if (x, y) in self:
                    set_pixel(image, x, y, color)


class Circle(Shape):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def area(self):
        return self.radius * self.radius

    def __contains__(self, p):
        # x=p[0]
        # y=p[1]
        # Incorrect:
        # return True if self.center[0]-self.area()/2<=x<=self.center[0]+self.area()/2 and self.center[1]-self.area()/2<=y<=self.center[1]+self.area()/2 else False
        return sum((x - y) ** 2 for x, y in zip(self.center, p)) <= self.area()


class Rectangle(Shape):
    """
    here are many different ways we could represent rectangles in code,
     but the one that we'll use as a running example here will store each rectangle's lower-left corner (as an (x, y) tuple),
      as well as its width and height (each as an integer):
    """

    def __init__(self, lower_left, width, height):
        self.x = lower_left[0]
        self.y = lower_left[1]
        self.lower_left = lower_left  # tuple of x and y
        self.height = height
        self.width = width

    @property
    def center(self):
        return (
            self.lower_left[0] + self.width // 2,
            self.lower_left[1] + self.height // 2,
        )

    @center.setter
    def center(self, value):
        self.lower_left = value[0] - self.width // 2, value[1] - self.height // 2

    def area(self):
        return self.width * self.height

    def __contains__(self, item):
        x = item[0]
        y = item[1]
        return (
            self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height
        )

    def draw(self, image, color):
        for x in range(self.lower_left[0], self.lower_left[0] + self.width):
            for y in range(self.lower_left[1], self.lower_left[1] + self.height):
                set_pixel(image, x, y, color)


class Square(Rectangle):
    def __init__(self, lower_left, side):
        Rectangle.__init__(self, lower_left, side, side)


class Combination(Shape):
    def __init__(self, shape1, shape2):
        self.shape1 = shape1
        self.shape2 = shape2

    @property
    def center(self):
        c1 = self.shape1.center
        c2 = self.shape2.center
        return (c1[0] + c2[0]) // 2, (c1[1] + c2[1]) // 2


class Union(Combination):
    """
    shape that represents the union of two shapes.
    Think for a little while about how we might implement this:
    What inputs should it take at initialization time?
     What attributes should it store? How and where should we implement __contains__?
    """

    def __or__(self, p):
        return p in self.shape1 or p in self.shape2

    def __contains__(self, p):
        return p in self.shape1 or p in self.shape2


class Intersection(Combination):

    def __and__(self, other):
        return other in self.shape1 and other in self.shape2

    def __contains__(self, item):
        return item in self.shape1 and item in self.shape2


class Difference(Combination):

    def __ior__(self, item):
        return item in self.shape1 and item not in self.shape2

    def __contains__(self, item):
        return item in self.shape1 and item not in self.shape2


if __name__ == "__main__":

    out_image = new_image(500, 500)
    shapes = [
        (Circle((100, 100), 30), COLORS["purple"]),
        (Rectangle((200, 300), 70, 20), COLORS["blue"]),
        (Square((150, 400), 40), COLORS["green"]),
    ]
    # rectangle = [
    #     (Rectangle((100,100),80,80),COLORS['red']),
    # ]
    # for shape,color in shapes:
    #     shape.draw(out_image,color)
    for shape, color in shapes:
        shape.draw(out_image, color)
    # add code here to draw some shapes
    # circle = Circle((0,0),1)
    rectangle = Rectangle((0, 0), 1, 1)
    rectangle.center = (2, 3)
    # rectangle.draw(out_image,COLORS['red'])
    # circle.draw(out_image,COLORS['purple'])
    # print((-.5,.5) in circle)
    # print((.5,0) in rectangle)
    # save_color_image(out_image, "test3.png")

    smiley = new_image(500, 500)
    c1 = Circle((250, 250), 100)
    c1 = Difference(c1, Circle((220, 280), 20))
    c1 = Difference(c1, Circle((280, 280), 20))
    c1 = Difference(
        c1, Difference(Circle((250, 250), 80), Rectangle((0, 250), 500, 500))
    )
    c1.draw(smiley, COLORS["grey"])
    # save_color_image(smiley,'smiley.png')
    img = new_image(500, 500)
    rectangle = Rectangle((200, 300), 70, 20)
    rectangle.draw(img, COLORS["purple"])
    save_color_image(img, "rectangle_test.png")
    c2 = Circle((250, 250), 100)
