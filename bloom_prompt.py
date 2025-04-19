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
