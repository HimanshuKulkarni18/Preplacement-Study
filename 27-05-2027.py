####LLM-AI !0 Q/A Thoery

1. What is Prompt Engineering?

Prompt engineering is the practice of designing effective inputs/prompts to get better outputs from LLMs.

Example:
Instead of:

“Write email”

Use:

“Write a professional apology email to a client for delayed delivery.”

#2. What is Generative AI?

Generative AI creates new content such as:

Text
Images
Audio
Video
Code

Examples:

ChatGPT
Midjourney
GitHub Copilot

#3. What is Hallucination in LLMs?

Hallucination happens when an AI model generates incorrect or fabricated information confidently.

Example:
Giving fake references or wrong facts.

#4. What is RAG in AI?

RAG = Retrieval-Augmented Generation.

It combines:

Information retrieval
LLM text generation

The model first fetches relevant information from documents/databases, then generates answers.

#5. What is Embedding?

Embeddings are numerical vector representations of text that capture semantic meaning.

Similar meanings → vectors close together.

Used in:

Search
Recommendation systems
RAG systems

#6. What is Vector Database?

A vector database stores embeddings for efficient similarity search.

Popular examples:

Pinecone
Weaviate
Chroma

#7. What is Temperature in LLMs?

Temperature controls randomness in AI responses.

Low temperature → More focused/deterministic
High temperature → More creative/random


#8. What is Context Window?

The context window is the amount of text/tokens an LLM can remember during a conversation.

Larger context windows help with:

Long documents
Multi-turn conversations
Code analysis

#9. What is Zero-shot, One-shot, and Few-shot Learning?
Zero-shot

No examples given.

One-shot

One example provided.

Few-shot

A few examples provided to guide the model.

#10. What are AI Agents?

AI agents are systems that can:

Reason
Plan
Use tools/APIs
Perform tasks autonomously

Examples:

Research agents
Coding agents
Customer support agents

####Small SCale Coding quetions Python
# 
# .Find Maximum Number
nums = [5, 2, 9, 1]

print(max(nums))

# Remove Duplicates
nums = [1,2,2,3,4,4]

print(list(set(nums)))

#Count Vowels
text = "python"

count = 0

for ch in text:
    if ch in "aeiou":
        count += 1

#print(count)
Swap Two Numbers
a = 5
b = 10

a, b = b, a

#print(a, b)
Find Largest Among Three Numbers
a = 10
b = 20
c = 15

print(max(a, b, c))

