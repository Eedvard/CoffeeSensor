
double arvo = 0;
int LVL = 3;
int TH = 100;
int ledsOn = 0;
int M = 0;

void setup(){
Serial.begin(9600);
pinMode(10, OUTPUT);
pinMode(11, OUTPUT);
pinMode(12, OUTPUT);
pinMode(13, OUTPUT);
}

void loop(){
  if(analogRead(3) > 100 && LVL != 3)
  {
   digitalWrite(10,LOW);
   digitalWrite(11,LOW);
   digitalWrite(12,LOW);
   digitalWrite(13,LOW);
   M = 1;
  }
  else{
    if (M == 1)
      for(int i = 0; i < ledsOn; i++)
    digitalWrite(10+i,HIGH);
    M = 0;
    delay(1000);
    arvo = analogRead(LVL);
    if (LVL == 1)
      arvo = arvo*0.25;
    else if (LVL == 2)
      arvo = arvo*0.5;
    else if (LVL == 3)
      arvo = arvo*0.25;
    
    if (arvo < TH){
      digitalWrite(13-LVL,HIGH);
      if (LVL > 0) LVL--;
      if (ledsOn < 4) ledsOn++;
    }
    else{
      digitalWrite(13-LVL,LOW);
      if (LVL < 3) LVL++;
      if (ledsOn > 0) ledsOn--;
    }
  }
  if(Serial.available())
  {
    int asd = Serial.read();
    if(asd == 0){Serial.write(ledsOn);}
    }
  delay(1000);
}
