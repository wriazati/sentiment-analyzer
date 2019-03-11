Server that will respond with emojis to your message.

TO USE:
pip install -e .
export FLASK_APP=src/server.py

flask run

curl http://127.0.0.1:5000/ -d "This app is great"
:)



OR use this to run:
python ./src/server.py