// the URL of the WAMP Router (Crossbar.io)
//

//com.barfly.drinkmotherfucker

var wsuri;
if (document.location.origin == "file://") {
	wsuri = "ws://127.0.0.1:8080/ws";

} else {
	wsuri = (document.location.protocol === "http:" ? "ws:" : "wss:") + "//" +
		document.location.host + "/ws";
}


// the WAMP connection to the Router
//
var connection = new autobahn.Connection({
	url: wsuri,
	realm: "realm1"
});


connection.onopen = function(session, details) {

	console.log("Connected");

	drinky = function() {
		var resOut = document.getElementById("imgOutput");
		session.call('com.barfly.drinkmotherfucker', ['drinkmotherfuckerdrinkmotherfuckerdrink']).then(
			function(res) {
				resOut.innerHTML = '<img src="/fileoutput/' + res + '"/><figcaption>' + res + '</figcaption>';
				console.log("drinkmotherfucker() result:", res);
			},
			function(err) {
				resOut.innerHTML = '<img src="http://thebusinessaim.com.ng/wp-content/uploads/2014/07/flesh_flies_mating_brian.jpg"/><figcaption>' + res + '</figcaption>';
				console.log("drinkmotherfucker() error:", err);
			}
		);

	}
};


// fired when connection was lost (or could not be established)
//
connection.onclose = function(reason, details) {
	console.log("Connection lost: " + reason);
}


// now actually open the connection
//
connection.open();
