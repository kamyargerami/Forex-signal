# Forex Rsi

We used Rsi daily and Rsi hourly to get best signals

## Installation

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python3 signal.py {twelvedata | alphavantage}
```

## Usage

```
python3 signal.py {twelvedata | alphavantage}
```

## Api Providers

we are using apis to get RSI value for our application

### Twelvedata

800 request per day

8 request per minute

[Website](https://twelvedata.com/)

### Alphavantage

500 request per day

5 request per minute

[Website](https://www.alphavantage.co/)