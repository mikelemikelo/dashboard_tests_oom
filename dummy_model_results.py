import json

# modelop.metrics
def metrics(df):
	filename = "dummy_data_5MB.json"
	with open(filename, "r") as f:
		contents = f.read()
	test_results = json.loads(contents)
	yield test_results

if __name__ == "__main__":
	result = metrics(None)
	for value in result:
		print(value)