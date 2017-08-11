//
// Created by hover on 11/8/2017.
//

#ifndef TEMPERATUREMONITORFORSIMBANK_RELAYDRIVE_H
#define TEMPERATUREMONITORFORSIMBANK_RELAYDRIVE_H
#include "suli2.h"
#include "grove_relay.h"

GroveRelay::GroveRelay(int pin)
{
    this->io = (IO_T *)malloc(sizeof(IO_T));

    suli_pin_init(io, pin, SULI_OUTPUT);
}

bool GroveRelay::write_onoff(int onoff)
{
    suli_pin_write(io, onoff);
    return true;
}

bool GroveRelay::read_onoff_status(int *onoff)
{
    *onoff = suli_pin_read(io);
    return true;
}

#endif //TEMPERATUREMONITORFORSIMBANK_RELAYDRIVE_H
