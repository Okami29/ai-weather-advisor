#include "DHT.h"

#define DHTPIN 4       // Data pin connected to GPIO 4
#define DHTTYPE DHT22  // DHT 22 (AM2302)
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
  Serial.println("ESP32 ready — sending DHT22 data...");
}

void loop() {
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  if (isnan(h) || isnan(t)) {
    Serial.println("Failed to read from DHT sensor!");
    delay(2000);
    return;
  }

  // Print as structured data
  Serial.print("Temperature:");
  Serial.print(t);
  Serial.print(",Humidity:");
  Serial.println(h);

  delay(3000);  // Update every 3 seconds
}
