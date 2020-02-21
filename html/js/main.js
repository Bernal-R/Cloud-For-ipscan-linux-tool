function request() {
    fetch('http://localhost:8081/api/v1/analysis_metric/123')
      .then(function(response) {
        return response.json();
      })
      .then(function(myJson) {
        console.log(myJson);
      });
}


jQuery(document).ready(function () {
  jQuery('#vmap').vectorMap({
    map: 'world_en',
    backgroundColor: 'transparent',
    color: '#C8EEFF',
    hoverOpacity: 0.7,
    selectedColor: '#666666',
    enableZoom: true,
    showTooltip: true,
    scaleColors: ['#C8EEFF', '#006491'],
    values: sample_data,
    normalizeFunction: 'polynomial'
  });
});
