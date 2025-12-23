# Dosya: main.py
from typing import Dict
from models import WorldState
from actions import AVAILABLE_ACTIONS # <--- Action listesini alır
from planner import calculate_plan    # <--- Planlayıcıyı çağırır

# LangChain importları (Simülasyon için mockluyoruz)
# from langchain... import ...

def perceive_intent(user_query: str) -> (WorldState, WorldState):
    """
    Normalde burada LLM çalışır ve user_query'den 
    mevcut durumu ve hedefi çıkarır.
    Şimdilik manuel simüle ediyoruz.
    """
    print(f"🤖 LLM Analiz Ediyor: '{user_query}'")
    
    # LLM Çıktısı (Simüle edilmiş)
    current_state = {"has_data": False, "report_ready": False, "mail_sent": False}
    goal_state = {"mail_sent": True}
    
    return current_state, goal_state

def execute_plan(plan, context):
    print("\n🚀 Plan Yürütülüyor...")
    for step in plan:
        print(f"--> Adım: {step.name} (Maliyet: {step.cost})")
        # Handler fonksiyonunu çağır
        result = step.handler(context)
        context.update({"last_result": result})

def main():
    user_request = "Satış verilerini çekip analiz et ve raporu gönder."
    
    # 1. Perception (Algı)
    start_state, goal_state = perceive_intent(user_request)
    
    # 2. Planning (Planlama)
    print("\n🧠 Plan Hesaplanıyor...")
    plan = calculate_plan(start_state, goal_state, AVAILABLE_ACTIONS)
    
    if not plan:
        print("❌ Hedefe giden bir plan bulunamadı!")
        return

    # Planı Göster
    print(f"✅ Plan Bulundu! Toplam Adım: {len(plan)}")
    
    # 3. Execution (Yürütme)
    context = {} # Agent hafızası (Context)
    execute_plan(plan, context)
    
    print("\n🏁 Görev Tamamlandı.")

if __name__ == "__main__":
    main()
