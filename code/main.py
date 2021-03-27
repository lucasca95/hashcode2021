import pdb

class Street():
    def __init__(self, *args, **kwargs):
        self.name = ""
        self.light = False
        self.time = 0
    def __str__(self,):
        return f"Street {self.name} with traffic_light {self.light}"

class Car():    
    def __init__(self, *args, **kwargs):
        self.id = -1
        self.c_streets_total = 0
        self.c_streets_done = 0
        self.streets_path = []
    def __str__(self,):
        return f"Car {self.id} with path {self.streets_path}"

class Intersection():
    def __init__(self, *args, **kwargs):
        self.id = []
        self.in_streets = []
        self.out_streets = []

    def __str__(self,):
        return f"Intersection {self.id} with\nIN_Steets {self.in_streets}\nOUT_Streets {self.out_streets}"

class City():
    def __init__(self, *args, **kwargs):
        self.intersections = []
        self.streets = []
        self.cars = []
        self.duration = 0
        self.bonus_points = 0
    
    def __str__(self):
        msg = f"City: {self.duration}\n"
        msg += 'Cars: '
        return msg + str(self.cars)
    
    def load_simulation(self):
        f = open('a.in', "r")
        line = f.readline()[:-1].split()
        self.duration = int(line[0])
        #
        c_intersections = int(line[1])
        # cargar intersecciones incompletas porque se completan cuando se cargan las calles
        for inter in range(c_intersections):
            intersection = Intersection()
            intersection.id = inter
            self.intersections.append(intersection)
        #
        c_streets = int(line[2])
        #
        c_cars = int(line[3])

        for s in range(c_streets):
            line = f.readline()[:-1].split()
            inter_from = int(line[0])
            inter_to = int(line[1])
            street_name = line[2]
            street_time = int(line[3])

            # asociar intersecciones con calles
            # REVISAR SI NO HAY QUE AGREGAR LA CALLE ENTERA
            inter1 = self.intersections[inter_from]
            inter1.out_streets.append(street_name)
            inter2 = self.intersections[inter_to]
            inter2.in_streets.append(street_name)

            street = Street()
            street.name = street_name
            street.time = street_time
            self.streets.append(street)
            # pdb.set_trace()

        car_i = 0
        for c in range(c_cars):
            car = Car()
            line = f.readline()[:-1].split()
            c_streets_total = int(line[0])

            expected_time = 0
            # Load streets for the car
            car.c_streets_total = c_streets_total
            for i in range(1, c_streets_total):
                street_name = line[i]
                car.streets_path.append(street_name)
                for s in self.streets:
                    if(street_name == s.name):
                        expected_time += s.time
                        # pdb.set_trace()

            # If it's impossible to achieve the goal for this car, i don't count it. THIS IS WRONG 'cause
            # one of these cars can be bothering another one on a street queue
            # if (expected_time < self.duration):
            car.id = car_i
            car_i += 1
            self.cars.append(car)

        # print('Data loaded!')

    def start_simulation(self,):
        while (self.duration >=0 ) and (input('Next step?\t ENTER to continue; "n" to quit ') != 'n'):
            print(self.duration)

            for inter in self.intersections:
                street_more_charged = ''
                max_c_cars = -1
                # por cada calle que entra
                for in_street in inter.in_streets:
                    c_cars = 0
                    # cuento los autos que tengo esperando 
                    for car in self.cars:
                        if (in_street == car.streets_path[0])
                            c_cars += 1
                    if (c_cars >= max_c_cars)
                        max_c_cars = c_cars
                        street_more_charged = in_street
            
            for inter in self.intersections:
                for in_street in inter.in_streets:
                    if (in_street.name == street_more_charged):
                        in_street.light = True
                    else:
                        sin_street.light = False

            
            self.duration -= 1
            continue

def main():
    city = City()
    city.load_simulation()
    city.start_simulation()

if __name__ == '__main__':
    main()