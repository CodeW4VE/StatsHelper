# MineWave fork of StatsHelper

This is a [CodeW4VE](https://github.com/CodeW4VE) / MineWave fork of
[TISUnion/StatsHelper](https://github.com/TISUnion/StatsHelper) (GPL-3.0).

## Changes vs upstream

- **UUID / rename de-duplication fix** — by **[KarlaPrz02](https://github.com/KarlaPrz02) (Katherina)**.
  Because the stats files are keyed by UUID, a renamed player could appear twice
  (old name + new name) and inflate ranks/scoreboards. The fix collapses each
  UUID to a single, up-to-date name: it dedups by UUID, prefers the name in
  `usercache.json`, and uses the most recent entry when there are several.
  See `deduplicate_uuid_list` in `stats_helper/__init__.py`.

Integrated and maintained for MineWave by TVTvirus. Upstream license (GPL-3.0)
unchanged; see `LICENSE`.
