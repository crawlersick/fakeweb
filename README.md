# fakeweb

fakeweb,using tornato web severice for web re-direct

run you app in localhost:8000 by 
python app.py

ENVIROMENT:
set up your password in ~/.config/fakeweb
install zip , python-tornado , pycurl

1. encode your request url
callenc.sh 'http://baidu.com'
aHR0cDovL2JhaWR1LmNvbQ==

2. send it
curl -X POST -d '{"keyl":"aHR0cDovL2JhaWR1LmNvbQ=="}' http://127.0.0.1:8000
PGh0bWw+CjxtZXRhIGh0dHAtZXF1aXY9InJlZnJlc2giIGNvbnRlbnQ9IjA7dXJsPWh0dHA6Ly93d3cuYmFpZHUuY29tLyI+CjwvaHRtbD4K

3. decode the response
echo -n 'PGh0bWw+CjxtZXRhIGh0dHAtZXF1aXY9InJlZnJlc2giIGNvbnRlbnQ9IjA7dXJsPWh0dHA6Ly93d3cuYmFpZHUuY29tLyI+CjwvaHRtbD4K' |base64 -d
<html>
<meta http-equiv="refresh" content="0;url=http://www.baidu.com/">
</html>

for proxy function:
curl -X POST -d '{"keyl":"http://baidu.com"}' http://127.0.0.1:5555/proxy
