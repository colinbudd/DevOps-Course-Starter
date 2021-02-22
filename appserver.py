from app import create_app
from dotenv import find_dotenv, load_dotenv

# if __name__ == '__main__':
#     create_app = create_app()
#     create_app.run()
# else:
#file_path = find_dotenv('.env')
#load_dotenv(file_path, override=True)
gunicorn_app = create_app()
