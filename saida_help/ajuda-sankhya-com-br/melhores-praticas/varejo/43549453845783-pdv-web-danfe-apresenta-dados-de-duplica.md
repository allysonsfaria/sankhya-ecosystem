---
id: "43549453845783"
titulo: "PDV Web: DANFE apresenta dados de duplicata divergentes do recebimento realizado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43549453845783-PDV-Web-DANFE-apresenta-dados-de-duplicata-divergentes-do-recebimento-realizado"
trilha: "Melhores Práticas > Varejo"
atualizado_em: "2026-10-15T19:17:25Z"
rotulos: ["Artigo criado KCS", "Varejo - KCS"]
---

# PDV Web: DANFE apresenta dados de duplicata divergentes do recebimento realizado

**SITUAÇÃO**

Ao finalizar uma venda pelo **PDV Web** e imprimir a Nota Fiscal (NF), o campo **Tipo de Negociação** pode apresentar um valor diferente daquele selecionado pelo operador durante a venda.

Nesses casos, a nota pode manter o tipo de negociação original do documento ou assumir um valor padrão definido pelo sistema, em vez de considerar a opção selecionada no momento da operação.

Esse comportamento pode gerar inconsistências fiscais e operacionais, especialmente quando a condição de pagamento é relevante para o cliente ou para o controle financeiro da empresa.

**CAUSA**

O sistema considera, para fins de impressão da Nota Fiscal, o **tipo de título vinculado ao tipo de negociação informado no cabeçalho da nota**.

Dessa forma, mesmo que o operador selecione um tipo de negociação ou tipo de título diferente durante a venda pelo PDV Web, a impressão poderá apresentar uma informação divergente caso o tipo de título vinculado ao tipo de negociação registrado no cabeçalho não corresponda à opção selecionada.

Esse comportamento está relacionado à forma como o sistema utiliza as informações do cabeçalho da nota para determinar o tipo de título apresentado na impressão do documento.

#### **(1)**Revisar a configuração do layout do PDV Web

Certifique-se de que o layout do **"PDV Web"** esteja configurado para permitir a seleção e atualização do tipo de negociação no cabeçalho da nota. Para isso:

Acesse a tela **"Configurador de Layout da Nota"** (Comercial » Configuração » Configurador de Layout da Nota).

Localize o layout vinculado à TOP utilizada no PDV Web e clique no **Botão** **Layout PDV**.
 Na aba **Preferências PDV Web**, verifique o campo **Tipo de Recebimento** e confirme se está configurado conforme o fluxo operacional desejado:

- Tipo de Título;
- Tipo de Negociação;
- Ambos.

**(4)** Na aba **Detalhes da Identificação**, verifique se o campo **Tipo de Negociação** está configurado como editável e/ou obrigatório, conforme a necessidade da operação.

#### **(1)** Validação dos tipos de negociação e títulos

Verifique se os tipos de negociação e de título utilizados na operação estão devidamente cadastrados e habilitados para uso no PDV Web.

**(5)** Acesse a tela **"Tipos de Negociação"** (Comercial » Arquivo » Cadastros » Tipos de Negociação) e confira se o tipo desejado está ativo e disponível para seleção.
**(6)** Na tela **"Tipos de Título"** (Financeiro » Arquivos » Cadastros » Tipos de Título » Tipos de Título), valide se o título está com a opção **"Utiliza no Fast Service?"** marcada na aba **"Fast Service"**.

Essas validações ajudam a garantir que o PDV Web reconheça as opções de negociação e de título configuradas para o processo de venda e recebimento.

#### **(1)** Fluxo correto de atualização do cabeçalho

Oriente o operador a utilizar o botão **[F2] Identificar** para abrir o pop-up de identificação e selecionar o tipo de negociação desejado antes de incluir os itens da venda.

Após selecionar o tipo de negociação, confirme a operação e prossiga normalmente com o lançamento dos itens e o recebimento.

Caso o campo **Tipo de Negociação** não seja atualizado ou gravado corretamente, o sistema poderá manter o valor original do documento, ocasionando divergência entre o tipo selecionado durante a venda e o informado na impressão da Nota Fiscal.
