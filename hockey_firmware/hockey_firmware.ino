#include <avr/io.h>
#include <avr/interrupt.h>
#include <Servo.h>
#include <usbdrv.h>

#define RQ_SET_STATUS 0
#define RQ_GET_SCORE1 1
#define RQ_GET_SCORE2 2
#define RQ_GET_STATUS 3

Servo myservo1;
Servo myservo2;

enum { ON, OFF };

unsigned long Watch, _micro, time = micros();
unsigned int Clock = 0, R_clock;
boolean Reset = false, Stop = false, Paused = false;
volatile boolean timeFlag = false;

uint8_t scorePlayer1 = 0 ;
uint8_t scorePlayer2 = 0;
uint8_t servoStatus;
uint8_t minutes;
uint8_t game_status = 0;
bool isLoop = false;
//////////////////////////////////////////////////////////////////////
usbMsgLen_t usbFunctionSetup(uint8_t data[8])
{
  usbRequest_t *rq = (usbRequest_t*)data;

  if (rq->bRequest == RQ_SET_STATUS)
  {
    game_status = rq->wValue.bytes[0];
    isLoop = false;
    myservo1.write(90);
    myservo2.write(90);
    return 0;
  }
  else if (rq->bRequest == RQ_GET_STATUS)
  {
    /* point usbMsgPtr to the data to be returned to host */
    if(isLoop)
      game_status = 1;
    else
      game_status = 0;
    usbMsgPtr = (uint8_t*) &game_status;

    /* return the number of bytes of data to be returned to host */
    return sizeof(game_status);
  }
    else if (rq->bRequest == RQ_GET_SCORE1)
  {
    /* point usbMsgPtr to the data to be returned to host */
    usbMsgPtr = (uint8_t*) &scorePlayer1;

    /* return the number of bytes of data to be returned to host */
    return sizeof(scorePlayer1);
  }
    else if (rq->bRequest == RQ_GET_SCORE2)
  {
    /* point usbMsgPtr to the data to be returned to host */
    usbMsgPtr = (uint8_t*) &scorePlayer2;

    /* return the number of bytes of data to be returned to host */
    return sizeof(scorePlayer2);
  }

  return 0;   /* nothing to do; return no data back to host */
}

//////////////////////////////////////////////////////////////////////


void setup() 
{
  // ตั้งค่าความเร็วในการรับ-ส่งข้อมูล ค่ามาตรฐาน คือ 9600
  Serial.begin(9600);
  pinMode(PIN_PB0, OUTPUT); //servo 1
  pinMode(PIN_PB1, OUTPUT); // servo 2
  pinMode(PIN_PC1, INPUT); // IR 1
  pinMode(PIN_PD0, INPUT); // IR 2
  pinMode(PIN_PC0, INPUT); // coin insert
  myservo1.attach(PIN_PB0);
  myservo2.attach(PIN_PB1);
  scorePlayer1 = 0;
  scorePlayer2 = 0;
  myservo1.write(90);
  myservo2.write(90);

  usbInit();
  usbDeviceDisconnect();
  delay(300);
  usbDeviceConnect();
}

void Player1() {
  static uint32_t ts1 = 0;
  int sensorPlayer1 = digitalRead(PIN_PC1);
  if (sensorPlayer1 == LOW) {
    if (millis() - ts1 >= 700 ) {
      ts1 = millis();
      scorePlayer1 += 1;
    }
  }
}


void Player2() {
  static uint32_t ts2 = 0;
  int sensorPlayer2 = digitalRead(PIN_PD0);
  if (sensorPlayer2 == LOW) {
    if (millis() - ts2 >= 800) {
      ts2 = millis();
      scorePlayer2 += 1;
    }
  }
}

void servo() {
  static uint32_t ts3 = 0;
  if(isLoop) {
    if (millis() - ts3 >= 100) {
      ts3 = millis();
      myservo1.write(45);
      myservo2.write(45);
    }
  }
}


void loop() {
  usbPoll();
  if (isLoop == false) {
    int sensorCoin = digitalRead(PIN_PC0);
    if (sensorCoin == LOW) {
      isLoop = true;
      scorePlayer1 = 0;
      scorePlayer2 = 0;
    }
  }
  else {
    servo();
    Player1();
    Player2();
    Serial.print("isLoop ");
    Serial.println(isLoop);
    Serial.print("score 1: ");
    Serial.print(scorePlayer1);
    Serial.print("     score 2: ");    
    Serial.println(scorePlayer2);
  }
}

