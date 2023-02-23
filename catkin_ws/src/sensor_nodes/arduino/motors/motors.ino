// motor 1
int INB_1 = 2;
int INA_1 = 3;
int EN_1 = 4;

#define outputA 6
#define outputB 7

int counter = 0; 
int aState;
int aLastState; 

void setup() {
  // put your setup code here, to run once:
  pinMode(INB_1, OUTPUT);
  pinMode(INA_1, OUTPUT);
  pinMode(EN_1, OUTPUT);

  digitalWrite(EN_1, HIGH);
  analogWrite(INA_1, 0);
  digitalWrite(INB_1, 1);
 

  pinMode (outputA,INPUT);
  pinMode (outputB,INPUT);

  Serial.begin (9600);
  // Reads the initial state of the outputA
  aLastState = digitalRead(outputA);   


}

void loop() {

  aState = digitalRead(outputA); // Reads the "current" state of the outputA
   // If the previous and the current state of the outputA are different, that means a Pulse has occured
   if (aState != aLastState){     
     // If the outputB state is different to the outputA state, that means the encoder is rotating clockwise
     if (digitalRead(outputB) != aState) { 
       counter ++;
     } else {
       counter --;
     }
     Serial.print("Position: ");
     Serial.println(counter);
   } 
   aLastState = aState; // Updates the previous state of the outputA with the current state    
}


 



