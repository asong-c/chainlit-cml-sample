print ("install chainlit from pip")
!pip install chainlit

print ("launch chainlit binary")
!chainlit run chainlit-sample.py -w --host 127.0.0.1 --port $CDSW_APP_PORT