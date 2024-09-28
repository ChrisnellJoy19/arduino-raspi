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
  int sensorOut = digitalRead(irPin2);
  if (sensorOut == LOW){
    Serial.println("1");
  }
  else{
    Serial.println("0");
  }
}