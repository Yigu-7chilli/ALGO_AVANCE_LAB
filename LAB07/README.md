# LAB6_01_Revision

## File Structure:
~~~
/LAB _ 07/
├── ex1_Spatia_Splitting.py
├── ex2_Recursive_Shapes.py
└── README.md
~~~

---


##  Brief description of each solution

### Solution of exercise1_

# algo avance lab

## exercise 1: divide & conquer – spatial splitting

**objective:** implement recursive functions that split a 2d space into smaller regions.

### requirements

1. implement `split_region(x, y, width, height, min_size)`
   - `x, y` are the top-left corner coordinates of a rectangular region `(width, height)`
   - if the region is smaller than `min_size`, stop
   - else, split into 4 equal quadrants
   - recursively call `split_region` on each quadrant

2. implement `count_points_in_region(points, region)`
   - `points` can be generated randomly
   - count how many points fall inside a given region
   - use with the split function to find dense areas

3. implement `find_dense_regions(points, min_size, density_threshold)`
   - recursively split space
   - return only regions where point density > threshold

### solution of exercise

#### 1. `split_region(x, y, width, height, min_size)`
this function recursively divides a rectangular region into 4 equal subregions.  
if the region is already smaller than the minimum size, the recursion stops.  
otherwise, the function calls itself on the 4 quadrants:
- top-left
- top-right
- bottom-left
- bottom-right

#### 2. `count_points_in_region(points, region)`
this function checks all points one by one and counts how many of them belong to the current region.  
it is used to support the density calculation.

#### 3. `find_dense_regions(points, x, y, width, height, min_size, density_threshold)`
this function recursively explores the space and keeps only the smallest regions whose density is greater than the threshold.  
the density is computed using:

`density = number_of_points / area`

### complexity analysis summary

- `split_region`
  - recursive quadtree subdivision
  - worst-case complexity: `O(4^k)`
  - if the final size is `1 x 1`, it is equivalent to `O(n^2)`

- `count_points_in_region`
  - scans all points once
  - complexity: `O(N)`

- `find_dense_regions`
  - may call `count_points_in_region` on many regions
  - worst-case complexity: `O(N * 4^k)`

---

## exercise 2: fractal drawing – recursive shapes

**objective:** draw self-similar shapes using recursion.

### requirements

1. implement `draw_sierpinski(canvas, x, y, size, depth)`
   - if `depth == 0`, draw a triangle
   - else, draw 3 smaller sierpinski triangles inside

2. implement `draw_tree(canvas, x, y, length, angle, depth)`
   - if `depth == 0`, draw a line (leaf)
   - else, draw a line, then draw 2 smaller branches at `±30` degrees

3. implement `fractal_dimension(fractal_image, box_sizes)`
   - for each box size, count how many boxes contain part of the fractal
   - plot `log(count)` vs `log(1/size)`
   - slope = fractal dimension

### solution of exercise

#### 1. `draw_sierpinski(canvas, x, y, size, depth)`
this function draws a sierpinski triangle recursively.  
if `depth = 0`, it draws one triangle.  
otherwise, it recursively draws 3 smaller triangles of size `size / 2`.

#### 2. `draw_tree(canvas, x, y, length, angle, depth)`
this function draws a fractal tree recursively.  
it first draws the current branch, then recursively draws 2 smaller branches:
- one with `angle + 30`
- one with `angle - 30`

#### 3. `fractal_dimension(fractal_image, box_sizes)`
this function uses the box-counting method.  
for each box size:
- divide the image into boxes
- count how many boxes contain at least one black pixel
- compute `log(1/size)` and `log(count)`

the slope of the final line estimates the fractal dimension.

### complexity analysis summary

draw_sierpinski
3 recursive calls at each level
complexity: O(3^d)

draw_tree
2 recursive calls at each level
complexity: O(2^d)

fractal_dimension
for each box size, the image is scanned
complexity: O(b * m^2)
where:
b= number of box sizes
m x m = image size
