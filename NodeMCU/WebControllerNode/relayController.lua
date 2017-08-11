-- Wemos Relay.lua
-- John Longworth December 2016
-- For use with WeMos single relay shield

local SSID = "cts retail"      -- Enter your SSID
local pwd  = "changi123!"      -- Enter your password

wifi.setmode(wifi.STATIONAP)
wifi.sta.config(SSID,pwd)
wifi.sta.autoconnect(1)
wifi.sta.setip({ip="192.168.0.197"})
ip = wifi.sta.getip()
print("Key this IP address "..ip.." into a browser")

local pin = 1
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
        local _on,_off = "",""
        if(_GET.pin == "ON1")then
            gpio.write(pin, gpio.HIGH);
        elseif(_GET.pin == "OFF1")then
            gpio.write(pin, gpio.LOW);
        end
        client:send(buf)
        client:close()
    end)
end)

