import pygame
import classes
import methods
import initializers


def main():
    win = pygame.display.set_mode((initializers.width, initializers.width))
    s = classes.snake((255, 0, 0), (10, 10))
    snack = classes.cube(methods.randomSnack(initializers.rows, s), color=(0, 255, 0))

    clock = pygame.time.Clock()

    while True:
        pygame.time.delay(initializers.timedisplay)
        clock.tick(initializers.clocktick)
        s.move()
        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = classes.cube(methods.randomSnack(initializers.rows, s), color=(0, 255, 0))

        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z:z.pos,s.body[x+1:])):
                print("Score: ", len(s.body))
                methods.nessage_box(initializers.loss_message)
                s.reset((10, 10))
                break
        methods.redrawWindow(win, initializers.width, initializers.rows, snack, s)


main()