import pygame
import math
pygame.init()
pygame.display.init()
pygame.font.init()

class Checkpoint:
    def __init__(self, x, y, size, index):
        self.x =x
        self.y=y
        self.size = size
        self.index = index
        self.colour = ROT
        self.thickness = 5
        
    def display(self):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.size, self.thickness)

        
class Area:
    def __init__(self, x1, y1, x2, y2, color):
        self.x1 = min(x1, x2)
        self.y1 = min(y1, y2)
        self.x2 = max(x1, x2)
        self.y2 = max(y1, y2)
        self.color = color
    def display(self):
        pygame.draw.rect(screen, self.color, (self.x1, self.y1, (self.x2-self.x1), (self.y2-self.y1)))  
    def isClicked(self, clickX, clickY):
        # works only if x2 > x1 and y2 > y1
        if self.x1 < clickX < self.x2 and self.y1 < clickY < self.y2:
            #print(self, "is clicked")
            return True
        
        else:
            return False
        
    def displayText(self, text):
        print(text)
        text = myfont.render(text, True, (255, 255, 100))
        #print("x1: ", self.x1+(self.x2-self.x1)/2)
        #print("x1: ", self.y1+(self.y2-self.y1)/2)
        screen.blit(text, (int(self.x1+(self.x2-self.x1)/2)-40, int(self.y1+(self.y2-self.y1)/2))) #-40
        
        
class Floor():
    def __init__(self, color):
        self.color = color
    def display(self):
        pygame.draw.rect(screen, self.color, (self.x1, self.y1, (self.x2-self.x1), (self.y2-self.y1)))        

class Group:
    def __init__(self, name):
        self.name = name
        self.startArea = None
        self.endArea = None 
        self.checkpointRoute = []
    def setStartArea(self, inputArea):
        self.startArea = inputArea
    def setEndArea(self, inputArea):
        self.endArea = inputArea   
    def addToCheckpointRoute(self, ClickedCheckpoint):
        self.checkpointRoute.append(ClickedCheckpoint)
    def printRoute(self):
        
        print("\n----------------------\n",
            "GroupName:  ", self.name,
            "\n startArea: (", self.startArea.x1, ",", self.startArea.y1, ")  - (", self.startArea.x2, ",", self.startArea.y2, ")",
            "\n checkpointRoute: ", [(checkpoint.x, checkpoint.y) for checkpoint in self.checkpointRoute],
            "\n endArea: (", self.endArea.x1, ",", self.endArea.y1, ")  - (", self.endArea.x2, ",", self.endArea.y2, ")\n",
             "----------------------\n")


class Line():
    def __init__(self, checkpoint1, checkpoint2, color, width):
        self .checkpoint1 = checkpoint1
        self.checkpoint2 = checkpoint2
        self.color = color
        self.width = width
    def display(self):
        pygame.draw.line(screen, self.color, self.checkpoint1, self.checkpoint2, self.width)
        
class Button:
    def __init__(self):
        pass

class Person:
    def __init__(self, x, y, group):
        self.group = group
        self.tooClose = 0
    def countClosePersons(self, distanceLimit):
        self.tooClose = 0
        for person in personList:
            if abs(math.dist([person.x, person.y], [self.x, self.y])) >= 5:
                print("too close")
                self.tooClose+=1
        
        
    

ORANGE  = ( 255, 140, 0)
ROT     = ( 255, 0, 0)
GRUEN   = ( 0, 255, 0)
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)
BLAU = (0, 0, 255)
GELB = (255, 255, 0)
LILA = (127, 0, 255)



screensize = (width,height)=(1000,1000)
screen = pygame.display.set_mode(screensize)
#surface = pygame.Surface(screensize)
pygame.display.set_caption("Brandschutzplaner")

clock = pygame.time.Clock()
clock.tick(10)


#font used for the text
myfont = pygame.font.SysFont('Comic Sans MS', 20)

screen.fill(WEISS)
        
def drawGrid(scale, margin):
    for column in range(43):
        for row in range(43):
            rect = pygame.Rect(margin+(row*scale)+row*margin, column*scale+column*margin+margin, scale,  scale)
            pygame.draw.rect(screen, SCHWARZ, rect)
drawGrid(20, 3.2)
    



modeButton = Area(50, 27, 161, 68, ROT)
modeButton.display()

pointBuffer = (None, None)
point = (None, None)

checkpointList = []
checkpointPath = []
areaList = []
Floor = []

SelectedGroup = False
groupList = []

modes = [("drawCheckpoint", ROT), ("drawArea", GRUEN), ("drawFloor", BLAU), ("drawPath", GELB)]
modeIndex = 0



spielaktiv = True

# Schleife Hauptprogramm
while spielaktiv:
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spielaktiv = False
            print("Spieler hat Quit-Button angeklickt")
            
        #------------------------check Mousecklick and safe mouse position---------------------------------- 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            #print(pos)
            #if changeModeButton was cklicked: switch to next mode
            if pos[0] <= 161 >= 50 and pos[1] <= 69 >= 27:
                if modeIndex == len(modes)-1:
                    modeIndex = 0
                    
                else:
                    modeIndex += 1
                #print("changed Mode to: " + modes[modeIndex][0])
                
                modeButton = Area(50, 27, 161, 68, modes[modeIndex][1])
                modeButton.display()
            #------------------------drawCheckpoints----------------------------------  
            elif modeIndex == 0:
                newCheckpoint = Checkpoint(pos[0], pos[1], 10, len(checkpointList))
                checkpointList.append(newCheckpoint)
                print("new checkpoint at position: ", (checkpointList[-1].x, checkpointList[-1].y))
                
                newCheckpoint.display()
                modeButton = Area(50, 27, 161, 68, modes[modeIndex][1])
                
                
                
            #------------------------draw Areas----------------------------------------- 
            elif modeIndex == 1:
                if pointBuffer != (None, None):
                    newArea = Area(pointBuffer[0], pointBuffer[1], pos[0], pos[1], modes[modeIndex][1])
                    newArea.display()
                    areaList.append(newArea)
                    pointBuffer=(None, None)
                else:
                    pointBuffer = pos
                    
                    
                    
             #------------------------drawFloors----------------------------------------   
            elif modeIndex == 2:
                if pointBuffer != (None, None):
                    newArea = Area(pointBuffer[0], pointBuffer[1], pos[0], pos[1], modes[modeIndex][1])
                    newArea.display()
                    pointBuffer=(None, None)
                else:
                    pointBuffer = pos
                    
                    
                    
            #-----------choose start area draw Lines chose end area-----------------------    
            elif modeIndex == 3:
                #check if startArea was chosen already-------------
                if SelectedGroup == False:
                        selectedArea = False
                        for area in areaList:
                            if area.isClicked(pos[0], pos[1]):
                                print("area is selected")
                                newGroup = Group(input("Please write the name of the group: "))
                                area.displayText(newGroup.name)
                                newGroup.setStartArea(area) 
                                SelectedGroup = newGroup
                                selectedArea = True
                                break
                                
                        if selectedArea == False:
                            print("couldn't select area")
                else:
                    checkpointClicked = False
                    #else(if Area was Checked): check if checkpoint was checked 
                    for checkpoint in checkpointList:
                        if checkpoint.x-10 <= pos[0] <= checkpoint.x+10 and checkpoint.y-10 <= pos[1] <= checkpoint.y+10:
                            print("checkpoint: ", checkpoint.x, checkpoint.y)
                            SelectedGroup.addToCheckpointRoute(checkpoint)
                            if pointBuffer != (None, None):
                                newLine = Line(pointBuffer, (checkpoint.x, checkpoint.y), GELB, 5)
                                newLine.display()
                                pointBuffer=(None, None)


                            pointBuffer = (checkpoint.x, checkpoint.y)
                            #print("pointBuffer: ", checkpoint)
                                
                            checkpointClicked = True
                            
                            break
                                
                    #if no checkpoint was clicked: check if endArea was Clicked
                        print("test1")
                    if checkpointClicked == False:
                        print("test2")
                        i = 0
                        for area in areaList:
                            i+=1
                            if area.isClicked(pos[0], pos[1]) and area != SelectedGroup.startArea:
                                print("endArea is selected")
                                SelectedGroup.setEndArea(area)
                                pointBuffer = (None, None)
                                area.displayText(str("Sammelplatz für " + str(SelectedGroup.name)))

                                SelectedGroup.printRoute()                                
                                groupList.append(SelectedGroup)
                                SelectedGroup = False
                                break
                            else:
                                print("no endearea selected")
                    else:
                        print("test3")
                                    
            
    # Spiellogik hier integrieren
    #Area = Area(50, 27, 161, 68, "q1", ORANGE)
    #Area.display()
    # Spielfeld löschen>
    #screen.fill(ORANGE)

    # Spielfeld/figuren zeichnen
    #drawGrid(20, 3.2)

    # Fenster aktualisieren
    pygame.display.flip()

    # Refresh-Zeiten festlegen
    clock.tick(60)
pygame.quit()
