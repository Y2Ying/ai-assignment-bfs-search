import math
import tkinter as tk

# Translation : Graph coordinate to UI coordinate
coordinates = {
    0: {
        0: (50, 75),
        1: (50, 125),
        2: (50, 175),
        3: (50, 225),
        4: (50, 275),
        5: (50, 325)
        0: (95, 50),
        1: (95, 100),
        2: (95, 150),
        3: (95, 200),
        4: (95, 250),
        5: (95, 300),
    },
    2: {
        0: (140, 75),
        1: (140, 125),
        2: (140, 175),
        3: (140, 225),
        4: (140, 275),
        5: (140, 325)
    },
    3: {
        0: (185, 50),
        1: (185, 100),
        2: (185, 150),
        3: (185, 200),
        4: (185, 250),
        5: (185, 300)
    },
    4: {
        0: (230, 75),
        1: (230, 125),
        2: (230, 175),
        3: (230, 225),
        4: (230, 275),
        5: (230, 325)
    },
    5: {
        0: (275, 50),
        1: (275, 100),
        2: (275, 150),
        3: (275, 200),
        4: (275, 250),
        5: (275, 300)
    },
    6: {
        0: (320, 75),
        1: (320, 125),
        2: (320, 175),
        3: (320, 225),
        4: (320, 275),
        5: (320, 325)
    },
    7: {
        0: (365, 50),
        1: (365, 100),
        2: (365, 150),
        3: (365, 200),
        4: (365, 250),
        5: (365, 300)
    },
    8: {
        0: (410, 75),
        1: (410, 125),
        2: (410, 175),
        3: (410, 225),
        4: (410, 275),
        5: (410, 325)
    },
    9: {
        0: (455, 50),
        1: (455, 100),
        2: (455, 150),
        3: (455, 200),
        4: (455, 250),
        5: (455, 300)
    }
}

def draw_hexagon(canvas, x, y):
    size = 30
    points = []
    for i in range(6):
        angle_deg = 60 * i
        angle_rad = math.radians(angle_deg)
        point_x = x + size * math.cos(angle_rad)
        point_y = y + size * math.sin(angle_rad)
        points.append((point_x, point_y))

    canvas.create_polygon(points, outline="black", fill="#F9D89B")

def draw_legend(canvas, x, y, color):
    size = 20
    points = []
    for i in range(6):
        angle_deg = 60 * i
        angle_rad = math.radians(angle_deg)
        point_x = x + size * math.cos(angle_rad)
        point_y = y + size * math.sin(angle_rad)
        points.append((point_x, point_y))

    return canvas.create_polygon(points, outline="black", fill=color)

def draw_TrapText(canvas, x, y, text):
    canvas.create_text(x, y, text=text, font=("Arial", 5, "bold"), fill="black")
    
def draw_RewardText(canvas, x, y, text):
    canvas.create_text(x, y, text=text, font=("Arial", 4, "bold"), fill="black")
    
# Create the main window
window = tk.Tk()
window.title("Breadth First Search Algorithm")

# Create a canvas widget
canvas = tk.Canvas(window, width=800, height=500, background="#AAE8AA")
canvas.pack()

# Print the hexagonal map
def printMap():
    for i in range(5):
        for j in range(6):
            draw_hexagon(canvas, 50 + (90 * i), 75 + (50 * j))

    for i in range(5):
        for j in range(6):
            draw_hexagon(canvas, 95 + (90 * i), 50 + (50 * j))

printMap()

# Print legend and virtual world
treasure1 = draw_legend(canvas, 185, 250, "orange")
treasure2 = draw_legend(canvas, 230, 125, "orange")
treasure3 = draw_legend(canvas, 365, 200, "orange")
treasure4 = draw_legend(canvas, 455, 200, "orange")

obstacle1 = draw_legend(canvas, 50, 225, "grey")
obstacle2 = draw_legend(canvas, 140, 175, "grey")
obstacle3 = draw_legend(canvas, 185, 200, "grey")
obstacle4 = draw_legend(canvas, 230, 175, "grey")
obstacle5 = draw_legend(canvas, 230, 275, "grey")
obstacle6 = draw_legend(canvas, 320, 225, "grey")
obstacle7 = draw_legend(canvas, 320, 275, "grey")
obstacle8 = draw_legend(canvas, 365, 250, "grey")
obstacle9 = draw_legend(canvas, 410, 125, "grey")

trap1 = draw_legend(canvas, 410, 175, "#F99DF9")
draw_TrapText(canvas, 410, 175, "Trap 1")
trap2 = draw_legend(canvas, 95, 100, "#F99DF9")
draw_TrapText(canvas, 95, 100, "Trap 2")
trap3 = draw_legend(canvas, 140, 275, "#F99DF9")
draw_TrapText(canvas, 140, 275, "Trap 2")
trap4 = draw_legend(canvas, 275, 200, "#F99DF9")
draw_TrapText(canvas, 275, 200, "Trap 3")
trap5 = draw_legend(canvas, 320, 125, "#F99DF9")
draw_TrapText(canvas, 320, 125, "Trap 3")
trap6 = draw_legend(canvas, 185, 100, "#F99DF9")
draw_TrapText(canvas, 185, 100, "Trap 4")

reward1 = draw_legend(canvas, 95, 200, "#4EEB4E")
draw_RewardText(canvas, 95, 200, "Reward 1")
reward2 = draw_legend(canvas, 230, 75, "#4EEB4E")
draw_RewardText(canvas, 230, 75, "Reward 1")
reward3 = draw_legend(canvas, 275, 300, "#4EEB4E")
draw_RewardText(canvas, 275, 300, "Reward 2")
reward4 = draw_legend(canvas, 365, 150, "#4EEB4E")
draw_RewardText(canvas, 365, 150, "Reward 2")

window.mainloop()