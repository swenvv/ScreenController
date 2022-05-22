class screenController{

	constructor(startAltitude, endAltitude, startAzimuth, endAzimuth){
		this.startAltitude = startAltitude;
		this.endAltitude = endAltitude;
		this.startAzimuth = startAzimuth;
		this.endAzimuth = endAzimuth;
	}

	
	ScreenInSunInReach(sunPos){

		let azimuthDeg = azimuthDegAdd180(radToDeg(sunPos.azimuth));
		let altitudeDeg = radToDeg(sunPos.altitude);

		if (azimuthDeg < this.startAzimuth) return 0;
		if (azimuthDeg > this.endAzimuth) return 0;
		if (altitudeDeg < this.startAltitude) return 0;
		if (altitudeDeg > this.endAltitude) return 0;

		return 1;
	}


}




var SunCalc = require ("suncalc");

const latitude = 52.00631560266013
const longitude = 4.97787767458043
const benschop_datetime_str = new Date();

var sunPos = SunCalc.getPosition(benschop_datetime_str, latitude , longitude);

let azimuth = azimuthDegAdd180(radToDeg(sunPos.azimuth))
let altitude = radToDeg(sunPos.altitude)

console.log("azimuth: ",  azimuth, "altitude: ", altitude);

let screenController1 = new screenController(-5,2,300,360);


console.log(screenController1.ScreenInSunInReach(sunPos));

function radToDeg(rad){
	return 360 * rad / (2*Math.PI);
}

function azimuthDegAdd180 (azi){
	azi += 180;
	if (azi > 360) azi -= 360;
	return azi;
}

