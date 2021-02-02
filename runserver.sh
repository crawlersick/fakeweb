source ~/miniconda3/bin/activate base
cd /home/sick/fakeweb
nohup python app.py  > /tmp/tornado.log 2>&1 &
