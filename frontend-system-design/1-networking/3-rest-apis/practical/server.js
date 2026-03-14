import express from "express";

import "dotenv/config";

import { router as todoRouter } from "./routes/todo.routes.js";

const app = express();

// middleware
app.use(express.json());


// routes
app.get("/health", (req, res) => {
  res.send("Health OK!");
})

app.use('/todos', todoRouter)

const PORT = process.env.PORT || 5000;

app.listen(PORT, () => {
  console.log(`Server is running!`)
})