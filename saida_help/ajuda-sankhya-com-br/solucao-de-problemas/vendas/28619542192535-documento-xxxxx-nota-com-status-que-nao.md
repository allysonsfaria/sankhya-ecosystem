---
id: "28619542192535"
titulo: "Documento XXXXX. Nota com status que não permite a impressão. Favor verificar o documento. NFe ignorada na impressão"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/28619542192535-Documento-XXXXX-Nota-com-status-que-n%C3%A3o-permite-a-impress%C3%A3o-Favor-verificar-o-documento-NFe-ignorada-na-impress%C3%A3o"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T14:37:45Z"
rotulos: ["Configuração", "Impressão", "NF-e", "XML", "SEFAZ", "TOP", "Passos para resolver", "Razão do erro", "Detalhe do erro", "status NFe", "Nota com status que não permite a impressão", "NFe ignorada na impressão", "Artigo atualizado KCS", "Docs Eletrônicos - KCS"]
---

# Documento XXXXX. Nota com status que não permite a impressão. Favor verificar o documento. NFe ignorada na impressão

**MENSAGEM**

A nota fiscal eletrônica encontra-se com status **"Enviada"**, mas não é possível realizar sua impressão. O sistema apresenta erro ao selecionar as impressoras, ignora a nota durante a tentativa de impressão ou exibe a mensagem: **"Documento XXXX: Nota com status que não permite a impressão"**.

**SITUAÇÃO**

Ao tentar realizar a impressão, o sistema apresenta erro ao selecionar as impressoras ou informa que o documento não pode ser impresso devido ao status atual. O problema ocorre por inconsistências na aprovação SEFAZ, falta de modelo de impressão vinculado ao TOP, XML incompleto na tabela TGFNFE ou falta de configuração no Web Connection.

**SOLUÇÃO**

**(1)** Verifique o **"Status da nota fiscal"** na tela "Portal de vendas" (Comercial >> Consulta >> Portal de vendas), "Portal de compras"(Comercial >> Consulta >> Portal de compras) ou "Portal de mov. interna"(Comercial >> Consulta >> Portal de mov.interna). Certifique-se de que a nota está com status **"Aprovada"** pela SEFAZ.

OBS: Se estiver com o status diferente de aprovada, necessário validar o motivo da não aprovação. EX:  rejeições, erro de configuração(impostos e etc..).

**(2)** Verificação do modelo(Caso a nota esteja aprovada):

Acesse a tela **"Tipos de Operação"** (Configurações >> Cadastros >> Tipos de Operação) e localize o **"TOP"** utilizado na nota.

 -Na aba **"Impressão"**, verifique o campo **"Modelo de Impressão"**. Certifique-se de que há um modelo válido vinculado.

 -Caso não haja modelo cadastrado, acesse a tela **"Modelo de Impressão (Nota/Pedido)"** (Comercial >> Preferências >> Modelo de Impressão (Nota/Pedido)), baixe o modelo padrão disponível e configure conforme a necessidade da empresa.

**(4)** Caso a nota seja antiga e o erro persista, realize a **"Impressão diretamente pelo portal da SEFAZ"**, pois o XML pode estar inconsistente devido a atualizações de layout.

**(5)** Verifique se o serviço **"Web Connection"** está configurado corretamente. Caso necessário, reconfigure o serviço para restabelecer a comunicação entre o sistema e as impressoras.

**(6)** Após as configurações, tente realizar a impressão novamente.

**Observações importantes:**

- Não utilize o modelo de DANFE para notas de terceiros.
- Não realize aprovações via banco de dados; utilize sempre a rotina de **"Buscar autorização"**.
- Se não tiver conhecimento técnico, solicite auxílio a um consultor.

**CAUSA**

- Ausência de modelo de impressão ou configuração incorreta do Web Connection.
- Nota sem aprovação SEFAZ ou com status de aprovação não sincronizado.
- Inconsistência na tabela TGFNFE causada por alterações manuais via banco de dados.
- XML inconsistente devido a atualizações de layout de notas antigas.
