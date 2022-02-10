from website import create_app

app = create_app()

# Run web server only if code is being run directly
# !! Set debug=True for developer mode, debug=False for production !!
if __name__ == '__main__':
    app.run(debug=True)