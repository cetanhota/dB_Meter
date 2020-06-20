const int MIC = 0; //the microphone amplifier output is connected to pin A0
int adc;
int dB, PdB; //the variable that will hold the value read from the microphone each time

void setup() {
Serial.begin(115200); //sets the baud rate at 9600 so we can check the values the microphone is obtaining on the Serial Monitor
  pinMode(13, OUTPUT);
}

void loop(){
  

  PdB = dB; //Store the previous of dB here
  
adc= analogRead(MIC); //Read the ADC value from amplifer 
//Serial.println (adc);//Print ADC for initial calculation 
float dB = (adc+83.2073) / 11.003; //Convert ADC value to dB using Regression values

//if (PdB!=dB)
if (dB >= 45)
{
Serial.println (dB);
delay(500);
}

}
