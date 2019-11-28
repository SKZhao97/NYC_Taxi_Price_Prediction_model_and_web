var map;
var geomapping = "./taxi_zone.json";
//document.getElementById("floating-panel").innerHTML="click on the map to set pick up point";

function initMap() {
	//get time part
	//var date = new Date();
	//console.log(date.getHours()+":"+date.getMinutes());
	var geocoder = new google.maps.Geocoder;
	var startwindow = new google.maps.InfoWindow;
	var endwindow = new google.maps.InfoWindow;
	var have_starting_point = 0;
	var have_ending_point = 0;
	map = new google.maps.Map(document.getElementById('map'), {
		center: {lat: 40.6735, lng: -73.9700},
		zoom: 11
	});
	var starting_point = {lat: 40.6735, lng: -73.9700};
	var ending_point = {lat: 40.6735, lng: -73.9700};
	var start_marker;
	var end_marker;
	//var marker = new google.maps.Marker({position: plaza, map: map});
	// listen to click, add a mark
	google.maps.event.addListener(map, 'click', function(event) {
		center = event.latLng;
		centerlat = center.lat();
		centerlng = center.lng();
		if(have_starting_point == 0) {
			// draw a starting point marker
			starting_point = center;
			have_starting_point = 1;
			start_marker = new google.maps.Marker({position:starting_point, map:map,
			icon: {url: "http://maps.google.com/mapfiles/ms/icons/red-dot.png"}});
			//console.log("your starting point is", centerlat, centerlng);
			reverse_geocoding(geocoder, map, startwindow, start_marker, 1);
			document.getElementById("tips_window").innerHTML="Click on the map to set your destination";
		}
		else if(have_ending_point == 0) {
			// draw a ending point marker
			ending_point = center;
			have_ending_point = 1;
			end_marker = new google.maps.Marker({position:ending_point, map: map, 
			icon: {url: "http://maps.google.com/mapfiles/ms/icons/blue-dot.png"}});
			//console.log("your ending point is", centerlat, centerlng);
			reverse_geocoding(geocoder, map, endwindow, end_marker, 2);
			document.getElementById("tips_window").innerHTML="Your fare may be: $xxx";
		}
	});

	google.maps.event.addListener(map, 'rightclick', function(event) {
		if (have_ending_point == 1) {
			//first delete the ending point
			end_marker.setMap(null);
			have_ending_point = 0;
			//console.log("cancel end point");
			document.getElementById("tips_window").innerHTML="Click on the map to set your destination";
			document.getElementById("info_window2").innerHTML=" ";
		}
		else if(have_starting_point == 1) {
			//then delete the bigin point
			start_marker.setMap(null);
			have_starting_point = 0;
			//console.log("cancel start point");
			document.getElementById("tips_window").innerHTML="Click on the map to set pick up point";
			document.getElementById("info_window1").innerHTML=" ";
		}
	});
	function reverse_geocoding(geocoder, map, infowindow, marker, x){
		var latlng = {lat: centerlat, lng:centerlng};
		//console.log(latlng);
		geocoder.geocode({'location': latlng}, function(results, status){
			if(status == 'OK'){
				if (results[0]){
					infowindow.setContent(results[0].formatted_address);
					infowindow.open(map, marker);
					if (x == 1) {//point to window one
						document.getElementById("info_window1").innerHTML="Your pick up point is: "+results[0].formatted_address;
					}
					else if(x == 2) {
					document.getElementById("info_window2").innerHTML="Your distination is: "+results[0].formatted_address;
					}
				}
				else {
					window.alert('No results found');
				}
			}
			else{
				window.alert('Geocoder failed due to: ' + status);
			}
		});
	};
}
