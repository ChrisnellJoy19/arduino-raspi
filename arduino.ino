const int PIN_RED   = 8;  // Red LED on pin 9
const int PIN_GREEN = 9; // Green LED on pin 10
const int PIN_BLUE  = 10; // Blue LED on Pin 11
const int LED = 13; // Onboard LED pin
const int irPin = 7;  // This is our input pin (IR LED at pin 7)
int sensorOut = HIGH;  // HIGH at No Obstacle
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
  pinMode(LED, OUTPUT);
  pinMode(irPin, INPUT);  
  pinMode(relayPin, OUTPUT);
}

void loop() {
  if(currentCommand == -1) {
    receiveCommand();
  }

  // Compartment 1 Commands
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
    //item detected
    detectItem();
    currentCommand = -1;
  }

  // Add other compartment commands
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

void detectItem() {
  sensorOut = digitalRead(irPin);
  if (sensorOut == LOW){
    Serial.println("item detected");
    digitalWrite(LED, HIGH);
    }
  else{
    Serial.println("No item detected");
    digitalWrite(LED, LOW);
    }
  delay(200);
}