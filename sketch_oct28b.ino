char incomingByte = "0"; // for incoming serial data

void setup() {
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  Serial.begin(115200); // opens serial port, sets data rate to 9600 bps
        digitalWrite(5, HIGH);
      digitalWrite(6, HIGH);
      digitalWrite(7, HIGH);
      digitalWrite(8, HIGH);
}

void loop() {


  // send data only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();

    Serial.print("I received: ");
    Serial.println(incomingByte);


    if (incomingByte == 'l' ) {
     
      digitalWrite(5, LOW);
      Serial.println("low");
     

    }

    if (incomingByte == 'm' ) {
  
      digitalWrite(5, LOW);
      digitalWrite(6, LOW);

      Serial.println("med");
  


    }

    if (incomingByte == 'h' ) {

      digitalWrite(5, LOW);
      digitalWrite(6, LOW);
      digitalWrite(7, LOW);
      digitalWrite(8, LOW);
      Serial.println("high");




    }



    if (incomingByte == 'd' ) {
          
      digitalWrite(5, HIGH);
      digitalWrite(6, HIGH);
      digitalWrite(7, HIGH);
      digitalWrite(8, HIGH);
      Serial.println("down");

 



    }

  }
}
