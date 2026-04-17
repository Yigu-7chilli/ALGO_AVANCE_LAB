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

## exercise 1: divide & conquer – spatial splitting

### solution of exercise

#### 1. split_region(x, y, width, height, min_size)
this function recursively divides a rectangular region into 4 equal subregions.  
if the region is already smaller than the minimum size, the recursion stops.  
otherwise, the function calls itself on the 4 quadrants:
- top-left
- top-right
- bottom-left
- bottom-right

#### 2. count_points_in_region(points, region)
this function checks all points one by one and counts how many of them belong to the current region.  
it is used to support the density calculation.

#### 3. find_dense_regions(points, x, y, width, height, min_size, density_threshold)
this function recursively explores the space and keeps only the smallest regions whose density is greater than the threshold.  
the density is computed using:

density = number_of_points / area

### complexity analysis summary

- split_region
  
  worst-case complexity: O(4^k)

- count_points_in_region
  
  complexity: O(N)

- find_dense_regions
  
  worst-case complexity: O(N * 4^k)

---

## exercise 2: fractal drawing – recursive shapes

### solution of exercise

#### 1. draw_sierpinski(canvas, x, y, size, depth)
this function draws a sierpinski triangle recursively.  
if depth = 0, it draws one triangle.  
otherwise, it recursively draws 3 smaller triangles of size size / 2.

#### 2. draw_tree(canvas, x, y, length, angle, depth)
this function draws a fractal tree recursively.  
it first draws the current branch, then recursively draws 2 smaller branches:
- one with angle + 30
- one with angle - 30

#### 3. fractal_dimension(fractal_image, box_sizes)
this function uses the box-counting method.  
for each box size:
- divide the image into boxes
- count how many boxes contain at least one black pixel
- compute log(1/size) and log(count)

the slope of the final line estimates the fractal dimension.

### complexity analysis summary

- draw_sierpinski

  complexity: O(3^d)

- draw_tree

  complexity: O(2^d)

- fractal_dimension

  complexity: O(b * m^2)
   
  where: b= number of box sizes
  
  m x m = image size



