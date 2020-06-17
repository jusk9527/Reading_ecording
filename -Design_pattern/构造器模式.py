# 有一天我们发现工厂模式很死，你交个东西给他，他只能造出标准的东西
# 比如我们需要买台戴尔的电脑，这个时候他总不能给你台标准的电脑吧
# 应为我们要自己需要的cpu,显卡等，这个时候工厂模式无法满足我们，直接用构造器模式
# 构造器模式相比工厂模式优秀的一点是他可以定制，按你要求造成你需要的东西


# 假设你需要买一台新电脑。如果你决定买预先配置好的电脑，例如最新的Apple 1.4Ghz Mac mini，你使用的是工厂模式。
# 所有硬件规格都已经由厂商预定义了，厂家不用问你也知道该干什么。厂商通常只会收到一条指令
# 你是给制造商（builder）下发个人定制电脑的经理人

class HardworeEngineer():
    """
    制造商
    """
    def __init__(self):
        self.bulder = None

    def construct_computer(self,hdd=None,memory=None,gpu=None):
        self.bulder = ComputerBuild()
        self.bulder.computer_Meorty(memory)
        self.bulder.computer_Hard(hdd)
        self.bulder.computer_Georty(gpu)

    @property
    def computer(self):
        return self.bulder.computer

class ComputerBuild():
    """
    电脑工厂
    """
    def __init__(self):
        self.computer = Computer()
    def computer_Meorty(self, Memory):
        self.computer.Memory = Memory

    def computer_Hard(self, Hard_Disk):
        self.computer.Hard_Disk = Hard_Disk

    def computer_Georty(self,Graphics_Card):
        self.computer.Graphics_Card = Graphics_Card

class Computer():
    """
    电脑
    """
    def __init__(self):
        self.Memory = None
        self.Hard_Disk = None
        self.Graphics_Card = None

    def __str__(self):
        infor = ("Memory: {}".format(self.Memory),
                 "Hard Disk: {}".format(self.Hard_Disk),
                 "Graphics Card: {}".format(self.Graphics_Card))

        return "\n".join(infor)





engineer = HardworeEngineer()
engineer.construct_computer(hdd=500, memory=8, gpu='GeForce GTX 650 Ti')
computer = engineer.computer
print(computer)


# Memory: 8
# Hard Disk: 500
# Graphics Card: GeForce GTX 650 Ti