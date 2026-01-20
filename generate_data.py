import numpy as np
import pandas as pd

rng = np.random.default_rng(7)

N_USERS = 20000
countries = ["US", "CA", "MX", "BR", "GB", "DE", "FR", "ES"]
channels = ["Google_Search", "Meta", "TikTok", "Apple_Search_Ads", "YouTube"]
campaigns = ["Brand", "Prospecting", "Retargeting"]

start = pd.Timestamp("2025-10-01")
end = pd.Timestamp("2025-12-31")
days = (end - start).days + 1

users = pd.DataFrame({
    "user_id": np.arange(1, N_USERS + 1),
    "country": rng.choice(countries, size=N_USERS, p=[0.35,0.08,0.10,0.07,0.12,0.10,0.10,0.08]),
    "signup_date": start + pd.to_timedelta(rng.integers(0, days, size=N_USERS), unit="D")
})

experiment_start = pd.Timestamp("2025-11-15")
test_countries = {"US", "GB", "DE", "FR"}

geo_experiment = pd.DataFrame({
    "country": countries,
    "is_test": [1 if c in test_countries else 0 for c in countries],
    "experiment_start": experiment_start
})

touch_rows = []
touch_id = 1

channel_weights = np.array([0.28, 0.30, 0.20, 0.12, 0.10])
cost_per_touch = {
    "Google_Search": 0.60,
    "Meta": 0.35,
    "TikTok": 0.25,
    "Apple_Search_Ads": 0.75,
    "YouTube": 0.30
}

for _, u in users.iterrows():
    k = rng.integers(0, 9)
    if k == 0:
        continue

    base_time = u["signup_date"] - pd.to_timedelta(rng.integers(0, 10), unit="D")

    for _ in range(k):
        ch = rng.choice(channels, p=channel_weights)
        camp = rng.choice(campaigns, p=[0.25, 0.55, 0.20])

        if (u["country"] in test_countries) and (u["signup_date"] >= experiment_start) and rng.random() < 0.25:
            ch = rng.choice(["Meta", "YouTube", "TikTok"], p=[0.45, 0.20, 0.35])
            camp = "Retargeting"

        event_type = "click" if rng.random() < 0.22 else "impression"
        ttime = base_time + pd.to_timedelta(rng.integers(0, 14), unit="D") + pd.to_timedelta(rng.integers(0, 24*60), unit="m")

        cost = cost_per_touch[ch] * (2.2 if event_type == "click" else 1.0)

        touch_rows.append([touch_id, u["user_id"], u["country"], ch, camp, ttime, event_type, round(cost, 4)])
        touch_id += 1

touchpoints = pd.DataFrame(
    touch_rows,
    columns=["touch_id", "user_id", "country", "channel", "campaign", "touch_time", "event_type", "cost"]
)

last_touch = (touchpoints.sort_values("touch_time")
              .groupby("user_id")
              .tail(1)[["user_id", "channel", "campaign", "touch_time", "country"]]
              .rename(columns={"channel":"last_channel","campaign":"last_campaign","touch_time":"last_touch_time"}))

base_conv = 0.06
channel_uplift = {
    "Google_Search": 0.03,
    "Meta": 0.015,
    "TikTok": 0.01,
    "Apple_Search_Ads": 0.035,
    "YouTube": 0.008
}
campaign_uplift = {
    "Brand": 0.01,
    "Prospecting": 0.0,
    "Retargeting": 0.025
}

conversions = []
for _, u in users.iterrows():
    lt = last_touch[last_touch.user_id == u.user_id]
    if lt.empty:
        prob = base_conv * 0.3
        country = u.country
        last_time = u.signup_date
    else:
        lt = lt.iloc[0]
        prob = base_conv + channel_uplift.get(lt.last_channel, 0) + campaign_uplift.get(lt.last_campaign, 0)

        if lt.country in test_countries and u.signup_date >= experiment_start:
            prob += 0.015

        country = lt.country
        last_time = lt.last_touch_time

    converted = rng.random() < min(prob, 0.5)
    revenue = max(rng.normal(12, 3), 0) if converted else 0

    conversions.append([
        u.user_id,
        last_time + pd.to_timedelta(rng.integers(0, 3), unit="D"),
        int(converted),
        round(revenue, 2),
        country
    ])

conversions = pd.DataFrame(conversions, columns=["user_id", "conversion_time", "converted", "revenue", "country"])

users.to_csv("data/users.csv", index=False)
touchpoints.to_csv("data/touchpoints.csv", index=False)
conversions.to_csv("data/conversions.csv", index=False)
geo_experiment.to_csv("data/geo_experiment.csv", index=False)

print("Done! Created CSVs in /data")
print("users:", len(users))
print("touchpoints:", len(touchpoints))
print("conversions:", len(conversions))
