import Chart


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

    # Variable declaration that stores chart info
    script += "var data = {\n"

    # Go through and print each label
    sorted_data_entries = chart.get_sorted_labels()
    script += 'labels:'+str(sorted_data_entries) + ', '

    # Print out the data set info
    script += "datasets : ["

    for s in range(len(chart.get_data_sets())):

        data_set = chart.get_data_sets()[s]

        script += '{\n'
        script += 'data: ' + str(chart.sort_data_set_by_label(data_set)) + ',\n'
        script += 'label:"' + chart.get_data_sets()[s] + '",\n'
        script += 'fillColor:' + "'rgba(220,220,220,0)'" + ',\n'
        script += 'strokeColor:' + "'rgba(220,220,220,1)'" + ',\n'
        script += 'pointColor:' + "'rgba(220,220,220,1)'" + ',\n'
        script += 'pointStrokeColor:' + "'#fff'" + ',\n'
        script += 'pointHighlightFill:' + "'#fff'" + ',\n'
        script += 'pointHighlightStroke:' + "'rgba(220,220,220,1)'\n"
        script += '}'

        if s < len(chart.get_data_sets())-1:
            script += ","

    script += "]};\n"

    script += "var myLineChart = new Chart(chartref.getContext('2d')).Line(data);\n"

    script += '\n</script>\n'


    return script

# charts = []
# export()
