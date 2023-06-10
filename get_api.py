import requests
import json

request = requests.get("https://liturgia.up.railway.app/")
liturgia = json.loads(request.content)

evangelho = f"{liturgia['data']}\n\n- Anúncio do Evangelho ({liturgia['evangelho']['referencia']})\n\n{liturgia['evangelho']['titulo']}\n\n- Glória a vós, senhor.\n\n{liturgia['evangelho']['texto']}\n\n- Palavra da Salvação.\n\n- Glória a vós, senhor."

data = liturgia['data'].replace('/', '')
meuArquivo = open(f"evangelho.txt", 'w')
meuArquivo.write(evangelho)
meuArquivo.close()