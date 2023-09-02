import re

def sanitize_input(input_text):
    # Use uma expressão regular para manter apenas letras e números
    sanitized_text = re.sub(r'[^a-zA-Z0-9à-ú,\. ]', '', input_text)
    return sanitized_text

# Exemplo de entrada
user_input = "Olá, este é um exemplo de 123# entrada 456! de texto."

# Sanitização da entrada
sanitized_input = sanitize_input(user_input)

# Resultado
print("Entrada original:", user_input)
print("Entrada sanitizada:", sanitized_input)
