import csv
import json

class Dataset:
    # lexical features
    URL: str
    URLLength: int
    Domain: str
    DomainLenght: int
    IsDomainIP: bool
    TopLevelDomain: str
    TopLevelDomainLength: int
    NumberOfSubDomains: int
    NumberOfDigitsInURL: int
    DigitRationInURL: float
    NumberOfSpecialCharactersInURL: int
    SpecialCharactersRatioInURL: float
    IsHTTPS: bool

    # network features
    IsResponsive: bool
    NumberOfURLRedirects: int
    NumberOfSelfRedirects: int
    URLSimilarityIndex: float

    # program features
    LinesOfCode: int
    LargestLineLenght: int
    HasTitle: bool
    HasFavicon: bool
    HasDescription: bool
    NumberOfPopUps: int
    HasPasswordField: bool
    HasCopyrightInfo: bool
    NumberOfImages: int
    HasPaymentFunctionality: bool

    # social feature
    HasSocialNetwork: bool

    # 1 - phishing URL, 0 - legitimite URL
    Label: bool

def extractFeatures(inputPath: str, outputPath: str):
    print(f"Extracting features from {inputPath} ...")

    data = []
    count = 0

    try:
        with open(inputPath, mode = "r", encoding = "utf-8") as inputFile:
            reader = csv.DictReader(inputFile)

            for row in reader:
                dataset = Dataset()
                dataset.URL = row["URL"]
                dataset.URLLength = int(row["URLLength"])
                dataset.Domain = row["Domain"]
                dataset.DomainLenght = int(row["DomainLength"])
                dataset.IsDomainIP = bool(row["IsDomainIP"])
                dataset.TopLevelDomain = row["TLD"]
                dataset.URLSimilarityIndex = float(row["URLSimilarityIndex"])
                dataset.TopLevelDomainLength = int(row["TLDLength"])
                dataset.NumberOfSubDomains = int(row["NoOfSubDomain"])
                dataset.NumberOfDigitsInURL = int(row["NoOfDegitsInURL"])
                dataset.DigitRationInURL = float(row["DegitRatioInURL"])
                dataset.NumberOfSpecialCharactersInURL = int(row["NoOfOtherSpecialCharsInURL"])
                dataset.SpecialCharactersRatioInURL = float(row["SpacialCharRatioInURL"])
                dataset.IsHTTPS = bool(row["IsHTTPS"])
                dataset.LinesOfCode = int(row["LineOfCode"])
                dataset.LargestLineLenght = int(row["LargestLineLength"])
                dataset.HasTitle = bool(row["HasTitle"])
                dataset.HasFavicon = bool(row["HasFavicon"])
                dataset.IsResponsive = bool(row["IsResponsive"])
                dataset.NumberOfURLRedirects = int(row["NoOfURLRedirect"])
                dataset.NumberOfSelfRedirects = int(row["NoOfSelfRedirect"])
                dataset.HasDescription = bool(row["HasDescription"])
                dataset.NumberOfPopUps = int(row["NoOfPopup"])
                dataset.HasSocialNetwork = bool(row["HasSocialNet"])
                dataset.HasPasswordField = bool(row["HasPasswordField"])
                dataset.HasPaymentFunctionality = bool(row["Pay"])
                dataset.HasCopyrightInfo = bool(row["HasCopyrightInfo"])
                dataset.NumberOfImages = int(row["NoOfImage"])
                dataset.Label = 1 if row["label"] == "0" else 0

                count += 1
                data.append(dataset.__dict__)

            with open(outputPath, mode = "w") as outputFile:
                json.dump(data, outputFile, indent = 4)

            print(f"Extracted {count} rows")

    except Exception as e:
        print(f"Unexpected error: {e}")

datasetFilePath = "../datasets/dataset.json"
inputFilePath = "../datasets/PhiUSIIL_Phishing_URL_Dataset.csv"

extractFeatures(inputFilePath, datasetFilePath)