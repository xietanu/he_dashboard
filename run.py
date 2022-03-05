"""
The entry point for the application to be run from the command line.
"""

from index import app

if __name__ == "__main__":
    HOST = "0.0.0.0"
    PORT = 8080
    app.run_server(host=HOST, port=PORT, debug=True)
