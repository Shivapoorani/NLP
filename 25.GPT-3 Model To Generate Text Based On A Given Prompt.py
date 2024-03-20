import openai

openai.api_key = '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'

def generate_text(prompt, max_tokens=100):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=max_tokens
    )

    generated_text = response['choices'][0]['text']
    return generated_text

def main():
    prompt = input("Enter a prompt: ")
    generated_text = generate_text(prompt)

    print("\nGenerated Text:")
    print(generated_text)

if __name__ == "__main__":
  main()
