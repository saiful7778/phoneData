import os
import json
import requests
from io import BytesIO
from PIL import Image
import base64


def deleteAllFile(folderDir: str):
    try:
        fileList: list = os.listdir(folderDir)
        for fileName in fileList:
            filePath: str = os.path.join(folderDir, fileName)
            if os.path.isfile(filePath):
                os.remove(filePath)
                print(f"Deleted: {fileName}")
            else:
                print(f"Skipped: {fileName} (not a file)")
        print("All file is deleted")
    except:
        print("Error on 'deleteAllFile' function")


def modifyData(inputData: dict):
    return {
        "itemName": inputData["itemName"],
        "slug": inputData["slug"],
        "releasedData": inputData["releasedData"],
        "price": inputData["price"],
        "productType": inputData["type"],
        "brandName": inputData["brandName"],
        "specification": {
            "processor": inputData["processor"],
            "displaySize": inputData["displaySize"],
            "displayRes": inputData["displayRes"],
            "cameraMgpix": inputData["cameraMgpix"],
            "cameraRes": inputData["cameraRes"],
            "ram": inputData["ram"],
            "batteryMah": inputData["batteryMah"],
            "systemOs": inputData["systemOs"],
            "storage": inputData["storage"],
            "charger": inputData["charger"],
            "body": inputData["body"],
        },
    }


def printJson(inputData: dict):
    print(json.dumps(inputData, indent=2))


def getImageData(href: str, errorStr: str = "Error to get fetch data"):
    try:
        res = requests.get(href)
        if res.status_code == 200:
            return BytesIO(res.content)
        else:
            print("Fetch data status code not equal 200")
            return False
    except:
        print(errorStr)
        return False


def makeThumbnail(inputImageData, outputPath: str):
    try:
        original_image = Image.open(inputImageData)

        backgroundSize = (500, 350)
        background = Image.new("RGB", backgroundSize, (255, 255, 255))

        imageXPosition: int = int(
            (backgroundSize[0] / 2) - (original_image.size[0] / 2)
        )
        imageYPosition: int = int(
            (backgroundSize[1] / 2) - (original_image.size[1] / 2)
        )
        imagePosition: tuple = (imageXPosition, imageYPosition)

        background.paste(original_image, imagePosition, (0))
        background.save(outputPath)
        return True
    except:
        print("Error to make thumbnail")
        return False


def uploadImage(imagePath: str, imageName: str):
    url: str = "https://api.imgbb.com/1/upload"
    try:
        with open(imagePath, "rb") as file:
            encoded_image = base64.b64encode(file.read()).decode("utf-8")
            payload = {
                "key": "6a18b90b5f691da4bc8573b5a3b48cf0",
                "name": imageName,
                "image": encoded_image,
            }
            res = requests.post(url, payload)

            print(res.json())
            if res.status_code == 200:
                result = res.json()
                return result["data"]["url"]
            else:
                print("Failed to upload image")
                return False
    except:
        print("error on upload image")
        return False


def makeImage(inputImageData, outputPath: str):
    try:
        original_image = Image.open(inputImageData)

        backgroundSize = (500, 350)
        background = Image.new("RGB", backgroundSize, (255, 255, 255))

        original_image.thumbnail(
            decreaseImageSize(backgroundSize[0], backgroundSize[1], 50)
        )

        imageXPosition: int = int(
            (backgroundSize[0] / 2) - (original_image.size[0] / 2)
        )
        imageYPosition: int = int(
            (backgroundSize[1] / 2) - (original_image.size[1] / 2)
        )

        imagePosition: tuple = (imageXPosition, imageYPosition)

        background.paste(original_image, imagePosition, (0))
        background.save(outputPath)
        return True
    except:
        print("Error to make image")
        return False


def decreaseImageSize(width: int, height: int, decreaseBy: int):
    aspectRatio = width / height
    newWidth = width - decreaseBy
    newHeight = newWidth / aspectRatio

    return (newWidth, newHeight)
