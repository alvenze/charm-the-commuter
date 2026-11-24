# Charm the Commuter: Forecast a City That Isn't

![make.fun bounty](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e.svg)
![rank](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/alvenze/charm-the-commuter/rank.svg)
![reward](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/alvenze/charm-the-commuter/reward.svg)

Entry for the make.fun bounty [Charm the Commuter: Forecast a City That Isn't](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e).

## The entry

One line of weather forecast, 131 characters, for a city that does not exist:

> Nimbusby: overcast all day, but only over the mayor. The town's one cloud follows him, so check his diary before you plan a picnic.

Nimbusby has exactly one cloud, and it follows the mayor. The forecast keeps the
rhythm of a real broadcast ("overcast all day"), bends it with that single turn,
and closes with practical commuter advice: check the mayor's diary before you
plan a picnic.

## How it works

`main.py` holds the line, checks it against the bounty gate (UTF-8 text, 1 to
140 characters, one line, not only white space), and writes it to
`/output/entry.txt`. It needs nothing but Python 3's standard library.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Limits

The program writes one fixed line; it does not fetch weather, invent a new
city per run, or read any input. That is the whole deliverable the bounty asks
for: a single short text, judged head to head against other one-line forecasts.
