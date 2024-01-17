import urllib.request
import json

eia_key = 'ltT34dIL9GNnCgWdRBAdSjw6iJFfx2kdzIsWzG87'

def get_brent_oil_prices_eia(api_key):
    api_call = f'https://api.eia.gov/v2/petroleum/pri/spt/data/?api_key={api_key}&frequency=daily&data[0]=value&facets[series][]=RBRTE&start=2010-01-01&sort[0][column]=period&sort[0][direction]=desc&offset=0'

    content = urllib.request.urlopen(api_call).read()

    return content

with open('brent_eia.json','w') as f:  
    json.dump(json.loads(get_brent_oil_prices_eia(eia_key)), f)