import os
import numpy as np
from PIL import Image, ImageChops
im1 = Image.open(
    "C:\\Users\\user\\Documents\\Etudes\\L3TDSI\\Khadim_Sauvegarde\\Programmation\\Python\\cryptohack\\general\\xor\\img\\lemur.png")
im2 = Image.open(
    "C:\\Users\\user\\Documents\\Etudes\\L3TDSI\\Khadim_Sauvegarde\\Programmation\\Python\\cryptohack\\general\\xor\\img\\flag.png")
print(os.getcwd())

result = ImageChops.logical_xor(im1, im2)
result.save('C:\\Users\\user\\Documents\\Etudes\\L3TDSI\\Khadim_Sauvegarde\\Programmation\\Python\\cryptohack\\general\\xor\\img\\result.png')
