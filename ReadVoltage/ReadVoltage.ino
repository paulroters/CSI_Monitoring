void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("Read Voltage from 230AC Input");
  Serial.println("+++++++++++++++++++++++++++++");
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println(readvoltage());
}

double readvoltage()
{
  // read the input on analog pin 0:
  int sensorValue = analogRead(A0);
  // Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
  float voltage = sensorValue * (5.0 / 1023.0);
  return voltage;
}
