# ⚙️ Intelligent Order-to-Cash (O2C) Automation & Revenue Leakage Analysis

## Executive Summary
This project reengineers the Order-to-Cash (O2C) pipeline for a global structural steel manufacturing enterprise. The legacy process suffered from a bloated 45-day Days Sales Outstanding (DSO) cycle and a 12% revenue leakage due to manual reconciliation of unstructured shop floor data against financial Purchase Orders (POs). By integrating a Generative AI Document Intelligence framework (RAG architecture), this system automatically extracts, semantically validates, and reconciles technical manufacturing logs, projecting a DSO reduction to 28 days.

## 1. Business Architecture & Gap Analysis
Invoices were previously bottlenecked by manual financial reviews of highly technical production documents (e.g., thermal distortion logs, Magnetic Particle Inspection results from Corimpex welding lines). 

| Category | Current State (As-Is) | Target State (To-Be) | Required Action / Gap to Close |
| :--- | :--- | :--- | :--- |
| **Process** | Invoicing waits 17 days for manual aggregation of shop floor QA and welding reports. | Continuous, real-time matching of production logs to ERP financial systems. | Redesign workflow so QA document generation triggers automated ERP webhooks. |
| **Technology** | Finance relies on manual visual checks of technical PDFs against legacy ERP screens. | GenAI (RAG/LangChain) engine semantically parses unstructured PDFs and validates data. | Deploy a vector database (ChromaDB) to process and store unstructured manufacturing reports. |
| **People** | Production Managers spend 15% of their week chasing paperwork for the finance department. | Production Managers manage by exception, only reviewing AI-flagged discrepancies. | Establish a new RACI matrix for exception handling. |

## 2. Requirements Traceability Matrix (RTM)
The RTM maps high-level business objectives to specific technical deliverables and User Acceptance Testing (UAT) criteria.

| Req ID | Business Requirement | Technical Implementation | UAT Criteria |
| :--- | :--- | :--- | :--- |
| **BR-01** | Accelerate invoice reconciliation by 15 days. | Ingest unstructured QA logs into **ChromaDB** for instant retrieval. | System ingests and indexes 500 synthetic PDF logs in < 10 seconds. |
| **BR-02** | Eliminate 12% revenue leakage from missed contract variances. | **all-MiniLM-L6-v2 Sentence Transformers** cross-reference PO specs with shop floor data. | AI successfully flags a 2.1mm thermal distortion against a 1.5mm PO tolerance. |
| **BR-03** | Prevent Finance from authorizing non-compliant shipments. | UI conditionally locks the "Approve Invoice" function upon detecting a discrepancy. | "Approve" button is replaced by "Route to Plant Manager" when exceptions occur. |

## 3. Stakeholder Matrix (RACI)
Defining operational governance for the automated "To-Be" state.

| Process / Task | Plant Production Mgr | Financial Analyst | IT / Data Engineer | Project Sponsor |
| :--- | :--- | :--- | :--- | :--- |
| **Log Technical QA Data (NDT, Temp)** | Responsible | Informed | Consulted | Informed |
| **Run Semantic RAG Reconciliation** | Informed | Accountable | Responsible | Informed |
| **Review Flagged Discrepancies** | Accountable | Responsible | Informed | Consulted |
| **Vector DB Maintenance & Model Drift** | Consulted | Informed | Responsible | Accountable |

*R = Responsible (Does the work), A = Accountable (Approves the work), C = Consulted (Provides input), I = Informed (Kept in the loop).*

## 4. Technical Architecture
* **Frontend:** Streamlit 
* **Data Processing:** Pandas, NumPy
* **AI / Vector Store:** ChromaDB, Sentence-Transformers (`all-MiniLM-L6-v2`)
* **Deployment:** Local executable for highly sensitive, on-premise industrial data environments.

## Quick Start
```bash
pip install -r requirements.txt
python data_builder.py
streamlit run app.py