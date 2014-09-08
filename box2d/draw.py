from Box2D import *
import pygame

class MyDraw(b2DebugDraw):
    """
    This debug draw class accepts callbacks from Box2D (which specifies what to draw)
    and handles all of the rendering.

    If you are writing your own game, you likely will not want to use debug drawing.
    Debug drawing, as its name implies, is for debugging.
    """
    def __init__(self, **kwargs):
        super(MyDraw, self).__init__()

        print 'Init Startdraw called'
    def StartDraw(self):
        print 'Startdraw called'
        """ Called when drawing starts.  """
    def EndDraw(self):
        print 'enddraw called'
        """ Called when drawing ends.  """
    def DrawPoint(self, p, size, color):
        """ Draw a single point at point p given a pixel size and color.  """
    def DrawAABB(self, aabb, color):
        """ Draw a wireframe around the AABB with the given color.  """
    def DrawSegment(self, p1, p2, color):
        """ Draw the line segment from p1-p2 with the specified color.  """
        pygame.draw.line(screen, (color.r * 256, color.g * 256, color.b *
                    256), Transform_Vertex((p1.x, p1.y)),
                Transform_Vertex((p2.x, p2.y)))

    def DrawTransform(self, xf):
        """ Draw the transform xf on the screen """
    def DrawCircle(self, center, radius, color, drawwidth=1):
        """ Draw a wireframe circle given the center, radius, axis of orientation and color.  """
        pygame.draw.circle(screen, (color.r * 256, color.g * 256, color.b *
                    256), Transform_Vertex(center), radius, 1)

    def DrawSolidCircle(self, center, radius, axis, color):
        """ Draw a solid circle given the center, radius, axis of orientation and color.  """
        v = Transform_Vertex((center.x, center.y))
        v = (int(v[0]), int(v[1]))
        r = Transform_Length(radius)
        r = int(r)
        pygame.draw.circle(screen, (color.r * 256, color.g * 256, color.b *
                    256), v, r, 1)

    def DrawPolygon(self, vertices, color):
        print 'poly called'
        """ Draw a wireframe polygon given the screen vertices (tuples) with the specified color.  """
    def DrawSolidPolygon(self, vertices, vertexCount, color):
        """ Draw a filled polygon given the screen vertices (tuples) with the specified color.  """
        ver=[]
        for v in vertices:
            ver.append(Transform_Vertex(v))
        pygame.draw.polygon(screen, (color.r * 256, color.g * 256, color.b *
                    256), ver)

def Transform_Vertex(ver):
    from objects import worldLow, worldSize
    x = (ver[0] - worldLow.x) / worldSize.x * screen.get_width()     
    y = screen.get_height() - (ver[1] - worldLow.y) / worldSize.y * screen.get_height()
    return (x, y)

def Inverse_Transform_Vertex(ver):
    from objects import worldLow, worldSize
    x = (ver[0] ) * worldSize.x / screen.get_width() + worldLow.x
    y = (screen.get_height() - ver[1]) * worldSize.y / screen.get_height() + worldLow.y
    return (x, y)

def Transform_Length(ln):
    from objects import worldLow, worldSize
    x = ln / worldSize.x * screen.get_width()     
    y = ln / worldSize.y * screen.get_height()
    return min(x, y)

def start_draw():
    screen.fill((0,0,0))

def finish_draw():
    pygame.display.flip()

def init():
    global screen
    pygame.init()
    screen = pygame.display.set_mode()

