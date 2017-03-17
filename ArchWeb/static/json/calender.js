var date = new Date(),
	locale = "en-GB",
	month = date.toLocaleString(locale, {
		month: "long"
	}),
	day = date.toLocaleString(locale, {
		day: "2-digit"
	});
setTimeout(function() {
	$('.cube-1 .face.front').text(day[0]);
	$('.cube-2 .face.front').text(day[1]);
	$('.rectangle-1 .face.front').text(month);
}, 500);