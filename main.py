from graphics import Graphic
from geometries import Geometry


triangles = [[0, 0, 0], [1, 0, 0], [0, 1, 0], [1, 1, 0]]
indexes = [[0, 1, 2], [1, 3, 2]]


if __name__ == '__main__':
	g = Graphic()
	triangle = Geometry()
	triangle.set_vertex_array(triangles)
	triangle.set_index_array(indexes)
	g.add_geometry('triangle', triangle)
	g.run()
