import express from "express";

import { completeTodo, createTodo, deleteTodo, getTodos } from "../controllers/todo.controllers.js";

const router = express.Router();

router.get("/", getTodos);
router.post("/", createTodo);
router.patch("/:todoId", completeTodo);
router.delete("/:todoId", deleteTodo);

export { router }