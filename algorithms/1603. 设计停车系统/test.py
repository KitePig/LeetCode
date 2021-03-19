class ParkingSystem:
    parking_space = [[] for _ in range(3)]
    def __init__(self, big: int, medium: int, small: int):
        self.parking_space[0] = [0] * big
        self.parking_space[1] = [0] * medium
        self.parking_space[2] = [0] * small

    def addCar(self, carType: int) -> bool:
        for i, x in enumerate(self.parking_space[carType-1]):
            if x == 0:
                self.parking_space[carType-1][i] = 1
                return True

        return False
        
# Your ParkingSystem object will be instantiated and called as such:
big = 1
medium = 2
small = 3
carType = 1
obj = ParkingSystem(big, medium, small)
param_1 = obj.addCar(carType)
param_2 = obj.addCar(carType)
print(param_1, param_2)
