from src.Chart import Chart
from src.ColorSelector import ColorSelector

def export_charts(title, desc, charts):

    file = open('exports/workfile.html', 'w')

    file.write('<html>')

    file.write(get_header())

    file.write('<br/><div class="container">')

    file.write('<div class="row">')

    file.write('<div class="col-md-6"><div class="jumbotron">' + title + '</div></div>')

    file.write('<div class="col-md-6">'+desc+'</div>')

    file.write('</div><div class="row">')

    file.write('<div id="ALL_CHARTS">')

    for i in range(len(charts)):

        if i == 0:

            file.write("<div class='col-md-12'>"+create_chart_div(charts[i])+"</div>")

        else:

            file.write("<div class='col-md-6'>"+create_chart_div(charts[i])+"</div>")

    file.write('</div></div>')

    file.write('<script>correctAllGraphs()</script>')

    for chart in charts:
        file.write(write_chart_script(chart))

    file.write('</div>')

    file.write('</html>')


def get_header():

    header = '<head>' \
             '  <script src="https://code.jquery.com/jquery-2.2.0.min.js"></script>' \
             '  <script src="dependencies/bootstrap/js/bootstrap.min.js"></script>' \
             '  <script src="dependencies/dragula/dragula.min.js"></script>'\
             '  <link href="dependencies/dragula/dragula.min.css" rel="stylesheet">'\
             '  <script src="dependencies/Helper.js"></script>'\
             '  <link href="dependencies/bootstrap/css/bootstrap.css" rel="stylesheet">' \
             '  <script src="dependencies/Chart.min.js"></script>' \
             '<head>'

    return header


def create_chart_div(chart):

    div = '<div class="panel panel-default"><div class="panel-heading"><h3 class="panel-title">'
    div += chart.get_name() + '</h3></div><div class="panel-body">'
    div += '<canvas class="pychart" id="' + chart.get_name() + '" width="100%" height="400"></canvas>'
    div += '</div></div>'

    return div


def write_chart_script(chart):

    script = '\n<script>\n'

    script += 'var chartref = document.getElementById("'+chart.get_name()+'");\n'

    if chart.get_chart_type() == "Line" or chart.get_chart_type() == "Bar":
        script += write_line_chart_data(chart)

    if chart.get_chart_type() == "Pie":
        script += write_pie_chart_data(chart)

    script += '\n</script>\n'

    return script


def write_pie_chart_data(chart):

    selector = ColorSelector()

    script = "var data = ["

    for i in range(len(chart.get_all_data_from_set(chart.get_data_sets()[0]))):

        color = selector.get_random_color()

        data_val = chart.get_all_data_from_set(chart.get_data_sets()[0])[i]

        script += '{value:'+str(data_val)+',color:"#'+color+'", highlight: "#'+color+'", label: "'+str(chart.get_data_labels()[i])+'" }'

        if i != (len(chart.get_all_data_from_set(chart.get_data_sets()[0]))) - 1:
            script += ','

    script += "];\n"

    script += 'var myPieChart = new Chart(chartref.getContext("2d")).Pie(data);'

    return script


def write_line_chart_data(chart):

    """

    :param chart :
    :return:
    """

    # create a selector for getting colors
    selector = ColorSelector()

    # Variable declaration that stores chart info
    script = "var data = {\n"

    # get correct labels
    labels = []
    if chart.can_sort_data_numerically():
        labels = chart.get_sorted_labels()
    else:
        labels = chart.get_data_labels()
    script += 'labels:'+str(labels) + ', '

    # Print out the data set info
    script += "datasets : ["

    for s in range(len(chart.get_data_sets())):

        data_set = chart.get_data_sets()[s]

        data = []

        if chart.can_sort_data_numerically():
            data = chart.sort_data_set_by_label(data_set)
        else:
            data = chart.get_all_data_from_set(data_set)

        color = selector.get_random_color()

        script += '{\n'
        script += 'data: ' + str(data) + ',\n'
        script += 'label:"' + data_set + '",\n'
        script += 'fillColor:' + '"rgba(220,220,220,0.0)" ,\n'
        script += 'strokeColor:' + '"#'+color + '",\n'
        script += 'pointColor:' + '"#'+color + '",\n'
        script += 'pointStrokeColor:' + '"#'+color + '",\n'
        script += 'pointHighlightFill:' + '"#'+color + '",\n'
        script += 'pointHighlightStroke:' + "'#"+color + "'\n"
        script += '}'

        if s < len(chart.get_data_sets())-1:
            script += ","

    script += "]};\n"

    if chart.get_chart_type() == "Line":
        script += "var myLineChart = new Chart(chartref.getContext('2d')).Line(data);\n"

    elif chart.get_chart_type() == "Bar":
        script += "var myBarChart = new Chart(chartref.getContext('2d')).Bar(data);\n"

    return script
