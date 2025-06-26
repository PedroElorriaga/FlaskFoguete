from src.main.server.server_settings import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(host='localhost', port=3000, debug=True)
