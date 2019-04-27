pass=`head -1 $HOME/.config/fakeweb`
echo $pass |zip -q -e --stdin |echo "$1" | base64 -d
