#include <AmazonDynamoDBClient.h>
#include <AmazonIOTClient.h>
#include <AmazonKinesisClient.h>
#include <AmazonS3Client.h>
#include <AmazonSNSClient.h>
#include <AWSClient.h>
#include <AWSClient2.h>
#include <AWSClient4.h>
#include <AWSFoundationalTypes.h>
#include <DeviceIndependentInterfaces.h>
#include <ESP8266AWSImplementations.h>
#include <jsmn.h>
#include <sha256.h>
#include <Utils.h>
#include <ESP8266WiFi.h>

void setup() {
  pinMode(6,OUTPUT);
  pinMode(9,OUTPUT);
}

void loop() {
  digitalWrite(6,HIGH);
  delay(540000);
  digitalWrite(6,LOW);
  delay(12000);
  digitalWrite(9,HIGH);
  delay(540000);
  digitalWrite(9,LOW);
  delay(12000);
}
// 写入Mac Addres 和 IP Address
byte MAC [] ={
  0xDE.0xAD,0xBE,0xEF,0xFE,0xED
};
byte IP [] = {
  192.168.3.140
  //192.168.0.130
}
//telnet port 23
//ssh port 22
//ftp port 21
Server server(23)
void setup (){
  ESPWiFi.begin(Mac,IP);
  server.begin();
  pinMode(RX,OUTPUT);
  pinMode(TX,OUTPUT);
  Serial.begin(115200);
  Serial.print("Server address");
  Serial.print("192.168.3.140");
  
}
void loop(){
  Client client = server.avaliable();
  if (client)
  {
    if(client.avaliabel()>0)
    {
      char thisChar = client.read();
      if(thisChar=='b')
      {
        digitalWrite(RX,HIGH);
        digitalWrite(TX.LOW);
      }
      else if (thisChar=='c')
      {
        digitalWrite(RX,LOW);
        digitalWrite(TX,HIGH);
      }
      else
      {
        digitalWrite(RX,LOW);
        digitalWrite(TX,LOW);
      }
    }
  }
}


