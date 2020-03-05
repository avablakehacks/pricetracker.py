import shrimpy

shrimpy_public_key = '...'
shrimpy_secret_key = '...'

client = shrimpy.ShrimpyApiClient(shrimpy_public_key, shrimpy_secret_key)

ticker = client.get_ticker('binance')