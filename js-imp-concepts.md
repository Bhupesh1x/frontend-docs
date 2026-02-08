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

---

## Throttling in JavaScript

Understanding how to limit the rate at which a function executes using throttling.

**What is Throttling?**

Throttling is a technique used for performance optimization and rate limiting. It ensures that a function is called at most once during a specified time interval, no matter how many times it's triggered.

Think of it like a speed limit for function execution.

**JavaScript Implementation**
```javascript
function throttle(fn, delay = 300) {
  let flag = true;

  return function(...args) {
    // If flag is false, we're in cooldown period
    if (!flag) {
      return; // Ignore this call
    }

    // Execute the function
    fn.apply(this, args);
    
    // Enter cooldown period
    flag = false;

    // After delay, exit cooldown period
    setTimeout(() => {
      flag = true;
    }, delay);
  };
}
```

**Using the Throttle Function**
```javascript
let count = 0;

function handleResize() {
  console.log(`Resize event occurred: ${count++}`);
}

// Create throttled version
let throttledResize = throttle(handleResize, 300);

// Use throttled version in event listener
window.addEventListener("resize", throttledResize);
```