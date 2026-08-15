import dotenv
import os

from snippsdk.snipp import SnippClient

dotenv.load_dotenv()

def main():
    snipp = SnippClient(os.getenv("API_KEY") or '')
    print("perfil daniel:")
    print(snipp.get_user("@me").json)

if __name__ == "__main__":
    main()
