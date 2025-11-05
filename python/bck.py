from lance_client_bdp import BdpLanceClient
import time

client = BdpLanceClient()
ds = client.load_dataset("bkeller.logblob_tsdal_cold_tier_small")
ds.list_indices()
ds.prewarm_index("time_series_id_idx")

start = time.time()

scan = ds.scanner(filter="time_series_id='HISETVK74500000000000000000000000003616680'")

end = time.time()
print(f"time: {end - start}")

reader = scan.to_reader()

end = time.time()
print(f"time: {end - start}")

reader.read_all()

end = time.time()
print(f"time: {end - start}")
