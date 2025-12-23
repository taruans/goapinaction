# Dosya: actions.py
from models import GoapAction # <--- models.py'ı çağırır

# --- Gerçek Fonksiyonlar (Tools) ---
def func_fetch_data(context):
    print(f"[EXEC] Veritabanından veri çekiliyor...")
    return {"raw_data": "Sales_2024.csv"}

def func_analyze_data(context):
    print(f"[EXEC] Veri analiz ediliyor...")
    return {"report_path": "/tmp/report.pdf"}

def func_send_email(context):
    print(f"[EXEC] Rapor yöneticiye e-postalandı.")
    return "Success"

# --- GOAP Tanımları (Registry) ---
# Bu listeyi main.py çağıracak
AVAILABLE_ACTIONS = [
    GoapAction(
        name="FetchData",
        cost=1,
        preconditions={"has_data": False},
        effects={"has_data": True},
        handler=func_fetch_data
    ),
    GoapAction(
        name="AnalyzeData",
        cost=5, # Pahalı işlem
        preconditions={"has_data": True, "report_ready": False},
        effects={"report_ready": True},
        handler=func_analyze_data
    ),
    GoapAction(
        name="SendEmail",
        cost=2,
        preconditions={"report_ready": True, "mail_sent": False},
        effects={"mail_sent": True},
        handler=func_send_email
    )
]
