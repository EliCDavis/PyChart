# PyChart
Combining the powers of Python and Chart.js

Open issues with suggestions!

### Usage
```Python
from Chart import Chart
from Export import export_charts
import math

trigChart = Chart('Trig Function')

for i in range(36):
    r = math.radians(i*10)
    trigChart.add_data_entry( math.sin(r), r, "Sin")

export_charts([trigChart], "Title", "Description")
```
