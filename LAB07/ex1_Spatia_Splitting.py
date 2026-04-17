import matplotlib.pyplot as plt
import matplotlib.patches as patches


def split_region(x, y, width, height, min_size):
    if width < min_size or height < min_size:
        return []

    if width / 2 < min_size or height / 2 < min_size:
        return [{
            "x": x,
            "y": y,
            "width": width,
            "height": height
        }]

    regions = []

    regions.extend(split_region(x, y, width / 2, height / 2, min_size))
    regions.extend(split_region(x + width / 2, y, width / 2, height / 2, min_size))
    regions.extend(split_region(x, y + height / 2, width / 2, height / 2, min_size))
    regions.extend(split_region(x + width / 2, y + height / 2, width / 2, height / 2, min_size))

    return regions


def count_points_in_region(points, region):
    count = 0
    for px, py in points:
        if (region["x"] <= px < region["x"] + region["width"] and
            region["y"] <= py < region["y"] + region["height"]):
            count += 1
    return count


def find_dense_regions(points, x, y, width, height, min_size, density_threshold):
    current_region = {
        "x": x,
        "y": y,
        "width": width,
        "height": height
    }

  
    if width / 2 < min_size or height / 2 < min_size:
        nb_points = count_points_in_region(points, current_region)
        area = width * height
        density = nb_points / area if area > 0 else 0

        if density > density_threshold:
            return [current_region]
        else:
            return []

    dense_regions = []

    dense_regions.extend(
        find_dense_regions(points, x, y, width / 2, height / 2, min_size, density_threshold)
    )
    dense_regions.extend(
        find_dense_regions(points, x + width / 2, y, width / 2, height / 2, min_size, density_threshold)
    )
    dense_regions.extend(
        find_dense_regions(points, x, y + height / 2, width / 2, height / 2, min_size, density_threshold)
    )
    dense_regions.extend(
        find_dense_regions(points, x + width / 2, y + height / 2, width / 2, height / 2, min_size, density_threshold)
    )

    return dense_regions

def draw_all_figures(points, regions, dense_regions, width, height):
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    x_values = [p[0] for p in points]
    y_values = [p[1] for p in points]

   
    axes[0].scatter(x_values, y_values, s=50)
    axes[0].set_xlim(0, width)
    axes[0].set_ylim(0, height)
    axes[0].set_aspect("equal")
    axes[0].set_title("figure 1: points distribution")
    axes[0].grid(True, linestyle="--", alpha=0.3)
    axes[1].scatter(x_values, y_values, s=50)

    for region in regions:
        rect = patches.Rectangle(
            (region["x"], region["y"]),
            region["width"],
            region["height"],
            fill=False,
            edgecolor="gray",
            linewidth=1
        )
        axes[1].add_patch(rect)

    axes[1].set_xlim(0, width)
    axes[1].set_ylim(0, height)
    axes[1].set_aspect("equal")
    axes[1].set_title("figure 2: split regions")
    axes[1].grid(True, linestyle="--", alpha=0.3)
    axes[2].scatter(x_values, y_values, s=50)

    for region in dense_regions:
        rect = patches.Rectangle(
            (region["x"], region["y"]),
            region["width"],
            region["height"],
            fill=True,
            facecolor="red",
            alpha=0.25,
            edgecolor="red",
            linewidth=2
        )
        axes[2].add_patch(rect)

        nb = count_points_in_region(points, region)
        area = region["width"] * region["height"]
        density = nb / area

        cx = region["x"] + region["width"] / 2
        cy = region["y"] + region["height"] / 2

        axes[2].text(
            cx, cy,
            f"pts={nb}\nd={density:.4f}",
            ha="center", va="center", fontsize=9
        )

    axes[2].set_xlim(0, width)
    axes[2].set_ylim(0, height)
    axes[2].set_aspect("equal")
    axes[2].set_title("figure 3: dense regions")
    axes[2].grid(True, linestyle="--", alpha=0.3)

    plt.tight_layout()
    plt.show()


###################################################### test ###################################################

if __name__ == "__main__":
    x = 0
    y = 0
    width = 100
    height = 100
    min_size = 25
    density_threshold = 0.005
    points = [
    (5, 5), (6, 6), (7, 8), (8, 9), (10, 10), (11, 12), (13, 14), (15, 16), (70, 70), (80, 20)
]

    regions = split_region(x, y, width, height, min_size)
    dense_regions = find_dense_regions(points, x, y, width, height, min_size, density_threshold)


    #draw_all_figures(points, regions, dense_regions, width, height)



    print("\n###########################  case 1  ###########################")

    x = 0
    y = 0
    width = 5
    height = 5
    min_size = 10
    density_threshold = 0.01
    points = [(1, 1), (2, 2), (4, 4)]

    regions = split_region(x, y, width, height, min_size)
    dense_regions = find_dense_regions(points, x, y, width, height, min_size, density_threshold)

    #draw_all_figures(points, regions, dense_regions, width, height)



    print("\n#################################### case 2 ######################################")

    x = 0
    y = 0
    width = 10
    height = 10
    min_size = 10
    density_threshold = 0.2
    points = [(2, 2), (5, 5), (8, 8)]

    regions = split_region(x, y, width, height, min_size)
    dense_regions = find_dense_regions(points, x, y, width, height, min_size, density_threshold)

    #draw_all_figures(points, regions, dense_regions, width, height)



    print("\n########################### case 3 #########################################")

    x = 0
    y = 0
    width = 10
    height = 0
    min_size = 10
    density_threshold = 0.1
    points = [(1, 0), (5, 0), (9, 0)]

    regions = split_region(x, y, width, height, min_size)
    dense_regions = find_dense_regions(points, x, y, width, height, min_size, density_threshold)


    #print("regions =", regions)
    #print("dense_regions =", dense_regions)



    print("\n################################ case 4 ###########################")

    x = 0
    y = 0
    width = 100
    height = 100
    min_size = 25
    density_threshold = 0.005
    points = []

    regions = split_region(x, y, width, height, min_size)
    dense_regions = find_dense_regions(points, x, y, width, height, min_size, density_threshold)

    #draw_all_figures(points, regions, dense_regions, width, height)




    print("\n####################################### case 5 ###########################################")

    x = 0
    y = 0
    width = 10
    height = 10
    min_size = 10
    density_threshold = 0.2
    points = [(0, 0), (10, 10), (10, 5), (5, 10), (0, 5), (5, 0)]

    regions = split_region(x, y, width, height, min_size)
    dense_regions = find_dense_regions(points, x, y, width, height, min_size, density_threshold)

    #draw_all_figures(points, regions, dense_regions, width, height)




    print("\n########################### case 6 #####################################")

    x = 0
    y = 0
    width = 0
    height = 0
    min_size = 10
    density_threshold = 0.1
    points = [(0, 0), (1, 1)]

    regions = split_region(x, y, width, height, min_size)
    dense_regions = find_dense_regions(points, x, y, width, height, min_size, density_threshold)

    #draw_all_figures(points, regions, dense_regions, width, height)

    test_region = {"x": x, "y": y, "width": width, "height": height}
    count = count_points_in_region(points, test_region)

    print("count in region =", count)
    print("regions =", regions)
    print("dense_regions =", dense_regions)



    print("\n############################## case 7 ###########################")

    x = 0
    y = 0
    width = 100
    height = 100
    min_size = 25
    density_threshold = 0.005
    points = [(10, 10)]

    regions = split_region(x, y, width, height, min_size)
    dense_regions = find_dense_regions(points, x, y, width, height, min_size, density_threshold)

    #draw_all_figures(points, regions, dense_regions, width, height)




    print("\n########################### case 8 ###################################")

    x = 0
    y = 0
    width = 100
    height = 100
    min_size = 25
    density_threshold = 0.005
    points = [
        (10, 10), (35, 10), (60, 10), (85, 10),
        (10, 35), (35, 35), (60, 35), (85, 35),
        (10, 60), (35, 60), (60, 60), (85, 60),
        (10, 85), (35, 85), (60, 85), (85, 85)
    ]

    regions = split_region(x, y, width, height, min_size)
    dense_regions = find_dense_regions(points, x, y, width, height, min_size, density_threshold)

    #draw_all_figures(points, regions, dense_regions, width, height)



    print("\n########################### case 9 ###########################")

    x = 0
    y = 0
    width = 100
    height = 100
    min_size = 25
    density_threshold = 100
    points = [
        (5, 5), (6, 6), (7, 8), (8, 9),(10, 10), 
        (11, 12), (13, 14), (15, 16),(70, 70), (80, 20)
    ]












  

    regions = split_region(x, y, width, height, min_size)
    dense_regions = find_dense_regions(points, x, y, width, height, min_size, density_threshold)

    draw_all_figures(points, regions, dense_regions, width, height)
