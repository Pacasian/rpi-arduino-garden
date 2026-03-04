// Arduino Uno: send JSON over Serial once per second
// No sensors yet: moisture/humidity/temperature are placeholders.
// You can replace these later when you add sensors.

void setup() {
  Serial.begin(9600);
  while (!Serial) { } // (mostly for boards with native USB; safe to keep)
}

void loop() {
  // placeholders for now:
  int moisture = 0;      // later from soil sensor
  int humidity = 0;      // later from DHT sensor
  float temperature = 0; // later from DHT sensor
  const char* pumpStatus = "OFF";

  // IMPORTANT: this prints a single JSON object per line
  Serial.print("{\"moisture\":");
  Serial.print(moisture);
  Serial.print(",\"humidity\":");
  Serial.print(humidity);
  Serial.print(",\"temperature\":");
  Serial.print(temperature, 1);
  Serial.print(",\"pump_status\":\"");
  Serial.print(pumpStatus);
  Serial.println("\"}");

  delay(1000);
}