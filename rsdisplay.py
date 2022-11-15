import sys
import time
import PySimpleGUI as sg
import win32gui
from projectStructures import ColorScheme, RocketTypeArg
import multiprocessing

class RocketSight:

    def __init__(self, rocket_type=RocketTypeArg.EXP):
        self.window = None
        self.graph = None
        self.create_window()
        self.create_distance_meter()
        self.draw_vertical_scale()
        self.draw_distance_marks(rocket_type)
        self.set_focus_onrust()

    def create_window(self):
        layout = [[sg.Graph(canvas_size=(int(1920/1.25), int(1080/1.25)),
                            graph_bottom_left=(0, 0),
                            graph_top_right=(100, 100),
                            background_color='grey', key='graph')]]

        window = sg.Window('Rocket sight alignment app',
                           layout,
                           keep_on_top=True,
                           auto_size_buttons=False,
                           grab_anywhere=False,
                           no_titlebar=True,
                           return_keyboard_events=False,
                           alpha_channel=0.6,
                           use_default_focus=False,
                           transparent_color='grey',
                           finalize=True)
        window.move(-15, -8)
        self.window = window
        self.graph = window['graph']

    def draw_line(self, coords_start, coords_end, color_scheme = ColorScheme.DEFAULT):
        if color_scheme == ColorScheme.DEFAULT:
            self.graph.DrawLine(coords_start, coords_end, color='black', width=3)
            self.graph.DrawLine(coords_start, coords_end, color='white', width=1)
        if color_scheme == ColorScheme.LIGHT:
            self.graph.DrawLine(coords_start, coords_end, color='white', width=2)
        if color_scheme == ColorScheme.DARK:
            self.graph.DrawLine(coords_start, coords_end, color='black', width=2)

    def draw_text(self, coords, text, font=10, color_scheme = ColorScheme.DEFAULT):
        if color_scheme == ColorScheme.DEFAULT:
            self.graph.DrawText(str(text), (coords[0] - 0.1, coords[1] - 0.1), font=("Arial", font), color='black')
            self.graph.DrawText(str(text), (coords[0], coords[1]), font=("Arial", font), color='white')
        if color_scheme == ColorScheme.LIGHT:
            self.graph.DrawText(str(text), coords, font=("Arial", font), color='white')
        if color_scheme == ColorScheme.DARK:
            self.graph.DrawText(str(text), coords, font=("Arial", font), color='black')

    def create_distancemeter_segment(self, coords, distance):
        x = coords[0]
        y = coords[1]
        x_shift = 3.6
        y_shift = 7
        distance_multiplier = 30/distance
        self.draw_line((x, y), (x, y - y_shift * distance_multiplier))
        self.draw_line((x, y), (x + x_shift * distance_multiplier, y))
        self.draw_text((x, y - y_shift * distance_multiplier - 1), distance)

    def create_distance_meter(self):
        self.draw_text((45, 65), 'compare lines with wall height or width')
        self.create_distancemeter_segment((41, 62), 10)
        self.create_distancemeter_segment((42, 61), 20)
        self.create_distancemeter_segment((43, 60), 30)
        self.create_distancemeter_segment((44, 59), 40)
        self.create_distancemeter_segment((45, 58), 50)
        self.create_distancemeter_segment((46, 57), 60)
        self.create_distancemeter_segment((47, 56), 70)
        self.create_distancemeter_segment((48, 55), 80)

    def draw_vertical_scale(self):
        for y_shift in range (0, 40, 1):
            if y_shift == 0: continue
            if y_shift % 5 == 0:
                self.draw_line((50 - 0.3, 50 - y_shift), (50 - 0.5, 50 - y_shift))
                self.draw_line((50 + 0.3, 50 - y_shift), (50 + 0.5, 50 - y_shift))
                self.draw_text((51.5 - 0.1, 50 - y_shift - 0.1), y_shift/5)
            self.draw_line((50 - 0.1, 50 - y_shift), (50 + 0.1, 50 - y_shift))
        self.draw_text((55, 22), 'relative scale')
        self.draw_text((55, 20), 'step = 0.2')

    def bind_relatedscale_with_distance(self, related_coords, distance):
        x0 = 50 - 0.3 - 0.2
        y0 = 50
        self.draw_line((x0, y0 - (related_coords*10)/2), (x0 - 1, y0 - (related_coords*10)/2))
        self.draw_text((x0 - 2, y0 - (related_coords*10)/2), f'{distance}m')

    def draw_distance_marks(self, rocket_type):
        if rocket_type == '-hvr':
            self.draw_text((30, 30), 'sight alignment for', 12)
            self.draw_text((30, 27), 'high velicity rocket', 18)
            self.bind_relatedscale_with_distance(0.2, '>100')
        elif rocket_type == '-ir':
            self.draw_text((30, 30), 'sight alignment for', 12)
            self.draw_text((30, 27), 'incendiary rocket', 18)
            self.bind_relatedscale_with_distance(0.4, 10)
            self.bind_relatedscale_with_distance(1.2, 20)
            self.bind_relatedscale_with_distance(1.8, 30)
            self.bind_relatedscale_with_distance(2.6, 40)
            self.bind_relatedscale_with_distance(3.2, 50)
            self.bind_relatedscale_with_distance(4, 60)
            self.bind_relatedscale_with_distance(4.8, 70)
            self.bind_relatedscale_with_distance(5.6, 80)
            self.bind_relatedscale_with_distance(6.6, 90)
            self.bind_relatedscale_with_distance(7.6, 100)
        elif rocket_type == '-er':
            self.draw_text((30, 30), 'sight alignment for', 12)
            self.draw_text((30, 27), 'explosive rocket', 18)
            self.bind_relatedscale_with_distance(0.4, 10)
            self.bind_relatedscale_with_distance(0.8, 20)
            self.bind_relatedscale_with_distance(1.6, 30)
            self.bind_relatedscale_with_distance(2.2, 40)
            self.bind_relatedscale_with_distance(3, 50)
            self.bind_relatedscale_with_distance(3.6, 60)
            self.bind_relatedscale_with_distance(4.8, 70)
            self.bind_relatedscale_with_distance(5.8, 80)
            self.bind_relatedscale_with_distance(6.6, 90)
            self.bind_relatedscale_with_distance(7.4, 100)

    def set_focus_onrust(self):
        whnd = win32gui.FindWindowEx(None, None, None, 'Rust')
        if not whnd:
            return
        win32gui.SetForegroundWindow(whnd)

    def read(self):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                break

    #  подпроцесс
    def display_rocket_sight(rocket_type):
        rsight = RocketSight(rocket_type)  # создаем прицел
        rsight.read()  # начинаем чтение событий чтобы окно отобразилось

    def run_subprocess(rocket_type):
        proc = multiprocessing.Process(target=RocketSight.display_rocket_sight, args=(rocket_type,))
        proc.start()
        return proc


# для прямого теста
if __name__ == '__main__':
    RocketSight.run_subprocess(RocketTypeArg.EXP)



