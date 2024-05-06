import { mainUrl } from "../staticData.js";
import getHtmlData from "../utils/getHtmlData.js";

export default async function getItems(link, brandName) {
  const $ = await getHtmlData(link);
  const items = $(".makers a");

  const itemsData = [];

  for (let x of items) {
    const element = $(x);
    const href = element.attr("href");
    const itemData = await getItem(`${mainUrl}/${href}`);
    console.log(itemData);
    itemsData.push(itemData);
  }

  return {
    [brandName]: itemsData,
  };
}

async function getItem(link) {
  const $ = await getHtmlData(link);
  const itemName = $("h1.specs-phone-name-title").text();
  const imageUrl = $(".specs-photo-main img").attr("src");
  const imageAlt = $(".specs-photo-main img").attr("alt");
  const imagesNavHref = $(".specs-photo-main a").attr("href");
  const processor = $(".help-expansion div").text();
  const displaySize = $(".help-display span").text();
  const displayRes = $(".help-display div").text();
  const cameraMgpix = $("strong.accent-camera").text();
  const cameraRes = $(".help-camera div").text();
  const ram = $("strong.accent-expansion").text();
  const batteryMah = $("strong.accent-battery").text();
  const releasedData = $("span[data-spec='released-hl']").text();
  const systemOs = $("span[data-spec='os-hl']").text();
  const storage = $("span[data-spec='storage-hl']").text();
  const charger = $(".help-battery div").text();
  const body = $("span[data-spec='body-hl']").text();

  const images = await getImages(`${mainUrl}/${imagesNavHref}`);

  return {
    itemName,
    imageUrl,
    imageAlt,
    imagesLink: `${mainUrl}/${imagesNavHref}`,
    images,
    processor,
    displaySize,
    displayRes,
    cameraMgpix,
    cameraRes,
    ram,
    batteryMah,
    releasedData,
    systemOs,
    storage,
    charger,
    body,
  };
}

async function getImages(link) {
  const $ = await getHtmlData(link);
  const images = $("#pictures-list img[src]");

  const imagesLink = [];

  for (let x of images) {
    const href = $(x).attr("src");
    imagesLink.push(href);
  }

  return imagesLink;
}
