if [ $# -eq 0 ]
  then
    IP="127.0.0.1" 
else
    IP=$1
fi

docker build -t sqli-finale .
docker run -p $IP:7002:7002 sqli-finale

