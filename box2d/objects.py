from Box2D import *
import draw

def create_ground(pos = (0, -50), size = (50, 10)):
    groundBodyDef = b2BodyDef()
    groundBodyDef.position = pos

    groundBody = world.CreateBody(groundBodyDef)

    groundShapeDef = b2PolygonDef()
    groundShapeDef.SetAsBox(size[0], size[1])

    groundBody.CreateShape(groundShapeDef)
    return groundBody

def create_box(pos = (-38, 4), size = (10, 10)):
    bodyDef = b2BodyDef()
    bodyDef.position = pos
    body = world.CreateBody(bodyDef)

    shapeDef = b2PolygonDef()
    shapeDef.SetAsBox(size[0], size[1])
    shapeDef.density = 1
    shapeDef.friction = 0.3
    shapeDef.restitution = 0.7
    body.CreateShape(shapeDef)
    body.SetMassFromShapes()
    return body

def create_ball(pos=(0, 0), rad=10):
    bodyDef = b2BodyDef()
    bodyDef.position = pos
    body = world.CreateBody(bodyDef)

    shapeDef = b2CircleDef()
    shapeDef.radius = rad
    shapeDef.density = 1
    shapeDef.friction = 0.3
    shapeDef.restitution = 0.7
    body.CreateShape(shapeDef)
    body.SetMassFromShapes()
    return body

def create_objects():
    gnd1 = create_ground()
    box1 = create_box()   
    ball1 = create_ball()
    ball1.SetAngularVelocity(1.7)
    box2 = create_box((8, 0), (2, 12))	
    gnd2 = create_ground((0, 0), (2, 2))
    joint1_def = b2RevoluteJointDef()
    joint1_def.Initialize(gnd2, ball1, (0, 0))
#    joint1_def.maxMotorTorque = 100
#    joint1_def.motorSpeed = 4
#    joint1_def.enableMotor = True
    world.CreateJoint(joint1_def)

    joint2 = b2RevoluteJointDef()
    joint2.Initialize(ball1, box2, (7, 0))
    world.CreateJoint(joint2)

def Step():	
    draw.start_draw()
    world.Step(timeStep, velocityIterations, positionIterations)
    draw.finish_draw()

def init():
    global worldAABB, world, timeStep, velocityIterations, positionIterations
    global drawer
    global worldLow, worldSize
    worldAABB=b2AABB()
    worldAABB.lowerBound = (-100, -100)
    worldAABB.upperBound = (100, 100)
    worldLow = worldAABB.lowerBound
    worldSize = worldAABB.upperBound - worldAABB.lowerBound

    gravity = (0, -10) # for pybox2d < 2.0.2b1, this must be a b2Vec2
    doSleep = True

    drawer = draw.MyDraw()
    world = b2World(worldAABB, gravity, doSleep)
#world.renderer = draw
    drawer.SetFlags(drawer.e_shapeBit | drawer.e_jointBit) # and whatever else you want it to draw 
    world.SetDebugDraw(drawer)
  
    create_objects() 
    
    timeStep = 1.0 / 60.0

    velocityIterations = 10
    positionIterations = 8

