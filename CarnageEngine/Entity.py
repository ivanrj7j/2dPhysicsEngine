import pygame
from pygame import color
from .Physics import Physics
from .Vector import Vector2

class Entity(Physics):
    def __init__(self,superParent:pygame.display,parent, object:pygame.Rect,color:tuple,collisionObjects:list, centreOfMass:Vector2,surface:pygame.Surface, gravityScale=1, defaultGravityAccelaration=9.81, mass = 1, doesapplyGravity = True, airDrag = 0.2, Kinematic=False, shouldUseColor=True, isActive = True):
        self.object = object
        self.surface = surface
        self.surfaceOriginal = self.surface
        self.gravityScale = gravityScale
        self.defaultGravityAccelaration = defaultGravityAccelaration
        self.mass = mass
        self.doesapplyGravity = doesapplyGravity
        self.color = color
        self.parent = parent
        self.superParent = superParent
        self.velocity = Vector2(0,0)
        self.collisionObjects = collisionObjects
        self.airDrag = airDrag
        self.kinematic = Kinematic
        self.kineticEnergy = 1
        self.centreOfMass = centreOfMass
        self.shouldUseColor = shouldUseColor
        self.rotation = 0
        self.isActive = isActive
        # Initialising all the variables 

    def update(self, deltaTime, offset:Vector2, scale:float):
        if self.isActive:
            newWidth = scale * self.object.width
            newHieght = scale * self.object.height
            newSurface = pygame.transform.scale(self.surface, (self.surface.get_width() * scale, self.surface.get_height() * scale))
            # scaling up the object according to the camera

            if not self.kinematic:
                self.collision(deltaTime)
                if self.doesapplyGravity:
                    self.applyGravity(deltaTime)
                    # applying gravity  
            # applying all the forces to the object 

            if self.shouldUseColor:
                self.surface.fill(self.color)
                # filling the color 

            objectOffset = Vector2((self.object.x + offset.x) * scale , (self.object.y + offset.y) * scale)
            print(objectOffset)
            self.superParent.blit(newSurface, (objectOffset.x, objectOffset.y, newWidth, newHieght))
            # drawing the object 
    
    def toggleActive(self, *keyWordArguments:bool):
        if keyWordArguments:
            self.isActive = keyWordArguments[0]
        else:
            if self.isActive == True:
                self.isActive = False
            else:
                self.isActive = True

        

        
        
    