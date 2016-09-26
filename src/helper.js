
function parentWidth(elem) {
    return elem.parentElement.clientWidth;
}

function correctAllGraphs(){

    var charts = document.getElementsByClassName("pychart");

    for( var i = 0; i < charts.length; i ++ ){

        console.log(charts[i]);

        charts[i].width = parentWidth(charts[i])-50;
        charts[i].style.width = parentWidth(charts[i])-50;
    }

    initDragula();

}

var dragStarted = false;

function initDragula(){

    if(dragStarted){
        return;
    }

    dragStarted = true;

    dragula([document.querySelector('#ALL_CHARTS')]);

}

var completeDownload = null;

function createCompleteDownload(){

    if(completeDownload !== null){
        return;
    }

    var dataWeCareAbout = [];

    for(var i = 0; i < allData.length; i ++){

        var item = {};

        // if the object we're looking at is an array, we're going to treat it as a pie chart
        if( Object.prototype.toString.call( allData[i] ) === '[object Array]' ) {

            item.labels = [];
            item.dataset1 = [];

            for(var j = 0; j < allData[i].length; j ++){
                item.labels.push(allData[i][j].label);
                item.dataset1.push(allData[i][j].value);
            }

        } else {

            item.labels = allData[i].labels;

            for(var d = 0; d < allData[i].datasets.length; d ++){
                item["dataset "+(d+1)] = allData[i].datasets[d].data;
            }

        }

        dataWeCareAbout.push(item);

    }

    completeDownload = Papa.unparse(dataWeCareAbout);

}

function allDownload(){

    saveContent(completeDownload, "data.csv");
}

function saveContent(fileContents, fileName)
{
    var link = document.createElement('a');
    link.download = fileName;
    link.href = 'data:,' + fileContents;
    link.click();
}