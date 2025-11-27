import cv2
import random
import numpy as np
import time

class Bar():
    def __init__(self, value):
        self.value = value

    def getValue(self):
        return(self.value)

    def draw(self, window, xPosition):
        window = cv2.line(window, (xPosition, 10), (xPosition, 10 + self.value*4),(0,255,150), thickness=2)
        return(window)

    def __str__(self):
        return(str(self.getValue()))


import pygame

playSound = False

def swapBars(barList, indexOne, indexTwo):
    barList[indexOne], barList[indexTwo] = barList[indexTwo], barList[indexOne]

    if playSound:
        try:
            filePath = "C:\\...\\bloop.mp3"

            pygame.mixer.init()
            pygame.mixer.music.load(filePath)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(20)
        except:
            print("\rerror: .mp3 file not found", end="", flush=True)

    return barList


barList = []

for x in range(1,101):
    newBar = Bar(x)
    barList.append(newBar)

random.shuffle(barList)

image = np.zeros((500, 500, 3), dtype=np.uint8)


print("Choose a sorting algorithm:")
print("1: Bubble Sort")
print("2: Selection Sort")
print("3: Bogo Sort (Joke)")
print("4: Stalin Sort (Joke)")
print("5: Gnome Sort (Joke)")
choice = int(input("Enter the number corresponding to your choice: "))

if choice not in [1,2,3,4,5]:
    print("invalid choice, defaulting to bubble")
    choice = 1


sorted = False

while not sorted:
    image.fill(0)   # clear the old bars

    # sorting algos:

    # bubble sort
    if choice == 1:
        for index, bar in enumerate(barList):
            if bar.getValue() > barList[index+1].getValue():
                #barList[index], barList[index+1] = barList[index+1], barList[index] # swap em
                swapBars(barList, index, index+1)
                break

    # selection sort
    if choice == 2:
        for i in range(len(barList) - 1):
            minIndex = i
            for j in range(i + 1, len(barList)):
                if barList[j].getValue() < barList[minIndex].getValue():
                    minIndex = j
            if minIndex != i:
                #barList[i], barList[minIndex] = barList[minIndex], barList[i]   # swap em
                swapBars(barList, i, minIndex)
                break

    #bogoSort (joke)
    if choice == 3:
        random.shuffle(barList)

    # stalin sort (joke)
    if choice == 4:
        for index, bar in enumerate(barList):
            if bar.getValue() > barList[index+1].getValue():
                barList.pop(index)
                break

    # gnome sort (v similiar to bubble sort (also kinda a joke))
    if choice == 5:
        index = 0
        while index < len(barList):
            if index == 0 or barList[index-1].getValue() <= barList[index].getValue():
                index += 1
            else:
                #barList[index], barList[index-1] = barList[index-1], barList[index]  # swap em
                swapBars(barList, index, index-1)
                index -= 1
                break


    # end sorting algos

    # draw bars
    for index, bar in enumerate(barList):
        image = bar.draw(image, index * 5)

    image = cv2.flip(image,0)
    cv2.imshow("", image)

    # early quit out
    if cv2.waitKey(1) == ord("q"):
        break

    # check if sorted
    sorted = True
    for x in range(len(barList)-1):
        if barList[x].getValue() > barList[x+1].getValue():
            sorted = False

    # the delay of switches is deterined by the sound (ik its bad but thats what locks flow)
    # if no sound plays, this delay prevents flow instead
    time.sleep(0.01)
    if sorted:
        time.sleep(3)

cv2.destroyAllWindows()
if pygame.mixer:
    pygame.mixer.quit()
