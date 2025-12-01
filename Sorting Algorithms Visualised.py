import pygame
import random
import time

pygame.init()

WIDTH = 800
HEIGHT = 600
BAR_WIDTH = WIDTH // 100

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Algorithm Visualization")

font = pygame.font.SysFont("Arial", 20)

COMPARISONS = 0
shouldExit = False


def drawBars(arr, highlightIndices=[], comparisons=0):
    screen.fill((0, 0, 0))
    for i, height in enumerate(arr):
        color = (0, 255, 155)
        if i in highlightIndices:
            color = (255, 0, 0)
        pygame.draw.rect(screen, color, (i * BAR_WIDTH, HEIGHT - height * 5, BAR_WIDTH - 1, height * 5))

    counterText = font.render(f"Comparisons: {comparisons}", True, (255, 255, 255))
    screen.blit(counterText, (10, 10))

    pygame.display.flip()


def checkForExit():
    global shouldExit
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            shouldExit = True

def bubbleSort(arr):
    global COMPARISONS, shouldExit
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            checkForExit()
            if shouldExit:
                return

            COMPARISONS += 1
            drawBars(arr, [j, j + 1], COMPARISONS)
            pygame.event.pump()

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                drawBars(arr, [j, j + 1], COMPARISONS)
            pygame.time.delay(10)
    drawBars(arr, comparisons=COMPARISONS)


def selectionSort(arr):
    global COMPARISONS, shouldExit
    n = len(arr)
    for i in range(n):
        minIdx = i
        for j in range(i + 1, n):
            checkForExit()
            if shouldExit:
                return

            COMPARISONS += 1
            drawBars(arr, [i, j], COMPARISONS)
            pygame.event.pump()

            pygame.time.delay(20)
            if arr[j] < arr[minIdx]:
                minIdx = j
        arr[i], arr[minIdx] = arr[minIdx], arr[i]
        drawBars(arr, [i, minIdx], COMPARISONS)
        pygame.time.delay(20)
    drawBars(arr, comparisons=COMPARISONS)


def mergeSort(arr, left=0, right=None):
    global COMPARISONS, shouldExit
    if right is None:
        right = len(arr) - 1

    if left < right:
        mid = (left + right) // 2

        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)

        merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    global COMPARISONS, shouldExit
    leftHalf = arr[left:mid + 1]
    rightHalf = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len(leftHalf) and j < len(rightHalf):
        checkForExit()
        if shouldExit:
            return

        COMPARISONS += 1
        drawBars(arr, [left + i, mid + 1 + j], comparisons=COMPARISONS)
        pygame.event.pump()

        pygame.time.delay(20)

        if leftHalf[i] <= rightHalf[j]:
            arr[k] = leftHalf[i]
            i += 1
        else:
            arr[k] = rightHalf[j]
            j += 1
        k += 1

    while i < len(leftHalf):
        checkForExit()
        if shouldExit:
            return

        drawBars(arr, [left + i], comparisons=COMPARISONS)
        pygame.event.pump()
        pygame.time.delay(20)
        arr[k] = leftHalf[i]
        i += 1
        k += 1

    while j < len(rightHalf):
        checkForExit()
        if shouldExit:
            return

        drawBars(arr, [mid + 1 + j], comparisons=COMPARISONS)
        pygame.event.pump()
        pygame.time.delay(20)
        arr[k] = rightHalf[j]
        j += 1
        k += 1

    drawBars(arr, comparisons=COMPARISONS)
    pygame.time.delay(20)


def bogoSort(arr):      # joke
    global COMPARISONS, shouldExit

    repeat = True
    while repeat:
        checkForExit()
        if shouldExit:
            return

        repeat = False
        for x in range(0, len(arr) - 1):
            COMPARISONS += 1
            if arr[x] > arr[x + 1]:
                repeat = True
                break

        drawBars(arr, [], COMPARISONS)
        pygame.event.pump()
        pygame.time.delay(10)

        if repeat:
            arr = random.sample(arr, len(arr))  # shuffle the array

def stalinSort(arr):      # joke
    global COMPARISONS, shouldExit

    pointer = 1
    while pointer < len(arr):
        checkForExit()
        if shouldExit:
            return

        if arr[pointer] < arr[pointer - 1]:
            arr.pop(pointer)
            COMPARISONS += 1
        else:
            pointer += 1

        drawBars(arr, [pointer, pointer - 1], COMPARISONS)
        pygame.event.pump()
        pygame.time.delay(10)

    drawBars(arr, comparisons=COMPARISONS)


def main():
    global COMPARISONS, shouldExit
    running = True
    arr = list(range(1, 101))
    algorithm = bubbleSort

    while running:
        screen.fill((0, 0, 0))
        drawBars(arr, comparisons=COMPARISONS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    algorithm = bubbleSort
                elif event.key == pygame.K_s:
                    algorithm = selectionSort
                elif event.key == pygame.K_m:
                    algorithm = mergeSort
                elif event.key == pygame.K_o:
                    algorithm = bogoSort
                elif event.key == pygame.K_t:
                    algorithm = stalinSort
                elif event.key == pygame.K_SPACE:
                    # reset the comparison counter and start sorting
                    COMPARISONS = 0
                    arr = random.sample(range(1, 101), 100)  # list of 100 unique heights
                    drawBars(arr, comparisons=COMPARISONS)
                    shouldExit = False  # reset exit flag
                    pygame.time.wait(500)
                    algorithm(arr)
                elif event.key == pygame.K_q:
                    shouldExit = True
                    running = False

        if shouldExit:
            break

        pygame.display.update()

if __name__ == "__main__":
    main()
    pygame.quit()