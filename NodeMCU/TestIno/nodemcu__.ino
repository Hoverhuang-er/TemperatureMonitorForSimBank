#include <ESP8266WiFi.h>
#include <ESP8266WiFiAP.h>
#include <ESP8266WiFiGeneric.h>
#include <ESP8266WiFiMulti.h>
#include <ESP8266WiFiScan.h>
#include <ESP8266WiFiSTA.h>
#include <ESP8266WiFiType.h>
#include <WiFiClient.h>
#include <WiFiClientSecure.h>
#include <WiFiServer.h>
#include <WiFiUdp.h>
#include<SPI.h>
void setup()
{
  IPAddress ip(192.168.3.110);
  WiFiServer server (80);
  File webFile;
  char HTTP_req[REQ_BUF_SZ] = {0};
  char req_index = 0;
  boolean Relay_state[2] = {0};

void setup()
{
  pinMode(16,OUTPUT);
  digitalWrite(16,HIGH);
  Serial.begin(115200);
}
if (url("index.html"))
{
  Serial.println("ERROR-Can't find index.htm file");
  return;
}
}
  Serial.println("SUCCESS-Found index");
  pinMode(1,HIGH);
  pinMode(1,LOW);
  pinMode(2,HIGH);
  pinMode(2,LOW);
  pinMode(3,HIGH);
  pinMode(3,LOW);
  pinMode(4,HIGH);
  pinMode(4,LOW);
  pinMode(5,HIGH);
  pinMode(5,LOW);
  pinMode(6,HIGH);
  pinMode(6,LOW);
  //pinMode(7,LOW);
  //pinMode(7,LOW);
  //pinMode(8,LOW);
  //pinMode(8,LOW);
void setup() {
  pinMode(7,OUTPUT);

}

void loop() {
  digitalWrite(7,LOW);
  delay(35000);
  digitalWrite(7,HIGH);
  delay(35000);
}
