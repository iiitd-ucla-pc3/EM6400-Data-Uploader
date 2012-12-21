$(function() {
	var a=document.URL;
	var n=a.split("/");
	var c=n[2];
	var d=c.split(":")[0];
	 
    var ws = new WebSocket("ws://"+d+":9999/test");
    var $placeholder = $('#placeholder');
    var datalen = 10;
    var plot = null;
    var series = {
        label: "Value",
        lines: { 
            show: true,
            fill: true,
            shadowSize: 50	
        },
        points: {
            show:true
        },
        data: []
    };
    ws.onmessage = function(evt) {
        var d = $.parseJSON(evt.data);
        series.data.push([d.x, d.y]);
        while (series.data.length > datalen) {
            series.data.shift();
        }
        if(plot) {
            plot.setData([series]);
            plot.setupGrid();
            plot.draw();
        } else if(series.data.length > 1) {
            plot = $.plot($placeholder, [series], {
                xaxis:{
                    mode: "time",
                    timeformat: "%H:%M:%S",
                    minTickSize: [1, "second"],
                },
                
            });
            plot.draw();
        }
    }
    ws.onopen = function(evt) {
        $('#conn_status').html('<b>Connected</b>');
    }
    ws.onerror = function(evt) {
        $('#conn_status').html('<b>Error</b>');
    }
    ws.onclose = function(evt) {
        $('#conn_status').html('<b>Closed</b>');
    }
});


