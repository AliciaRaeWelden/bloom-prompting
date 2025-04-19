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
