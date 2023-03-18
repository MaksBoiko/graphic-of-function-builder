import math
import mpmath
import os

class Graphic:
    def __init__(self, x, y, points):
        self.x = x
        self.y = y
        self.points = points
        self.expr = ""
        self.graphic_arr = []
        self.pow = lambda x, degree: math.pow(x, degree)
        self.root = lambda x, root_of: x ** (1 / root_of)
        self.factorial = lambda x: math.factorial(x)
        self.log = lambda x, base: math.log(x, base)
        self.exp = lambda x: math.e ** x
        self.tan = lambda x: math.tan(math.degrees(x))
        self.sin = lambda x: math.sin(math.degrees(x))
        self.cos = lambda x: math.cos(math.degrees(x))
        self.cot = lambda x: mpmath.cot(math.degrees(x))
        for row in range(self.y):
            for col in range(self.x):
                self.graphic_arr.append(" ")

    def help(self):
        print("This program can draw graphics of functions what were given.")
        print("Rules of assignment functions: ")
        print("1. Never use another names of variables except 'x'")
        print("2. Operators what you can use: +(addition), -(subtraction),")
        print("*(multiplication), /(division), **(exponentiation),")
        print(" %(modulo), //(division without remainder)")
        print("3. Description of functions what you can use: ")
        print("pow(x, degree) - calculate degree of x;")
        print("root(x, root_of)  - calculate root of x;")
        print("log(x, base) - calculate logarithm of x with given base;")
        print("factorial(x) - calculate factorial of x;")
        print("exp(x) - calculate exponent of x;")
        print("sin(x), cos(x), tan(x), cot(x) - can calculate sinus,")
        print("cosinus, tangens, cotangens of x respectively.")
        print("What do those symbol on graphics mean?")
        print("@ - point, * - point of graphic, # - point on point of graphic")

    def append(self, el, index):
        new_str = ""
        for i in range(len(self.graphic_arr)):
            if i == index:
                new_str += str(el)
            else:
                new_str += self.graphic_arr[i]
        return new_str

    def fill_data_arr(self):
        data_arr_y = []
        data_arr_x = []
        result = ""
        print("You can enter 'help' if you dont know how to use this program")
        self.expr = input("f(x) = ")

        for x in range(1, self.x):
            eval_variables = {'x': x, 'root': self.root, 'pow': self.pow, 'factorial': self.factorial, 'log': self.log, 'exp': self.exp, 'sin': self.sin, 'cos': self.cos, 'tan': self.tan, 'cot': self.cot}
            if self.expr == "help":
                self.help()
                self.expr = input("f(x) = ")
            try:
                result = int(eval(self.expr, eval_variables))
            except (NameError, SyntaxError) as e:
                print("What you enter is not expression or don't exist among predefined functions!\nSource: ", e)
                os.abort()
            except ZeroDivisionError as e:
                print("You committed division by zero!\nSource", e)
                os.abort()

            data_arr_y.append(result)

            data_arr_x.append(x)

        return data_arr_x, data_arr_y

    def insert_gaps_y(self, num, full_width):
        gap = " "
        gaps = (full_width-len(num))*gap
        return gaps

    def insert_gaps_x(self):
        gap = " "
        line = " "
        for i in range(self.x):
            i += 1
            gaps = (3 - len(str(i))) * gap
            line += str(i)+gaps

        return line

    def create_points_index_arr(self):
        points_arr_x = []
        points_arr_y = []
        points_index_arr = []
        for i in range(len(self.points)):
            el = self.points[i]
            points_arr_x.append(el[0])
            points_arr_y.append(el[1]+1)
        # invert y coordinate
        for j in range(len(points_arr_y)):
            points_arr_y[j] = self.y - points_arr_y[j] + 1
        # coordinates x and y to index
        for j in range(len(points_arr_y)):
            point_index = (self.y * points_arr_y[j] - 1) - (self.y - points_arr_x[j])
            points_index_arr.append(point_index)
        return points_index_arr

    def create_index_arr(self, arr_x, arr_y):
        index_arr = []
        # invert y coordinate
        for j in range(len(arr_y)):
             arr_y[j] = len(arr_y) - arr_y[j] + 1
        # coordinates x and y to index
        for j in range(len(arr_y)):
            index = (self.y * arr_y[j]-1) - (self.y - arr_x[j])
            index_arr.append(index)

        return index_arr

    def print(self, data_arr_x, data_arr_y):
        points_index_arr = self.create_points_index_arr()
        index_arr = self.create_index_arr(data_arr_x, data_arr_y)

        for i in range(len(points_index_arr)):
            self.graphic_arr = self.append("@", int(points_index_arr[i]))

        for i in range(len(index_arr)):
            self.graphic_arr = self.append("*", int(index_arr[i]))

        for j in range(len(points_index_arr)):
            for i in range(len(self.graphic_arr)):
                if(self.graphic_arr[i] == "*" and points_index_arr[j] == i):
                    self.graphic_arr = self.append("#", i)



        index = 0
        print("     ", '^')
        print("     ", 'Y')
        for row in range(self.y-1):
            print(self.y-row-1, self.insert_gaps_y(str(self.y-row-1), 4), "|> ", end="")
            for col in range(self.x):
                print(self.graphic_arr[index]+"  ", end="")
                index += 1
            print()
        print("      0", "_|_"*self.x, 'X >')
        print("       ", self.insert_gaps_x())
        print("f(x) =", self.expr)

points = [[]]
x_or_y = "x"
element = 0
index = 0

while True:

    print("Enter", x_or_y, " coordinate element ", element+1, " or 'x' for exit")

    enter = input()

    if (enter == "x"):
        points.pop()
        os.system('cls')
        break
    if (x_or_y == "x"):
        points[element].append(int(enter))
        x_or_y = "y"
    elif (x_or_y == "y"):
        points[element].append(int(enter))
        x_or_y = "x"
        element += 1
        points.append([])

    print(points)


graphic = Graphic(10, 10, points)

data_arr_x, data_arr_y = graphic.fill_data_arr()
graphic.print(data_arr_x, data_arr_y)
