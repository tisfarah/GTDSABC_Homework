// Creating map object
var myMap = L.map("map", {
  center: [40.7, -73.95],
  zoom: 11
});

// Adding tile layer to the map
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets",
  accessToken: API_KEY
}).addTo(myMap);

// TODO:
//https://data.cityofnewyork.us/resource/fhrw-4uyv.json?$where=created_date between '' and ''"
// Store API query variables
var baseURL = "https://data.cityofnewyork.us/resource/fhrw-4uyv.json?";
// Add the dates in the ISO formats
var date = "$where=created_date between '2016-01-01' and '2016-12-31'";
// Add the complaint type
var complaint = "&complaint_type=Rodent";
// Add a limit
var limit = "&$limit=10000";
//https://data.cityofnewyork.us/resource/fhrw-4uyv.json?complaint_type=Rodent&$limit=20&created_date between '2016-01-01' and '2016-12-31'

var newtry = baseURL + date + complaint + limit;
var markers = L.markerClusterGroup();

console.log(newtry);
//Example data
//https://github.com/Leaflet/Leaflet.markercluster#examples

//Use Template format from documentation
//var markers = L.markerClusterGroup();
//Loop through each data point and add coordinates
//markers.addLayer(L.marker(getRandomLatLng(map)));
//... Add more layers ...
//map.addLayer(markers);

  d3.json(newtry, function(response) {
  
    for (var i = 0; i < response.length; i++) {
      if ("latitude" in response[i] && "longitude" in response[i]) {
        // From sample code --- markers.addLayer(L.marker(getRandomLatLng(map)));
        markers.addLayer(L.marker([Number(response[i].latitude), Number(response[i].longitude)]));
      }
    }
    //From sample code - map.addLayer(markers); --- here map is myMap
    myMap.addLayer(markers);
  });

