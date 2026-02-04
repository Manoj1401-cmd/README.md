import pandas as pd


fear_greed = pd.read_csv("fear_greed_index.csv")
historical = pd.read_csv("historical_data.csv")
print("Fear & Greed shape:", fear_greed.shape)
print("Historical shape:", historical.shape)

print("Missing values Fear & Greed:\n", fear_greed.isnull().sum())
print("Missing values Historical:\n", historical.isnull().sum())

print("Duplicates Fear & Greed:", fear_greed.duplicated().sum())
print("Duplicates Historical:", historical.duplicated().sum())


fear_greed['timestamp'] = pd.to_datetime(fear_greed['timestamp'])
historical['Timestamp'] = pd.to_datetime(historical['Timestamp'])


fear_greed['date'] = fear_greed['timestamp'].dt.date
historical['date'] = historical['Timestamp'].dt.date

merged = pd.merge(historical, fear_greed, on='date', how='inner')

daily_pnl = merged.groupby(['date','trader_id'])['PnL'].sum().reset_index()

win_rate = merged.groupby('trader_id').apply(lambda x: (x['PnL']>0).mean()).reset_index(name='win_rate')

avg_trade_size = merged.groupby('trader_id')['trade_size'].mean().reset_index()

leverage_dist = merged['leverage'].describe()

trades_per_day = merged.groupby('date')['trade_size'].count().reset_index(name='num_trades')

long_short_ratio = merged['side'].value_counts(normalize=True)

print(daily_pnl.head())
print(win_rate.head())
print(avg_trade_size.head())
print(leverage_dist)
print(trades_per_day.head())
print(long_short_ratio)





