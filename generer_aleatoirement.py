import sys
import os
from random import randint
from MainUser import LARGEUR, HAUTEUR

TAILLE_SEQUENCE = 14
GLOBAL_FOLDER = "generated_csv"
SPACE_BETWEEN_TARGETS = 15

def generateNameFolder(number_of_targets, size_of_targets):
    name_folder = f"{GLOBAL_FOLDER}/partie_{number_of_targets}_{size_of_targets}"
    if not os.path.exists(GLOBAL_FOLDER):
        os.mkdir(GLOBAL_FOLDER)
    if not os.path.exists(name_folder):
        os.mkdir(name_folder)
    return name_folder

def generateTargetsRandomly(number_of_targets, size_of_targets):
    targets = []

    while len(targets) < number_of_targets:
        size = size_of_targets

        x = randint(size, LARGEUR - size)
        y = randint(size, HAUTEUR - size)

        valid = True
        for target in targets:
            other_x, other_y, other_size = target
            distance = ((x - other_x)**2 + (y - other_y)**2)**0.5
            if distance < (size + other_size) / 2 + SPACE_BETWEEN_TARGETS:
                valid = False
                break

        if valid:
            targets.append((x, y, size))

    return targets

def exportTargetsAsCSV(folderName, targets):
    with open(f"{folderName}/targets.csv", "w") as file:
        for x, y, size in targets:
            file.write(f"{x},{y},{size}\n")

def generateSequenceRandomly(targets):
    sequence = []
    copy_targets = [False for _ in targets]

    while len(sequence) < TAILLE_SEQUENCE:
        index = randint(0, len(targets) - 1)
        if not copy_targets[index]:
            copy_targets[index] = True
            sequence.append(index)

    return sequence

def exportSequenceAsCSV(folderName, sequence):
    with open(f"{folderName}/sequence.csv", "w") as file:
        for index in sequence:
            file.write(f"{index}\n")

def main():
    if len(sys.argv) != 3:
        print("Usage: python generer_aleatoirement.py <number_of_targets> <size_of_targets>")
        sys.exit(1)

    number_of_targets = int(sys.argv[1])
    size_of_targets = int(sys.argv[2])

    folderName = generateNameFolder(number_of_targets, size_of_targets)

    targets = generateTargetsRandomly(number_of_targets, size_of_targets)
    exportTargetsAsCSV(folderName, targets)

    sequence = generateSequenceRandomly(targets)
    exportSequenceAsCSV(folderName, sequence)

if __name__ == "__main__":
    main()