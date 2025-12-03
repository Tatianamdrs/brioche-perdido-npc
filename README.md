# GenAI NPC: O Mestre da Fermentação

> Mecânica de RPG que utiliza Generative AI para criar diálogos dinâmicos e não-lineares, parte do projeto "A Jornada do Brioche Perdido".

## Sobre o Projeto
Em jogos tradicionais, NPCs (Non-Playable Characters) têm falas limitadas e repetitivas. Este projeto implementa uma classe em **Python** que conecta o personagem a uma **LLM (Large Language Model)**, permitindo que ele:
* Mantenha uma "persona" consistente (prompt engineering).
* Reaja ao input livre do jogador.
* Guarde o contexto da conversa (memória de curto prazo).

## Engenharia de Prompt
O personagem foi instruído via *System Prompt* a:
1.  Nunca quebrar a "quarta parede".
2.  Utilizar metáforas relacionadas a panificação e alquimia.
3.  Manter uma personalidade rabugenta e excêntrica.

## 🛠️ Tecnologias
* **Python 3.12**
* **OpenAI API**
* **Dotenv** (Gerenciamento de Segredos)

## 🚀 Como Jogar Localmente
1. Clone o repositório.
2. Instale as dependências: `pip install openai python-dotenv`
3. Configure o `.env` com sua API Key.
4. Execute: `python npc.py`

---
*Desenvolvido por Tatiana Medeiros. Código escrito com farinha digital e Python.*