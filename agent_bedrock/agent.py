import os
import re
from groq import Groq
from tools import create_ticket, get_faq_answer

MODEL_ID = "llama-3.1-8b-instant"


def get_groq_client(api_key):
    return Groq(api_key=api_key)


def invoke_groq(client, prompt):
    try:
        response = client.chat.completions.create(
            model=MODEL_ID,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful customer support AI agent. Respond only in plain text without HTML or div tags."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.5,
            max_tokens=300
        )

  
        reply = response.choices[0].message.content

 
        clean_reply = re.sub(r'<.*?>', '', reply)

        return clean_reply

    except Exception as e:
        return f"❌ Error: {str(e)}"


def agent_response(client, user_input):

    faq = get_faq_answer(user_input)

    if faq:
        return faq

   
    decision_prompt = f"""
User Query: {user_input}

Rules:
- If user reports a problem, respond ONLY with CREATE_TICKET
- Otherwise respond normally
"""

    decision = invoke_groq(client, decision_prompt)

  
    if decision and "CREATE_TICKET" in decision:
        return create_ticket(user_input)

    final_response = invoke_groq(client, user_input)

    if not final_response or final_response.strip() == "":
        return "⚠️ No response generated"

    return final_response