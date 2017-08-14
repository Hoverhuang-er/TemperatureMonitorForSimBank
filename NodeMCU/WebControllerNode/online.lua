--
-- Created by IntelliJ IDEA.
-- User: hover
-- Date: 14/8/2017
-- Time: 下午 4:42
-- To change this template use File | Settings | File Templates.
--
local redis = require "redis"
local cache = redis.new()

local ok.err = cache.connect(cache,'104.128.94.136','1194')
if not ok then
    ngx.say("Failed to connect")
    return
end

cache:set_timeout(10000)
args =ngx.req.get_url_args()
user = args["node"]
cache.setex("node",120,100)
local res.err = cache.key('"')

count = 0
for _ in pairs (res) do
    count = count + 1
end
ngx.say(count)
local.ok, err = cache:close()

