---
id: "44011000132375"
titulo: "[Tracking] Alerta de atraso na entrega"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011000132375--Tracking-Alerta-de-atraso-na-entrega"
trilha: "Lincros > Tracking"
atualizado_em: "2026-10-05T18:51:56Z"
rotulos: ["sync_hc", "lincros", "lincros_13438050", "sync_hash_6f4a0bd27564"]
---

# [Tracking] Alerta de atraso na entrega

**Menu:** Mapa sinótico

**Objetivo:** Identificar, em tempo real, entregas com possibilidade de atraso ou já atrasadas por meio de ícones visuais no mapa sinótico, permitindo ações preventivas e melhor gerenciamento pela equipe de monitoramento.

## Considerações:

- Funcionalidade disponível a partir da versão **Tracking 4.31.9**;
- A unidade de negócio precisa ter o parâmetro **"Habilitar cálculo de ETA"** habilitado;
- O serviço de processamento de cálculo do ETA deve estar ativo;
- As entregas devem conter a informação de **Data prevista da entrega**.

## Como funciona

O recurso aprimora o Tracking adicionando uma representação visual no mapa sinótico que indica, de forma clara e direta, quais entregas têm possibilidade de atraso e quais já estão atrasadas. Assim que as rotas são iniciadas, o Tracking realiza automaticamente o primeiro cálculo do ETA (Tempo Estimado de Chegada) para todas as entregas pendentes.

Foram adicionados três ícones no mapa sinótico, cada um sinalizando um status diferente:

**Possibilidade de atraso — relógio amarelo:** exibido nas entregas não realizadas em que o tempo estimado de chegada (ETA) seja posterior à data prevista. Indica que a entrega pode estar sujeita a atraso.

![Imagem 1: Possibilidade de atraso — relógio amarelo: exibido nas entregas não realizadas em que o tempo estimado de chegada (ETA)…](https://ajuda.sankhya.com.br/hc/article_attachments/44011000321047)

**Atrasado — entrega não realizada — ícone vermelho:** exibido nas entregas não realizadas (bolinha cinza) em que o horário atual seja maior que a data prevista. A entrega já está atrasada e ainda não foi concluída.

![Imagem 2: Atrasado — entrega não realizada — ícone vermelho: exibido nas entregas não realizadas (bolinha cinza) em que o horário…](https://ajuda.sankhya.com.br/hc/article_attachments/44010984842519)

**Atrasado — entrega realizada — ícone vermelho:** exibido nas entregas já realizadas (bolinha verde) em que a data realizada de entrega seja superior à data prevista. A entrega foi concluída, mas com atraso em relação ao planejado.

![Imagem 3: Atrasado — entrega realizada — ícone vermelho: exibido nas entregas já realizadas (bolinha verde) em que a data…](https://ajuda.sankhya.com.br/hc/article_attachments/44011000593943)

**Importante:** o cálculo do ETA é realizado somente para entregas com os seguintes status: **Não realizado**, **Baldeada** e **Devolução Revertida** (bolinha roxa).

## Como o ETA é calculado

Quando a entrega ou devolução registrada está alinhada com a sequência prevista, o ETA calcula as demais entregas na ordem subsequente:

- Da posição atual do motorista até a próxima entrega;
- Da posição da próxima entrega até a subsequente na sequência.

  ![Imagem 4: Da posição da próxima entrega até a subsequente na sequência.](https://ajuda.sankhya.com.br/hc/article_attachments/44010991840151)

Caso o registro de entrega ou devolução seja realizado **fora da ordem sequencial esperada**, o ETA calcula a rota a partir da posição atual do motorista até as posições de todas as entregas pendentes.

Nos detalhes da entrega, na linha **Data Prevista de Entrega (Calculada)**, um ícone de dica estará disponível informando como o cálculo foi realizado:

![Imagem 5: Nos detalhes da entrega, na linha Data Prevista de Entrega (Calculada) , um ícone de dica estará disponível informando…](https://ajuda.sankhya.com.br/hc/article_attachments/44010991974295)

![Imagem 6: Nos detalhes da entrega, na linha Data Prevista de Entrega (Calculada) , um ícone de dica estará disponível informando…](https://ajuda.sankhya.com.br/hc/article_attachments/44010956567831)

A cada novo apontamento de entrega ou devolução recebido pelo Tracking, o ETA reinicia o cálculo automaticamente para todas as entregas nos status **Pendente**, **Revertido** e **Baldeada**.

## Apresentação da diferença de tempo no ETA

A diferença entre o ETA e a data prevista é exibida junto ao ícone, seguindo as regras abaixo:

- **Atraso em minutos** — para diferenças entre 00:01 e 00:59, o valor é exibido seguido da letra **"m"**;
- **Atraso em horas** — para diferenças entre 01:00 e 23:59, o valor é exibido seguido da letra **"h"**;
- **Atraso em dias** — para diferenças iguais ou maiores que um dia, o valor é exibido seguido da letra **"d"**.

  ![Imagem 7: Atraso em dias — para diferenças iguais ou maiores que um dia, o valor é exibido seguido da letra "d" .](https://ajuda.sankhya.com.br/hc/article_attachments/44010956673431)

## Configurações necessárias

**Importante:** para ativar essa funcionalidade, entre em contato com o suporte da Lincros pelo Intercom e solicite a ativação do serviço de integração. Embora o parâmetro na unidade de negócio possa ser habilitado pelo próprio cliente, é importante que a Lincros habilite o serviço de integração para garantir o funcionamento correto.

1. Habilitar o parâmetro de cálculo ETA em: **Cadastro > Unidade de negócio > Configurações gerais > Habilitar cálculo ETA**. Essa configuração habilita o processamento do tempo estimado de chegada nas entregas. Os ícones de alerta só serão exibidos quando esse parâmetro estiver ativo.

   ![Imagem 8: Habilitar o parâmetro de cálculo ETA em: Cadastro > Unidade de negócio > Configurações gerais > Habilitar cálculo ETA .…](https://ajuda.sankhya.com.br/hc/article_attachments/44011001309975)
2. Habilitar o **Serviço de processamento de Cálculo de ETA** no menu **Integrações**.

   ![Imagem 9: Habilitar o Serviço de processamento de Cálculo de ETA no menu Integrações .](https://ajuda.sankhya.com.br/hc/article_attachments/44010992416151)

Com a integração e os parâmetros ativos, o alerta está pronto para uso. Assim que as rotas são iniciadas, o Tracking realiza automaticamente o primeiro cálculo do ETA para todas as entregas pendentes.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos."
