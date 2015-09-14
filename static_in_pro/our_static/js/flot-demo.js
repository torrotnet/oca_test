$(function() {
    var barOptions = {
        series: {
            lines: {
                show: true,
                lineWidth: 2,
                fill: true,
                fillColor: {
                    colors: [{
                        opacity: 0.0
                    }, {
                        opacity: 0.0
                    }]
                }
            },
            points: {
                show: false,
            }
        },
        xaxes: [{
            position: "bottom",
            tickDecimals: 0,
            min: 0.5,
            max: 10.5,
            //labelWidth:
        }, {
            position: "top",
            tickDecimals: 0,
            labelWidth: 10,
            min: 0.5,
            max: 10.5,
        }],

        //xaxis: {
        //    tickDecimals: 0
        //},
        yaxis: {
            max: 100,
            min: -100
        },
        colors: ["#1ab394"],
        grid: {
            color: "#999999",
            hoverable: true,
            clickable: true,
            tickColor: "#D4D4D4",
            borderWidth:0,
        },
        legend: {
            show: true
        },
        tooltip: true,
        tooltipOpts: {
            content: "x: %x, y: %y"
        }
    };
    var barData1 = {
        lines: {lineWidth: 6},
        xaxis:2,
        label: "\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u0442\u0435\u0441\u0442\u0430",
        data: [
            [1, 34],
            [2, 25],
            [3, 19],
            [4, 34],
            [5, 32],
            [6, -44],
            [7, 50],
            [8, -33],
            [9, 40],
            [10, 22]
        ]

    };
    var barData2 = {
        color: "rgba(208,224,208,1)",
        lines:{
            fillColor: "rgba(20,100,20,0.2)"
        },
        label: "\u041f\u0440\u0438\u0435\u043c\u043b\u0435\u043c\u043e\u0435 \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435",
        data: [
            [0.5, 32],
            [10.5, 32]
        ]};
    var barData3 = {
        color: "rgba(185,161,161,1)",
        lines:{
            fillColor: "rgba(80,20,20,0.4)",

        },
        label: "\u0416\u0435\u043b\u0430\u0442\u0435\u043b\u044c\u043d\u043e \u043e\u0431\u0440\u0430\u0442\u0438\u0442\u044c \u0432\u043d\u0438\u043c\u0430\u043d\u0438\u0435",
        data: [
            [0.5, -18],
            [10.5, -18]
        ]};
    var barData4 = {
        color: "rgba(150,150,150,1)",
        lines:{
            fillColor: "rgba(217,150,177,0.75)"
        },
        label: "\u0422\u043e\u0447\u043a\u0430 \u043e\u0442\u0441\u0447\u0435\u0442\u0430",
        data: [
            [0.5, 7],
            [10.5, 7]
        ]};
    $.plot($("#flot-line-chart"), [barData4, barData2, barData3, barData1], barOptions);
})