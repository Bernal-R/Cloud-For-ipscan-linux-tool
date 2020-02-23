function request() {
  fetch('http://localhost:8081/api/v1/analysis_metric/last')
    .then(function(response) {
      return response.json();
    })
    .then(function(myJson) {
      document.getElementById("id_score").innerHTML = myJson.score;
      document.getElementById("id_ip").innerHTML = myJson.ip;
      changeColorCategories(myJson.bots, myJson.crypto_mining, myJson.ip_scan,myJson.ip_dynamic,myJson.malware,myJson.anonymization,myJson.botnets_command_center,myJson.spam);
    });
}

function changeColorCategories(bots, crypto_mining, ip_scan, ip_dynamic, malware, anonymization, botnets_command_center, spam) {
if (bots === true){document.getElementById("id_bots").style.backgroundColor = "#bd1111";}
if (crypto_mining === true){document.getElementById("id_crypto_mining").style.backgroundColor = "#bd1111";}
if (ip_scan === true){document.getElementById("id_ip_scan").style.backgroundColor = "#bd1111";}
if (ip_dynamic === true){document.getElementById("id_ip_dynamic").style.backgroundColor = "#bd1111";}
if (malware === true){document.getElementById("id_malware").style.backgroundColor = "#bd1111";}
if (anonymization === true){document.getElementById("id_anonymization").style.backgroundColor = "#bd1111";}
if (botnets_command_center === true){document.getElementById("id_botnets_command_center").style.backgroundColor = "#bd1111";}
if (spam === true){document.getElementById("id_spam").style.backgroundColor = "#bd1111";}
}



jQuery(document).ready(function () {
jQuery('#vmap').vectorMap({
  map: 'world_en',
  backgroundColor: 'transparent',
  color: '#C8EEFF',
  hoverOpacity: 0.7,
  selectedColor: '#C8EEFF',
  enableZoom: true,
  showTooltip: true,
  scaleColors: ['#C8EEFF', '#bd1111'],
  values: sample_data,
  normalizeFunction: 'polynomial'
});
});
