from OpenGL.GL import *
from numpy import array, float32, uint16


class Geometry(object):

	def __init__(self):
		self.type_vertex = float32
		self.type_index = uint16

	def set_vertex_array(self, vertex_array):
		self.vertex_array = array(vertex_array, dtype=float32)
	
	def set_index_array(self, index_array):
		self.index_array = array(index_array, dtype=uint16)

	def draw(self):
		glVertexPointerf(self.vertex_array)
		glDrawElementsui(GL_TRIANGLES, self.index_array)
