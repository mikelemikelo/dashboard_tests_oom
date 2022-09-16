import json

# modelop.metrics
def metrics(baseline, comparator) -> dict:

	jsonResult = loadJsonFromFilename("dummy_base_mtr.json")
	dummyDataJson = loadJsonFromFilename("dummy_data_empty.json")
	# dummyDataJson = loadJsonFromFilename("dummy_data_5MB.json")
	jsonResult.update(dummyDataJson)
	yield jsonResult

def loadJsonFromFilename(filename):
	with open(filename, "r") as f:
		contents = f.read()
	fileAsJson = json.loads(contents)
	return fileAsJson

if __name__ == "__main__":
	result = metrics(None,None)
	for value in result:
		print(value)