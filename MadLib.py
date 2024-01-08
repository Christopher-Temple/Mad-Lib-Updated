import PySimpleGUI as psg
import textwrap

psg.set_options(font=('Arial Bold', 16))
layout = [
   [psg.Text('Name ', size=(30,1)), psg.Input(expand_x=True, key= '-NM-')],
   [psg.Text('Currency such as dollars, peso, etc.', size=(30,1)), psg.Input(expand_x=True, key= '-CURRENCY-')],
   [psg.Text('Website that sells product ', size=(30,1)), psg.Input(expand_x=True, key= '-WEBSITE-')],
   [psg.Text('Type of Seed ', size=(30,1)), psg.Input(expand_x=True, key= '-SEED-')],
   [psg.Text('Number 1-100 ', size=(30,1)), psg.Input(expand_x=True, key= '-DAY-')],
   [psg.Text('Object ', size=(30,1)), psg.Input(expand_x=True, key= '-OBJECT-')],
   [psg.Text('Number 1-100 ', size=(30,1)), psg.Input(expand_x=True, key= '-SIZE-')],
   [psg.Text(expand_x=True, key= '-OUTPUT-')],
   [psg.OK(), psg.Exit()]
]
window = psg.Window('Mad Lib', layout, size=(1015,400))
while True:
    event, values = window.read()
    print (event, values)
    out = values['-NM-'] + ' was down to his last two ' + values['-CURRENCY-']+ '. He saw a listing on ' + values['-WEBSITE-'] + ' for a pack of ' + values['-SEED-'] + ' seeds. It took ' + values['-DAY-'] + ' days to arrive. After planting the seeds, ' + values['-NM-'] + ' had a vivid dream that the seeds grew into a ' + values['-OBJECT-'] + '. The next morning, much to the surprise of everyone, the seeds grew into a ' + values['-SIZE-'] + ' foot tall ' + values['-OBJECT-'] + '.'
    madlib = textwrap.fill(out, 100)
    window['-OUTPUT-'].update(madlib)
    if event == psg.WIN_CLOSED or event == 'Exit':
        break
window.close()
