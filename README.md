# Forex signal with RSI, CCI and MFI indicators

Get forex pairs that have good RSI, CCI and MFI rates in daily timeframe.

you can change the timeframe in provider.py file to hourly or weekly.

## Installation

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

after that you must copy .env.example file to .env and change the variables with your data.

```
cp .env.example .env
```

then edit the .env file and add your API keys.

```
TELEGRAM_CHAT_ID=
TELEGRAM_BOT_TOKEN=

ALPHAVANTAGE_API_KEY=
TWELVEDATA_API_KEY=
```

after that you can run the script with below command:

```
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