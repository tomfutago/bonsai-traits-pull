import json
import pandas as pd
import requests

for i in range(1, 8889, 100):
  query = """query {
    bonsais (
      first: 100,
      orderBy: tokenID,
      where: {
      tokenID_gte: %i
      tokenID_lte: %i
    }) {
      tokenID
      name
      image
      animation_url
      pot
      pet
      bark
      leaves
      fruit
      numberOfFruit
      groundCover
      background
    }
  }
  """ % (i, i+100)

  url = "https://api.thegraph.com/subgraphs/name/tomfutago/bonsai"
  r = requests.post(url, json={"query": query})
  #print(r.status_code)
  json_data = json.loads(r.text)
  #print(json_data)
  df_tmp = pd.json_normalize(json_data["data"]["bonsais"])
  if i == 1: # only once
    df = pd.concat([df_tmp])
  else:
    df = pd.concat([df, df_tmp])
  #print(df_tmp)

print(df)
df.to_csv("bonsai.csv", encoding="utf-8")
