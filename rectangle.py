from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import random

class RectangleMesh:

    def __init__(self, width, height, depth, eulers, position):
            
        self.width = width/2
        self.height = height/2
        self.depth = depth/2
        self.eulers= np.array(eulers, dtype=np.float32) # angle
        self.position= np.array(position, dtype=np.float32) # position
        
        # Cube vertices and edges
        self.vertices = (
            (self.width,  self.height,  self.depth),
            (-self.width, self.height, self.depth),
            (-self.width, -self.height, self.depth),
            (self.width, -self.height, self.depth),
            (self.width, self.height, -self.depth),
            (-self.width, self.height, -self.depth),
            (-self.width, -self.height, -self.depth),
            (self.width, -self.height, -self.depth)
        )

        self.edges = (
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 0),
            (4, 5),
            (5, 6),
            (6, 7),
            (7, 4),
            (0, 4),
            (1, 5),
            (2, 6),
            (3, 7)
        )
    
    def set_translation(self, pos_x, pos_y , pos_z):
        self.position = np.array((pos_x, pos_y, pos_z),dtype=np.float32)
    
    def set_rotation(self, rot_x, rot_y, rot_z):
        self.eulers = np.array((rot_x, rot_y, rot_z),dtype=np.float32)

    def draw_rect(self):
        
        glMatrixMode(GL_MODELVIEW)
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        
        glTranslatef(self.position[0], self.position[1], self.position[2])
        glRotatef(self.eulers[0], 1, 0, 0)
        glRotatef(self.eulers[1], 0, 1, 0)
        glRotatef(self.eulers[2], 0, 0, 1)

        # Set material properties
        glColor3f(1.0, 1.0, 1.0)  # Set the color to white
        glMaterialfv(GL_FRONT, GL_AMBIENT, [0.1, 0.1, 0.1, 1.0])  # Ambient material property
        glMaterialfv(GL_FRONT, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])  # Diffuse material property
        glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])  # Specular material property
        glMaterialf(GL_FRONT, GL_SHININESS, 50.0)  # Shininess of the material
    
        glBegin(GL_QUADS)
        # front plane
        glVertex3f(self.width, self.height, self.depth) # front top right
        glVertex3f(-self.width, self.height, self.depth) # front top left
        glVertex3f(-self.width, -self.height, self.depth) # front bottom left
        glVertex3f(self.width, -self.height, self.depth) # front bottom right
        
        # Back plane
        glVertex3f(self.width, self.height, -self.depth) # back top right
        glVertex3f(-self.width, self.height, -self.depth) # back top left
        glVertex3f(-self.width, -self.height, -self.depth) # back bottom left
        glVertex3f(self.width, -self.height, -self.depth) # back bottom right
         
        # left    
        glVertex3f(-self.width, self.height, self.depth) # front top left
        glVertex3f(-self.width, -self.height, self.depth) # front bottom left
        glVertex3f(-self.width, -self.height, -self.depth) # back bottom left
        glVertex3f(-self.width, self.height, -self.depth) # back top left
        
        # right
        glVertex3f(self.width, self.height, self.depth) # front top right
        glVertex3f(self.width, -self.height, self.depth) # front bottom right
        glVertex3f(self.width, -self.height, -self.depth) # back bottom right
        glVertex3f(self.width, self.height, -self.depth) # back top right
        
        # top
        glVertex3f(-self.width, self.height, self.depth) # front top left
        glVertex3f(self.width, self.height, self.depth) # front top right
        glVertex3f(self.width, self.height, -self.depth) # back top right
        glVertex3f(-self.width, self.height, -self.depth) # back top left
        
        # bottom
        glVertex3f(-self.width, -self.height, self.depth) # front bottom left
        glVertex3f(self.width, -self.height, self.depth) # front bottom right
        glVertex3f(self.width, -self.height, -self.depth) # back bottom right
        glVertex3f(-self.width, -self.height, -self.depth) # back bottom left
        glEnd()
        
        glPopMatrix()

    def draw_wired_rect(self):
        
        glMatrixMode(GL_MODELVIEW)
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        glEnable(GL_DEPTH_TEST)
        
        glPushMatrix() 
    
        glTranslatef(self.position[0], self.position[1], self.position[2])
        glRotatef(self.eulers[0], 1, 0, 0)
        glRotatef(self.eulers[1], 0, 1, 0)
        glRotatef(self.eulers[2], 0, 0, 1) 
        
        glEnable(GL_LINE_SMOOTH)  # Enable line smoothing
        glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)  # Use the highest quality for line smoothing
        glLineWidth(2.5)
        
        glBegin(GL_LINES)
        glColor3f(1.0, 1.0, 1.0)  
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
        glEnd()
        
        # Set material properties
        
        glColor3f(0.0, 0.0, 0.0)  
    
        glBegin(GL_QUADS)
        # front plane
        glVertex3f(self.width, self.height, self.depth) # front top right
        glVertex3f(-self.width, self.height, self.depth) # front top left
        glVertex3f(-self.width, -self.height, self.depth) # front bottom left
        glVertex3f(self.width, -self.height, self.depth) # front bottom right
        
        # Back plane
        glVertex3f(self.width, self.height, -self.depth) # back top right
        glVertex3f(-self.width, self.height, -self.depth) # back top left
        glVertex3f(-self.width, -self.height, -self.depth) # back bottom left
        glVertex3f(self.width, -self.height, -self.depth) # back bottom right
         
        # left    
        glVertex3f(-self.width, self.height, self.depth) # front top left
        glVertex3f(-self.width, -self.height, self.depth) # front bottom left
        glVertex3f(-self.width, -self.height, -self.depth) # back bottom left
        glVertex3f(-self.width, self.height, -self.depth) # back top left
        
        # right
        glVertex3f(self.width, self.height, self.depth) # front top right
        glVertex3f(self.width, -self.height, self.depth) # front bottom right
        glVertex3f(self.width, -self.height, -self.depth) # back bottom right
        glVertex3f(self.width, self.height, -self.depth) # back top right
        
        # top
        glVertex3f(-self.width, self.height, self.depth) # front top left
        glVertex3f(self.width, self.height, self.depth) # front top right
        glVertex3f(self.width, self.height, -self.depth) # back top right
        glVertex3f(-self.width, self.height, -self.depth) # back top left
        
        # bottom
        glVertex3f(-self.width, -self.height, self.depth) # front bottom left
        glVertex3f(self.width, -self.height, self.depth) # front bottom right
        glVertex3f(self.width, -self.height, -self.depth) # back bottom right
        glVertex3f(-self.width, -self.height, -self.depth) # back bottom left
        glEnd()
            
        glPopMatrix()

    def write_dim_csv(self):
        # normalize dimensions
        w = self.width / self.height
        h = 1
        d = self.depth / self.height