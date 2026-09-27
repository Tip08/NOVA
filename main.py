from core.assistant import Nova



def main():
    nova = Nova()
    nova.start()


    while nova.running:
        try:
            command = input("\nNOVA >")

            if not command.strip():
                continue


            response = nova.process_command(command)

            if response: 
                print(response)

        except KeyboardInterrupt:
             print("\nShutting down NOVA.")
             break

        except EOFError:
            print("\nShutting down NOVA.")
            break

if __name__ == "__main__":
    main()
