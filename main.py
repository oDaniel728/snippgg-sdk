import dotenv
import os

from snippsdk.snipp import Snipp

dotenv.load_dotenv()

def main():
    snipp = Snipp(os.getenv("API_KEY") or '')
    print("perfil daniel:")
    print(snipp.get_user("@me").json)

if __name__ == "__main__":
    main()
