
const TODOS = [
  {
    id: 1,
    title: "Complete homework",
    isCompleted: false
  },
  {
    id: 2,
    title: "Go play",
    isCompleted: false
  },
  {
    id: 3,
    title: "Take bath",
    isCompleted: false
  },
]

export function getTodos(req, res) {
  try {
    const todos = TODOS;

    res.status(200).json({
      success: true,
      data: todos
    });
  } catch (error) {
    return res.status(500).json({
      success: false,
      message: "Internal server error"
    })
  }
}

export function createTodo(req, res) {
  try {
    const body = req.body;

    const todo = body?.todo;

    if (!todo?.trim()) {
      return res.status(400).json({
        success: false,
        message: "Todo is required"
      })
    }

    const lastTodoId = TODOS[TODOS?.length - 1]?.id;

    const newTodo = {
      id: lastTodoId + 1,
      title: todo,
      isCompleted: false
    };

    TODOS.push(newTodo);

    return res.status(201).json({
      success: false,
      message: "Todo created successfully"
    })

  } catch (error) {
    return res.status(500).json({
      success: false,
      message: "Internal server error"
    })
  }
}

export function completeTodo(req, res) {
  try {
    const params = req.params;

    if (!params?.todoId?.trim()) {
      return res.status(400).json({
        success: false,
        message: "Todo ID is required"
      })
    }

    const todoId = parseInt(params?.todoId);


    const todoToUpdateIndex = TODOS?.findIndex((todo) => todo.id === todoId);

    if (todoToUpdateIndex === -1) {
      return res.status(404).json({
        success: false,
        message: "Todo not found"
      })
    }

    const todoToUpdate = TODOS[todoToUpdateIndex];

    TODOS[todoToUpdateIndex] = {
      ...todoToUpdate,
      isCompleted: true,
    }

    return res.status(200).json({
      success: false,
      message: "Todo completed successfully"
    })

  } catch (error) {
    return res.status(500).json({
      success: false,
      message: "Internal server error"
    })
  }
}

export function deleteTodo(req, res) {
  try {
    const params = req.params;

    if (!params?.todoId?.trim()) {
      return res.status(400).json({
        success: false,
        message: "Todo ID is required"
      })
    }

    const todoId = parseInt(params?.todoId);

    const todoToDeleteIndex = TODOS?.findIndex((todo) => todo.id === todoId);

    if (todoToDeleteIndex === -1) {
      return res.status(404).json({
        success: false,
        message: "Todo not found"
      })
    }

    TODOS.splice(todoToDeleteIndex, 1);

    return res.status(200).json({
      success: false,
      message: "Todo deleted successfully"
    })

  } catch (error) {
    return res.status(500).json({
      success: false,
      message: "Internal server error"
    })
  }
}