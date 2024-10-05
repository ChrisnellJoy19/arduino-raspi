const int redPin1   = 2; 
const int greenPin1 = 3; 
const int bluePin1  = 4; 
const int irPin1 = 5;
const int relayPin1 = 6;

const int redPin2   = 7; 
const int greenPin2 = 8; 
const int bluePin2  = 9; 
const int irPin2 = 10;
const int relayPin2 = 11;


const int redPin3   = 12; 
const int greenPin3 = 13; 
const int bluePin3  = 14; 
const int irPin3 = 15;
const int relayPin3 = 16;

const int redPin4   = __; 
const int greenPin4 = __; 
const int bluePin4  = __; 
const int irPin4 = __;
const int relayPin4 = __;

const int redPin5   = __; 
const int greenPin5 = __; 
const int bluePin5  = __; 
const int irPin5 = __;
const int relayPin5 = __;

const int redPin6   = __; 
const int greenPin6 = __; 
const int bluePin6  = __; 
const int irPin6 = __;
const int relayPin6 = __;

const int redPin7   = __; 
const int greenPin7 = __; 
const int bluePin7  = __; 
const int irPin7 = __;
const int relayPin7 = __;

const int redPin8   = __; 
const int greenPin8 = __; 
const int bluePin8  = __; 
const int irPin8 = __;
const int relayPin8 = __;

const int redPin9   = __; 
const int greenPin9 = __; 
const int bluePin9  = __; 
const int irPin9 = __;
const int relayPin9 = __;

int currentCommand = -1;

void setup() {
  Serial.begin(9600);
  pinMode(redPin1,   OUTPUT);
  pinMode(greenPin1, OUTPUT);
  pinMode(bluePin1,  OUTPUT);
  pinMode(irPin1, INPUT);  
  pinMode(relayPin1, OUTPUT);

  pinMode(redPin2,   OUTPUT);
  pinMode(greenPin2, OUTPUT);
  pinMode(bluePin2,  OUTPUT);
  pinMode(irPin2, INPUT);  
  pinMode(relayPin2, OUTPUT);

  pinMode(redPin3,   OUTPUT);
  pinMode(greenPin3, OUTPUT);
  pinMode(bluePin3,  OUTPUT);
  pinMode(irPin3, INPUT);  
  pinMode(relayPin3, OUTPUT);

  pinMode(redPin4,   OUTPUT);
  pinMode(greenPin4, OUTPUT);
  pinMode(bluePin4,  OUTPUT);
  pinMode(irPin4, INPUT);  
  pinMode(relayPin4, OUTPUT);

  pinMode(redPin5,   OUTPUT);
  pinMode(greenPin5, OUTPUT);
  pinMode(bluePin5,  OUTPUT);
  pinMode(irPin5, INPUT);  
  pinMode(relayPin5, OUTPUT);

  pinMode(redPin6,   OUTPUT);
  pinMode(greenPin6, OUTPUT);
  pinMode(bluePin6,  OUTPUT);
  pinMode(irPin6, INPUT);  
  pinMode(relayPin6, OUTPUT);
  
  pinMode(redPin7,   OUTPUT);
  pinMode(greenPin7, OUTPUT);
  pinMode(bluePin7,  OUTPUT);
  pinMode(irPin7, INPUT);  
  pinMode(relayPin7, OUTPUT);

  pinMode(redPin8,   OUTPUT);
  pinMode(greenPin8, OUTPUT);
  pinMode(bluePin8,  OUTPUT);
  pinMode(irPin8, INPUT);  
  pinMode(relayPin8, OUTPUT);
  
  pinMode(redPin9,   OUTPUT);
  pinMode(greenPin9, OUTPUT);
  pinMode(bluePin9,  OUTPUT);
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

  // Compartment 2 commands
  else if(currentCommand == 5) {
    digitalWrite(relayPin2, LOW);
    currentCommand = -1;
  }
  else if(currentCommand == 6) {
    digitalWrite(relayPin2, HIGH);
    currentCommand = -1;
  }
  else if(currentCommand == 7) {
    setColor2(255, 0, 0);
    currentCommand = -1;
  }
  else if(currentCommand == 8) {
    setColor2(0, 255, 0);
    currentCommand = -1;
  }
  else if(currentCommand == 9) {
    detectItem2();
    currentCommand = -1;
  }

  // Compartment 3 commands
  else if(currentCommand == 10) {
    digitalWrite(relayPin3, LOW);
    currentCommand = -1;
  }
  else if(currentCommand == 11) {
    digitalWrite(relayPin3, HIGH);
    currentCommand = -1;
  }
  else if(currentCommand == 12) {
    setColor3(255, 0, 0);
    currentCommand = -1;
  }
  else if(currentCommand == 13) {
    setColor3(0, 255, 0);
    currentCommand = -1;
  }
  else if(currentCommand == 14) {
    detectItem3();
    currentCommand = -1;
  }

  // Compartment 4 commands
  else if(currentCommand == 15) {
    digitalWrite(relayPin4, LOW);
    currentCommand = -1;
  }
  else if(currentCommand == 16) {
    digitalWrite(relayPin4, HIGH);
    currentCommand = -1;
  }
  else if(currentCommand == 17) {
    setColor4(255, 0, 0);
    currentCommand = -1;
  }
  else if(currentCommand == 18) {
    setColor4(0, 255, 0);
    currentCommand = -1;
  }
  else if(currentCommand == 19) {
    detectItem4();
    currentCommand = -1;
  }

  // Compartment 5 commands
  else if(currentCommand == 20) {
    digitalWrite(relayPin5, LOW);
    currentCommand = -1;
  }
  else if(currentCommand == 21) {
    digitalWrite(relayPin5, HIGH);
    currentCommand = -1;
  }
  else if(currentCommand == 22) {
    setColor5(255, 0, 0);
    currentCommand = -1;
  }
  else if(currentCommand == 23) {
    setColor5(0, 255, 0);
    currentCommand = -1;
  }
  else if(currentCommand == 24) {
    detectItem5();
    currentCommand = -1;
  }

  // Compartment 6 commands
  else if(currentCommand == 25) {
    digitalWrite(relayPin6, LOW);
    currentCommand = -1;
  }
  else if(currentCommand == 26) {
    digitalWrite(relayPin6, HIGH);
    currentCommand = -1;
  }
  else if(currentCommand == 27) {
    setColor6(255, 0, 0);
    currentCommand = -1;
  }
  else if(currentCommand == 28) {
    setColor6(0, 255, 0);
    currentCommand = -1;
  }
  else if(currentCommand == 29) {
    detectItem6();
    currentCommand = -1;
  }

  // Compartment 7 commands
  else if(currentCommand == 30) {
    digitalWrite(relayPin7, LOW);
    currentCommand = -1;
  }
  else if(currentCommand == 31) {
    digitalWrite(relayPin7, HIGH);
    currentCommand = -1;
  }
  else if(currentCommand == 32) {
    setColor7(255, 0, 0);
    currentCommand = -1;
  }
  else if(currentCommand == 33) {
    setColor7(0, 255, 0);
    currentCommand = -1;
  }
  else if(currentCommand == 34) {
    detectItem7();
    currentCommand = -1;
  }

  // Compartment 8 commands
  else if(currentCommand == 35) {
    digitalWrite(relayPin8, LOW);
    currentCommand = -1;
  }
  else if(currentCommand == 36) {
    digitalWrite(relayPin8, HIGH);
    currentCommand = -1;
  }
  else if(currentCommand == 37) {
    setColor8(255, 0, 0);
    currentCommand = -1;
  }
  else if(currentCommand == 38) {
    setColor8(0, 255, 0);
    currentCommand = -1;
  }
  else if(currentCommand == 39) {
    detectItem8();
    currentCommand = -1;
  }

  // Compartment 9 commands
  else if(currentCommand == 40) {
    digitalWrite(relayPin9, LOW);
    currentCommand = -1;
  }
  else if(currentCommand == 41) {
    digitalWrite(relayPin9, HIGH);
    currentCommand = -1;
  }
  else if(currentCommand == 42) {
    setColor9(255, 0, 0);
    currentCommand = -1;
  }
  else if(currentCommand == 43) {
    setColor9(0, 255, 0);
    currentCommand = -1;
  }
  else if(currentCommand == 44) {
    detectItem9();
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
  analogWrite(bluePin1,  B);
}

void setColor2(int R, int G, int B) {
  analogWrite(redPin2,   R);
  analogWrite(greenPin2, G);
  analogWrite(bluePin2,  B);
}

void setColor3(int R, int G, int B) {
  analogWrite(redPin3,   R);
  analogWrite(greenPin3, G);
  analogWrite(bluePin3,  B);
}

void setColor4(int R, int G, int B) {
  analogWrite(redPin4,   R);
  analogWrite(greenPin4, G);
  analogWrite(bluePin4,  B);
}

void setColor5(int R, int G, int B) {
  analogWrite(redPin5,   R);
  analogWrite(greenPin5, G);
  analogWrite(bluePin5,  B);
}

void setColor6(int R, int G, int B) {
  analogWrite(redPin6,   R);
  analogWrite(greenPin6, G);
  analogWrite(bluePin6,  B);
}

void setColor7(int R, int G, int B) {
  analogWrite(redPin7,   R);
  analogWrite(greenPin7, G);
  analogWrite(bluePin7,  B);
}

void setColor8(int R, int G, int B) {
  analogWrite(redPin8,   R);
  analogWrite(greenPin8, G);
  analogWrite(bluePin8,  B);
}

void setColor9(int R, int G, int B) {
  analogWrite(redPin9,   R);
  analogWrite(greenPin9, G);
  analogWrite(bluePin9,  B);
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