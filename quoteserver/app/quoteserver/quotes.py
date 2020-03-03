from elasticsearch import Elasticsearch
from flask import Flask, request, render_template

app = Flask(__name__)

client = Elasticsearch([{'host':'host.docker.internal','port':9200}])

index = 'quotes'

@app.route('/byId', methods=['GET'])
def getById():
    docId = request.args.get('id')
    quote = client.get(index=index, id=docId)
    return render_template('quote.html',quote=quote)
