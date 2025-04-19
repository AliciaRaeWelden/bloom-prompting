# 🌱 Prompting as Pedagogy: A Bloom's Taxonomy Framework for Agentic LLMs

This repository contains a minimal viable implementation of **prompting-as-pedagogy**, where Bloom's Taxonomy is used to scaffold agent prompts and guide cognitive development in large language models.

## 🎯 Project Goal
Use prompts based on **Bloom's cognitive levels** (Remember → Understand → Apply → Analyze → Evaluate → Create) to:
- Scaffold model reasoning
- Evaluate output depth
- Improve generalization and reflection

## 🧪 MVP Deliverables

### 1. `bloom_prompt.py`
A Python module that takes a user task (natural language instruction) and outputs a chain of prompts, each targeting a Bloom level.

```python
# bloom_prompt.py

BLOOM_TEMPLATES = {
    "Remember": "List key facts or definitions relevant to the following: {task}",
    "Understand": "Paraphrase the following concept in your own words: {task}",
    "Apply": "Use the concept described to solve a new but related problem: {task}",
    "Analyze": "Compare and contrast key elements or causes within this topic: {task}",
    "Evaluate": "Form a reasoned judgment about the strengths or weaknesses of: {task}",
    "Create": "Propose a novel approach, idea, or solution based on the following: {task}"
}

def scaffold_prompt(task, levels=None):
    """
    Generate a list of Bloom-level prompts for a given task.

    Args:
        task (str): The original user instruction.
        levels (list): Optional list of Bloom levels to include.

    Returns:
        list of str: Scaffolded prompts.
    """
    if levels is None:
        levels = list(BLOOM_TEMPLATES.keys())

    prompts = []
    for level in levels:
        template = BLOOM_TEMPLATES.get(level)
        if template:
            prompts.append(template.format(task=task))
    return prompts

if __name__ == "__main__":
    example_task = "Explain how rain forms."
    bloom_chain = scaffold_prompt(example_task, levels=["Understand", "Analyze", "Evaluate"])
    for p in bloom_chain:
        print(f"\n[{p.split(':')[0]}] {p}")
```

### 2. `bloom_eval_rubric.json`
A human evaluation rubric that links Bloom levels to output characteristics.

```json
{
  "Understand": "Response paraphrases or restates the concept accurately.",
  "Analyze": "Response identifies patterns, relationships, or distinctions.",
  "Evaluate": "Response includes a reasoned judgment or comparison based on evidence."
}
```

### 3. `agent_bloom_curriculum.md`
A curriculum of task examples organized by Bloom level.

```markdown
### Bloom Curriculum

#### Understand
- "Explain the causes of World War I."

#### Analyze
- "Compare and contrast Keynesian and monetarist approaches to inflation."

#### Evaluate
- "Which is a more sustainable energy source: wind or solar? Justify your answer."
```

### 4. `ReflectionBloom.md`
A reusable scaffold for prompting reflection in LLMs using Bloom levels.

```markdown
### Bloom-Based Reflection Template

1. **Describe** (Remember): What did I do?
2. **Explain** (Understand): Why did I do it that way?
3. **Critique** (Analyze): What worked or didn't?
4. **Evaluate**: Was this the best approach?
5. **Revise** (Create): How could I improve this next time?
```

---

### 🚀 Interactive App: Run from GitHub
We include a small Streamlit app so users can generate Bloom-scaffolded prompts directly from their browser.

To try it out locally:

```bash
pip install streamlit
streamlit run app.py
```

Create a file called `app.py`:

```python
# app.py
import streamlit as st
from bloom_prompt import scaffold_prompt

st.title("🧠 Bloom's Prompt Builder")

task = st.text_area("Enter a learning or reasoning task")
selected_levels = st.multiselect(
    "Choose Bloom levels to scaffold",
    ["Remember", "Understand", "Apply", "Analyze", "Evaluate", "Create"],
    default=["Understand", "Analyze"]
)

if st.button("Generate Prompts"):
    if task:
        prompts = scaffold_prompt(task, levels=selected_levels)
        for i, prompt in enumerate(prompts):
            st.markdown(f"**{selected_levels[i]}**: {prompt}")
    else:
        st.warning("Please enter a task first.")
```

---

## 🚧 To Do
- [x] Add prompt templates for each Bloom level
- [x] Add Streamlit app for browser-based use
- [ ] Integrate with OpenAI/GPT API for live completions
- [ ] Create few-shot examples for reflection
- [ ] Evaluate performance across different prompting structures

## 📜 License
MIT

---

> Inspired by educational frameworks from Ash & Clayton (2009) and Bloom's Taxonomy. Developed as a prototype for reflective and developmental LLM agents.
