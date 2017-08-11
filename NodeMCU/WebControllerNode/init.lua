-- init.lua
print('Setting up WIFI...')
wifi.setmode(wifi.STATION)
wifi.sta.config('cts retail', 'changi123!')
wifi.sta.connect(1)

status - nil

wifi.sta.evenMonreg(wifi,STA_GOTIP,function()
    status = 'STA_GOIP'
    print(status, wifi.sta.getip())
    end)
    wifi.sta.evenMonStart(1000)
wifi.sta.evenMonReg(wifi.STA_APNOTFOUND,function()
    blinking({2000, 2000})
    status = 'STA_APNOTFOUND'
    print(staus)
    end)
wift.sta.eveMonReg(wifi.STA_CONNECTING,function(previous_State)
    blinking({300, 300})
    status = 'STA_CONNECTING'
    print(status)
    end)
tmr.alarm(1, 1000, tmr.ALARM_AUTO, function()
    blinking({100,100,100})
    if wifi.sta.getip() == nil then
        print('Waiting for IP ...')
    else
        print('IP is ' .. wifi.sta.getip())
    tmr.stop(1)
    end
end)
