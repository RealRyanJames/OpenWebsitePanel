class WelcomePage:
    def __init__(self, load: bool, x: float, y: float):
        self.onLoad = load
        self.x = x
        self.y = y

    def isLoaded(self) -> bool:
        return self.onLoad

    def pos_x(self) -> float:
        return self.x * 2

    def pos_y(self) -> float:
        return self.y + 10