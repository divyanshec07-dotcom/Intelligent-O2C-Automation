import streamlit as st
import pandas as pd
import chromadb
from chromadb.utils import embedding_functions

st.set_page_config(page_title="O2C AI Reconciliation", layout="wide")

st.title("⚙️ Intelligent Order-to-Cash (O2C) Automation")
st.markdown("Generative AI Document Intelligence for Structural Steel Fabrication")

@st.cache_resource
def setup_chromadb():
    # Initialize local vector database and embedding model
    chroma_client = chromadb.Client()
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
    collection = chroma_client.create_collection(name="qa_documents", embedding_function=sentence_transformer_ef)
    return collection

@st.cache_data
def load_data():
    pos_df = pd.read_csv("data/purchase_orders.csv")
    qa_df = pd.read_csv("data/qa_logs.csv")
    return pos_df, qa_df

collection = setup_chromadb()
pos_df, qa_df = load_data()

# Feed unstructured QA logs into the Vector Database
if collection.count() == 0:
    collection.add(
        documents=qa_df['raw_text'].tolist(),
        metadatas=[{"log_id": row['log_id'], "linked_po": row['linked_po']} for _, row in qa_df.iterrows()],
        ids=qa_df['log_id'].tolist()
    )

st.subheader("Pending Invoice Reconciliations")

# UI Logic: Compare PO requirements against Vector DB semantic search
for index, po in pos_df.iterrows():
    with st.expander(f"🧾 {po['po_id']} - {po['client']}"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Contractual Requirement (ERP):**")
            st.info(po['req_spec'])
            
        with col2:
            st.markdown("**AI Extracted Shop Floor Data:**")
            # Query ChromaDB for the matching QA log
            results = collection.query(query_texts=[po['req_spec']], n_results=1)
            retrieved_doc = results['documents'][0][0]
            metadata = results['metadatas'][0][0]
            
            # Simple keyword heuristic for MVP anomaly detection (Can be replaced with LLM API later)
            if "exceeds" in retrieved_doc.lower() or "fail" in retrieved_doc.lower():
                st.error(f"⚠️ **Discrepancy Flagged in {metadata['log_id']}!**\n\n{retrieved_doc}")
                st.button("Route to Plant Manager", key=po['po_id'])
            else:
                st.success(f"✅ **Compliance Verified in {metadata['log_id']}**\n\n{retrieved_doc}")
                st.button("Approve Invoice", type="primary", key=po['po_id'])