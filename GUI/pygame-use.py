import pygame

def main():
    # init pygame module
    python.init()
    # init display window and set window size
    screen = pygame.diplay.set_mode(800, 600)
    # set window title
    pygame.display.set_caption('big ball eat little ball')
    running = True

    # start a loop to do event
    while running:
        # get even from message queue and deal it
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running= False

if __name__ == '__main__':
    main()
