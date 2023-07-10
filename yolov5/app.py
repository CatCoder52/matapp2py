import PySimpleGUI as sg

class SpinopelvicPara:
    def __init__(self):
        # Properties that correspond to app components
        self.UIFigure = sg.Window('SpinopelvicPara', layout=[
            [sg.Menu([['Automatic Spinopelvic Parameters'], ['Menu']])],
            [sg.Button('New Patient')],
            [sg.Text('PILL standing:'), sg.Text(''), sg.Text('Sacral slope:'), sg.Text('')],
            [sg.Text('LL:'), sg.Text(''), sg.Text('PI:'), sg.Text(''), sg.Text('PT:'), sg.Text(''), sg.Text('SS:'), sg.Text('')],
            [sg.Text('Stiffness Alignment'), sg.DiscreteSlider(range=(0, 10), default_value=5, orientation='h', size=(10, 20)),
             sg.Text('')],
            [sg.Table(values=[], headings=[], key='UITable_stand')],
            [sg.Button('Stand Spinopelvic Parameters')],
            [sg.Button('Load Standing Xray')],
            [sg.Table(values=[], headings=[], key='UITable_stiffness')],
            [sg.Button('Stiffness Parameters')],
            [sg.Table(values=[], headings=[], key='UITable')],
            [sg.Button('Spinopelvic Parameters')],
            [sg.Button('Load Sitting Xray')],
            [sg.Canvas(size=(400, 400), key='canvas_standing'), sg.Canvas(size=(400, 400), key='canvas_sitting')]
        ])
        
        # Global parameters
        self.fileLoc = ''
        self.pathloc = ''
        self.sizeloc = ''
        self.imageloc = ''
        self.imgnameloc = ''
        self.maxszloc = ''
        self.paraloc = ''
        self.fileLoc2 = ''
        self.pathloc2 = ''
        self.sizeloc2 = ''
        self.imageloc2 = ''
        self.imgnameloc2 = ''
        self.maxszloc2 = ''
        self.paraloc2 = ''
        self.StiffVarloc = ''

    # Callbacks that handle component events
    def run(self):
        while True:
            event, values = self.UIFigure.read()
            if event == sg.WINDOW_CLOSED:
                break

            # Button pushed function: LoadSittingXrayButton
            if event == 'Load Sitting Xray':
                # import sitting X-ray image
                ext = '*.png'
                folder = './IntellijointData'
                filename, path = sg.Window('Load Sitting Xray', layout=[
                    [sg.Text('Select a file to open')],
                    [sg.Input(key='filename'), sg.FolderBrowse('Browse')],
                    [sg.OK(), sg.Cancel()]
                ]).read(close=True)
                if event == 'OK':
                    f = cv2.imread(path + '/' + filename, 0)
                    imfilepath, imname, imext = os.path.splitext(filename)
                    sz = f.shape
                    maxsz = max(sz)

                    # image display and setups
                    imgbytes = cv2.imencode('.png', f)[1].tobytes()
                    self.UIFigure['canvas_sitting'].draw_image(data=imgbytes, location=(0, 0))

                    # keeping local parameters
                    self.fileLoc = filename
                    self.pathloc = path
                    self.imgnameloc = imname
                    self.sizeloc = sz
                    self.imageloc = f
                    self.maxszloc = maxsz

            # Button down function: UIAxes
            if event == 'canvas_standing':
                pass

            # Callback function: LoadStandingPostureXrayButtonPushed
            if event == 'Load Standing Xray':
                pass

spinopelvic_para = SpinopelvicPara()
spinopelvic_para.run()
