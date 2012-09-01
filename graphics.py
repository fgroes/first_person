from numpy import array
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import pygame
from pygame.locals import *


class Graphic():

	def __init__(self, screen_size=(800, 600), cam_pos=array([0.0, 0.0, 0.0])):
		self.screen_size = screen_size
		self.cam_pos = cam_pos
		self.cam_speed = array([0.0, 0.0, 0.0])
		self.speed = 0.1
		self.geometries = {}

	def set_movement_speed(self, speed):
		self.speed = speed

	def add_geometry(self, name, geometry):
		self.geometries[name] = geometry

	def reshape(self, width, height, angle=60, cut_near=0.1, cut_far=1000):
		glViewport(0, 0, width, height)
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluPerspective(angle, 1.0 * width / height, cut_near, cut_far)
		#glFrustum(-1, 1, -1, 1, 1, 100)
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()

	def init(self, light_position=(0, 1, 1, 0), color_background=(1, 1, 1, 0)):
		glEnable(GL_DEPTH_TEST)
		#glEnable(GL_NORMALIZE)
		glShadeModel(GL_SMOOTH)
		glClearColor(*color_background)
		glEnable(GL_COLOR_MATERIAL)
		glEnable(GL_LIGHTING)
		glEnable(GL_LIGHT0)
		glLight(GL_LIGHT0, GL_POSITION, light_position)
		glEnableClientState(GL_VERTEX_ARRAY)
		#glEnableClientState(GL_NORMAL_ARRAY)

	def display(self):
		self.cam_pos += self.cam_speed
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		gluLookAt(0, 0, 0, 0, 0, -100, 0, 1, 0)
		glPushMatrix()
		glTranslate(*self.cam_pos)
		self.draw_objects()
		glPopMatrix()
		glFlush()
		pygame.display.flip()

	def draw_objects(self):
		for g in self.geometries: 
			self.geometries[g].draw()	

	def run(self, fullscreen=False):
		pygame.init()
		glutInit()
		if fullscreen:
			self.screen = pygame.display.set_mode(self.screen_size, \
				HWSURFACE | OPENGL | DOUBLEBUF | FULLSCREEN)
		else:
			self.screen = pygame.display.set_mode(self.screen_size, \
				HWSURFACE | OPENGL | DOUBLEBUF)
		self.reshape(*self.screen_size)
		self.init()
		self.display()
		while True:
			for event in pygame.event.get():
				if event.type == QUIT:
					sys.exit(0)
				elif event.type == KEYDOWN:
					if event.key == K_w:
						self.cam_speed[2] += self.speed
					elif event.key == K_s:
						self.cam_speed[2] -= self.speed
					elif event.key == K_a:
						self.cam_speed[0] += self.speed
					elif event.key == K_d:
						self.cam_speed[0] -= self.speed
				elif event.type == KEYUP:
					if event.key == K_w:
						self.cam_speed[2] -= self.speed
					elif event.key == K_s:
						self.cam_speed[2] += self.speed
					elif event.key == K_a:
						self.cam_speed[0] -= self.speed
					elif event.key == K_d:
						self.cam_speed[0] += self.speed 
			self.display()
