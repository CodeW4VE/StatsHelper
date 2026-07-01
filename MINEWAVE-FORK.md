# MineWave fork of StatsHelper

This is a [CodeW4VE](https://github.com/CodeW4VE) / MineWave fork of
[TISUnion/StatsHelper](https://github.com/TISUnion/StatsHelper) (GPL-3.0).

## Changes vs upstream

- **UUID / rename de-duplication fix**, by **[KarlaPrz02](https://github.com/KarlaPrz02) (Katherina)**.
  Because the stats files are keyed by UUID, a renamed player could appear twice
  (old name + new name) and inflate ranks/scoreboards. The fix collapses each
  UUID to a single, up-to-date name: it dedups by UUID, prefers the name in
  `usercache.json`, and uses the most recent entry when there are several.
  See `deduplicate_uuid_list` in `stats_helper/__init__.py`.

- **Wider bot filter** (by TVTvirus). The default `player_name_blacklist` only
  caught a `bot` prefix (`^bot.*`), so bots named with a `_bot` suffix
  (`load_bot`, `Slime_BOT`, ...) still showed up in ranks and inflated totals.
  Added `bot_.*` and `.*_bot` to the default blacklist (matched case-insensitive).
  See `stats_helper/config.py`.

Integrated and maintained for MineWave by TVTvirus. Upstream license (GPL-3.0)
unchanged; see `LICENSE`.
