from search import search_prompt


def main():
    print("Chat iniciado! Digite 'sair' para encerrar.")
    print("-" * 50)

    while True:
        try:
            question = input("\nSua pergunta: ").strip()
            if question.lower() in ["sair", "exit", "quit"]:
                print("Chat encerrado!")
                break

            if not question:
                print("Por favor, digite uma pergunta válida.")
                continue

            print("\nBuscando resposta...")
            response = search_prompt(question)
            print(f"\nResposta: {response}")

        except KeyboardInterrupt:
            print("\n\nChat encerrado!")
            break
        except Exception as e:
            print(f"\nErro: {e}")
            print("Tente novamente.")


if __name__ == "__main__":
    main()
