// band name generator taking name from the user and using various middleware to display the name

import express from "express";
import bodyParser from "body-parser";
import { dirname } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const app = express();
const port = 3000;
var name = "";

app.use(bodyParser.urlencoded({ extended: true }));

function bandName(req, res, next) {
  console.log(req.body);
  name = req.body["street"] + req.body["pet"];
  next();
}

app.use(bandName);

app.get("/", (req, res) => {
  res.sendFile(__dirname + "/public/index.html");
});

app.post("/submit", (req, res) => {
  res.send(`<h1>Your band name is:</h1><h2>${name}✌️</h2>`);
});

app.listen(port, () => {
  console.log(`Listening on port ${port}`);
});
