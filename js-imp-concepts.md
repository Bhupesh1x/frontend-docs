## Debounce in JavaScript

- Debounce is a technique used to optimize applications. It delays the execution of a function until a certain amount of time has passed since the last time it was called.

- If the function is called again before the delay finishes, the timer resets.

- Main use cases: Search inputs, form validation, resize events

**js implementation**

```js
function getData() {
  let inputValue = document.getElementById("input").value;

  console.log("Fetching data...", inputValue);
}

function debounce(fn, delay = 300) {
  let timeout;
  return function () {
    clearTimeout(timeout);

    timeout = setTimeout(() => {
      fn.apply(this, arguments);
    }, delay);
  };
}

let debouncedFn = debounce(getData, 300);
```

**React.js implementation with hook**

```js
import { useEffect, useState } from "react";

export function useDebouncedValue(value, delay = 300) {
  const [debouncedValue, setDebouncedValue] = useState(value);

  useEffect(() => {
    const id = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);

    return () => clearTimeout(id);
  }, [value, delay]);

  return debouncedValue;
}
```
