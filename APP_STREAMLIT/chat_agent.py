# Gestisce la parte “intelligente” o linguistica, per generare spiegazioni e risposte da LLM

from openai import OpenAI
from dotenv import load_dotenv
import os

# Carica le variabili d'ambiente definite in .env
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

if api_key is None:
    raise ValueError("Chiave API OpenRouter non trovata. Assicurati di avere un file .env con OPENROUTER_API_KEY=...")

# Inizializza il client OpenRouter
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    default_headers={
        "X-Title": "Chatbot Pattini a rotelle"  # opzionale, titolo descrittivo
    }
)

def ask_llm(prompt, model="qwen/qwen3-vl-235b-a22b-thinking"):
    """Invia un prompt al modello linguistico e restituisce la risposta generata."""
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "Sei un esperto di manutenzione per pattini in linea."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content


## explain_rotation da implementare
def explain_rotation(usure, ordered_indices):
    """
    Genera una spiegazione base della rotazione consigliata.
    """
    msg = f"Le ruote con usura minore ({ordered_indices[0]}, {ordered_indices[1]}) possono essere spostate in avanti per garantire maggior controllo. "
    msg += "Le ruote più consumate andrebbero in posizioni posteriori per bilanciare la durata residua."
    return msg


# 👇 BLOCCO DI TEST — aggiunto qui
if __name__ == "__main__":
    print("🚀 Test rapido del modello LLM...\n")
    prompt_test = "Ciao! Raccontami in una frase perché dovrei ruotare regolarmente le ruote dei miei pattini."
    risposta = ask_llm(prompt_test)
    print("💬 Risposta del modello:\n")
    print(risposta)