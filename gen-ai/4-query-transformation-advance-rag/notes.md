## Query Transformation — Advanced RAG Techniques

**Recap: Basic RAG**

In the previous doc we covered basic RAG, which follows three steps:
```
Indexing → Retrieval → Generation
```

This works well for clean, well-formed queries. But in real-world usage, users rarely ask perfect questions. They might be vague, use the wrong words, have typos, or phrase things in a way that doesn't match how the content was written. That's where the basic approach breaks down.

---

**Advanced RAG Pipeline**

Advanced RAG adds three new steps before the original three:
```
Query Transformation → Routing → Query Construction → Indexing → Retrieval → Generation
```

The last three steps (Indexing, Retrieval, Generation) are the same as basic RAG. The first three are new additions that make the system smarter and more robust. Now focuses on the first step: **Query Transformation**.

---

### Why Query Transformation?

In a RAG system, the user's query drives everything. If the query is poor, the vector search returns irrelevant chunks, and the LLM generates a bad or incomplete answer. The problem is you can't control what the user types.
```
Garbage In → Garbage Out
```

Users might:
- Ask something too vague ("tell me about the system")
- Misspell words ("authenication" instead of "authentication")
- Use different terminology than what's in the documents ("log in" vs "OAuth flow")
- Ask a multi-part question that would be better split into separate searches

Query Transformation is the step where you **improve the user's query before retrieval**, so the semantic search has the best possible input to work with.

> 💡 **Analogy:** Just how google does it for the bad queries. Even if we ask too vague or misspell queries to the google search it get's us the correct or relevant search results.

---

####Technique 1 — Parallel Query (Fan Out) Retrieval

**The core idea:** Instead of searching with just the user's original query, generate multiple alternative versions of the query using an LLM, then search with all of them simultaneously.

**Why this works:**
The user's query might not use the same words as your indexed documents. By generating 3–5 variations, you increase the chance that at least one of them closely matches the language used in the relevant chunks.

**The flow:**
```
User Query
     │
     ▼
LLM generates N alternative queries (e.g. 3 variations)
     │
     ▼
Embed all queries (original + generated)
     │
     ▼
Run semantic search for each query in parallel
     │
     ▼
Merge and deduplicate retrieved chunks
     │
     ▼
Pass combined context to LLM for final answer
```

**Concrete example:**

User asks: "how do i get into the system"

The LLM generates alternative queries:
1. "user authentication and login process"
2. "how to access the platform with credentials"
3. "sign in flow and OAuth setup"

Now all four queries (original + 3 generated) are embedded and searched. Even if the original query wouldn't have matched the relevant docs, one of the generated ones almost certainly will.

**Simple code structure:**
```python
def generate_parallel_queries(user_query: str, n: int = 3) -> list[str]:
    prompt = f"""
    Generate {n} different version of the following query.
    Each version should have a slightly different phrasing or perspective, but it should be related to the original query and preserve the original intent.
    
    Original query: {user_query}  
    
    Output: Return only the queries, one per line, without numbering or bullets. 
    """
    response = llm.generate(prompt)
    return [user_query] + response.split("\n")  # original + generated
```

**What it fixes:**
- Vague queries: generates more specific versions
- Spelling mistakes: LLM corrects them in generated queries
- Terminology mismatch: generated queries use alternative vocabulary
- Narrow queries: fan-out covers more angles of the same topic
---

**Practical Example at - ./query-transformation-fanout-practical**

---

![parallel query fan out technique diagram](./images/parallel-query-fan-out-technique-diagram.png)

---

**When to Use Query Transformation**

Query Transformation adds an extra LLM call per query, which means latency and cost. It's worth it when:

- Your users are non-technical and ask vague or informal questions
- Your documents use technical or domain-specific language users might not know
- The quality of retrieval is more important than response speed
- You're getting poor results from basic RAG on certain types of queries 