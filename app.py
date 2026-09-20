model = genai.GenerativeModel(
    model_name='gemini-1.0-pro',
    system_instruction=system_instruction,
    generation_config=generation_config,
)
