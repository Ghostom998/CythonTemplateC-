# ignore the import error below in your IDE as it should run fine in python
from rect import PyRectangle
# Then implement!
def main():
    x0, x1, y0, y1 = 1, 3, 4, 7
    # Create rectangle object
    rectangle = PyRectangle(x0, y0, x1, y1)

    # Run methods
    width, height = rectangle.get_size()
    area = rectangle.get_area()
    print("Width of rectangle is: %s" % width)
    print("Height of rectangle is: %s" % height)
    print("Area of rectangle is %s" % area )

#if __name__ == __main__:
main()