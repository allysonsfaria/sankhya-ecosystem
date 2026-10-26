---
id: "44012538356887"
titulo: "[Routing] - Alerta de baixa ocupação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012538356887--Routing-Alerta-de-baixa-ocupa%C3%A7%C3%A3o"
trilha: "Lincros > Roteirizador > Relatórios - Roteirizador"
atualizado_em: "2026-10-05T19:31:39Z"
rotulos: ["sync_hc", "lincros", "lincros_13433476", "sync_hash_f841796458df"]
---

# [Routing] - Alerta de baixa ocupação

**Menu**:
1. **Parametrizar**: Roteirizador> Cadastros> Estratégia de roteirização;
2. **Alerta na sessão**: Roteirizador> Iniciar uma nova sessão;
3. **Relatório**: Roteirizador> Relatórios> Ocupação de veículos.

**Objetivo**: Explicar como configurar alertas de baixa ocupação e como analisar esses alertas durante a sessão e no relatório.

**Considerações**: A configuração dos alertas é opcional.
                          Os alertas servem apenas como suporte para a tomada de decisão e não impedem a roteirização.

**Orientações para utilização dos Alertas:**
1. Parametrização:
Para parametrizar os alertas, o caminho é:
   →Roteirizador →Cadastros → Estratégia de Roteirização → Alertas;

Atualmente, é possível configurar alertas para baixa ocupação de:
  Peso;
 Cubagem;
 Pallets;
 Valor.

Os valores são inseridos em percentuais e aceitam apenas números inteiros.

![Imagem 1: Considerações : A configuração dos alertas é opcional. Os alertas servem apenas como suporte para a tomada de decisão e…](https://ajuda.sankhya.com.br/hc/article_attachments/44012552955927)

Após a configuração, o Roteirizador exibirá os alertas durante a roteirização.

**Exemplo**:
Suponha que você configurou os seguintes percentuais para alerta de baixa ocupação:
Peso: 80%
Cubagem: 80%
Pallets: 80%
Valor: 80%

Para essa roteirização, foi utilizado um veículo com as seguintes capacidades:
Peso: 15.000kg
Capacidade (m³): 30
Quantidade de pallets: 30
Valor R$: 29.999,00

Os pedidos na rota possuem os seguintes dados:
Peso: 10.000kg
Cubagem: 10m³
Pallets: 10
Valor total R$: 10.000,00

**Exibição dos Alertas:**
1. **Na lateral esquerda:** Abaixo do título "Rotas", o percentual de ocupação será destacado.

![Imagem 2: Após a configuração, o Roteirizador exibirá os alertas durante a roteirização. Exemplo : Suponha que você configurou os…](https://ajuda.sankhya.com.br/hc/article_attachments/44012544262679)

2. **No mapa:** O percurso da rota ficará em vermelho, indicando baixa ocupação.

![Imagem 3: 2. No mapa: O percurso da rota ficará em vermelho, indicando baixa ocupação.](https://ajuda.sankhya.com.br/hc/article_attachments/44012524495255)

3. **Na atividade no mapa:** O alerta também será registrado.

![Imagem 4: 3. Na atividade no mapa: O alerta também será registrado.](https://ajuda.sankhya.com.br/hc/article_attachments/44012539084567)

4. **Informações da rota selecionada:** O alerta será exibido junto aos detalhes da rota.

![Imagem 5: 4. Informações da rota selecionada: O alerta será exibido junto aos detalhes da rota.](https://ajuda.sankhya.com.br/hc/article_attachments/44012531029399)

**Relatório de Ocupação de Veículos:**
Além dos alertas, é possível extrair um relatório da ocupação dos veículos. Esse relatório não depende da parametrização de alerta de baixa ocupação.
O mesmo pode ser acessado de duas formas:
  1. Diretamente na sessão, clicando no ícone de visualizar relatório de ocupação de veículos (

![Imagem 6: Relatório de Ocupação de Veículos: Além dos alertas, é possível extrair um relatório da ocupação dos veículos. Esse…](https://ajuda.sankhya.com.br/hc/article_attachments/44012525107991)

).
  2. Roteirizador > Relatórios > Ocupação de Veículos.

Também é possível acessar o relatório na opção:
Roteirizador> Relatórios> Ocupação de Veículos.

O relatório inclui:

Data do roteiro
Nº de embarque (esse campo é preenchido após a exportação da sessão ao TMS, quando é gerado o embarque)
Sessão
Nº da rota
Placa do veículo
Tipo de veículo
Ocupação em Kg (%)
Ocupação em m³ (%)
Ocupação em Pallets (%)
Valor da carga
Total de agrupamentos
Total de destinos

O relatório pode ser exportado em formato **CSV**.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
