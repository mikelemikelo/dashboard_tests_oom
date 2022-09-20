import json

# modelop.metrics
def metrics(baseline, comparator) -> dict:

	jsonResult = loadJsonFromFilename("dummy_base_mtr.json")
	# additionalData = loadJsonFromFilename("dummy_data_empty.json")
	# jsonResult.update(additionalData)
	# additionalData = loadJsonFromFilename("dummy_data_3MB.json")
	# jsonResult.update(additionalData)
	# additionalData = loadJsonFromFilename("dummy_data_1MB.json")
	# jsonResult.update(additionalData)
	# additionalData = loadJsonFromFilename("dummy_data_2MB.json")
	# jsonResult.update(additionalData)
	additionalData = loadJsonFromFilename("dummy_data_50KB.json")
	jsonResult.update(additionalData)
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