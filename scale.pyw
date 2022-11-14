import sys
from enum import Enum
import PySimpleGUI as sg
import win32gui

class ColorScheme(Enum):
    DEFAULT = 1
    DARK = 2
    LIGHT = 3

def create_window():
    layout = [[sg.Graph(canvas_size=(1920/1.25, 1080/1.25),
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
    return window

def draw_line(graph, coords_start, coords_end, color_scheme = ColorScheme.DEFAULT):
    if color_scheme == ColorScheme.DEFAULT:
        graph.DrawLine(coords_start, coords_end, color='black', width=3)
        graph.DrawLine(coords_start, coords_end, color='white', width=1)
    if color_scheme == ColorScheme.LIGHT:
        graph.DrawLine(coords_start, coords_end, color='white', width=2)
    if color_scheme == ColorScheme.DARK:
        graph.DrawLine(coords_start, coords_end, color='black', width=2)


def draw_text(graph, coords, text, font=10, color_scheme = ColorScheme.DEFAULT):
    if color_scheme == ColorScheme.DEFAULT:
        graph.DrawText(str(text), (coords[0] - 0.1, coords[1] - 0.1), font=("Arial", font), color='black')
        graph.DrawText(str(text), (coords[0], coords[1]), font=("Arial", font), color='white')
    if color_scheme == ColorScheme.LIGHT:
        graph.DrawText(str(text), coords, font=("Arial", font), color='white')
    if color_scheme == ColorScheme.DARK:
        graph.DrawText(str(text), coords, font=("Arial", font), color='black')


def create_distancemeter_segment(graph, coords, distance):
    x = coords[0]
    y = coords[1]
    x_shift = 3.6
    y_shift = 7
    distance_multiplier = 30/distance
    draw_line(graph, (x, y), (x, y - y_shift * distance_multiplier))
    draw_line(graph, (x, y), (x + x_shift * distance_multiplier, y))
    draw_text(graph, (x, y - y_shift * distance_multiplier - 1), distance)


def create_distance_meter(window):
    graph = window['graph']
    draw_text(graph, (45, 65), 'compare lines with wall height or width')
    create_distancemeter_segment(graph, (41, 62), 10)
    create_distancemeter_segment(graph, (42, 61), 20)
    create_distancemeter_segment(graph, (43, 60), 30)
    create_distancemeter_segment(graph, (44, 59), 40)
    create_distancemeter_segment(graph, (45, 58), 50)
    create_distancemeter_segment(graph, (46, 57), 60)
    create_distancemeter_segment(graph, (47, 56), 70)
    create_distancemeter_segment(graph, (48, 55), 80)


def draw_vertical_scale(window):
    graph = window['graph']
    for y_shift in range (0, 40, 1):
        if y_shift == 0: continue
        if y_shift % 5 == 0:
            draw_line(graph, (50 - 0.3, 50 - y_shift), (50 - 0.5, 50 - y_shift))
            draw_line(graph, (50 + 0.3, 50 - y_shift), (50 + 0.5, 50 - y_shift))
            draw_text(graph, (51.5 - 0.1, 50 - y_shift - 0.1), y_shift/5)
        draw_line(graph, (50 - 0.1, 50 - y_shift), (50 + 0.1, 50 - y_shift))
    draw_text(graph, (55, 22), 'relative scale')
    draw_text(graph, (55, 20), 'step = 0.2')

def bind_relatedscale_with_distance(window, related_coords, distance):
    x0 = 50 - 0.3 - 0.2
    y0 = 50
    draw_line(window['graph'], (x0, y0 - (related_coords*10)/2), (x0 - 1, y0 - (related_coords*10)/2))
    draw_text(window['graph'], (x0 - 2, y0 - (related_coords*10)/2), f'{distance}m')

def draw_distance_marks(window, rocket_type):
    if rocket_type == '-hvr':
        draw_text(window['graph'], (30, 30), 'sight alignment for', 12)
        draw_text(window['graph'], (30, 27), 'high velicity rocket', 18)
        bind_relatedscale_with_distance(window, 0.2, '>100')
    elif rocket_type == '-ir':
        draw_text(window['graph'], (30, 30), 'sight alignment for', 12)
        draw_text(window['graph'], (30, 27), 'incedinary rocket', 18)
        bind_relatedscale_with_distance(window, 0.4, 10)
        bind_relatedscale_with_distance(window, 1.2, 20)
        bind_relatedscale_with_distance(window, 1.8, 30)
        bind_relatedscale_with_distance(window, 2.6, 40)
        bind_relatedscale_with_distance(window, 3.2, 50)
        bind_relatedscale_with_distance(window, 4, 60)
        bind_relatedscale_with_distance(window, 4.8, 70)
        bind_relatedscale_with_distance(window, 5.6, 80)
        bind_relatedscale_with_distance(window, 6.6, 90)
        bind_relatedscale_with_distance(window, 7.6, 100)
    elif rocket_type == '-er':
        draw_text(window['graph'], (30, 30), 'sight alignment for', 12)
        draw_text(window['graph'], (30, 27), 'explosive rocket', 18)
        bind_relatedscale_with_distance(window, 0.4, 10)
        bind_relatedscale_with_distance(window, 0.8, 20)
        bind_relatedscale_with_distance(window, 1.6, 30)
        bind_relatedscale_with_distance(window, 2.2, 40)
        bind_relatedscale_with_distance(window, 3, 50)
        bind_relatedscale_with_distance(window, 3.6, 60)
        bind_relatedscale_with_distance(window, 4.8, 70)
        bind_relatedscale_with_distance(window, 5.8, 80)
        bind_relatedscale_with_distance(window, 6.6, 90)
        bind_relatedscale_with_distance(window, 7.4, 100)

def set_focus_onrust():
    whnd = win32gui.FindWindowEx(None, None, None, 'Rust')
    if not whnd:
        return
    win32gui.SetForegroundWindow(whnd)

def main():

    window = create_window()
    create_distance_meter(window)
    draw_vertical_scale(window)

    rocket_type = sys.argv[1]
    draw_distance_marks(window, rocket_type)
    set_focus_onrust()


    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

if __name__ == '__main__':
    main()

# color_scheme = sys.argv[1] #default, dark, light
# if color_scheme not in ['default', 'dark', 'light']:
#     raise Exception("Invalid 2nd arg. Acceptable values: default, dark, light")




