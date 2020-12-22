#include <SoftwareSerial.h>

SoftwareSerial mySerial(2, 3); //TX, RX
// (Send and Receive)

void setup() {
  Serial.begin(9600);
  mySerial.begin(9600);
}

void loop() {
  
  

    String input = "out";
   // mySerial.println(input);    

 
  if(mySerial.available() > 1){//Read from  OSOYOO UART LoRa wireless module and send to serial monitor
    Serial.println("Print from Lora"); 
    String input = mySerial.readString();
    Serial.println(input);    
  }
  delay(20);
}
