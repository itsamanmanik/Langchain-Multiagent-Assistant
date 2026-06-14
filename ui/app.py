import streamlit as st
from graph import run_pipeline

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Multi-Agent Coding Assistant",
    page_icon="🤖",
    layout="wide",
)

# ── Styling ───────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    .agent-box {
        background: #1e1e2e;
        border-radius: 10px;
        padding: 1rem 1.2rem;
        margin-bottom: 1rem;
        border-left: 4px solid;
    }
    .planner  { border-color: #a78bfa; }
    .coder    { border-color: #34d399; }
    .debugger { border-color: #fb923c; }
    .tag {
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-bottom: 0.4rem;
    }
    .planner  .tag { color: #a78bfa; }
    .coder    .tag { color: #34d399; }
    .debugger .tag { color: #fb923c; }
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.title("🤖 Multi-Agent Coding Assistant")
st.caption("Powered by LangChain · LangGraph · Ollama — runs 100% locally, no API keys needed")
st.divider()

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ Settings")
    model = st.selectbox(
        "Ollama Model",
        ["llama3", "llama3.1", "codellama", "mistral", "gemma2"],
        help="Make sure the model is pulled via: ollama pull <model>",
    )
    st.markdown("---")
    st.markdown("**Agents pipeline:**")
    st.markdown("1. 🧠 **Planner** — breaks down the problem")
    st.markdown("2. 💻 **Coder** — writes the code")
    st.markdown("3. 🐛 **Debugger** — reviews & fixes the code")
    st.markdown("---")
    st.markdown("Made by **Aman Manikpuri**")

# ── Input ─────────────────────────────────────────────────────────────────────
user_request = st.text_area(
    "📝 Describe your coding task or paste code to debug:",
    placeholder="e.g. Write a Python function to merge two sorted lists. OR: Debug this code: ...",
    height=140,
)

run_btn = st.button("🚀 Run Agents", type="primary", use_container_width=True)

# ── Pipeline execution ────────────────────────────────────────────────────────
if run_btn:
    if not user_request.strip():
        st.warning("Please enter a coding task first.")
        st.stop()

    col1, col2, col3 = st.columns(3)

    # Planner
    with col1:
        with st.spinner("🧠 Planner thinking..."):
            plan_placeholder = st.empty()

    # Coder
    with col2:
        with st.spinner("💻 Coder writing..."):
            code_placeholder = st.empty()

    # Debugger
    with col3:
        with st.spinner("🐛 Debugger reviewing..."):
            debug_placeholder = st.empty()

    with st.spinner("Running agent pipeline... this may take a minute on first run."):
        result = run_pipeline(user_request, model=model)

    # ── Display results ───────────────────────────────────────────────────────
    st.divider()
    st.subheader("🧠 Planner Agent")
    st.markdown(
        f'<div class="agent-box planner"><div class="tag">Plan</div>{result["plan"]}</div>',
        unsafe_allow_html=True,
    )

    st.subheader("💻 Coder Agent")
    st.markdown(result["code"], unsafe_allow_html=False)

    st.subheader("🐛 Debugger Agent — Final Output")
    st.markdown(result["final_code"], unsafe_allow_html=False)

    # Download button
    st.divider()
    import re
    code_blocks = re.findall(r"```python\n(.*?)```", result["final_code"], re.DOTALL)
    final_code_clean = code_blocks[0] if code_blocks else result["final_code"]

    st.download_button(
        label="⬇️ Download Final Code (.py)",
        data=final_code_clean,
        file_name="generated_code.py",
        mime="text/plain",
        use_container_width=True,
    )
