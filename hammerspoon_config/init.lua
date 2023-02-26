DEFAULT_BALANCE = 0.5

audioWatcher = nil

function audioChangedCallback(event)
    audioDevice = hs.audiodevice.defaultOutputDevice()
    cur_balance = audioDevice:balance()
    if cur_balance ~= DEFAULT_BALANCE then
	audioDevice:setBalance(DEFAULT_BALANCE)
    end
end
hs.audiodevice.watcher.setCallback(audioChangedCallback)
hs.audiodevice.watcher.start() 

function screenCallback()
  local lg = hs.screen.find("LG")
end

function screenCallback(eventType, screen)
  if eventType == hs.screen.watcher.connected then
      if screen:name() == "LG" then
          screen:setMode(3440, 1440, 1.0, 50.0, 8)
      end
  end
end

local screenWatcher = hs.screen.watcher.new(screenCallback)
screenWatcher:start()