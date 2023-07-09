class Shape:

    shapes = {'Square', 'Rectangle', 'Circle', 'Ellipse'}
    colours = {'Black', 'White', 'Red', 'Green', 'Yellow',
               'Blue', 'Brown', 'Orange', 'Pink', 'Purple',
               'Grey'}

    def __init__(self, name, colour, corner_count):
        self.verify_name(name)
        self.verify_colour(colour)
        self.verify_count_of_corners(corner_count)

        self.name = name
        self.colour = colour
        self.corner_count = corner_count

    @classmethod
    def verify_name(cls, name):
        if type(name) != str:
            raise TypeError('Имя должно быть строкой!')
        if name not in cls.shapes:
            raise AttributeError('Неправильное имя фигуры!')

    @classmethod
    def verify_colour(cls, colour):
        if type(colour) != str:
            raise TypeError('Цвет должен быть строкой!')
        if colour not in cls.colours:
            raise AttributeError('Неправильное название цвета!')

    @classmethod
    def verify_count_of_corners(cls, count):
        if type(count) != int:
            raise TypeError('Количество углов должно быть целым числом!')


data = [
    ['Rectangle', 'White', 5], ['Rectangle', 'Green', 4], ['Rectangle', 'Red', 4],
    ['Rectangle', 'Black', 4], ['Square', 'Green', 4], ['Square', 'Purple', 4],
    ['Square', 'Pink', 4], ['Square', 'Grey', 4], ['Circle', 'Red', 0],
    ['Circle', 'Black', 0], ['Circle', 'White', 0], ['Circle', 'Pink', 0],
    ['Ellipse', 'Blue', 0], ['Ellipse', 'Green', 0], ['Ellipse', 'Grey', 0], ['Ellipse', 'Yellow', 0]
        ]

list_of_shapes = []

c = 0

for l in data:
    list_of_shapes.append(Shape(l[0], l[1], l[2]))


def query(n=None, col=None, count=None):

    q = []
    counter = 0

    for i in list_of_shapes:
        if i.name == n or n is None:
            counter += 1
        if i.colour == col or col is None:
            counter += 1
        if i.corner_count == count or count is None:
            counter += 1

        if counter == 3:
            q.append(i)
            counter = 0
        else:
            counter = 0

    for x in q:
        print(x.__dict__)

print('-----------')
query(col='White')
print('-----------\n')

print('-----------')
query(col='Black')
print('-----------\n')

print('-----------')
query(col='Orange')
print('-----------\n')