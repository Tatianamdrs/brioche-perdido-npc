import os
import sys
from dotenv import load_dotenv
from openai import OpenAI

# carrega o .env da pasta raiz 
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key) if api_key else None

class IntelligentNPC:
    def __init__(self, name, role, personality):
        self.name = name
        self.role = role
        self.personality = personality
        self.conversation_history = [
            {"role": "system", "content": f"Você é {self.name}, um {self.role} neste jogo de RPG. "
                                          f"Sua personalidade é: {self.personality}. "
                                          f"Responda de forma curta, ríspida mas sábia. Use metáforas de pão e fermentação. "
                                          f"Nunca quebre a quarta parede."}
        ]

    def talk(self, user_input):
        self.conversation_history.append({"role": "user", "content": user_input})

        # MODO COM IA REAL
        if client and api_key:
            try:
                print("🌀 (O Mestre está fermentando a resposta...)")
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=self.conversation_history,
                    temperature=0.8 # Um pouco mais criativo para RPG
                )
                npc_reply = response.choices[0].message.content
                self.conversation_history.append({"role": "assistant", "content": npc_reply})
                return npc_reply
            except Exception as e:
                print(f"⚠️ Erro Mágico: {e}")
                print("-> Usando pergaminho de reserva (Simulação)...")

        # MODO SIMULAÇÃO (FALLBACK)
        # Respostas aleatórias para quando a API falhar
        import random
        frases_simuladas = [
            "Você tem a paciência de um pão sem fermento. Saia da minha frente!",
            "O segredo da vida é como a massa madre: precisa de tempo e calor. Você não tem nenhum dos dois.",
            "Humph. Sinto cheiro de farinha barata em você.",
            "Traga-me o Brioche Perdido ou cale-se. Minha fornalha não espera por ninguém."
        ]
        return random.choice(frases_simuladas)

# loop do Jogo
if __name__ == "__main__":
    npc = IntelligentNPC(
        name="Mestre da Fermentação", 
        role="Alquimista Padeiro", 
        personality="Rabugento, místico, obcecado por glúten e tempo."
    )

    print(f"\n🥖 Você encontrou o {npc.name} em sua oficina cheia de farinha brilhante.\n")
    print("(Digite 'sair' para encerrar)")
    
    while True:
        user_msg = input("\nVocê: ")
        if user_msg.lower() in ["sair", "exit", "tchau"]:
            print(f"{npc.name}: Que seu caminho não sole. Adeus.")
            break
            
        reply = npc.talk(user_msg)
        print(f"{npc.name}: {reply}")