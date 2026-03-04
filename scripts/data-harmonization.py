import csv
import json

class HarmonizedData:
    def __init__(self, URL: str, Label: bool):
        self.URL = URL
        self.Label = Label

def harmonizeKaggle(inputPath: str, outputPath: str):

    print(f"Harmonizing data from {inputPath} ...")

    data = []
    count = 0

    try:   
        with open(inputPath, mode="r", encoding="utf-8") as inputFile:
            reader = csv.DictReader(inputFile)

            for row in reader:
                label = 1 if row["Label"] == 'bad' else 0
                harmonizedData = HarmonizedData(row["URL"], label)
                count += 1

                data.append(harmonizedData.__dict__)

        with open(outputPath, mode="w") as outputFile:
            json.dump(data, outputFile, indent = 4)

        print(f"Harmonized {count} rows")

    except Exception as e:
        print(f"Unexpected error: {e}")
        
def harmonizePhisTank(inputPath: str, outputPath: str):

    print(f"Harmonizing data from {inputPath} ...")

    data = []
    count = 0

    try:
        with open(outputPath, mode="r") as existingFile:
            data = json.load(existingFile)
        with open(inputPath, mode="r", encoding="utf-8") as inputFile:
            reader = json.load(inputFile)

            for row in reader:
                harmonizedData = HarmonizedData(row["url"], 1)
                count += 1

                data.append(harmonizedData.__dict__)
            
        with open(outputPath, mode="w") as outputFile:
            json.dump(data, outputFile, indent = 4)

        print(f"Harmonized {count} rows")

    except Exception as e:
        print(f"Unexpected error: {e}")

def harmonizePhiUSIIL(inputPath: str, outputPath: str):
    print(f"Harmonizing data from {inputPath} ...")

    data = []
    count = 0

    try:
        with open(outputPath, mode="r") as existingFile:
            data = json.load(existingFile)
        with open(inputPath, mode="r", encoding="utf-8") as inputFile:
            reader = csv.DictReader(inputFile)

            for row in reader:
                label = 1 if row["label"] == "0" else 0
                harmonizedData = HarmonizedData(row["URL"], label)
                count += 1

                data.append(harmonizedData.__dict__)
            
        with open(outputPath, mode="w") as outputFile:
            json.dump(data, outputFile, indent = 4)

        print(f"Harmonized {count} rows")

    except Exception as e:
        print(f"Unexpected error: {e}")

kaggleFilePath = "../datasets/kaggle-phishing_site_urls.csv"
PhisTankFilePath = "../datasets/phistank-verified_online.json"
PhiUSIILFilePath = "../datasets/PhiUSIIL_Phishing_URL_Dataset.csv"
outputFilePath = "../datasets/harmonized-data.json"

harmonizeKaggle(kaggleFilePath, outputFilePath)
harmonizePhisTank(PhisTankFilePath, outputFilePath)
harmonizePhiUSIIL(PhiUSIILFilePath, outputFilePath)