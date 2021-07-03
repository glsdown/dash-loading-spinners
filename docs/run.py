from docs_app import app

application = app.server

if __name__ == "__main__":
    app.run_server(debug=True)
