---
id: "44011176605335"
titulo: "[Control Tower] - Portal de Fretes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011176605335--Control-Tower-Portal-de-Fretes"
trilha: "Lincros > Control Tower"
atualizado_em: "2026-10-05T18:56:02Z"
rotulos: ["sync_hc", "lincros", "lincros_13439367", "sync_hash_d5db2427e1f8"]
---

# [Control Tower] - Portal de Fretes

**Menu**: Portal de Fretes

**Objetivo**: O Portal de Fretes foi implementado para que viagens pudessem ser importadas sem a necessidade de informar a placa do cavalo relacionado à carga.

**Considerações**:

- O portal de fretes possibilita a integração de viagens antes da definição do veículo que fará o transporte da carga, possibilitando um acompanhamento em tempo real do aceite das cargas ofertadas;
- A oferta é realizada através da importação da planilha Excel “Rotas e Faturamento”, o layout fica disponível de exemplo para o usuário baixar;

Abaixo segue os procedimentos:

1. Acesse o Portal de Fretes, para visualizar as ofertas atribuídas para sua Transportadora;

![Imagem 1: Acesse o Portal de Fretes, para visualizar as ofertas atribuídas para sua Transportadora;](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1965075804/7c46eaee38064ff8393bc0c99c5d/3022F3C83DE4C8501B714A009D0A2860?expires=1791331200&signature=b4e47d2567fd20a984c2728e0f2b816faed04aa7fa28adce1b13faf3f20d7bd3&req=dSkhE8l5mIlfXfMW3nq%2BgeEyaJdFy3MrNTFaYjX8z2saiTzJ0er3NjKTeKpA%0AA2n%2B8UNtrR2ALDX6UUj28JNzXGY%3D%0A)

2. No painel são exibidas as informações relacionadas às ofertas que foram importadas;

3. São exibidos Numero da Oferta, Placa do Cavalo, Data Agendada do Carregamento, Transportadora, Paradas que deverão ocorrer na viagem e Ação, que possibilita o cancelamento de Ofertas;

4. Essa última função apenas fica disponível para usuários da equipe de monitoramento ou administradores.Configuração – Parâmetro.

Dentro do conceito de parada temos alguns parâmetros nos quais podemos incluir, por exemplo:

- Tempo meta para carregamento;
- Tempo meta para descarregamento;
- Tipo de saída (por posição ou integração);
- Medida do raio da parada;

**Cadastro de tipo de saída da parada:**Menu Cadastros > Paradas > Nova Parada (ou selecione uma já existente) > Tipo de saída

Para contabilizarmos o tempo que o caminhão ficou dentro do raio da parada, precisamos configurar um método de saída para a mesma.

Temos 5 configurações possíveis:

1. Manual: este tipo de saída se dá através de uma finalização manual (ação do usuário) da parada em questão.
2. Posição: este tipo de saída se dá através das posições enviadas pelo rastreador do caminhão, ou seja, é de forma automática.
3. Integração: também de forma automática, este tipo de saída se dá através do envio de um arquivo via integração que será usado como um “gatilho” para avançar a parada.
4. Posição ou integração: neste tipo de saída, o avanço da parada pode se dar tanto por posição como por integração. A informação que chegar primeiro irá efetivar a saída da parada.
5. Posição e integração: neste tipo de saída, é necessário que tenhamos tanto a informação de posição como do arquivo de integração para efetivarmos a saída da parada.

## Exemplo

Clicando na load e seguindo o caminho abaixo, será possível visualizar a informação de tipo de saída da parada, conforme a configuração realizada;

Caminho:  Load > Histórico > Paradas;

## Finalizando uma parada manualmente

1. Na tela inicial de monitoramento, clique sobre a load ou parada na qual você deseja avançar o processo de forma manual;
2. Após isso, clique na aba “Opções”, insira a data respectiva à finalização e clique em “Encerrar Parada”;

**Obs**.: Caso sinta a necessidade de alteração de alguns desses parâmetros, entre em contato com a nossa equipe de Help Desk.

 "Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
