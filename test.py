import os
import sys
import asyncio
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import requests
from src.tanxconnector import exception  # noqa: E402


from src.tanxconnector.starknet import StarkNetHelper
from src.tanxconnector import Client

client = Client()
starknet = StarkNetHelper()


ETH_ADDRESS="0xEBD0a775f8213A75b0f5631a462Ef5DD4BF6ed2b"
PRIVATE_ADDRESS="1a4b0778fa075bc3880db9cc5c81b891191e305657626e99fc33fff87c8298bb"
PRIVATE_ADDRESS="1a4b0778fa075bc3880db9cc5c81b891191e305657626e99fc33fff87c8298bb"
PRIVATE_ADDRESS="1a4b0778fa075bc3880db9cc5c81b891191e305657626e99fc33fff87c8298bb"


try:
    # login to use private endpoints
    login = client.complete_login(ETH_ADDRESS, PRIVATE_ADDRESS)
    print('Login Successful')
# Error: AuthenticationError | requests.exceptions.HTTPError
except exception.AuthenticationError as exc:
    print(exc)
except requests.exceptions.HTTPError as exc:
    print(exc.response.json())



async def balance():
    res = await client.starknet_deposit(STARKNET_RPC, STARKNET_PUBLIC_KEY,STARKNET_PRIVATE_KEY, amount=4, currency='usdc')
    return res
res = asyncio.run(balance())
print(res)

