generation_config = {
    "temperature": 0.1,
}

model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    system_instruction=system_instruction,
    generation_config=generation_config,
)
  
