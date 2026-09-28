from core.assistant import Nova
from core.logger import logger


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
             logger.info("NOVA interrupted by keyboard")
             print("\nShutting down NOVA.")
             break

        except EOFError:
            logger.info("NOVA received EOF and is shutting down")
            print("\nShutting down NOVA.")
            break

        except Exeption as error:
            logger.exception(f"Unexpected error: {error}")
            print("An unexpected error occurred. Check logs/nova.log.")

if __name__ == "__main__":
    main()
