To run the background image must be properly sourced

To do this, download the image file from github and save it to the same directory as the pygame code

Go to line 10

Change it to
background = pygame.image.load('filepath/filepath/filename.png')
Swapping filepath and filename as appropriate, include the full filepath

The game will then run