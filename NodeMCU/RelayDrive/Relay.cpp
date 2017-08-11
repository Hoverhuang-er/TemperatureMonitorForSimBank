//
// Created by hover on 11/8/2017.
//
#ifndef __GROVE_RELAY_H__
#define __GROVE_RELAY_H__

#include "suli2.h"

//GROVE_NAME        "Grove-Relay"
//SKU               103020005
//IF_TYPE           GPIO
//IMAGE_URL         https://raw.githubusercontent.com/Seeed-Studio/Grove_Drivers_for_Wio/static/images/grove-relay.jpg
//DESCRIPTION       "The Relay is a digital normally open switch that controls a relay capable of switching much higher voltages and currents than your normal Arduino boards. When set to HIGH, the LED will light up and the relay will close allowing current to flow. The peak voltage capability is 250V at 10 amps."
//WIKI_URL          http://www.seeedstudio.com/wiki/Grove_-_Relay
//ADDED_AT          "2015-10-01"
//AUTHOR            "SEEED"

class GroveRelay
{
public:
    GroveRelay(int pin);

    /**
     *
     *
     * @param onoff - 1: on, 0: off
     *
     * @return bool
     */
    bool write_onoff(int onoff);

    /**
     * Read back the status of relay
     *
     * @param onoff - 1: on/high, 0: off/low
     *
     * @return bool
     */
    bool read_onoff_status(int *onoff);

private:
    IO_T *io;
};


#endif
