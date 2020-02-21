function request() {
    fetch('http://localhost:8081/api/v1/analysis_metric/123')
      .then(function(response) {
        return response.json();
      })
      .then(function(myJson) {
        console.log(myJson);
      });
}

