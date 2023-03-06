import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

width, height = 800, 600                                                    # width and height of the screen created

########################################### Lecture examples ####################################################
def example_initTeapot():  # initiated at  origin
    glColor3f(1.0, 1.0, 1.0)                                                # specify object color as white
    glLineWidth(1.0)                                                        # reset line width to 1.0
    glutWireTeapot(5.0)                                                     # draw a teaport of size 5 in wireframe mode

def example_translate():
    glTranslatef(15.0, 0.0, 0.0)                                            # construct translation matrix with a translation vector
    glColor3f(1.0, 0.2, 0.6)                                                # draw the transformed teaport in pink
    glutWireTeapot(5.0)

def example_scale():
    glScalef(2.0, 2.0, 2.0)                                                 # construct scaling matrix with three scaling factors
    glColor3f(1.0, 0.2, 0.6)                                                # draw the transformed teaport in pink
    glutWireTeapot(5.0)

def example_rotate():
    glRotatef(-90.0, 0.0, 0.0, 1.0)                                         # construct rotation matrix along z-axis (0,0,1)
    glColor3f(1.0, 0.2, 0.6)                                                # draw the transformed teaport in pink
    glutWireTeapot(5.0)

def example_rotate_tranlate():                                              # rotate then translate
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glColor3f(0.2, 0.5, 0.4)
    glBegin(GL_TRIANGLES)                                                   # draw the initial triangle in green
    glVertex3f(-2.5, -2.5, 0.1)
    glVertex3f(2.5, -2.5, 0.1)
    glVertex3f(0.0, 5.0, 0.1)
    glEnd()

    glTranslatef(10.0, 10.0, 0.0)                                           # M1: translate
    glRotatef(90.0, 0.0, 0.0, 1.0)                                          # M2: rotate along z-axis (0,0,1)
    
    glColor3f(1.0, 0.0, 0.0)                                                # draw the transformed triangle in red
    glBegin(GL_TRIANGLES)
    glVertex3f(-2.5, -2.5, 0.1)
    glVertex3f(2.5, -2.5, 0.1)
    glVertex3f(0.0, 5.0, 0.1)
    glEnd()

def example_translate_rotate():                                              # translate then rotate
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glColor3f(0.2, 0.5, 0.4)
    glBegin(GL_TRIANGLES)                                                    # draw the initial triangle in green
    glVertex3f(-2.5, -2.5, 0.1)
    glVertex3f(2.5, -2.5, 0.1)
    glVertex3f(0.0, 5.0, 0.1)
    glEnd()

    glRotatef(90.0, 0.0, 0.0, 1.0)                                          # M1: rotate along z-axis (0,0,1)    
    glTranslatef(10.0, 10.0, 0.0)                                           # M2: translate
    
    glColor3f(1.0, 0.0, 0.0)                                                # draw the transformed triangle in red
    glBegin(GL_TRIANGLES)
    glVertex3f(-2.5, -2.5, 0.1)
    glVertex3f(2.5, -2.5, 0.1)
    glVertex3f(0.0, 5.0, 0.1)
    glEnd()

########################################### Exercise ####################################################
# Exercise 1
def exercise1_transfOrder():
    # create an initial triangle centered at (4, 3, 0.1) in white
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)                               
    glColor3f(1.0, 1.0, 1.0)                                                
    glBegin(GL_TRIANGLES)                                                    
    glVertex3f(4.0, 8.0, 0.1)
    glVertex3f(2.0, 2.0, 0.1)
    glVertex3f(6.0, 2.0, 0.1)
    glEnd() 

    # TODO: rotate the triangle around a pivot-point (4, 3, 0.1) along z-axis about 90 degrees
    # work bottom to top
    glTranslatef(4.0, 3.0, 0.0) # third translate object back to pivot point
    glRotatef(90.0, 0.0, 0.0, 1.0) # second rotate object
    glTranslatef(-4.0, -3.0, 0.0) # first translate object to origin (except the axis that is being rotated on)
  
    # draw the transformed triangle centered at (4, 3, 0.1) in blue
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)                               
    glColor3f(0.6, 0.8, 1.0)
    glBegin(GL_TRIANGLES)                                                   
    glVertex3f(4.0, 8.0, 0.1)
    glVertex3f(2.0, 2.0, 0.1)
    glVertex3f(6.0, 2.0, 0.1)
    glEnd()

def exercise2_push_pop():
    # configure quatratic drawing
    quadratic = gluNewQuadric()
    gluQuadricDrawStyle(quadratic, GLU_FILL)
  
    # TODO: Rotate the cylinder around x-axis by -90
    glColor3f(1.0, 1.0, 0.0)
    glPushMatrix() # push matrix to stack
    glRotatef(-90.0, 1.0, 0.0, 0.0) # transform (rotate) cylinder
    gluCylinder(quadratic, 2.5, 2.5, 10.0, 32, 32) # quadratic, radius, radius, length, layers of mesh
    glPopMatrix() # pop matrix from stack (resetting any transformations made)

    # TODO: Translate the sphere by (10, 10, 0)
    glColor3f(0.0, 1.0, 0.0)
    glPushMatrix() # push matrix to stack
    glTranslatef(10.0, 10.0, 0.0) # transform (translate) sphere
    gluSphere(quadratic, 2.5, 32, 32) # quadratic, radius, layers of mesh
    glPopMatrix() # pop matrix from stack

########################################### OpenGL Program ####################################################
def drawAxes():                                                             # draw x-axis and y-axis
    glLineWidth(3.0)                                                        # specify line size (1.0 default)
    glBegin(GL_LINES)                                                       # replace GL_LINES with GL_LINE_STRIP or GL_LINE_LOOP
    glColor3f(1.0, 0.0, 0.0)                                                # x-axis: red
    glVertex3f(0.0, 0.0, 0.0)                                               # v0
    glVertex3f(100.0, 0.0, 0.0)                                             # v1
    glColor3f(0.0, 1.0, 0.0)                                                # y-axis: green
    glVertex3f(0.0, 0.0, 0.0)                                               # v0
    glVertex3f(0.0, 100.0, 0.0)                                             # v1
    glColor3f(0.0, 0.0, 1.0)                                                # z-axis: green
    glVertex3f(0.0, 0.0, 0.0)                                               # v0
    glVertex3f(0.0, 0.0, 100.0)                                             # v1
    glEnd()

def draw():                                                                 # This is the drawing function drawing all graphics (defined by you)
    glClearColor(0, 0, 0, 1)                                                # set background RGBA color 
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)                        # clear the buffers initialized in the display mode
    
    # initialize a teapot in white at origin
    #example_initTeapot()

    glPushMatrix()                                                          # save the current model-view trans matrix in the stack
    
    # geometric transformation examples (uncomment "example_initTeatpot")
    #example_translate()                                                    # translate
    #example_scale()                                                        # scale
    #example_rotate()                                                       # rotate

    # composite transformation examples (comment out "example_initTeatpot")
    #example_rotate_tranlate()
    #example_translate_rotate()

    # exercise: random pivot-point rotation 
    #exercise1_transfOrder()

    # push-pop example: transform 3D objects separately 
    exercise2_push_pop()

    glPopMatrix()                                                           # restore the saved model-view trans matrix back

def main():
    pygame.init()                                                           # initialize a pygame program
    glutInit()                                                              # initialize glut library 

    screen = (width, height)                                                # specify the screen size of the new program window
    display_surface = pygame.display.set_mode(screen, DOUBLEBUF | OPENGL)   # create a display of size 'screen', use double-buffers and OpenGL
    pygame.display.set_caption('CPSC 360')                                  # set title of the program window

    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)                                             # set mode to projection transformation
    glLoadIdentity()                                                        # reset transf matrix to an identity
    gluPerspective(45, (width / height), 0.1, 100.0)                        # specify perspective projection view volume

    glMatrixMode(GL_MODELVIEW)                                              # set mode to modelview (geometric + view transf)
    initmodelMatrix = glGetFloat(GL_MODELVIEW_MATRIX)
    modelMatrix = glGetFloat(GL_MODELVIEW_MATRIX)

    while True:
        bResetModelMatrix = False
        glPushMatrix()
        glLoadIdentity()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:
                    glRotatef(event.rel[1], 1, 0, 0)
                    glRotatef(event.rel[0], 0, 1, 0)
                    #print(event.rel[0], event.rel[1])

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    bResetModelMatrix = True        

        #glRotatef(1, 0, 1, 0)                                              # allow the whole scene to spin around y-axis
        if (bResetModelMatrix):
            glLoadIdentity()
            modelMatrix = initmodelMatrix
        glMultMatrixf(modelMatrix)
        modelMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

        glLoadIdentity()
        gluLookAt(0, 0, 50, 0, 0, -1, 0, 1, 0)
        glMultMatrixf(modelMatrix)
        draw()
        drawAxes()

        glPopMatrix()
        pygame.display.flip()
        pygame.time.wait(10)

main()