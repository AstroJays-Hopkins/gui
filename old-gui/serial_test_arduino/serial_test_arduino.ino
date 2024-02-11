typedef struct {
  char header = 0x55;
  float lat = 90;
  char padding1 = '1';
  float lon = 90;
  char padding2 = '2';
  float altitude = 90;
  char padding3 = '3';
} __attribute__((packed)) Packet;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("Start sending: ");
}

void loop() {
  // put your main code here, to run repeatedly:
  Packet packet;
  char * packet_addr = (char *)(&packet);
  Serial.write(packet_addr,sizeof(packet));
  Serial.println();
  delay(100);
}
