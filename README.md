# Minecraft-Files

This is a collection of mods, resource packs and other files I use when playing Minecraft.

A full list of all clients, mods, resource packs and shaders including all the original download links can be found in [this post](https://www.reddit.com/user/MordorsElite/comments/p5y2va/my_minecraftmods/?utm_source=share&utm_medium=web2x&context=3).

_Below you can find explantations for all the folders and files_

# Client

`options.txt` holds all ingame settings including keybinds, mouse- and video-settings.

## \config

This folder includes config-files for all the mods in the mod folder. These will be created automatically when starting minecraft with the mods installed. However you can instead you the configs I have provided here in order to use my customised keybinds and settings.

## \mods

This folder holds all the client-side mods I use in 1.18.0

Not all of them have 1.18.1 versions yet, so I wont be switching until then. However please make sure to use newer versions if possible as 1.18.0 contains some security flaws that are only fixed for later versions.

## \resource packs

This folder holds all resourcepacks that have either been assembled by me on the [vanillatweaks](https://vanillatweaks.net/picker/resource-packs/) website or are hard to find on google. Not included here are texture packs that can be downloaded in full on the creators websites.

I do not use all the texturepacks in this folder at all times.

_This is how my resourcepacks are ordered in the games resourcepack-settings_

| Texture pack | Permanent Use | Temporary Use |
|:-|:-:|:-:|
| Fabric Mods (added automatically) | X | |
| Rainbow_Ores6.zip | | X |
| Obvious_Debris.zip | | X |
| All other VanillaTweaks packs | | X |
| VanillaTweaks_InvisibleTotem.zip | X | |
| VanillaTweaks_OldMenuSelect.zip | X | |
| VanillaTweaks_AngledDotCrosshair.zip | X | |
| VanillaTweaks_18N2.zip | X | |
| [Depixel_1.18.zip](https://resourcepack.net/default-32x32-resource-pack/) | X | |

## \schematics

Since schematica has not been updated to versions above 1.12.2, I just recommend using [litematica](https://www.curseforge.com/minecraft/mc-mods/litematica) for all versions. (It can also work with the old x.schematic files from 1.12). While a lot of the farms from older versions do still work in 1.18, I would test them in creative first before building them in survival. Please also note that I haven't checked all schematics, so there might be some broken stuff mixed in.

# Server

``BackupMinecraftServer.py``

This is a python script that creates a zip-file of the target folder and saves it in the output folder. 

Usage: `python BackupMinecraftServer.py *folderToBackup* *folderToPutBackup*`

Running this script requires python to be installed on your system.

``run12GB.bat``

Script I use to start my server. Detailed explanation at the bottom

## \config

Server config folder

## \mods

Mods I use in my 1.18.0 fabric server

## \worldfiles

All the files and folders that have to be put into the servers world folder

`carpet.conf`: The config-file for fabric-carpet specifies the carpet-options I have set for my server

### \datapacks

All the datapacks I use. I recommend having a look at the [VanillaTweaks website](https://vanillatweaks.net/) yourself to browse other datapacks or select different crafting recepies.

### \scripts (only works with the carpet mod)

In the `sripts` folder you can put different scarpet scripts of your choosing. To find existing ones or write your own you refer to [Gnembons GitHub project](https://github.com/gnembon/scarpet). You can get help and advice on the [carpet discord](https://discord.com/invite/gn99m4QRY4).

The `bot.sc` file allows you to use the custom `/bot` command ingame that can spawn specific bots at predefined locations. For this to work properly in your world please specify the bots names and location as shown by the existing examples.

# Explanation

## run12GB.bat

`"C:\Program Files\Java\jdk-17\bin\java"` specifies which java version to use. The path has to point to the java.exe file

`-Xmx12G -Xms12G` allocates 12GB of RAM to the server. 

`-Dlog4j2.formatMsgNoLookups=true` should mitigate a security flaw that will be fixed when I update to 1.18.1 (not sure if this works tho)

`-jar fabric-server-launch.jar` specifies the server jar to use (can be installed with the [fabric installer](https://fabricmc.net/use/installer/))

`nogui` disables the GUI window of the server leaving just the commandline window (GUI might cause PC-stuttering)

`python path_to_backup_script path_to_server_folder path_to_backup_folder` runs the server-backup script. Remember to fill in the required paths before use

`pause` keeps the commandline window open after backup-script finishes