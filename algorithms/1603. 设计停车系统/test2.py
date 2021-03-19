class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parking_space = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.parking_space[carType-1] == 0:
            return False

        self.parking_space[carType-1] -= 1
        return True

    def leaveCar(self, carType: int) -> bool:
        '''
        车子离开车位
        '''
        if self.parking_space[carType-1] == 0:
            return False

        self.parking_space[carType-1] += 1
        return True

    def addCarCompatible(self, carType: int) ->bool:
        '''
        允许小车停在大车车位中
        '''
        # carType -= 1
        for x in range(carType, 0, -1):
            if self.parking_space[carType-1] != 0:
                self.parking_space[carType-1] -= 1
                return True
        return False

# Your ParkingSystem object will be instantiated and called as such:
big = 1
medium = 2
small = 3
carType = 1
obj = ParkingSystem(big, medium, small)
param_1 = obj.addCarCompatible(carType)
param_2 = obj.addCar(carType)
print(param_1, param_2)
