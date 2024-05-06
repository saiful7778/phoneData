export default function getRandomNumber(minNum, maxNum) {
  if (typeof minNum !== "number" || typeof maxNum !== "number") {
    throw new Error("Please put number in aregument");
  }
  return Math.floor(Math.random() * (maxNum - minNum + 1)) + minNum;
}
