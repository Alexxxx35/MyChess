from Chess import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8005, debug=True)
