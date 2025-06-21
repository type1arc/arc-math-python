from math import *
import os
import time
import cmath

class Vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

        v = (x, y, z)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        return (self.x + other.x, self.y + other.y, self.z + other.z);

    def normalize(self):
        return (self.x / abs(self.x), self.y / abs(self.y), self.z / abs(self.z))
        raise TypeError("[ERROR] invalid value: Vec3 component cannot be 0.")

    def dot(self, other):
        if isinstance(other, Vec3):
            return self.x * other.x + self.y * other.y + self.z * other.z
        raise TypeError("[ERROR] type mismatch: not a Vec3 argument")

class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        v = (x, y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return (self.x + other.x, self.y + other.y);

    def normalize(self):
        return (self.x / abs(self.x), self.y / abs(self.y))
        raise TypeError("[ERROR] invalid value: Vec3 component cannot be 0.")

    def dot(self, other):
        if isinstance(other, Vec3):
            return self.x * other.x + self.y * other.y
        raise TypeError("[ERROR] type mismatch: not a Vec3 argument")

class Matrix:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.data = [[0 for _ in range(col)] for _ in range(row)]

        for n in range(min(row, col)):
            self.data[n][n] = 1

    def mprint(self):
        for row in self.data:
            print(' '.join(map(str, row)))

    def transpose(self):
        transposed_data = [[self.data[j][i] for j in range(self.row)] for i in range(self.col)]
        transposed = Matrix(self.col, self.row)
        transposed.data = transposed_data

        return transposed

IOTA = cmath.sqrt(-1)
class complex_number:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        self.val = real + IOTA * imaginary

    def cprint(self):
        print( f"({self.real}, {self.imaginary} i)")

    def abs(self) -> float:
        return sqrt(self.real ** 2 + self.imaginary ** 2)

    def conjugate(self):
        self.imaginary *= -1;
        return complex_number(self.real, self.imaginary)

    def add(self, other):
        return complex_number(self.real + other.real, self.imaginary + other.imaginary)

    def substract(self, other):
        return complex_number(self.real - other.real, self.imaginary - other.imaginary)

def clear():
    os.system("cls")
pass

def draw():
    for y in range(100):
        for x in range(100):
            text = "x" if x == y else "#"
            print(text, end="")
        print()


def main() -> None:
    print("[ENTRY POINT]")

    mat = Matrix(3, 3)
    mat.mprint()
    print(" ")
    mat.transpose()
    mat.mprint()

    val = complex_number(1, 1)
    val.cprint()
    val.conjugate()
    val.cprint()

pass

if __name__ == "__main__":
    main()
