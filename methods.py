import pygame
import random
import tkinter as tk
from tkinter import messagebox


def drawGrid(w, rows, surface):
    # Draw initial grid in the game window with indicated "w" width and rows.
    size_btwn = w//rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + size_btwn
        y = y + size_btwn

        pygame.draw.line(surface, (0, 0, 0), (x, 0), (x, w))
        pygame.draw.line(surface, (0, 0, 0), (0, y), (w, y))


def redrawWindow(surface, width, rows, snack, s):
    # Draws game window each time positions change.

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
