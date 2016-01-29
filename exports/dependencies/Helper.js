
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