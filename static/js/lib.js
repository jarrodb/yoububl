function getHeight(coords) {
    var c = coords.split(',');
    return parseInt(c[3]) - parseInt(c[1]);
}

function getWidth(coords) {
    var c = coords.split(',');
    return parseInt(c[2]) - parseInt(c[0]);
}

function getRelativeTop(coords) {
    var c = coords.split(',');
    var comic = $('#comic');
    var cpos = comic.offset();
    return cpos.top + parseInt(c[1])
}

function getRelativeLeft(coords) {
    var c = coords.split(',');
    var comic = $('#comic');
    var cpos = comic.offset();
    return cpos.left + parseInt(c[0])
}

