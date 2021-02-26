# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np

class GeneralInfo:

    def __init__(self, info):
        self.durationSimulation = info[0]
        self.numberIntersections = info[1]
        self.numberStreets = info[2]
        self.numberCars = info[3]
        self.bonusPoints = info[4]

    def __str__(self):
        return f'Simulation: {self.durationSimulation}s\nIntersections: {self.numberIntersections}\nStreets: {self.numberStreets}\nCars: {self.numberCars}\nBonus points: {self.bonusPoints}'

class Street:

    start = 0
    end = 0
    name = ''
    timeLength = 0
    intersection = None

    def __str__(self):
        return f'Length {self.timeLength}'
        #return f'{self.name} starts at {self.start}, ends at {self.end} with a duration of {self.timeLength}s\n'

class Car:

    numberStreetsToTravel = 0
    streets = []
    cost = 0

    def __str__(self):
        return f'Car with cost: {self.cost}'

def read_input(filename):

    with open(filename) as reader:
        generalInfo = GeneralInfo([int(num) for num in reader.readline().rstrip('\n').split(' ')])

        streets = {}

        for i in range(generalInfo.numberStreets):
            line = reader.readline().rstrip('\n').split(' ')

            street = Street()
            street.start = int(line[0])
            street.end = int(line[1])
            street.name = line[2]
            street.timeLength = int(line[3])

            streets[street.name] = street

        cars = []

        for i in range(generalInfo.numberCars):
            line = reader.readline().rstrip('\n').split(' ')
            car = Car()
            car.numberStreetsToTravel = line[0]
            car.streets = line[1:]

            for street in car.streets[1:]:
                car.cost += streets[street].timeLength

            cars.append(car)

        return generalInfo, streets, cars

def create_graph(streets):

    graph = {}

    for key, street in streets.items():
        if street.end not in graph:
            graph[street.end] = [street.name]
        else:
            graph[street.end].append(street.name)

    for key, intersection in graph.items():
        for street in intersection:
            streets[street].intersection = key

    return graph

def create_output(filename, generalInfo, intersections):

    with open(filename+'.out', 'w') as writer:
        writer.write(str(generalInfo.numberIntersections)+'\n')

        for i in range(generalInfo.numberIntersections):
            writer.write(str(i)+'\n')
            writer.write(str(len(intersections[i]))+'\n')

            for street in intersections[i]:
                writer.write(street + ' 1'+'\n')

def create_output_optimize(filename, generalInfo, streets, cars, intersections):

    schedule = {}
    count_intersections = {}
    count_streets = {}

    for car in cars:

        for street in car.streets[:-1]:
            count_streets[street] = count_streets.get(street, 0) + 1
            street = streets[street]

            if street.intersection not in schedule:
                schedule[street.intersection] = set()
            schedule[street.intersection].add(street.name)
            count_intersections[street.intersection] = count_intersections.get(street.intersection, 0) + 1

    with open(filename+'2.out', 'w') as writer:
        writer.write(str(len(schedule))+'\n')

        for intersection, items in schedule.items():
            writer.write(str(intersection) + '\n')
            writer.write(str(len(items)) + '\n')
            streets_aux = []
            for item in items:
                streets_aux.append(streets[item])

            streets_aux.sort(key=lambda x: x.timeLength)

            for item in streets_aux:
                writer.write(item.name + ' 640\n')

if __name__ == '__main__':

    filenames = ['a', 'b', 'c', 'd', 'e', 'f']

    for filename in filenames:

        generalInfo, streets, cars = read_input(filename+'.txt')

        cars.sort(key=lambda x: x.cost)

        intersections = create_graph(streets)

        #create_output(filename, generalInfo, intersections)
        create_output_optimize(filename, generalInfo, streets, cars, intersections)
