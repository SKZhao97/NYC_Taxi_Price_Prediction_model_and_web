var map;
var geomapping = "./taxi_zone.json";
var parameters = {};
var zone_start = [];
var zone_end = [];
var prediction;

//document.getElementById("floating-panel").innerHTML="click on the map to set pick up point";

function initMap() {

	var zone_start_id = 0;
	var zone_end_id = 0;

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
			zone_start = [center.lng(), center.lat()];
		}
		else if(have_ending_point == 0) {
			// draw a ending point marker
			ending_point = center;
			have_ending_point = 1;
			end_marker = new google.maps.Marker({position:ending_point, map: map, 
			icon: {url: "http://maps.google.com/mapfiles/ms/icons/blue-dot.png"}});
			//console.log("your ending point is", centerlat, centerlng);
			zone_end = [center.lng(), center.lat()];

			$.ajaxSetup({			// Set async as false because the .ajax in this web needs to be in order
				async: false 
			});

			$.getJSON("static/NYC_Taxi_Zones.json", function(data) {
				var start_point_in_nyc = false;
				var end_point_in_nyc = false;
				var x = data["features"];
				for(i= 0;i<263;i++) {
					if (d3.geoContains(x[i], zone_start)) {
						zone_start_id = x[i]["properties"]["objectid"];
						start_point_in_nyc = true;
					}
					if (d3.geoContains(x[i], zone_end)) {
						zone_end_id = x[i]["properties"]["objectid"];
						end_point_in_nyc = true;
					}
				}
				if(start_point_in_nyc&&end_point_in_nyc) {
					console.log(zone_start_id + " to " + zone_end_id);

					parameters["start"] = zone_start_id;
					parameters["destination"] = zone_end_id;

					var date = new Date();
					currentTime = date.getHours()+":"+date.getMinutes() + " " + (date.getMonth()+1) + "/" + date.getDate() + "/" + date.getFullYear();
					console.log(currentTime);
					
					parameters["time"] = currentTime;


					document.getElementById("tips_window").innerHTML="Your fare may be: $xxx";
				}else {
					document.getElementById("tips_window").innerHTML="One of your point is not in NYC! Cancel and reclick.";
				}
			})
			
			reverse_geocoding(geocoder, map, endwindow, end_marker, 2);
			//document.getElementById("tips_window").innerHTML="Your fare may be: " + prediction ;
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
	//if (start==1 && destination==1)
	//	console.log(parameters);
	function reverse_geocoding(geocoder, map, infowindow, marker, x) {
		var latlng = {lat: centerlat, lng:centerlng};
		//console.log(latlng);
		geocoder.geocode({'location': latlng}, function(results, status){
			if(status == 'OK'){
				if (results[0]){
					infowindow.setContent(results[0].formatted_address);
					infowindow.open(map, marker);
					if (x == 1) {//point to window one
						//console.log(results[0].formatted_address);
						document.getElementById("info_window1").innerHTML="Your pick up point is: "+results[0].formatted_address;
						// parameters["start"]=results[0].formatted_address;
					}
					else if(x == 2) {
						//console.log(results[0].formatted_address);
						document.getElementById("info_window2").innerHTML="Your distination is: "+results[0].formatted_address;
						// parameters["destination"]=results[0].formatted_address;
						console.log(parameters);
						//$.when(
						$.ajax({
							type: "POST",
							async:false,
							contentType: "application/json;charset=utf-8",
							url: "/your/flask/endpoint",
							traditional: "true",
							data: JSON.stringify({parameters}),
							dataType: "json"
						});
						//).done(function(){
						$.ajax({
							url: "/getpythondata",
							type : "get",
							async: false,
							success: function(data) {
								prediction = $.parseJSON(data);
							}
						});
						//$.get("/getpythondata", function(data) {
						//	prediction = $.parseJSON(data);
							//console.log($.parseJSON(data));
						//});
						document.getElementById("tips_window").innerHTML="Your fare may be: $ " + prediction +".00";
						//})
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
