from src.main.server.server_settings import create_app

if __name__ == '__main__':
    app = create_app()
    app.run('localhost', port=3000, debug=True)
