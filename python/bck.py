from lance_client_bdp import BdpLanceClient

client=BdpLanceClient()
print(client.load_dataset("bkeller.foobar").count_rows())