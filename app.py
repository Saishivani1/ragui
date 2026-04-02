import streamlit as st

st.set_page_config(page_title="RAG Builder Pro", layout="wide")

# -------------------------------
# STATE
# -------------------------------
if "config" not in st.session_state:
    st.session_state.config = {}

# -------------------------------
# HEADER
# -------------------------------
st.title("🧠 RAG Builder Pro")
st.caption("Clean, structured RAG pipeline builder aligned with architecture")

st.divider()

# -------------------------------
# TABS
# -------------------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "🔍 Query",
    "📂 Data",
    "⚙️ Pipeline",
    "🚀 Run"
])

# =====================================================
# 🔍 TAB 1 — QUERY
# =====================================================
with tab1:
    st.subheader("Query & Understanding")

    st.session_state.config["query"] = st.text_area("User Query", height=120)

    col1, col2 = st.columns(2)

    with col1:
        st.session_state.config["query_strategy"] = st.selectbox(
            "Query Strategy",
            ["None", "Query Rewriting", "Query Expansion", "Multi-query", "HyDE"]
        )

    with col2:
        st.session_state.config["response_mode"] = st.selectbox(
            "Response Style",
            ["Concise", "Detailed", "Bullet Points", "JSON"]
        )

# =====================================================
# 📂 TAB 2 — DATA INGESTION (FULLY FIXED)
# =====================================================
with tab2:
    st.subheader("Data Ingestion Layer")

    # ---------------- Sources ----------------
    with st.expander("📁 Sources", expanded=True):
        sources = st.multiselect(
            "Select Data Sources",
            ["PDF", "DOCX", "PPT", "HTML", "Markdown",
             "CSV / Excel", "Images (OCR)", "Audio", "Video"]
        )
        st.session_state.config["sources"] = sources

        st.markdown("### 📥 Provide Data")

        if any(x in sources for x in ["PDF", "DOCX", "PPT"]):
            st.file_uploader("Upload Documents", accept_multiple_files=True)

        if "CSV / Excel" in sources:
            st.file_uploader("Upload CSV/Excel Files", accept_multiple_files=True)

        if "Images (OCR)" in sources:
            st.file_uploader("Upload Images", accept_multiple_files=True)

        if "Audio" in sources:
            st.file_uploader("Upload Audio Files", accept_multiple_files=True)

        if "Video" in sources:
            st.file_uploader("Upload Video Files", accept_multiple_files=True)

        if any(x in sources for x in ["HTML", "Markdown"]):
            st.text_area("Paste HTML/Markdown content or URL")

    # ---------------- Connectors ----------------
    with st.expander("🔗 Connectors"):
        connectors = st.multiselect(
            "External Integrations",
            ["Google Drive", "Notion", "Slack", "Confluence",
             "S3 / Blob Storage", "APIs", "Web Scraping"]
        )
        st.session_state.config["connectors"] = connectors

        st.markdown("### 🔐 Configure Connections")

        if "Google Drive" in connectors:
            st.text_input("Google Drive Folder URL")

        if "Notion" in connectors:
            st.text_input("Notion Page/Database URL")

        if "Slack" in connectors:
            st.text_input("Slack Token / Channel")

        if "Confluence" in connectors:
            st.text_input("Confluence Space URL")

        if "S3 / Blob Storage" in connectors:
            st.text_input("Bucket Name")
            st.text_input("Access Key")

        if "APIs" in connectors:
            st.text_input("API Endpoint URL")

        if "Web Scraping" in connectors:
            st.text_input("Website URL")

    # ---------------- Preprocessing ----------------
    with st.expander("🧹 Preprocessing"):
        preprocessing = st.multiselect(
            "Preprocessing Steps",
            ["OCR", "Cleaning", "Table Extraction",
             "Language Detection", "Translation", "Metadata Extraction"]
        )
        st.session_state.config["preprocessing"] = preprocessing

        if "OCR" in preprocessing:
            st.selectbox("OCR Engine", ["Tesseract", "EasyOCR"])

        if "Translation" in preprocessing:
            st.selectbox("Target Language", ["English", "Hindi", "Spanish"])

        if "Metadata Extraction" in preprocessing:
            st.checkbox("Extract metadata fields")

# =====================================================
# ⚙️ TAB 3 — PIPELINE
# =====================================================
with tab3:
    st.subheader("RAG Pipeline Configuration")

    # Processing
    with st.expander("🧩 Chunking & Embedding", expanded=True):
        col1, col2 = st.columns(2)

        with col1:
            st.session_state.config["chunking"] = st.selectbox(
                "Chunking Strategy",
                ["Fixed-size", "Recursive", "Semantic",
                 "Sliding Window", "Hierarchical", "Code-aware"]
            )
            st.session_state.config["chunk_size"] = st.slider("Chunk Size", 100, 2000, 500)

        with col2:
            st.session_state.config["embedding"] = st.selectbox(
                "Embedding Model",
                ["OpenAI", "Cohere", "HuggingFace"]
            )

    # Vector Store
    with st.expander("💾 Vector Store"):
        st.session_state.config["vector_db"] = st.selectbox(
            "Vector Database",
            ["Pinecone", "Weaviate", "FAISS", "Chroma", "pgvector"]
        )

    # Retrieval
    with st.expander("🔎 Retrieval"):
        retrieval = st.selectbox(
            "Retrieval Strategy",
            ["Dense", "Sparse (BM25)", "Hybrid", "Graph RAG", "Parent-child"]
        )
        st.session_state.config["retrieval"] = retrieval

        st.session_state.config["top_k"] = st.slider("Top-K", 1, 20, 5)

        if retrieval == "Hybrid":
            st.info("Requires Dense + BM25")
        elif retrieval == "Graph RAG":
            st.warning("Requires Knowledge Graph (Neo4j)")
        elif retrieval == "Parent-child":
            st.warning("Requires Hierarchical Chunking")

    # Reranking
    with st.expander("📊 Reranking"):
        st.session_state.config["rerank"] = st.selectbox(
            "Reranker",
            ["None", "Cross-encoder", "LLM reranker", "MMR"]
        )

    # Context
    with st.expander("🧠 Context Construction"):
        st.session_state.config["context"] = st.selectbox(
            "Context Strategy",
            ["Simple concat", "Ranked concat", "Compression", "Summarization"]
        )

    # Generation
    with st.expander("🤖 Generation"):
        col1, col2 = st.columns(2)

        with col1:
            st.session_state.config["llm"] = st.selectbox(
                "LLM",
                ["GPT", "Claude", "Gemini", "Mistral"]
            )

        with col2:
            st.session_state.config["temperature"] = st.slider(
                "Temperature", 0.0, 1.0, 0.3
            )

    # Advanced
    with st.expander("🚀 Advanced (Memory, Agents, Guardrails)"):
        st.session_state.config["memory"] = st.selectbox(
            "Memory",
            ["None", "Sliding Window", "Summary", "Vector Memory"]
        )

        st.session_state.config["agent"] = st.selectbox(
            "Agent",
            ["None", "ReAct", "Plan & Execute"]
        )

        st.session_state.config["guardrails"] = st.multiselect(
            "Guardrails",
            ["Hallucination Detection", "Citation Enforcement",
             "Toxicity Filter", "PII Masking", "Prompt Injection"]
        )

    # System
    with st.expander("⚙️ System (Infra + Observability + Security)"):
        st.session_state.config["observability"] = st.multiselect(
            "Observability",
            ["Logging", "Tracing", "Metrics", "LLM-as-judge"]
        )

        st.session_state.config["infra"] = st.multiselect(
            "Infrastructure",
            ["Caching", "Streaming", "Async Processing"]
        )

        st.session_state.config["security"] = st.selectbox(
            "Security",
            ["RBAC", "ACL", "Audit Logs", "Encryption"]
        )

# =====================================================
# 🚀 TAB 4 — RUN
# =====================================================
with tab4:
    st.subheader("Run & Debug")

    st.markdown("### Configuration Preview")
    st.json(st.session_state.config)

    if st.button("▶ Run Pipeline"):
        if not st.session_state.config.get("query"):
            st.error("Please enter a query")
        else:
            st.success("Pipeline executed successfully")

            st.markdown("### Output")
            st.info("Generated response will appear here")

            col1, col2, col3 = st.columns(3)
            col1.metric("Latency", "1.2s")
            col2.metric("Docs Retrieved", "5")
            col3.metric("Tokens", "1100")