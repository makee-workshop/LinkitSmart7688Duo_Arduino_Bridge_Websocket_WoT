#include "DHT.h"
#include <Bridge.h>

#define DHTPIN A1     //訊號來源為第2腳位
#define EARTHPIN A0     //訊號來源為第A1腳位
#define DHTTYPE DHT11 //感應器為DHT11
DHT dht(DHTPIN, DHTTYPE); //宣告一個DHT物件

void setup() {
// 開啟 Serial Port，通訊速率為 9600bps (Bits Per Second)
  Bridge.begin();
  Serial.begin(9600); 
  dht.begin();

}
void loop() {
  float h = dht.readHumidity();// 取出濕度的數值
  float t = dht.readTemperature();//取出溫度的數值
  int dirtyVal = analogRead(EARTHPIN);
  
  // 檢查返回是否是有效的
  if (isnan(t) || isnan(h)) {
    Serial.println("Failed to read from DHT");
  } else {
    Serial.print("EARTH:");
    Serial.print(dirtyVal);
    Serial.print(" %\t");
    Serial.print("Humidity: "); 
    Serial.print(h);
    Serial.print(" %\t");
    Serial.print("Temperature: "); 
    Serial.print(t);
    Serial.println(" *C");

    Bridge.put("EARTH", String(dirtyVal));
    Bridge.put("h", String(h));
    Bridge.put("t", String(t));
  }

   delay(1000); //每秒回傳一次資料
}
