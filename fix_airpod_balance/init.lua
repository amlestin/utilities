DEFAULT_BALANCE = 0.5

function audioChangedCallback()
    cur_balance = hs.audiodevice:balance()
    if cur_balance != DEFAULT_BALANCE then
        hs.audiodevice:setBalance(DEFAULT_BALANCE)
    end
end

audioWatcher = hs.audiodevice:watcherCallback(audioChangedCallback)

audioWatcher:start()