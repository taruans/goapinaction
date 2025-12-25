# actions.py içeriği
import time
from models import GoapAction

# --- Gerçek İş Mantığı (Handlers) ---
# Buraları normalde AWS SDK (boto3) veya Slack API ile dolduracaksın.

def handler_backup_db(context):
    print(">> [AWS RDS] Snapshot alınıyor...")
    time.sleep(1) # Simülasyon
    return {"backup_id": "snap-12345", "timestamp": "2024-05-21T10:00:00"}

def handler_restore_db(context):
    backup_id = context.get("last_result", {}).get("backup_id", "default-snap")
    print(f">> [AWS RDS] {backup_id} test sunucusuna yükleniyor...")
    return {"status": "restored", "endpoint": "test-db.local"}

def handler_check_integrity(context):
    print(">> [SQL] 'SELECT COUNT(*) FROM Users' çalıştırılıyor...")
    return {"status": "healthy", "row_count": 1500}

def handler_send_slack(context):
    print(">> [Slack API] #devops kanalına 'İşlem Başarılı' mesajı atılıyor.")
    return "MessageSent"

# --- GOAP Tanımları ---
DEVOPS_ACTIONS = [
    # Adım 1: Yedek Al
    GoapAction(
        name="TakeBackup",
        cost=10, # Pahalı işlem
        preconditions={"db_backup_taken": False},
        effects={"db_backup_taken": True},
        handler=handler_backup_db
    ),
    # Adım 2: Yedeği Dön
    GoapAction(
        name="RestoreToTest",
        cost=5,
        preconditions={"db_backup_taken": True, "test_db_restored": False},
        effects={"test_db_restored": True},
        handler=handler_restore_db
    ),
    # Adım 3: Kontrol Et (Opsiyonel ama iyi bir pratik)
    GoapAction(
        name="HealthCheck",
        cost=1,
        preconditions={"test_db_restored": True, "integrity_checked": False},
        effects={"integrity_checked": True},
        handler=handler_check_integrity
    ),
    # Adım 4: Haber Ver
    GoapAction(
        name="NotifyTeam",
        cost=1,
        preconditions={"integrity_checked": True, "slack_notified": False},
        effects={"slack_notified": True},
        handler=handler_send_slack
    )
]
