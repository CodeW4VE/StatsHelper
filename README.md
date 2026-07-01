StatsHelper
-------

An [MCDReforged](https://github.com/Fallen-Breath/MCDReforged) plugin for statistics: query, rank, and list all kinds of stats using scoreboards.

Supported versions: servers 1.13+

> This is a fork maintained for [MineWave](https://w4ve.xyz/). See [MINEWAVE-FORK.md](MINEWAVE-FORK.md) for the changes made on top of the original [TISUnion/StatsHelper](https://github.com/TISUnion/StatsHelper).

# Command format

`!!stats` Show the help message

`!!stats save` <alias> <stat_class> <stat_target> <title> Save a quick scoreboard

`!!stats del` <alias> Delete a quick scoreboard

`!!stats list` List the saved quick scoreboards

`!!stats query` <player> <stat_class> <stat_target> [<-uuid>] [<-tell>]

`!!stats query` <player> <alias> [<-uuid>] [<-tell>]

`!!stats rank` <stat_class> <stat_target> (-bot) [<-tell>]

`!!stats rank` <alias> (-bot) [<-tell>]

`!!stats scoreboard` <stat_class> <stat_target> (title) (-bot)

`!!stats scoreboard` <alias> Show a quick scoreboard

`!!stats scoreboard show` Show this plugin's scoreboard

`!!stats scoreboard hide` Hide this plugin's scoreboard

## Arguments

<stat_class>: killed, killed_by, dropped, picked_up, used, mined, broken, crafted, custom. For killed and killed_by, <stat_target> is an [entity id].

For picked_up, used, mined, broken and crafted, <stat_target> is an item/block id.

For custom, see <stat_target> in the game's stats JSON files, or the [MC Wiki](https://minecraft.wiki/w/Statistics).

None of the above need the `minecraft` prefix.

[<-uuid>]: use the UUID instead of the player name; (-bot): include bots and cameras; [<-tell>]: only visible to you.

## Examples

`!!stats save fly custom aviate_one_cm Flight`

`!!stats query Fallen_Breath used water_bucket`

`!!stats rank custom time_since_rest -bot`

`!!stats scoreboard mined stone Stone_mined`

# Config file

`server_path`: the server's working directory.

`world_folder`: the world save folder, located inside the server working directory.

`save_world_on_query`: whether to run `/save-all` to save the world when `!!stats query` is used.

`save_world_on_rank`: whether to run `/save-all` to save the world when `!!stats rank` is used.

`save_world_on_scoreboard`: whether to run `/save-all` to save the world when `!!stats scoreboard` is used.

`player_name_blacklist`: a list of strings acting as a query blacklist; players in it are not counted. Each string is a regular expression, and a player is ignored when their name matches any of the patterns.
