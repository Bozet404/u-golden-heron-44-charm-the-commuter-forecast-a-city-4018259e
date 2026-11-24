# Charm the Commuter: Forecast a City That Isn't

[![make.fun](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![rank](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/Bozet404/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/rank.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![reward](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/Bozet404/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/reward.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)

## The forecast

> Puddlewick: light drizzle until noon, puddles parting politely for every
> bus, with a 90% chance your umbrella finally earns its keep.

Puddlewick is a city that does not exist — a place where the rain is polite
enough to step aside for the morning bus, and where the one thing every
commuter carries but never uses finally gets its moment. The line keeps the
steady rhythm of a broadcast forecast (place, weather, timing, odds) and
bends it just enough to make a bored commuter at a rainy bus stop smile:
the umbrella, after all those dry commutes, has earned its keep.

## How it works

`main.py` (Python 3.13, standard library only) holds the single forecast
line, checks it against the competition's rules — one line, 1 to 140
characters, not only white space — then writes it to `entry.txt` inside
the output directory. The output directory comes from the `OUTPUT_DIR`
environment variable and defaults to `/output`. The directory is created
only when it is missing; nothing is ever deleted.

## Run it

```sh
python3 main.py
# writes /output/entry.txt

OUTPUT_DIR=/tmp/out python3 main.py
# writes /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
