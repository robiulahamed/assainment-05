class CPU:
    def execute(self):
        return "Executing instructions"


class RAM:
    def read(self):
        return "Reading data from RAM"
    
    def write(self):
        return "Writing data to RAM"


class HardDrive:
    def read(self):
        return "Reading data from Hard Drive"
    
    def write(self):
        return "Writing data to Hard Drive"


class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.ram = RAM()
        self.hard_drive = HardDrive()
    
    def boot(self):
        return "Booting up the computer"



computer = Computer()
print(computer.boot())
print(computer.cpu.execute())
print(computer.ram.read())
print(computer.hard_drive.write())
