        Highcharts.chart('container', {
    chart: {
        type: 'spline'
    },
    data: {
        enablePolling: true,
        csvURL: 'https://raw.githubusercontent.com/RealStr1ke/COVID-19/main/data/ny_cases.csv'
    },
    title: {
        text: 'New York New Daily Cases Over Time'
    },
    xAxis: {
        type: 'datetime'
    },
    yAxis: {
        title: {
            text: 'New Daily Cases'
        }
    }
});
