if [ $# -eq 0 ]
  then
    IP="127.0.0.1" 
else
    IP=$1
fi

docker build -t ssti-finale .
docker run -p $IP:7003:7003 ssti-finale