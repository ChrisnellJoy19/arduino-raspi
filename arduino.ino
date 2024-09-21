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
    digitalWrite(relayPin1, LOW);
    currentCommand = -1;
  }
  else if(currentCommand == 6) {
    digitalWrite(relayPin1, HIGH);
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
