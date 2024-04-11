import os

from py_clob_client.client import ClobClient

from py_clob_client.clob_types import ApiCreds, DropNotificationParams
from dotenv import load_dotenv

from py_clob_client.constants import AMOY

load_dotenv()


def main():
    host = "http://localhost:8080"
    key = os.getenv("PK")
    creds = ApiCreds(
        api_key=os.getenv("CLOB_API_KEY"),
        api_secret=os.getenv("CLOB_SECRET"),
        api_passphrase=os.getenv("CLOB_PASS_PHRASE"),
    )
    chain_id = AMOY
    client = ClobClient(host, key=key, chain_id=chain_id, creds=creds)

    print(client.drop_notifications(params=DropNotificationParams(ids=["1", "2"])))


main()
