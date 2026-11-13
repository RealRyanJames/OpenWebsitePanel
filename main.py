import webbrowser
from tkinter import Tk, Label, Button, Text
from Pages.WelcomePages import WelcomePage

running = True

class PadPos:
    def __init__(self, x: float, y: float):
        self.x = x * 5
        self.y = y * 3

    def GetX(self) -> float:
        return self.x

    def GetY(self) -> float:
        return self.y

    def GetGeo(self) -> str:
        return f"{self.x}x{self.y}"

fontSize = (10 + 4) + 5

r = Tk()


while running:

        l = Label(
            text="Welcome to Multi Tool",
            font=("sans-serif", fontSize - 4, "bold"),
            padx=30,
            pady=20
        )

        window2 = PadPos(100, 100)
        text = Text(r, height=-15, width=40, padx=10, pady=10, font=("sans-serif", 14 - 2))
        lbl = Label(r, text="Enter Site to Visit",

        font = ("sans-serif", fontSize - 4, "bold"),
        padx = 30,
        pady = 20
        )


        lbl.pack()
        text.pack()

        welcome = WelcomePage(True, 10, 30)

        if welcome.isLoaded():
            def openWebsite() -> None:
                webbrowser.open(url=str(text.get("1.0", "end")))

            r.geometry(window2.GetGeo())
            b2 = Button(r, text="Open Website", command=openWebsite)
            b2.config(bg="black", fg="white", pady=7, padx=80)
            b2.pack(side="bottom", anchor="n")
            r.mainloop()