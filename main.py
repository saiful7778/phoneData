from functions.functions import (
    deleteAllFile,
    modifyData,
    getImageData,
    makeThumbnail,
    uploadImage,
    makeImage,
)
import json


def main():
    deleteAllFile("./assets/thumbnails")
    deleteAllFile("./assets/images")

    allProductData: list = []

    with open("./data/allData.json", "r") as file:
        data: dict = json.load(file)
        idx: int = 1

        for x in data["allItemsData"]:
            if x["type"] == "phone":
                imageUrl: str = x["imageUrl"]
                images: list = x["images"]
                slug: str = x["slug"]
                productData: dict = modifyData(x)

                thumbnail = getImageData(imageUrl)

                if thumbnail == False:
                    break

                outputThumbnailPath: str = f"./assets/thumbnails/{slug}_thumbnail.jpg"

                isThumbnailMade: bool = makeThumbnail(thumbnail, outputThumbnailPath)

                if isThumbnailMade != True:
                    break

                # thumbnailUrl = uploadImage(outputThumbnailPath, slug)

                # if thumbnailUrl == False:
                #     break

                imagesUrl: list = getImages(images, slug)

                productData["thumbnail"] = outputThumbnailPath
                productData["images"] = imagesUrl

                allProductData.append(productData)

                print(f"{idx} - {slug} complate")

                idx += 1
    with open("./data.json", "w") as dataFile:
        dataFile.write(json.dumps({"allItemsData": allProductData}))
        print("All complated")


def getImages(images: list, slug: str):
    allImages: list = []
    idx: int = 1

    for y in images:
        image = getImageData(y)

        if image == False:
            break

        outputImagePath: str = f"./assets/images/{slug}_image_{idx}.jpg"

        isImageMade: bool = makeImage(image, outputImagePath)

        if isImageMade != True:
            break

        # imageUrl = uploadImage(outputImagePath, slug)

        # if imageUrl == False:
        #     break

        # allImages.append(imageUrl)
        allImages.append(outputImagePath)
        idx += 1

    return allImages


if __name__ == "__main__":
    main()
