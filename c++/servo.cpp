#include <stdio.h>
#include <errno.h>
#include <string.h>

#include <wiringPi.h>

int pwmPin = 18;

int main()
{

    wiringPiSetupGpio ();
    pinMode (pwmPin, PWM_OUTPUT);
    pwmSetMode (PWM_MODE_MS);
    pwmSetRange (2000);

    pwmSetClock (192);
    pwmWrite(pwmPin, 150);
    delay(1000);
    pwmWrite(pwmPin, 200);  

    return 0;
}