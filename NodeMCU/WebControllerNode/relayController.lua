-- Wemos Relay.lua
-- HUANGSHUHAO-11-AUG-2017
-- For using SIMBANK relay control module

local SSID = "dlink-BC40"      -- Enter your SSID
local pwd  = "ueqid58778"      -- Enter your password

wifi.setmode(wifi.STATIONAP)
wifi.sta.config(SSID,pwd)
wifi.sta.autoconnect(1)
wifi.sta.setip({ip="192.168.0.197"})
ip = wifi.sta.getip()
print("Key this IP address "..ip.." into a browser")

local pin1 = 1
local pin2 = 2
local pin3 = 3
local pin4 = 4
local pin5 = 5
local pin6 = 6
local pin7 = 7
local pin8 = 8
local pin9 = 9
gpio.mode(pin, gpio.OUTPUT)

srv=net.createServer(net.TCP)
srv:listen(80,function(conn)
    conn:on("receive", function(client,request)
        local buf = "";
        local _, _, method, path, vars = string.find(request, "([A-Z]+) (.+)?(.+) HTTP");
        if(method == nil)then
            _, _, method, path = string.find(request, "([A-Z]+) (.+) HTTP");
        end
        local _GET = {}
        if (vars ~= nil)then
            for k, v in string.gmatch(vars, "(%w+)=(%w+)&*") do
                _GET[k] = v
            end
        end
        buf = "<!DOCTYPE html>"
                .."<HTML><HEAD><TITLE>NodeMCU ESP8266 Relay Control</TITLE></HEAD><BODY><CENTER>"
                .."<h1>WeMos Relay Control</h1>"
                .."<p><h2>Switch &nbsp<a href=\"?pin=ON1\"><button style='height:40px;width:100px;background-color:green;color:white'>ON</button>"
                .."</a>&nbsp;<a href=\"?pin=OFF1\"><button style='height:40px;width:100px;background-color:red; color:white'>OFF</button></a></h2></p>"
                .."<BR><p>HUANG SHUHAO 11-AUG-2017-SG</p>"
                .."</CENTER></BODY></HTML>"
        --  pin1
        local _on,_off = "",""
        if(_GET.pin1 == "ON1")then
            gpio.write(pin1, gpio.HIGH);
        elseif(_GET.pin1 == "OFF1")then
            gpio.write(pin1, gpio.LOW);
        end
        --  pin2
        local _on,_off = "",""
        if(_GET.pin2 == "ON2")then
            gpio.write(pin2, gpio.HIGH);
        elseif(_GET.pin2 == "OFF2")then
            gpio.write(pin2, gpio.LOW);
        end
        --  pin3
        local _on,_off = "",""
        if(_GET.pin3 == "ON3")then
            gpio.write(pin3, gpio.HIGH);
        elseif(_GET.pin3 == "OFF3")then
            gpio.write(pin3, gpio.LOW);
        end
        --  pin4
        local _on,_off = "",""
        if(_GET.pin4 == "ON4")then
            gpio.write(pin4, gpio.HIGH);
        elseif(_GET.pin4 == "OFF4")then
            gpio.write(pin4, gpio.LOW);
        end
        --  pin5
        local _on,_off = "",""
        if(_GET.pin5 == "ON5")then
            gpio.write(pin5, gpio.HIGH);
        elseif(_GET.pin5 == "OFF5")then
            gpio.write(pin5, gpio.LOW);
        end
        --  pin6
        local _on,_off = "",""
        if(_GET.pin6 == "ON6")then
            gpio.write(pin6, gpio.HIGH);
        elseif(_GET.pin6 == "OFF6")then
            gpio.write(pin6, gpio.LOW);
        end
        --  pin7
        local _on,_off = "",""
        if(_GET.pin7 == "ON1")then
            gpio.write(pin7, gpio.HIGH);
        elseif(_GET.pin7 == "OFF1")then
            gpio.write(pin7, gpio.LOW);
        end
        --  pin8
        local _on,_off = "",""
        if(_GET.pin8 == "ON1")then
            gpio.write(pin8, gpio.HIGH);
        elseif(_GET.pin8 == "OFF1")then
            gpio.write(pin8, gpio.LOW);
        end
        --  pin9
        local _on,_off = "",""
        if(_GET.pin9 == "ON1")then
            gpio.write(pin9, gpio.HIGH);
        elseif(_GET.pin9 == "OFF1")then
            gpio.write(pin9, gpio.LOW);
        end
        client:send(buf)
        client:close()
    end)
end)

