docker rm -f fakeweb; docker run --restart=always  -d -v $PWD:/usr/src/app -p 8000:8000 --name fakeweb dk_tornado bash -c ' python app.py'
