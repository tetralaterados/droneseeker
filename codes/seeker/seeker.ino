#include <SoftwareSerial.h> 
#include <SPI.h>
#include <RH_RF95.h>
#include <PString.h>
#include <TinyGPS++.h>


static const int RXPin = 5, TXPin = 7;
static const uint32_t GPSBaud = 9600;
SoftwareSerial ss(RXPin, TXPin);
TinyGPSPlus gps;
String timegps = "";
SoftwareSerial loraSerial(3, 4); // e32 TX e32 RX

RH_RF95 SX1278;


String seeker = "SB";
int loc_decimals = 5;
char buffer[40];
String rssi = "";

void setup() {
// PC Serial

Serial.begin(115200);
Serial.println("Setup");
  // LoRa
  loraSerial.begin(9600);

// RSSI
  if (!SX1278.init()){
        Serial.print(seeker);
        Serial.println("init failed");}

// GPS

ss.begin(GPSBaud);


}


void loop() {

///////////////////// Prepare of sending String
  PString str(buffer, sizeof(buffer));
  str += seeker;
  str += ",";
  



//////////////////////GPS
printDateTime(gps.date, gps.time);
str+= String(timegps);
str += ",";
str+= String(gps.location.lat(),loc_decimals);
str += ",";
str+= String(gps.location.lng(),loc_decimals);
str += ",";
str+= String(gps.altitude.meters(),0);
str += ",";



/////////////////////RSSI
if (SX1278.available()){
            rssi = String(SX1278.lastRssi(),DEC);
            }
str += rssi;

////////////// Sending via LoRa
  Serial.println(str);
  loraSerial.println(str);


smartDelay(1000);

  if (millis() > 5000 && gps.charsProcessed() < 10){
    Serial.println(F("No GPS data received: check wiring"));}



}


static void smartDelay(unsigned long ms)
{
  unsigned long start = millis();
  do 
  {
    while (ss.available())
      gps.encode(ss.read());
  } while (millis() - start < ms);
}


static void printDateTime(TinyGPSDate &d, TinyGPSTime &t)
{
  if (!d.isValid())
  {
    //Serial.print(F("********** "));
  }
  else
  {
    char sz[32];
    sprintf(sz, "%02d/%02d/%02d ", d.month(), d.day(), d.year());
    //Serial.print(sz);
  }
  
  if (!t.isValid())
  {
   // Serial.print(F("******** "));
  }
  else
  {
    char sz[32] = "";
    sprintf(sz, "%02d:%02d:%02d", t.hour(), t.minute(), t.second());
   // Serial.print(sz);
    timegps = sz;
  }
  
 // printInt(d.age(), d.isValid(), 5);
  smartDelay(0);
}
