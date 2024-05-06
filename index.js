import getItems from "./functions/getItem.js";
import { mainUrl, phonesBrand } from "./staticData.js";
import delay from "./utils/delay.js";
import getHtmlData from "./utils/getHtmlData.js";
import { writeFile } from "node:fs/promises";

(async () => {
  try {
    console.log("Data fetching");
    const $ = await getHtmlData(mainUrl);
    const brandNames = $(".brandmenu-v2 li a");

    const allItemsData = [];

    for (let x of brandNames) {
      const element = $(x);
      const brandName = element.text().toLowerCase();
      if (phonesBrand.includes(brandName)) {
        const href = element.attr("href");
        const itemsData = await getItems(`${mainUrl}/${href}`, brandName);
        allItemsData.push(itemsData);
      }
    }

    await writeFile("./allData.json", JSON.stringify({ allItemsData }), {
      encoding: "utf-8",
      flag: "w",
    });
    console.log("Complated");
  } catch (err) {
    console.error(err);
  }
})();
