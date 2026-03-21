## Master Prompting for LLMs

Prompting is the art of giving meaningful, structured input to an LLM (Large Language Model) so it can generate the most accurate, relevant, and useful output. The better your prompt, the better the response.

> 💡 **Analogy:** Think of an LLM like a very capable intern on their first day. If you say "do the thing" you'll get a random result. If you say "summarise this customer complaint in 2 sentences, in a professional tone, focusing on the main issue" you get exactly what you need. Prompting is just being specific and clear.

---

**How LLMs Actually Work (Brief Context)**

LLMs generate text by predicting the next most likely token (word/chunk) based on everything before it. Your prompt is the starting context everything you put in shapes what comes out.

- More context = better predictions
- Structured prompts = more controlled outputs
- Examples in the prompt = the model learns the pattern you want

---

**Prompting Styles (Prompt Formats)**

These are the structural formats used to send prompts to different LLMs. Think of them as the "template" your prompt is wrapped in before reaching the model.

---

**1. Alpaca Prompt**

Originally used to fine-tune the Alpaca model (by Stanford). It separates the prompt into three clear sections using special tokens: `### Instruction`, `### Input`, and `### Response`.

The model is trained to expect this exact format the `### Response` token acts as the trigger that tells the model "now generate your answer here."
```
### Instruction:
For the given number by user, please perform the arithmetic operation.

### Input:
What is 2 + 2?

### Response:
```

> 💡 The empty `### Response:` at the end is intentional you leave it blank and the model fills it in. This is how token prediction works: you set the stage, the model completes it.

**When to use:** Fine-tuned open-source models (LLaMA, Alpaca, Mistral fine-tunes) that were trained with this format.

---

**2. ChatML (OpenAI)**

ChatML (Chat Markup Language) is the format used by OpenAI's chat models (GPT-3.5, GPT-4). Instead of a single text block, it uses a structured list of messages, each with a `role` and `content`.

**Roles:**
- `system` Sets the overall behaviour and personality of the model
- `user` The human's message
- `assistant` The model's previous responses (used in multi-turn conversations)
```python
[
  {"role": "system", "content": "You are a helpful assistant who explains things simply."},
  {"role": "user", "content": "What is LRU Cache?"},
]
```

**Multi-turn conversation example:**
```python
[
  {"role": "system", "content": "You are a helpful coding assistant."},
  {"role": "user", "content": "What is a closure in JavaScript?"},
  {"role": "assistant", "content": "A closure is a function that remembers variables from its outer scope even after the outer function has finished executing."},
  {"role": "user", "content": "Can you show me an example?"},
]
```

> 💡 The `assistant` role is how you give the model "memory" of the conversation you replay the history with each request since LLMs are stateless.

**When to use:** OpenAI API, most modern LLM APIs (Anthropic, Gemini, OpenRouter, etc.) this has become the de facto standard format.

---

**Prompting Techniques**

These are strategies for *how* you construct what's inside the prompt to get better results.

---

**1. Zero-Shot Prompting**

You ask the model a question directly with no examples, no context, no instructions. Just the raw query. The model relies entirely on its training to answer.
```python
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "What is 2 + 2?"}
    ]
)
# Output: 4
```

**When it works well:** Simple, clear questions that the model has definitely seen during training (common knowledge, basic maths, factual lookups).

**When it falls short:** Complex tasks, specific formats, niche domains, or anything where you want a particular style/structure in the output.

**Example with code** : ./project/zero-shot-prompting.py

---

**2. Few-Shot Prompting**

You provide a `system` prompt that includes instructions AND a few examples of the input-output pattern you want. The model learns the pattern from your examples and applies it to the new query.
```python
system_prompt = """
You are an AI assistant specialised in maths.
You should not answer any query that is not related to maths.

Example:
Input: 2 + 2
Output: 2 + 2 is 4, calculated by adding 2 with 2.

Example:
Input: 3 * 10
Output: 3 * 10 is 30, calculated by multiplying 3 with 10.

Example:
Input: What is the colour of the sky?
Output: Bruh? That's not maths.
"""

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "What is 5 + 4?"}
    ]
)
# Output: 5 + 4 is 9, calculated by adding 5 with 4.
```

**Why it works:** LLMs are pattern matchers at their core. When you show them 3 examples of the format you want, they continue that pattern for the new input.

**When to use:** Any time you need a specific output format, tone, or behaviour. Especially useful when you want to restrict what the model talks about (like the maths-only example above).

> 💡 **Rule of thumb:** 3–5 examples is usually enough. More than that and you're wasting context window the model gets the pattern quickly.

**Example with code** : ./project/few-shot-prompting.py


---

**3. Chain of Thought (CoT) Prompting**

Instead of asking the model to jump straight to an answer, you instruct it to reason step by step. This dramatically improves accuracy on logic, planning, maths, and multi-step problems.

The key insight: making the model "think out loud" forces it to catch its own mistakes before committing to a final answer.
```python
system_prompt = """
You are a reasoning assistant. For every problem, think step by step before answering.
Return your response as strict JSON with these steps: analyse, think, output, validate, result.
"""

# Example output for "What is 2 + 2?":
{
  "step": "analyse",
  "content": "User is asking a basic arithmetic addition question."
}
{
  "step": "think",
  "content": "To add, I go left to right: 2 + 2. Starting from 2, adding 2 more gives 4."
}
{
  "step": "output",
  "content": "4"
}
{
  "step": "validate",
  "content": "4 is correct verified by counting: 1, 2, 3, 4."
}
{
  "step": "result",
  "content": "2 + 2 = 4, calculated by simple addition."
}
```

**Simple CoT trigger phrases** (you don't always need JSON sometimes just adding one of these to your prompt is enough):
- `"Think step by step."`
- `"Reason through this before answering."`
- `"Show your work."`

**When to use:** Math problems, logic puzzles, code debugging, planning tasks, anything where accuracy matters more than speed.

**Example with code** : ./project/chain-of-thought.py

---

**4. Self-Consistency Prompting**

You ask the model to solve the same problem multiple times using slightly different reasoning approaches, then pick the most common/consistent answer. This reduces the chance of a confident but wrong answer.
```python
system_prompt = """
You are an expert reasoning assistant.

Solve the problem step by step.

Important:
- Try a slightly different reasoning style each time (direct logic, rephrasing, verification).
- Double-check your conclusion.

Return strict JSON:
{
  "reasoning": "step-by-step explanation",
  "answer": "final answer"
}
"""
```

**Why it works:** LLMs can be confidently wrong (this is called hallucination). By generating multiple reasoning paths and checking for consistency, you get a more reliable answer the same way you'd cross-check an answer with multiple sources.

**When to use:** High-stakes outputs where accuracy is critical medical, financial, legal reasoning, complex maths, or anything where a wrong answer has real consequences.

> 💡 **In practice:** You can implement this by calling the model 3–5 times with the same prompt (with some temperature variation) and writing code to pick the most frequent answer from the responses.

---

**Prompting Best Practices**

**Be specific** Vague prompts get vague answers. Instead of "summarise this", say "summarise this in 3 bullet points for a non-technical audience."

**Give it a role** "You are a senior backend engineer reviewing code for security issues" gives the model a frame of reference.

**Specify the format** If you need JSON, say "return strict JSON with these fields: ...". If you need a table, say so.

**Use examples** Even one or two examples dramatically improves output quality (few-shot).

**Break complex tasks down** Instead of one giant prompt, chain multiple focused prompts together.

**Control the temperature** Lower temperature (0.1–0.3) = more deterministic/factual. Higher temperature (0.7–1.0) = more creative/varied.

---

**Summary Table**

| Technique | What You Provide | Best For |
|-----------|-----------------|----------|
| **Zero-Shot** | Just the question | Simple, clear queries |
| **Few-Shot** | Instructions + examples | Specific format/tone/behaviour |
| **Chain of Thought** | Step-by-step reasoning instruction | Logic, maths, planning |
| **Self-Consistency** | Multiple reasoning passes | High-accuracy, critical outputs |