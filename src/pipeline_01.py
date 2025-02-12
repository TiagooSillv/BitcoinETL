import requests;

url ="https://api.coinbase.com/v2/prices/spot";

def extractDadosBTC(url):
    response = requests.get(url);

    dados = response.json();
    return dados;

def transformDadosBTC(dados):
    valor = dados["data"]["amount"];
    criptoMoeda = dados["data"]["base"]
    moeda = dados["data"]["currency"]

    dadosTransformado = {
        "valor" : valor,
        "criptoMoeda" : criptoMoeda,
        "moeda" : moeda
    }

    return dadosTransformado;





print(extractDadosBTC(url));

