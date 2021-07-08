from app import create_app


def run_server(app):
    app.run(port=3000, debug=True)


if __name__ == "__main__":
    app = create_app()

    # start web server
    run_server(app)
