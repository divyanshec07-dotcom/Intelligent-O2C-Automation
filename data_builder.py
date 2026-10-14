import pandas as pd
import os

# Create data directory
os.makedirs('data', exist_ok=True)

# Simulated Purchase Orders (The Financial Requirement)
pos = [
    {"po_id": "PO-9901", "client": "Larsen & Toubro", "req_spec": "Submerged arc welding, max thermal distortion 2.0mm. Preheating induction at 150C."},
    {"po_id": "PO-9902", "client": "Tata Projects", "req_spec": "Flange straightening required. Max distortion 1.5mm. Preheating induction at 140C."},
    {"po_id": "PO-9903", "client": "Reliance Infra", "req_spec": "Magnetic Particle Inspection clear. Preheating induction at 160C."}
]

# Simulated QA Logs from the shop floor (The Unstructured Reality)
qa_logs = [
    {"log_id": "QA-001", "linked_po": "PO-9901", "raw_text": "Corimpex line 3 operator notes: Weld completed. Thermal distortion measured at 1.8mm. Induction coils held steady at 150C. NDT passed."},
    {"log_id": "QA-002", "linked_po": "PO-9902", "raw_text": "FICEP TIPO drill complete. Flange straightened. Distortion variance detected: measured 2.1mm (exceeds tolerance). Preheating at 140C."},
    {"log_id": "QA-003", "linked_po": "PO-9903", "raw_text": "MPI scan clear. No micro-cracking. Heating zones maintained at 160C."}
]

pd.DataFrame(pos).to_csv("data/purchase_orders.csv", index=False)
pd.DataFrame(qa_logs).to_csv("data/qa_logs.csv", index=False)
print("Synthetic manufacturing data generated successfully.")