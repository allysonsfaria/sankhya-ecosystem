---
id: "37638971367447"
titulo: "Como realizar a liberação de valor divergente entre pedido e nota"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37638971367447-Como-realizar-a-libera%C3%A7%C3%A3o-de-valor-divergente-entre-pedido-e-nota"
trilha: "Universidade Sankhya > Jornada de Compras"
atualizado_em: "2026-07-22T14:12:13Z"
rotulos: ["Pedidos", "Configuração", "Liberação de Limites", "XML", "Financeiro", "Notas Fiscais"]
---

# Como realizar a liberação de valor divergente entre pedido e nota

| Categoria |
| --- |
| [O que é a liberação de diferença de valores entre pedido nota?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37638971367447-Como-realizar-a-libera%C3%A7%C3%A3o-de-valor-divergente-entre-pedido-e-nota#h_01KEVRQWWGG5Y1TT7SDR86NQBB) |
| [Quais os problemas este recurso resolve?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37638971367447-Como-realizar-a-libera%C3%A7%C3%A3o-de-valor-divergente-entre-pedido-e-nota#h_01KEVRSA72YYZVHK25DYQB1JZF) |
| [Quais os riscos de não utilizar a liberação da diferença de valores entre pedido nota?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37638971367447-Como-realizar-a-libera%C3%A7%C3%A3o-de-valor-divergente-entre-pedido-e-nota#h_01KEVRSNXV8ZZ5FTE99YKHS407) |
| [Vídeo com demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37638971367447-Como-realizar-a-libera%C3%A7%C3%A3o-de-valor-divergente-entre-pedido-e-nota#h_01KFBKVE9SDMQ0TQK3Q9B8VWY0) |
| [Cenário prático e passo a passo para realizar a atividade no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37638971367447-Como-realizar-a-libera%C3%A7%C3%A3o-de-valor-divergente-entre-pedido-e-nota#h_01KFBKVTDV3QDCCEFSSZGDD092) |
| [É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/37638971367447-Como-realizar-a-libera%C3%A7%C3%A3o-de-valor-divergente-entre-pedido-e-nota#h_01KEVRTFJWDNWBGMF706F0070Q) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37638971367447-Como-realizar-a-libera%C3%A7%C3%A3o-de-valor-divergente-entre-pedido-e-nota#h_01KEVRW8N0024P86YPY7EN1542) |

## Liberação de diferença de valores entre pedido nota

#### O que é a liberação de diferença de valores entre pedido nota?

A liberação de diferença de valores entre pedido e nota consiste na validação das discrepâncias financeiras entre os valores registrados no Pedido de Compra e os dados contidos no XML da Nota Fiscal enviada pelo fornecedor. Essa validação é realizada automaticamente no momento da importação do XML, e, caso seja identificada alguma diferença, o sistema possibilita a aprovação ou ajuste por meio de um processo de liberação formal.

#### Quais os problemas este recurso resolve?

- **Dificuldade em detectar divergências financeiras:** Quando os valores entre o pedido e a nota fiscal não coincidem, há risco de pagamentos indevidos ou conflitos com o fornecedor.
- **Exposição a penalidades fiscais:** Inconsistências não tratadas podem gerar autuações, multas e desconformidades com obrigações legais.
- **Retrabalho e lentidão nos processos de validação:** A ausência de automação nesses casos aumenta o tempo de análise manual, comprometendo a produtividade.
- **Falta de transparência nas auditorias e relações comerciais:** informações divergentes entre sistemas dificultam a rastreabilidade e diminuem a confiança nas transações realizadas.

#### Quais os riscos de não utilizar a liberação da diferença de valores entre pedido nota?

Sem o recurso de liberação de diferenças entre pedido e nota fiscal, a empresa arrisca sofrer impactos em sua saúde financeira, incluindo pagamentos indevidos ou valores acima do negociado com fornecedores. Essa ausência de controle pode levar a erros acumulados, resultando em perdas financeiras significativas e dificultando a identificação de desvios sistêmicos. Além disso, a falta de controle sobre essas diferenças pode prejudicar a conformidade fiscal, expondo a empresa a multas e auditorias fiscais desfavoráveis. 

##### Vídeo com demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1052444974)

#### Cenário prático e passo a passo para realizar a atividade no ERP Sankhya

**Contexto:** Durante a importação de um XML de nota fiscal de compra, a compradora da **Axis** identificou que o valor total informado no XML era maior do que o registrado no sistema. A diferença aconteceu por um ajuste no valor unitário feito pelo fornecedor, que não havia sido atualizado no pedido original.

Pelas diretrizes da empresa, sempre que houver divergência de valor, o comprador deve solicitar autorização do gestor responsável antes de seguir. Só após a aprovação, o comprador poderá corrigir os dados no sistema e concluir a importação da nota.

**Tarefa:** Realize a liberação para variação do valor unitário acima do permitido (**Evento 68**) seguindo as orientações indicadas abaixo.

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

1. **Acesse a tela Portal de Importação de XML**

Menu: Comercial »  Rotinas »  Portal de Importação de XML

- Clique no botão **"+"** (**Cadastrar Importação de XML de Notas**) para carregar o arquivo XML.
- Selecione o arquivo no botão “**Escolher arquivo**”
- Clique no botão "**Enviar**”.
- Clique em **Processar** para que o sistema valida o XML.

2. **Definir o Liberador**

- Dentro do **Portal de Importação de XML.**
- Clique no botão **Liberações**.
- Selecione o **Usuário Gestor** como liberador.
- Clique em **Confirmar**.

3. **Liberação de Limites**

- Acesse a tela **Liberação de Limite**
  Menu: Configurações »  Avançado »  Liberação de Limite
- Insira os dados do **Liberador** (usuário e senha).
- Clique em **Aplicar**.

O sistema exibirá todas as solicitações pendentes para o liberador.

Localize o **Pedido de Compra** correspondente.

- Selecione e clique em **Liberar**.

4. **Validação da Importação**

- Retorne ao **Portal de Importação de XML**.
- Clique no botão “**Validar Importação**”.
- O sistema exibirá a mensagem **"Importado com sucesso"**.
- Clique em **Ok**.

5. **Confirmação na Central de Compras**

- Clique no botão “**Abrir Documento**”

Direciona para a **Central de Compras**.

- Revise os dados, garantindo que o valor do produto foi ajustado conforme a liberação.
- Antes de confirmar, verifique no cabeçalho o campo **Dt. Entrada/Saída e Dt.Faturamento** estão preenchidos com a data do dia. Caso não estejam, atualize as informações e salve as alterações.
- Clique em **Confirmar**, para finalizar.

#### Correção e Repetição

- Verifique se colocou todas as informações do XML e do Pedido de Compra.
- Valide as informações de todas as abas dentro do Portal de Importação XML.
- Não esqueça de corrigir uma divergência clicar em Validar Importação.
- Caso não tenha sido concluído conforme esperado, refaça o processo corrigindo as informações necessárias.
- Certifique-se de que configurou o Modelo de importação de XML.
- Atente-se para as configurações necessárias das Preferências da Empresa.
- Certifique-se de que o **Usuário Gestor** está devidamente cadastrado como **liberador**.
- Para praticar, experimente criar novamente um novo, com outros produtos e fornecedores.
