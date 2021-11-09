let map = new Map();
map.set('al', 'Alabama');
map.set('ak', 'Alaska');
map.set('az', 'Arizona');
map.set('ar', 'Arkansas');
map.set('ca', 'California');
map.set('co', 'Colorado');
map.set('ct', 'Connecticut');
map.set('de', 'Delaware');
map.set('fl', 'Florida');
map.set('ga', 'Georgia');
map.set('hi', 'Hawaii');
map.set('id', 'Idaho');
map.set('il', 'Illinois');
map.set('in', 'Indiana');
map.set('ia', 'Iowa');
map.set('ks', 'Kansas');
map.set('ky', 'Kentucky');
map.set('la', 'Louisiana');
map.set('me', 'Maine');
map.set('md', 'Maryland');
map.set('ma', 'Massachusetts');
map.set('mi', 'Michigan');
map.set('mn', 'Minnesota');
map.set('ms', 'Mississippi');
map.set('mo', 'Missouri');
map.set('mt', 'Montana');
map.set('ne', 'Nebraska');
map.set('nv', 'Nevada');
map.set('nh', 'New Hampshire');
map.set('nj', 'New Jersey');
map.set('nm', 'New Mexico');
map.set('ny', 'New York');
map.set('nc', 'North Carolina');
map.set('nd', 'North Dakota');
map.set('oh', 'Ohio');
map.set('ok', 'Oklahoma');
map.set('or', 'Oregon');
map.set('pa', 'Pennsylvania');
map.set('ri', 'Rhode Island');
map.set('sc', 'South Carolina');
map.set('sd', 'South Dakota');
map.set('tn', 'Tennessee');
map.set('tx', 'Texas');
map.set('ut', 'Utah');
map.set('vt', 'Vermont');
map.set('va', 'Virginia');
map.set('wa', 'Washington');
map.set('wv', 'West Virginia');
map.set('wi', 'Wisconsin');
map.set('wy', 'Wyoming');
map.forEach(function(name, id) {
    Highcharts.chart(id, {
      chart: {
          type: 'spline'
      },
      data: {
          enablePolling: true,
          csvURL: './data/' + id + '_cases.csv'
      },
      annotations: [{
        labelOptions: {
          backgroundColor: 'rgba(255,255,255,0.8)',
          verticalAlign: 'top',
          y: 10
        },
        labels: annotationPoints
      }],
      title: {
          text: name + ' New Daily Cases Over Time'
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
  });
