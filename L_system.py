import pygame
import sys 

class Rule:
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Var:
    def __init__(self, name):
        self.name = name
    def rule(self, left, right):
        rule = Rule(left, right)
        self.rule = rule
    def getRule(self):
        return self.rule.right


F = Var("F")
G = Var("G")
F.rule("F", "F+G")
G.rule("G", "F-G")
variables = [ F, G ]
axiom = "F"
sequence = axiom
n = 10
x = 700
y = 340
delay = 2
i = 0
direction = "right"
distance = 5


'''
F = Var("F")
F.rule("F", "F+F−F−F+F")
variables = [ F ]
axiom = "F"
sequence = axiom
n = 6
x = 0
y = 850
delay = 3
i = 0
direction = "right"
distance = 3
'''

#ability to apply a rule to a variable
#func(variable)
#   returns rHand side from that variables rule

def applyRule(variable):
    for var in variables:
        if var.name == variable:
            return var.getRule()
    return None

def isVar(character):
    for var in variables:
        if var.name == character:
            return True
    return False

for i in range(n-1):
    newSeq = ""
    for char in sequence:
        if isVar(char):
            newSeq += applyRule(char)
        else:
            newSeq += char
    sequence = newSeq

print(sequence)


pygame.init()
screen = pygame.display.set_mode((1440, 900))
screen.fill((255, 255, 255))  # White background

# ==== Cellular Automaton Setup (Rule 90) ====
def next_gen(cells):
    return [cells[i-1] ^ cells[i+1] if 0 < i < len(cells)-1 else 0 for i in range(len(cells))]

ca_width = 128
cell_size = 6
ca_cells = [0] * ca_width
ca_cells[ca_width // 2] = 1
ca_gens = [ca_cells[:]]  # Save generations

for _ in range(80):
    ca_cells = next_gen(ca_cells)
    ca_gens.append(ca_cells[:])

# ==== Animation Loop ====
clock = pygame.time.Clock()
x, y = 512, 500
angle = 90
stack = []


# Draw a line
#surface, color, startPos, endPos, lineWidth

#starting position in the middle 
#x,y

for char in sequence:
    if char == "F" or char == "G":
        #draw current direction
        if direction == "up":
            y2 = y-distance
            pygame.draw.line(screen, (0, 0, 255), (x,y), (x, y2), 1)
            y = y2
            pygame.display.flip()
            pygame.time.delay(delay)
        elif direction == "left":
            x2 = x - distance
            pygame.draw.line(screen, (0, 0, 255), (x,y), (x2, y), 1)
            x = x2
            pygame.display.flip()
            pygame.time.delay(delay)
        elif direction == "down":
            y2 = y + distance
            pygame.draw.line(screen, (0, 0, 255), (x,y), (x, y2), 1)
            y = y2
            pygame.display.flip()
            pygame.time.delay(delay)
        elif direction == "right":
            x2 = x + distance
            pygame.draw.line(screen, (0,0,255), (x,y), (x2, y), 1)
            x = x2
            pygame.display.flip()
            pygame.time.delay(delay)
    elif char == "+":
        #update orientation
        if direction == "up":
            direction = "left"
        elif direction == "left":
            direction = "down"
        elif direction == "down":
            direction = "right"
        else:
            direction = "up"
    else:
        if direction == "up":
            direction = "right"
        elif direction == "right":
            direction = "down"
        elif direction == "down":
            direction = "left"
        else:
            direction = "up"

# Draw CA at the bottom
for row, gen in enumerate(ca_gens):
    for col, cell in enumerate(gen):
        color = (0, 0, 0) if cell else (255, 255, 255)
        pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))
    pygame.display.flip()
    pygame.time.delay(30)

# Reset for L-system drawing
x, y = 512, 500
angle = 90
for char in sequence:
    if char == "F" or char == "G":
        #draw current direction
        if direction == "up":
            y2 = y-distance
            pygame.draw.line(screen, (0, 0, 255), (x,y), (x, y2), 1)
            y = y2
            pygame.display.flip()
            pygame.time.delay(delay)
        elif direction == "left":
            x2 = x - distance
            pygame.draw.line(screen, (0, 0, 255), (x,y), (x2, y), 1)
            x = x2
            pygame.display.flip()
            pygame.time.delay(delay)
        elif direction == "down":
            y2 = y + distance
            pygame.draw.line(screen, (0, 0, 255), (x,y), (x, y2), 1)
            y = y2
            pygame.display.flip()
            pygame.time.delay(delay)
        elif direction == "right":
            x2 = x + distance
            pygame.draw.line(screen, (0,0,255), (x,y), (x2, y), 1)
            x = x2
            pygame.display.flip()
            pygame.time.delay(delay)
    elif char == "+":
        #update orientation
        if direction == "up":
            direction = "left"
        elif direction == "left":
            direction = "down"
        elif direction == "down":
            direction = "right"
        else:
            direction = "up"
    else:
        if direction == "up":
            direction = "right"
        elif direction == "right":
            direction = "down"
        elif direction == "down":
            direction = "left"
        else:
            direction = "up"

pygame.time.wait(3000)  # Display for 3 seconds
pygame.quit()


pygame.time.wait(3000)
pygame.quit()