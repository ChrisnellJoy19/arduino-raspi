const int PIN_RED   = 9;  // Red LED on pin 9
const int PIN_GREEN = 10; // Green LED on pin 10
const int PIN_BLUE  = 11; // Blue LED on Pin 11
const int trigPin = 7;
const int echoPin = 8;
const int relayPin= A1;

int currentCommand = -1;

void setColor(int R, int G, int B) {
  analogWrite(PIN_RED,   R);
  analogWrite(PIN_GREEN, G);
  analogWrite(PIN_BLUE,  B);
}

void setup() {
  Serial.begin(9600);
  pinMode(PIN_RED,   OUTPUT);
  pinMode(PIN_GREEN, OUTPUT);
  pinMode(PIN_BLUE,  OUTPUT);
  pinMode(trigPin, OUTPUT);  
	pinMode(echoPin, INPUT);  
  pinMode(relayPin, OUTPUT);
}

void loop() {
  if(currentCommand == -1) {
    receiveCommand();
  }

  else if(currentCommand == 0) {
    turnOffRelay();
    //unlock
    currentCommand = -1;
  }

  else if(currentCommand == 1) {
    turnOnRelay();
    //lock
    currentCommand = -1;
  }

  else if(currentCommand == 2) {
    setColorRed();
    currentCommand = -1;
  }

  else if(currentCommand == 3) {
    setColorGreen();
    currentCommand = -1;
  }

  else if(currentCommand == 4) {
    float distance = getDistance();
    Serial.println(distance);
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

void turnOffRelay() {
  //unlock
  digitalWrite(relayPin, LOW);
  delay(100);
}

void turnOnRelay() {
  //lock
  digitalWrite(relayPin, HIGH);
  delay(100);
}

void setColorRed() {
  setColor(255, 0, 0);
}

void setColorGreen() {
  setColor(0, 255, 0);
}

float getDistance() {
  digitalWrite(trigPin, LOW);  
	delayMicroseconds(2);  
	digitalWrite(trigPin, HIGH);  
	delayMicroseconds(10);  
	digitalWrite(trigPin, LOW);
  long duration = pulseIn(echoPin, HIGH);
  float distance = (duration*.0343)/2;
  return distance;
}
