curl -X POST -H "Content-Type: application/json" --data '
{"name": "mongosinkUrgent_data",
   "config": {
     "connector.class":"com.mongodb.kafka.connect.MongoSinkConnector",
     "tasks.max":"1",
     "topics":"urgent_data",
     "connection.uri":"mongodb://root:root@mongo:27017",
     "database":"Patient",
     "collection":"sensorlogs",
     "key.converter":"org.apache.kafka.connect.storage.StringConverter",
     "key.converter.schemas.enable":false,
     "value.converter":"org.apache.kafka.connect.storage.StringConverter",
     "value.converter.schemas.enable":false
}}' http://localhost:8083/connectors -w "\n" 
curl -X POST -H "Content-Type: application/json" --data '
{"name": "mongosinkNormal_data",
   "config": {
     "connector.class":"com.mongodb.kafka.connect.MongoSinkConnector",
     "tasks.max":"1",
     "topics":"normal_data",
     "connection.uri":"mongodb://root:root@mongo:27017",
     "database":"Patient",
     "collection":"sensorlogs",
     "key.converter":"org.apache.kafka.connect.storage.StringConverter",
     "key.converter.schemas.enable":false,
     "value.converter":"org.apache.kafka.connect.storage.StringConverter",
     "value.converter.schemas.enable":false
}}' http://localhost:8083/connectors -w "\n" 
echo "\nmongod connector configured"
echo "\nKafka Connectors:"
curl -X GET "http://localhost:8083/connectors/" -w "\n"
echo "'"
