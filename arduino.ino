const int relayPin1 = 41;
const int relayPin2 = 25;
const int relayPin3 = 27;
const int relayPin4 = 29;
const int relayPin5 = 39;
const int relayPin6 = 31;
const int relayPin7 = 37;
const int relayPin8 = 35;
const int relayPin9 = 33;

const int irPin1 = 4;
const int irPin2 = 8;
const int irPin3 = 9;
const int irPin4 = 10;
const int irPin5 = 5;
const int irPin6 = 6;
const int irPin7 = 11;
const int irPin8 = 12;
const int irPin9 = 7;

const int redPin1   = 52; 
const int greenPin1 = 53;
 
const int redPin2   = 14; 
const int greenPin2 = 15;

const int redPin3   = 16; 
const int greenPin3 = 17;

const int redPin4   = 18; 
const int greenPin4 = 19;

const int redPin5   = 48; 
const int greenPin5 = 50;
  
const int redPin6   = 20; 
const int greenPin6 = 21;
 
const int redPin7   = 44; 
const int greenPin7 = 46;

const int redPin8   = 22; 
const int greenPin8 = 23; 

const int redPin9   = 40;
const int greenPin9 = 42;

int currentCommand = -1;

void setup() {
  Serial.begin(9600);
  pinMode(redPin1,   OUTPUT);
  pinMode(greenPin1, OUTPUT);
  pinMode(irPin1, INPUT);  
  pinMode(relayPin1, OUTPUT);

  pinMode(redPin2,   OUTPUT);
  pinMode(greenPin2, OUTPUT);
  pinMode(irPin2, INPUT);  
  pinMode(relayPin2, OUTPUT);

  pinMode(redPin3,   OUTPUT);
  pinMode(greenPin3, OUTPUT);
  pinMode(irPin3, INPUT);  
  pinMode(relayPin3, OUTPUT);

  pinMode(redPin4,   OUTPUT);
  pinMode(greenPin4, OUTPUT);
  pinMode(irPin4, INPUT);  
  pinMode(relayPin4, OUTPUT);

  pinMode(redPin5,   OUTPUT);
  pinMode(greenPin5, OUTPUT);
  pinMode(irPin5, INPUT);  
  pinMode(relayPin5, OUTPUT);

  pinMode(redPin6,   OUTPUT);
  pinMode(greenPin6, OUTPUT);
  pinMode(irPin6, INPUT);  
  pinMode(relayPin6, OUTPUT);
  
  pinMode(redPin7,   OUTPUT);
  pinMode(greenPin7, OUTPUT);
  pinMode(irPin7, INPUT);  
  pinMode(relayPin7, OUTPUT);

  pinMode(redPin8,   OUTPUT);
  pinMode(greenPin8, OUTPUT);
  pinMode(irPin8, INPUT);  
  pinMode(relayPin8, OUTPUT);
  
  pinMode(redPin9,   OUTPUT);
  pinMode(greenPin9, OUTPUT);
  pinMode(irPin9, INPUT);  
  pinMode(relayPin9, OUTPUT);
}

void loop() {
  if(currentCommand == -1) {
    receiveCommand();
  }

  // Compartment 1 Commands
  else if(currentCommand == 0) {
    digitalWrite(relayPin1, LOW);
    currentCommand = -1;
  }
  else if(currentCommand == 1) {
    digitalWrite(relayPin1, HIGH);
    currentCommand = -1;
  }
  else if(currentCommand == 2) {
    setColor1(255, 0, 0);
    currentCommand = -1;
  }
  else if(currentCommand == 3) {
    setColor1(0, 255, 0);
    currentCommand = -1;
  }
  else if(currentCommand == 4) {
    detectItem1();
    currentCommand = -1;
  }
  else if(currentCommand == 5){
    offLED1();
    currentCommand = -1;
  }

  // Compartment 2 commands
  else if(currentCommand == 6) {
    digitalWrite(relayPin2, LOW);
    currentCommand = -1;
  }
  else if(currentCommand == 7) {
    digitalWrite(relayPin2, HIGH);
    currentCommand = -1;
  }
  else if(currentCommand == 8) {
    setColor2(255, 0, 0);
    currentCommand = -1;
  }
  else if(currentCommand == 9) {
    setColor2(0, 255, 0);
    currentCommand = -1;
  }
  else if(currentCommand == 10) {
    detectItem2();
    currentCommand = -1;
  }
  else if(currentCommand == 11){
    offLED2();
    currentCommand = -1;
  }

  // Compartment 3 commands
  else if(currentCommand == 12) {
    digitalWrite(relayPin3, LOW);
    currentCommand = -1;
  }
  else if(currentCommand == 13) {
    digitalWrite(relayPin3, HIGH);
    currentCommand = -1;
  }
  else if(currentCommand == 14) {
    setColor3(255, 0, 0);
    currentCommand = -1;
  }
  else if(currentCommand == 15) {
    setColor3(0, 255, 0);
    currentCommand = -1;
  }
  else if(currentCommand == 16) {
    detectItem3();
    currentCommand = -1;
  }
  else if(currentCommand == 17){
    offLED3();
    currentCommand = -1;
  }
  // Compartment 4 commands
  else if(currentCommand == 18) {
    digitalWrite(relayPin4, LOW);
    currentCommand = -1;
  }
  else if(currentCommand == 19) {
    digitalWrite(relayPin4, HIGH);
    currentCommand = -1;
  }
  else if(currentCommand == 20) {
    setColor4(255, 0, 0);
    currentCommand = -1;
  }
  else if(currentCommand == 21) {
    setColor4(0, 255, 0);
    currentCommand = -1;
  }
  else if(currentCommand == 22) {
    detectItem4();
    currentCommand = -1;
  }
  else if(currentCommand == 23){
    offLED4();
    currentCommand = -1;
  }

  // Compartment 5 commands
  else if(currentCommand == 24) {
    digitalWrite(relayPin5, LOW);
    currentCommand = -1;
  }
  else if(currentCommand == 25) {
    digitalWrite(relayPin5, HIGH);
    currentCommand = -1;
  }
  else if(currentCommand == 26) {
    setColor5(255, 0, 0);
    currentCommand = -1;
  }
  else if(currentCommand == 27) {
    setColor5(0, 255, 0);
    currentCommand = -1;
  }
  else if(currentCommand == 28) {
    detectItem5();
    currentCommand = -1;
  }
    else if(currentCommand == 29){
    offLED5();
    currentCommand = -1;
  }

  // Compartment 6 commands
  else if(currentCommand == 30) {
    digitalWrite(relayPin6, LOW);
    currentCommand = -1;
  }
  else if(currentCommand == 31) {
    digitalWrite(relayPin6, HIGH);
    currentCommand = -1;
  }
  else if(currentCommand == 32) {
    setColor6(255, 0, 0);
    currentCommand = -1;
  }
  else if(currentCommand == 33) {
    setColor6(0, 255, 0);
    currentCommand = -1;
  }
  else if(currentCommand == 34) {
    detectItem6();
    currentCommand = -1;
  }
    else if(currentCommand == 35){
    offLED6();
    currentCommand = -1;
  }

  // Compartment 7 commands
  else if(currentCommand == 36) {
    digitalWrite(relayPin7, LOW);
    currentCommand = -1;
  }
  else if(currentCommand == 37) {
    digitalWrite(relayPin7, HIGH);
    currentCommand = -1;
  }
  else if(currentCommand == 38) {
    setColor7(255, 0, 0);
    currentCommand = -1;
  }
  else if(currentCommand == 39) {
    setColor7(0, 255, 0);
    currentCommand = -1;
  }
  else if(currentCommand == 40) {
    detectItem7();
    currentCommand = -1;
  }
  else if(currentCommand == 41){
    offLED7();
    currentCommand = -1;
  }

  // Compartment 8 commands
  else if(currentCommand == 42) {
    digitalWrite(relayPin8, LOW);
    currentCommand = -1;
  }
  else if(currentCommand == 43) {
    digitalWrite(relayPin8, HIGH);
    currentCommand = -1;
  }
  else if(currentCommand == 44) {
    setColor8(255, 0, 0);
    currentCommand = -1;
  }
  else if(currentCommand == 45) {
    setColor8(0, 255, 0);
    currentCommand = -1;
  }
  else if(currentCommand == 46) {
    detectItem8();
    currentCommand = -1;
  }
    else if(currentCommand == 47){
    offLED8();
    currentCommand = -1;
  }
  

  // Compartment 9 commands
  else if(currentCommand == 48) {
    digitalWrite(relayPin9, LOW);
    currentCommand = -1;
  }
  else if(currentCommand == 49) {
    digitalWrite(relayPin9, HIGH);
    currentCommand = -1;
  }
  else if(currentCommand == 50) {
    setColor9(255, 0, 0);
    currentCommand = -1;
  }
  else if(currentCommand == 51) {
    setColor9(0, 255, 0);
    currentCommand = -1;
  }
  else if(currentCommand == 52) {
    detectItem9();
    currentCommand = -1;
  }
  else if(currentCommand == 53){
    offLED9();
    currentCommand = -1;
  }
}

void receiveCommand() {
  // Get and return command from Raspberry Pi
  if(Serial.available()) {
    int sent = Serial.readStringUntil('\n').toInt();
    Serial.println("ok");
    currentCommand = sent;
  }
}

void sendResponse(String response) {
  // Send response to the Raspberry Pi
  Serial.println(response);    
}

void setColor1(int R, int G, int B) {
  analogWrite(redPin1,   R);
  analogWrite(greenPin1, G);
}

void setColor2(int R, int G, int B) {
  analogWrite(redPin2,   R);
  analogWrite(greenPin2, G);
}

void setColor3(int R, int G, int B) {
  analogWrite(redPin3,   R);
  analogWrite(greenPin3, G);
}

void setColor4(int R, int G, int B) {
  analogWrite(redPin4,   R);
  analogWrite(greenPin4, G);
}

void setColor5(int R, int G, int B) {
  analogWrite(redPin5,   R);
  analogWrite(greenPin5, G);
}

void setColor6(int R, int G, int B) {
  analogWrite(redPin6,   R);
  analogWrite(greenPin6, G);
}

void setColor7(int R, int G, int B) {
  analogWrite(redPin7,   R);
  analogWrite(greenPin7, G);
}

void setColor8(int R, int G, int B) {
  analogWrite(redPin8,   R);
  analogWrite(greenPin8, G);
}

void setColor9(int R, int G, int B) {
  analogWrite(redPin9,   R);
  analogWrite(greenPin9, G);
}

void detectItem1() {
  int sensorOut = digitalRead(irPin1);
  if (sensorOut == LOW){
    Serial.println("1");
  }
  else{
    Serial.println("0");
  }
}

void detectItem2() {
  int sensorOut = digitalRead(irPin2);
  if (sensorOut == LOW){
    Serial.println("1");
  }
  else{
    Serial.println("0");
  }
}

void detectItem3() {
  int sensorOut = digitalRead(irPin3);
  if (sensorOut == LOW){
    Serial.println("1");
  }
  else{
    Serial.println("0");
  }
}

void detectItem4() {
  int sensorOut = digitalRead(irPin4);
  if (sensorOut == LOW){
    Serial.println("1");
  }
  else{
    Serial.println("0");
  }
}

void detectItem5() {
  int sensorOut = digitalRead(irPin5);
  if (sensorOut == LOW){
    Serial.println("1");
  }
  else{
    Serial.println("0");
  }
}

void detectItem6() {
  int sensorOut = digitalRead(irPin6);
  if (sensorOut == LOW){
    Serial.println("1");
  }
  else{
    Serial.println("0");
  }
}

void detectItem7() {
  int sensorOut = digitalRead(irPin7);
  if (sensorOut == LOW){
    Serial.println("1");
  }
  else{
    Serial.println("0");
  }
}

void detectItem8() {
  int sensorOut = digitalRead(irPin8);
  if (sensorOut == LOW){
    Serial.println("1");
  }
  else{
    Serial.println("0");
  }
}

void detectItem9() {
  int sensorOut = digitalRead(irPin9);
  if (sensorOut == LOW){
    Serial.println("1");
  }
  else{
    Serial.println("0");
  }
}

void offLED1(){
  digitalWrite(redPin1, LOW);
  digitalWrite(greenPin1, LOW);
}

void offLED2(){
  digitalWrite(redPin2, LOW);
  digitalWrite(greenPin2, LOW);
}

void offLED3(){
  digitalWrite(redPin3, LOW);
  digitalWrite(greenPin3, LOW);
}

void offLED4(){
  digitalWrite(redPin4, LOW);
  digitalWrite(greenPin4, LOW);
}

void offLED5(){
  digitalWrite(redPin5, LOW);
  digitalWrite(greenPin5, LOW);
}

void offLED6(){
  digitalWrite(redPin6, LOW);
  digitalWrite(greenPin6, LOW);
}

void offLED7(){
  digitalWrite(redPin7, LOW);
  digitalWrite(greenPin7, LOW);
}

void offLED8(){
  digitalWrite(redPin8, LOW);
  digitalWrite(greenPin8, LOW);
}

void offLED9(){
  digitalWrite(redPin9, LOW);
  digitalWrite(greenPin9, LOW);
}