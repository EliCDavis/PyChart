from Vector2 import *
import math
from Chart import Chart
from Export import export_charts


sinValues = []
cosValues = []

for i in range(36):

    r = math.radians(i*10)

    sinValues.append(Vector2(r, math.sin(r)))
    cosValues.append(Vector2(r, math.cos(r)))

trigChart = Chart('Trig Functions')

for v in sinValues:
    trigChart.add_data_entry(v.y, str(v.x), "Sin")

for v in cosValues:
    trigChart.add_data_entry(v.y, str(v.x), "Cos")


powChart = Chart('Powers Of Two')

for i in range(33):
    powChart.add_data_entry(math.pow(2, i), i, 'Powers Of Two')

logChart = Chart('Log values')

for i in range(20):
    logChart.add_data_entry(math.log10(i+1), i+1, "Log Values")

# Finally export the chart we have created
description = "<div class='well'><h4>Create beautiful charts in just a few lines of Python</h4>"

description += "<code><pre>"\
               "from Chart import Chart<br>"\
               "from Export import export_charts<br>"\
               "import math<br><br>"\
               "trigChart = Chart('Trig Function')<br><br>"

description += 'for i in range(36):<br>' \
               '    r = math.radians(i*10)<br>'\
                '    trigChart.add_data_entry( math.sin(r), r, "Sin")<br><br>'\
                'export_charts([trigChart], "Title", "Description")'

description += "</pre></code></div>"

export_charts('<h1>PyChart <br/><small>Combining the powers of Python and Chart.js</small></h1>', description,
              [trigChart, powChart, logChart])
