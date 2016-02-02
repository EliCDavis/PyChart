import math

from src.Chart import Chart

from src.Export import export_charts

# Create a chart showcasing trig function
trigChart = Chart('Common Trig Functions')

for i in range(36):

    r = math.radians(i*10)

    trigChart.add_data_entry(math.sin(r), str(r), "Sin")
    trigChart.add_data_entry(math.cos(r), str(r), "Cos")


# Create a chart showcasing the powers of two
powChart = Chart('Powers Of Two')

for i in range(33):
    powChart.add_data_entry(math.pow(2, i), i, 'Powers Of Two')


# Create a chart showcasing some log values
logChart = Chart('Log values')

for i in range(20):
    logChart.add_data_entry(math.log10(i+1), i+1, "Log Values")


# Create example pie chart
howMuchYouLikeThisChart = Chart("How Much You Like PyChart")

howMuchYouLikeThisChart.add_data_entry(1000, "Love it")
howMuchYouLikeThisChart.add_data_entry(100, "Like it")
howMuchYouLikeThisChart.add_data_entry(10, "Hate it")

howMuchYouLikeThisChart.set_chart_type("Pie")


# Create example bar chart
popularity = Chart("Expected Popularity Trends Of Pychart and My Other Projects")

popularity.add_data_entry(10, "February", "PyChart")
popularity.add_data_entry(0, "February", "Others")

popularity.add_data_entry(100, "March", "PyChart")
popularity.add_data_entry(10, "March", "Others")

popularity.add_data_entry(1200, "April", "PyChart")
popularity.add_data_entry(23, "April", "Others")

popularity.add_data_entry(3000, "May", "PyChart")
popularity.add_data_entry(100, "May", "Others")

popularity.add_data_entry(5000, "June", "PyChart")
popularity.add_data_entry(230, "June", "Others")


popularity.set_chart_type("Bar")

# Create a title for our page
title = "<h1>PyChart <br/><small>Combining the powers of Python and Chart.js</small></h1>"

# Create a description for our page
description = "<div class='well'><h4>Create beautiful charts in just a few lines of Python</h4>"\
               "<code><pre>"\
               "from Chart import Chart<br>"\
               "from Export import export_charts<br>"\
               "import math<br><br>"\
               "trigChart = Chart('Trig Function')<br><br>"\
               'for i in range(36):<br>' \
               '    r = math.radians(i*10)<br>'\
               '    trigChart.add_data_entry( math.sin(r), r, "Sin")<br><br>'\
               'export_charts([trigChart], "Title", "Description")'\
               "</pre></code></div>"


# Finally export the chart we have created
export_charts(title, description, [trigChart, powChart, logChart, howMuchYouLikeThisChart, popularity])
