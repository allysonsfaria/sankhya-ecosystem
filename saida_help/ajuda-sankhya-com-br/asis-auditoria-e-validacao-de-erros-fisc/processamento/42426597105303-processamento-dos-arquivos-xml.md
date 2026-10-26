---
id: "42426597105303"
titulo: "Processamento dos arquivos XML"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42426597105303-Processamento-dos-arquivos-XML"
trilha: "ASIS: Auditoria e validação de erros fiscais > Base de conhecimento > Processamento"
atualizado_em: "2026-08-03T12:24:21Z"
rotulos: ["asis", "sync_hc", "asis_52941214170259", "sync_hash_40a0902cbba1"]
---

# Processamento dos arquivos XML

Após importar os arquivos XMLs na plataforma, seja por Upload, robô de Importação Automática ou API, cada um deles entra em fila de processamento e o tempo para cada XML processar é de até 14 segundos, dependendo das auditorias acionas por documento fiscal.

Isso quer dizer que para estimar o tempo de processamento, deve-se multiplicar a quantidade de XML pelos segundos.

Exemplo :

Quantidade de XML: 1.200

1.200 X 14= 16800 segundos

Ou seja 4,6666667 horas.

Vale ressaltar que se em um segundo momento suba mais 2.000 arquivos, esse novo upload de 2.000 irá entrar na fila e deve aguardar o processamento dos 1.200,  para posteriormente iniciar o upload dos 2.000 arquivos.

Antes de realizar qualquer cruzamento ou processo na plataforma que utilize os dados dos XMLs, os arquivos devem obrigatoriamente estarem processados.
