---
id: "44013494911383"
titulo: "[Control Tower] - Cadastro de Parada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013494911383--Control-Tower-Cadastro-de-Parada"
trilha: "Lincros > Control Tower"
atualizado_em: "2026-10-05T19:59:30Z"
rotulos: ["sync_hc", "lincros", "sync_hash_cc3647b1653f", "lincros_13432342"]
---

# [Control Tower] - Cadastro de Parada

**Menu**: Cadastros > Paradas

**Objetivo** :Neste artigo, iremos ensiná-lo como cadastrar uma parada. Uma parada é qualquer local no qual o motorista irá parar durante a sua rota (carga e descarga, por exemplo).
 Também pode ser uma parada não prevista durante a rota, nesse caso iremos chamar esse tipo de parada como Parada não programada (PNP).

**Considerações**:

- O sistema possui 3 categorias de paradas. Abaixo, um breve explicativo de cada uma delas:

1. Parada: é todo cliente, CD, fábrica e etc;
2. Pré-definida: é todo ponto de parada em que é possível que qualquer motorista pare, porém não é considerado uma irregularidade. O sistema não gera PNP quando o motorista estiver parado nestes locais (ex.: posto de gasolina, hotéis);
3. Ponto de interesse: é todo ponto de parada que foge às regras anteriores, mas que há um interesse em identificar o local no mapa;

- O tipo irá variar de acordo com a categoria selecionada;
- O Código da Parada e Nome são apenas critérios de identificação, podendo incluir números ou letras;
- Latitude, longitude e polígono(raio) da parada são itens necessários para o bom funcionamento do sistema;

Abaixo segue os procedimentos:

## Configuração – Parâmetro

Dentro do conceito de parada temos alguns parâmetros nos quais podemos incluir, por exemplo:

- Tempo meta para carregamento;
- Tempo meta para descarregamento;
- Tipo de saída (por posição ou integração);
- Medida do raio da parada;

Caso sinta a necessidade de alteração de alguns desses parâmetros, entre em contato com a nossa equipe de Help Desk.

## Cadastro de tipo de saída da parada

1. Acessar o menu: Cadastros > Paradas > Nova Parada (ou selecione uma já existente) > Tipo de saída;
2. Para contabilizarmos o tempo que o caminhão ficou dentro do raio da parada, precisamos configurar um método de saída para a mesma.

Temos 5 configurações possíveis:

1. Manual: este tipo de saída se dá através de uma finalização manual (ação do usuário) da parada em questão;
2. Posição: este tipo de saída se dá através das posições enviadas pelo rastreador do caminhão, ou seja, é de forma automática;
3. Integração: também de forma automática, este tipo de saída se dá através do envio de um arquivo via integração que será usado como um “gatilho” para avançar a parada;
4. Posição ou integração: neste tipo de saída, o avanço da parada pode se dar tanto por posição como por integração. A informação que chegar primeiro irá efetivar a saída da parada;
5. Posição e integração: neste tipo de saída, é necessário que tenhamos tanto a informação de posição como do arquivo de integração para efetivarmos a saída da parada;

## Exemplo

1. Clicando na load e seguindo o caminho abaixo, será possível visualizar a informação de tipo de saída da parada, conforme a configuração realizada;

2. Acessar o Menu: Load > Aba histórico > Aba paradas;

![Imagem 1: 2. Acessar o Menu: Load > Aba histórico > Aba paradas;](https://ajuda.sankhya.com.br/hc/article_attachments/44013503520791)

## Finalizando uma parada manualmente

Na tela inicial de monitoramento, clique sobre a load ou parada na qual você deseja avançar o processo de forma manual;

![Imagem 2: Na tela inicial de monitoramento, clique sobre a load ou parada na qual você deseja avançar o processo de forma manual;](https://ajuda.sankhya.com.br/hc/article_attachments/44013488021527)

Após isso, clique na aba “Opções”, insira a data respectiva à finalização e clique em “Encerrar Parada”;

 "Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
