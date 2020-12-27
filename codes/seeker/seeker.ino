#include <SoftwareSerial.h> 
#include <SPI.h>
#include <RH_RF95.h>
#include <Adafruit_GPS.h>
#include <PString.h>


SoftwareSerial loraSerial(3, 4); // e32 TX e32 RX
SoftwareSerial gpsSerial(5, 7);
Adafruit_GPS GPS(&gpsSerial);

RH_RF95 SX1278;


String seeker = "SB";
int loc_decimals = 4;
char buffer[40];
String rssi = "";

void setup() {
// PC Serial

Serial.begin(115200);

  // LoRa
  loraSerial.begin(9600);

// RSSI
  if (!SX1278.init()){
        Serial.print(seeker);
        Serial.println("init failed");}

// GPS

  // 9600 NMEA is the default baud rate for Adafruit MTK GPS's- some use 4800
  GPS.begin(9600);
  // uncomment this line to turn on RMC (recommended minimum) and GGA (fix data) including altitude
  GPS.sendCommand(PMTK_SET_NMEA_OUTPUT_RMCGGA);
  // Set the update rate
  GPS.sendCommand(PMTK_SET_NMEA_UPDATE_1HZ);   // 1 Hz update rate


}


void loop() {

///////////////////// Prepare of sending String
  PString str(buffer, sizeof(buffer));
  str += seeker;
  str += ",";
  



//////////////////////GPS 
  char c = GPS.read();
  if (GPS.newNMEAreceived()) {
    // a tricky thing here is if we print the NMEA sentence, or data
    // we end up not listening and catching other sentences!
    // so be very wary if using OUTPUT_ALLDATA and trytng to print out data
    //Serial.println(GPS.lastNMEA());   // this also sets the newNMEAreceived() flag to false

  if (!GPS.parse(GPS.lastNMEA()))   // this also sets the newNMEAreceived() flag to false
      return;  // we can fail to parse a sentence in which case we should just wait for another
  }


  
  str += String(GPS.hour, DEC);
  str += ":";
  str += String(GPS.minute, DEC);
  str += ":";
  str += String(GPS.seconds, DEC);
  str += ",";

  if(GPS.lat == 'E'){ str += "-";}
  str += String(GPS.latitude, loc_decimals);
  str += ",";
  if(GPS.lon == 'S'){ str += "-";}
  str += String(GPS.longitude, loc_decimals);
  str += ",";
  str += String(GPS.altitude);
  str += ",";    
/////////////////////RSSI
if (SX1278.available()){
            rssi = String(SX1278.lastRssi(),DEC);
            }
str += rssi;

////////////// Sending via LoRa

  loraSerial.println(str);
  Serial.println(str);



delay(1000);
}
