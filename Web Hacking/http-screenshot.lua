-- Copyright (C) 2018 esapromesa
-- .nse

-- The Head Section --
description = [[
    Gets a screenshot from the host
]]

author = "esapromesa"

categories = {"default", "discovery", "safe"}

license = "http://iver.iptime.org"

-- The Rule Section --
local shortport = require "shortport"
portrule = shortport.http

-- The Action Section --
action = function(host, port)
    local prefix = "http"
    local ssl = port.version.service_tunnel
    if ssl == "ssl" then
        prefix = "https"
    end

    local filename = "fail.png"
    local filename = host.ip .. ":" .. port.number .. ".png"

    local cmd = "mkdir ./http_screenshot"
    local execute = os.execute(cmd)

    if port.number == 80 or port.number == 443 then
        cmd = "cutycapt --url=" .. prefix .. "://" .. host.ip .. " --out=./http_screenshot/" .. filename .. " --max-wait=3000 --insecure"
    else
        cmd = "cutycapt --url=" .. prefix .. "://" .. host.ip .. ":" .. port.number .. " --out=./http_screenshot/" .. filename .. " --max-wait=3000 --insecure"
    end
    execute = os.execute(cmd)

    return "Saved to " .. filename
end
