from src.Chart import Chart
from src.ColorSelector import ColorSelector
import os

def export_charts(title, desc, charts):

    export = ''

    export += '<html>'

    export += get_header()

    export += '<br/><div class="container">'

    export += '<div class="row">'

    export += '<div class="col-md-6"><div class="jumbotron">' + title + '</div></div>'

    export += '<div class="col-md-6">'+desc+'</div>'

    export += '</div><div class="row">'

    export += '<div id="ALL_CHARTS">'

    for i in range(len(charts)):

        if i == 0:

            export += "<div class='col-md-12'>"+create_chart_div(charts[i], i)+"</div>"

        else:

            export += "<div class='col-md-6'>"+create_chart_div(charts[i], i)+"</div>"

    export += '</div></div>'

    export += '<script>correctAllGraphs()</script>'

    for i in range(len(charts)):
        export += write_chart_script(charts[i], i)

    export += '<script> allData = ['

    for i in range(len(charts)):
        export += 'data'+str(i)

        if i < len(charts) -1:
            export += ','

    export += '];createCompleteDownload()</script>'

    export += '<br/><br/><br/>'

    export += write_footer()

    export += '</div>'

    export += '</html>'

    return export


def get_header():

    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

    scripts = open(os.path.join(__location__, 'script.js'), 'r')
    styles = open(os.path.join(__location__, 'style.css'), 'r')
    helper = open(os.path.join(__location__, 'helper.js'), 'r')

    header = '<head>'
    header += '<script>' + scripts.read().replace('\n', '') + '</script>'
    header += '<script>' + helper.read() + '</script>'
    header += '<style>' + styles.read().replace('\n', '') + '</style>'
    header += '</head>'

    return header


def create_chart_div(chart, index):

    div = '<div class="panel panel-default"><div class="panel-heading"><h3 class="panel-title">'
    div += chart.get_name() + '</h3></div><div class="panel-body">'
    div += '<canvas class="pychart" id="c' +str(index) + '" width="100%" height="400"></canvas>'
    div += '</div></div>'

    return div


def write_chart_script(chart, index):

    script = '\n<script>\n'

    script += 'var chartref = document.getElementById("c'+str(index)+'");\n'

    if chart.get_chart_type() == "Line" or chart.get_chart_type() == "Bar" or chart.get_chart_type() == "Radar":
        script += write_line_chart_data(chart, index)

    if chart.get_chart_type() == "Pie":
        script += write_pie_chart_data(chart, index)

    script += '\n</script>\n'

    return script


def write_pie_chart_data(chart, index):

    selector = ColorSelector()

    script = "var data"+str(index)+" = ["

    for i in range(len(chart.get_all_data_from_set(chart.get_data_sets()[0]))):

        color = selector.get_random_color()

        data_val = chart.get_all_data_from_set(chart.get_data_sets()[0])[i]

        script += '{value:'+str(data_val)+',color:"#'+color+'", highlight: "#'+color+'", label: "'+str(chart.get_data_labels()[i])+'" }'

        if i != (len(chart.get_all_data_from_set(chart.get_data_sets()[0]))) - 1:
            script += ','

    script += "];\n"

    script += 'var myPieChart = new Chart(chartref.getContext("2d")).Pie(data'+str(index)+');'

    return script


def write_line_chart_data(chart, index):

    """

    :param chart :
    :return:
    """

    # create a selector for getting colors
    selector = ColorSelector()

    # Variable declaration that stores chart info
    script = "var data"+str(index)+" = {\n"

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
        script += "var myLineChart = new Chart(chartref.getContext('2d')).Line(data"+str(index)+");\n"

    elif chart.get_chart_type() == "Bar":
        script += "var myBarChart = new Chart(chartref.getContext('2d')).Bar(data"+str(index)+");\n"

    elif chart.get_chart_type() == "Radar":
        script += "var myRadarChart = new Chart(chartref.getContext('2d')).Radar(data"+str(index)+");\n"

    return script


def write_footer():

    footer = '<nav class="navbar navbar-default navbar-fixed-bottom">'\
             '<div class="container-fluid">'\
             '<p class="text-center" style="margin-top:10px" > <a href="#" onclick="allDownload()" class="navbar-link">Download</a></p>'\
             '</div>'\
             '</nav>'

    return footer
