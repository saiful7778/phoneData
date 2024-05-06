import { readFile } from "node:fs/promises";
import getRandomNumber from "./utils/randomNum.js";

(async () => {
  try {
    const dataString = await readFile("./data/allData.json", {
      encoding: "utf-8",
      flag: "r",
    });
    const data = JSON.parse(dataString);

    const phones = [];
    const watchs = [];
    const tabs = [];
    const tablets = [];

    for (let x of data.allItemsData) {
      if (x.itemName.search(/watch/gi) >= 0) {
        x.type = "watch";
        x.price = getRandomNumber(50, 500);
        watchs.push(x);
      } else if (x.itemName.search(/tablet/gi) >= 0) {
        x.type = "tablet";
        x.price = getRandomNumber(200, 1000);
        tablets.push(x);
      } else if (x.itemName.search(/tab/gi) >= 0) {
        x.type = "tab";
        x.price = getRandomNumber(100, 800);
        tabs.push(x);
      } else {
        x.price = getRandomNumber(100, 2000);
        x.type = "phone";
        phones.push(x);
      }
    }
    console.log(data.allItemsData);
  } catch (err) {
    console.error(err);
  }
})();
