# PyChart
Combining the powers of Python and Chart.js!
Check out the [demo page](http://jayusstudios.com/Projects/PyChart/) that was generated with [80 lines of Python](https://github.com/EliCDavis/PyChart/blob/master/test/Tryout.py).

Open issues with what you'd like to see!

## Usage

#### Quick Example
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

### Creating a chart
```Python
chart_instance = Chart(chart_name:string)
```
### Chart Methods (that you care about)
**Adding Data To your chart**
```Python
# Adds a data entry of some number type and label the value what you'd like
# Including a dataset is optional, which groups data entries together under a common set
chart_instance.add_data_entry(data:num, label:string, ?data_set:string)

# Example
chart_instance.add_data_entry(15302, "January", "Product A")
```

**Changing Chart Representation**

Types: Pie,  Radar, Bar, and Line
```Python
chart_instance.set_chart_type(chart_type:string)

# Example
chart_instance.set_chart_type("Pie")
```
**Thing to Note**: When you make your chart representation a pie chart, theirs no need to specify datasets, because a pie chart can only represent one.  When exporting a Pie chart with multiple datasets, the dataset that was first added is picked to display.  If you have multiple datasets then you need to create multiple charts if you want to use pies.
### Exporting Your Charts
Exporting your charts means generating an html page that has it's own dependencies such as chart.js and bootstrap.
```Python
export_charts(all_charts:array, title:string, description:string)

# Example
export_charts([chart_one, chart_two], "<h1>Title</h1>", "<div class='well'>Description</div>")
```
**Notice:**  The title and the description has html tags in them.  This is because your title and description are simply written to the html file, allowing you to add whatever extra content and formatting you want to your page.  The title section is wrapped in Bootstrap's [Jumbotron](http://getbootstrap.com/components/#jumbotron) component, and the description is not wrapped in anything.  Both are wrapped in col-md-6 tags so that they stand side by side on the page.
## Technologies Being Used
* [Python 3.5.1](https://www.python.org/)
* [Chart.js](http://www.chartjs.org/)
* [Bootstrap 3](http://getbootstrap.com/)
* [Papa Parse](http://papaparse.com/)
* [Dragula](http://bevacqua.github.io/dragula/)
