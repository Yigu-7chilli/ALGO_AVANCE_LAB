import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


class Canvas:
  
    def __init__(self):
        self.fig, self.ax = plt.subplots()

  
    def draw_triangle(self, x, y, size):
        h = math.sqrt(3) / 2 * size
        points = [
            (x, y),
            (x + size, y),
            (x + size / 2, y + h)
        ]
        triangle = Polygon(points, closed=True, edgecolor="black", fill=False)
        self.ax.add_patch(triangle)

  
    def draw_line(self, x1, y1, x2, y2):
        self.ax.plot([x1, x2], [y1, y2], color="black")

    def show(self, title=""):
        self.ax.set_aspect("equal")
        self.ax.relim()
        self.ax.autoscale_view()
        self.ax.set_title(title)
        plt.show()



def draw_sierpinski(canvas, x, y, size, depth):
    if depth == 0:
        canvas.draw_triangle(x, y, size)
        return

    draw_sierpinski(canvas, x, y, size / 2, depth - 1)
    draw_sierpinski(canvas, x + size / 2, y, size / 2, depth - 1)
    draw_sierpinski(canvas, x + size / 4, y + (math.sqrt(3) / 4) * size, size / 2, depth - 1)



def draw_tree(canvas, x, y, length, angle, depth):
    x2 = x + length * math.cos(math.radians(angle))
    y2 = y + length * math.sin(math.radians(angle))

    canvas.draw_line(x, y, x2, y2)

    if depth == 0:
        return

    draw_tree(canvas, x2, y2, length * 0.75, angle + 30, depth - 1)
    draw_tree(canvas, x2, y2, length * 0.75, angle - 30, depth - 1)




def fractal_dimension(fractal_image, box_sizes):
    height, width = fractal_image.shape
    log_inv_size = []
    log_count = []

    for size in box_sizes:
        count = 0

        for y in range(0, height, size):
            for x in range(0, width, size):
                found_pixel = False

                for py in range(y, min(y + size, height)):
                    for px in range(x, min(x + size, width)):
                        if fractal_image[py, px] == 1:
                            found_pixel = True
                            break
                    if found_pixel:
                        break

                if found_pixel:
                    count += 1

        if count > 0:
            log_inv_size.append(math.log(1 / size))
            log_count.append(math.log(count))
            print("size =", size, ", count =", count,
                  ", log(1/size) =", math.log(1 / size),
                  ", log(count) =", math.log(count))

    if len(log_inv_size) >= 2:
        slope, intercept = np.polyfit(log_inv_size, log_count, 1)
        return slope, log_inv_size, log_count
    else:
        return None, log_inv_size, log_count




def generate_line_image(size):
    image = np.zeros((size, size), dtype=int)
    for i in range(size):
        image[i, i] = 1
    return image




def generate_filled_square_image(size):
    image = np.ones((size, size), dtype=int)
    return image




########################## test ###################################################################################

if __name__ == "__main__":

    canvas1 = Canvas()
    draw_sierpinski(canvas1, 0, 0, 8, 3)
    canvas1.ax.set_xlim(0, 8)
    canvas1.ax.set_ylim(0, 8)
    canvas1.show("sierpinski triangle")

    canvas2 = Canvas()
    draw_tree(canvas2, 0, 0, 8, 90, 5)
    canvas2.show("fractal tree")

    line_image = generate_line_image(64)
    box_sizes = [1, 2, 4, 8, 16]
    dim_line, x_line, y_line = fractal_dimension(line_image, box_sizes)
    print("estimated fractal dimension of line =", dim_line)

    plt.figure()
    plt.plot(x_line, y_line, marker="o")
    plt.title("box counting for line")
    plt.xlabel("log(1/size)")
    plt.ylabel("log(count)")
    plt.show()

    square_image = generate_filled_square_image(64)
    dim_square, x_square, y_square = fractal_dimension(square_image, box_sizes)
    print("estimated fractal dimension of filled square =", dim_square)

    plt.figure()
    plt.plot(x_square, y_square, marker="o")
    plt.title("box counting for filled square")
    plt.xlabel("log(1/size)")
    plt.ylabel("log(count)")
    plt.show()


    print("\n#################################### case 1 ########################################")

    canvas3 = Canvas()
    draw_sierpinski(canvas3, 0, 0, 8, 0)
    canvas3.ax.set_xlim(0, 8)
    canvas3.ax.set_ylim(0, 8)
    canvas3.show("case 1 : depth = 0")


    print("\n####################################### case 2 ######################################")

    canvas4 = Canvas()
    draw_sierpinski(canvas4, 0, 0, 0, 3)
    canvas4.ax.set_xlim(-1, 1)
    canvas4.ax.set_ylim(-1, 1)
    canvas4.show("case 2 : size = 0")


    print("\n#################################### case 3 ###########################")

    canvas5 = Canvas()
    draw_sierpinski(canvas5, 0, 0, -8, 2)
    canvas5.ax.set_xlim(-10, 2)
    canvas5.ax.set_ylim(-10, 2)
    canvas5.show("case 3 : size < 0")


    print("\n########################### case 4 #######################################")

    canvas6 = Canvas()
    draw_tree(canvas6, 0, 0, 0, 90, 3)
    canvas6.ax.set_xlim(-1, 1)
    canvas6.ax.set_ylim(-1, 1)
    canvas6.show("case 4 : length = 0")





    print("\n##################################### case 5 ##########################################")

    canvas7 = Canvas()
    draw_tree(canvas7, 0, 0, -8, 90, 3)
    canvas7.ax.set_xlim(-10, 10)
    canvas7.ax.set_ylim(-10, 10)
    canvas7.show("case 5 : length < 0")




    print("\n################################### case 6 ######################################")

    empty_image = np.zeros((64, 64), dtype=int)
    box_sizes = [1, 2, 4, 8, 16]

    dim_empty, x_empty, y_empty = fractal_dimension(empty_image, box_sizes)

   
    print("estimated fractal dimension =", dim_empty)
    print("log(1/size) =", x_empty)
    print("log(count) =", y_empty)

    plt.figure()
    plt.imshow(empty_image, cmap="gray", origin="lower")
    plt.title("case 6 : no black pixels")
    plt.show()




    print("\n############################### case 7 ###############################")

    line_image = generate_line_image(64)
    box_sizes = []

    dim_empty_box, x_empty_box, y_empty_box = fractal_dimension(line_image, box_sizes)

 
    print("estimated fractal dimension =", dim_empty_box)
    print("log(1/size) =", x_empty_box)
    print("log(count) =", y_empty_box)

    plt.figure()
    plt.imshow(line_image, cmap="gray", origin="lower")
    plt.title("case 7 : box_sizes = []")
    plt.show()














