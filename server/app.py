from server import create_app
import os

app = create_app()

if __name__ == '__main__':
    port = os.getenv('PORT', '5000')
    app.run()
