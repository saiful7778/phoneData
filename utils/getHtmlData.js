import axios from "axios";
import { load } from "cheerio";
import delay from "./delay.js";

export default async function getHtmlData(link) {
  console.log("fetch delay");
  await delay(1000);
  console.log("fetching....");
  const { data } = await axios.get(link);
  return load(data);
}
