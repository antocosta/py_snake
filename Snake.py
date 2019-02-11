import random
import pygame
import tkinter as tk
from tkinter import messagebox
import classes
import initializers



def drawGrid(w, rows, surface):
    # Draw initial grid in the game window with indicated "w" width and rows.
    sizeBtwn = w//rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (0, 0, 0), (x, 0), (x, w))
        pygame.draw.line(surface, (0, 0, 0), (0, y), (w, y))

def redrawWindow(surface, width, rows, snack, s):
    # Draws game window each time positions change.
    #global rows, width, s, snack
    surface.fill((0, 0, 0))
    s.draw(surface)
    snack.draw(surface)
    drawGrid(width, rows, surface)
    pygame.display.update()

def randomSnack(rows, item):
    # Places food inside game window in a random position.
    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
            continue
        else:
            break
    return (x,y)

def nessage_box(subject, content):
    # Creates message box with game is lost with input "subject" and "content".
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass

def main():

    win = pygame.display.set_mode((initializers.rows, initializers.width))
    s = classes.snake((255, 0, 0), (10, 10))
    snack = classes.cube(randomSnack(initializers.rows, s), color=(0, 255, 0))
    flag = True

    clock = pygame.time.Clock()

    print("Width = " + str(initializers.width))
    print("rows = " + str(initializers.rows))

    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        s.move()
        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = classes.cube(randomSnack(initializers.rows, s), color=(0, 255, 0))

        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z:z.pos,s.body[x+1:])):
                print("Score: ", len(s.body))
                nessage_box("You Lost!!!", "Please, try again...")
                s.reset((10, 10))
                break

        redrawWindow(win, initializers.width, initializers.rows, snack, s)

main()