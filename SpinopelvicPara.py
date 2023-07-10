import PySimpleGUI as sg
import math
# sg.theme('BlueMono')
sg.theme_background_color('lightgray')
sg.theme_text_color('black')

# Define the layout
#   +-----------------------------------------------------------------------------------+
# 1 |              Sitting X-ray                            Standing X-ray              |
# 2 |                                         |                                         |
# 3 |                                         |                                         |
# 4 |                                         |                                         |
# 5 |                                         |                                         |
# 6 |                                         |                                         |
# 7 |                                         |                                         |
# 8 |                                         |                                         |
# 9 |                                         |                                         |
# 10|                                         |                                         |
# 11|                                         |                                         |
# 12|                                         |                                         |
# 13+-----------------------------------------+-----------------------------------------+
# 14|+------------------+ +------------------+ +------------------+ +------------------+|
# 15||Load Sitting X-ray| |Spinopelvic Parame| |Load StandingX-ray| |Spinopelvic Parame||
# 16|+------------------+ +------------------+ +------------------+ +------------------+|
# 17|+---------+---------+---------+---------+ +---------+---------+---------+---------+|
# 18||   SS    |   PT    |   PI    |   LL    | |   SS    |   PT    |   PI    |   LL    ||
# 19|+---------+---------+---------+---------+ +---------+---------+---------+---------+|
# 20||         |         |         |         | |         |         |         |         ||
# 21|+---------+---------+---------+---------+ +---------+---------+---------+---------+|
# 22|          +-------------------+                                                    |
# 23|          |Stiffness Parameter|                                Stiff & Deformity   |
# 24|          +-------------------+                                     _______        |
# 25|+---------+---------+---------+---------+                    Normal/       \Stiff  |
# 26||   Sacral Slope    | (PI-LL) standing  | +-------------------+   /_________\      |
# 27|+---------+---------+---------+---------+ |Stiffness Parameter| NA|_________|Deform|
# 28||                   |                   | +-------------------+   \         /      |
# 29|+---------+---------+---------+---------+                          \_______/       |
#   +-----------------------------------------+-----------------------------------------+

# 1: Label
# 2-13: Graph
# 14-16: Button
# 17-21: Table
# 22-24: Button
# 25-29: Table
# [Stiffness Parameter]: Button
# [Stiff & Deformity]: Label
# [       _______        ]
# [Normal/       \Stiff  ]
# [     /_________\      ]
# [   NA|_________|Deform]
# [     \         /      ]
# [      \_______/       ]: Knob

KNOB_RADIUS = 53
KNOB_CENTER = (102, 67)
KNOB_COLOR = 'white'
MARKER_COLOR = 'gray'
image_filename = 'image.png'

def calculate_knob_value(x, y):
    dx = x - KNOB_CENTER[0]
    dy = KNOB_CENTER[1] - y  # Invert y-axis because GUI coordinates are flipped
    angle = math.atan2(dy, dx)
    value = (angle + math.pi) / (2 * math.pi)  # Normalize the angle to [0, 1]
    return value

layout = [
    [   
        [sg.Text("Sitting X-ray", size=(54, 1), justification='center', background_color='lightgray', text_color='black')],
        [sg.Graph((459, 476), (0, 0), (459, 476), key='-graph1-', background_color='white')],
        [sg.Button("Load Sitting X-ray", size=(26, 2), button_color=('black on white')), sg.Button("Spinopelvic Parameters", size=(26, 2))],
        [
            sg.Table(
                [['', '', '', '']],
                headings=['SS', 'PT', 'PI', 'LL'],
                justification='center',
                num_rows=1,
                col_widths=[12, 12, 12, 12],
                auto_size_columns=False,
                key='-table1-',                
                background_color='white'
            )
        ],
        [sg.Text("", size=(54, 2), justification='center', background_color='lightgray')],
        [sg.Button("Stiffness Parameter", size=(54, 2))],
        [
            sg.Table(
                [['', '']],
                headings=['Sacral Slope', '(PL - LL) Standing'],
                justification='center',
                num_rows=1,
                col_widths=[24, 24],
                auto_size_columns=False,
                key='-table1-',                
                background_color='white'
            )
        ]
    ],
    [
        [sg.Text("Stiff & Deformity", size=(54, 1), justification='center', background_color='lightgray', text_color='black')],
        [sg.Graph((459, 476), (0, 0), (459, 476), key='-graph2-', background_color='white')],
        [sg.Button("Load Sitting X-ray", size=(26, 2), button_color=('black on white')), sg.Button("Spinopelvic Parameters", size=(26, 2))],
        [
            sg.Table(
                [['', '', '', '']],
                headings=['SS', 'PT', 'PI', 'LL'],
                justification='center',
                num_rows=1,
                col_widths=[12, 12, 12, 12],
                auto_size_columns=False,
                key='-table1-',                
                background_color='white'
            )
        ],
        [
            sg.Button("New Patient", size=(20, 2), button_color=('white on red'), pad = (15, 15)),
            sg.Graph((247, 170), (0, 0), (247, 200), background_color='lightgray', key='-knob-', enable_events=True)
        ],
        [sg.Text("Stffness | Alignment", size=(48, 1), justification='right', background_color='lightgray', text_color='black')],
    ],
]

column_layout = [
    [sg.Button("AutomaticSpinopelvicParametersMenu", size=(30, 1), button_color='black')],
    [
        sg.Column(layout[0], vertical_alignment='top', pad=(0, 0), element_justification='left'),
        sg.Column(layout[1], vertical_alignment='top', pad=(0, 0), element_justification='left')
    ]
]

# Create the window
window = sg.Window("GUI Example", column_layout, size= (961, 868))

knob = window['-knob-']

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == '-knob-':
        x, y = values['-knob-']
        if math.sqrt((x - KNOB_CENTER[0]) ** 2 + (y - KNOB_CENTER[1]) ** 2) <= KNOB_RADIUS:
            knob_value = calculate_knob_value(x, y)
        else:
            # Limit the knob value within the valid range
            dx = x - KNOB_CENTER[0]
            dy = y - KNOB_CENTER[1]
            angle = math.atan2(dy, dx)
            knob_value = (angle + math.pi) / (2 * math.pi)
    
    # Clear the knob and redraw the knob
    knob.erase()
    knob.draw_image(image_filename, location=(0, 170))
    knob.draw_circle(KNOB_CENTER, KNOB_RADIUS, fill_color=KNOB_COLOR, line_color=KNOB_COLOR)
    
    # Draw the marker based on the current knob value
    marker_angle = knob_value * 2 * math.pi - math.pi
    marker_x = KNOB_CENTER[0] + int(math.cos(marker_angle) * KNOB_RADIUS * 0.8)
    marker_y = KNOB_CENTER[1] - int(math.sin(marker_angle) * KNOB_RADIUS * 0.8)
    knob.draw_line(KNOB_CENTER, (marker_x, marker_y), color=MARKER_COLOR, width=5)

# Close the window
window.close()
