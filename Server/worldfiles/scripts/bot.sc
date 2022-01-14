__config() -> {
    'stay_loaded' -> true,
    'legacy_command_type_support' -> true,
    'scope' -> 'global',
};

__command()-> 'bot';

// Removes all not-whitelisted players (all the bots)
killall() -> (
    for(player('*'),
        player_on_server = _;
        equals = false;
        for(system_info('server_whitelist'),
            if(player_on_server==_,
                equals = true;
                break()
            );
        );
        if(!equals,
            run('/player ' + _ + ' kill');
        );
    );
);

// Spawns bot called 'Base' in villager hut near base
base() -> (
    run('/player Base spawn at -1266.5 93.00 -1652.5 in minecraft:overworld in survival');
);

// Spawns bot called 'MobFarm' over general mobfarm
mobfarm() -> (
    run('/player Mobfarm spawn at -1282.5 221.00 -1565.5 in minecraft:overworld in survival');
);

// Spawns bot called 'slimefarm' over first slimefarm
slimefarm() -> (
    run('/player Slimefarm spawn at -1255.5 133.00 -1640.5 in minecraft:overworld in survival');
);

// Spawns bots required to load sandduper
sandduper() -> (
    run('/player sandduperow spawn at -219.5 7 -1688.5 facing -90 90 in minecraft:overworld in spectator');
    sleep(3000);
    run('/player sandduperend spawn at 100.5 50 0.5 facing 90 90 in minecraft:the_end in spectator');
);

// Removes bots required to load sandduper
sandduperkill() -> (
    run('/player sandduperow kill');
    sleep(3000);
    run('/player sandduperend kill');
);

// Clicks lever of shulkerfarm once - Does not work!
shulkerfarm() -> (
    run('/player shulkerfarm spawn at -800.8 144.5 -1.5 facing 0 -90 in minecraft:overworld in survival');
    sleep(5000);
    run('/player shulkerfarm use once');
    sleep(15000);
    run('/player shulkerfarm kill');
);