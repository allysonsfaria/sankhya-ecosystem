---
id: "33252693301655"
titulo: "Como alterar o telefone ou endereço no PDF da Nota Fiscal (DANFE)?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33252693301655-Como-alterar-o-telefone-ou-endere%C3%A7o-no-PDF-da-Nota-Fiscal-DANFE"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T14:29:11Z"
rotulos: ["Configuração", "Relatórios", "Empresa", "NF-e", "DANFE", "Passos para resolver", "Razão do erro", "Detalhe do erro", "DANF", "telefone incorreto", "alterar telefone", "telefone errado", "dados incorretos", "dados danf", "telefone danf", "Como alterar o telefone", "tabela TSIEMP", "ou endereço no PDF da Nota Fiscal (DANFE)?"]
---

# Como alterar o telefone ou endereço no PDF da Nota Fiscal (DANFE)?

**SITUAÇÃO:**

Ao gerar o PDF da Nota Fiscal Eletrônica (DANFE), constata-se que o campo referente ao telefone ou ao endereço da empresa emissora encontra-se incorreto, ou desatualizado.

**SOLUÇÃO:**

Se o modelo estiver utilizando dados dinâmicos (conforme é o padrão nos modelos oficiais da Sankhya):

**(1)** Acesse o Sankhya;

**(2)** Vá até a tela **''Empresas''** (Configurações» Cadastros» Empresas);

**(3)** Localize a empresa desejada;

**(4)** Na aba **''Endereço''** atualize o campo **''Telefone''** e demais informações, como endereço, razão social, entre outros;

**(5)** Salve as alterações;

**(6)** Gere uma nova nota fiscal e verifique o PDF.

**Observações:**

- As modificações no registro da empresa serão refletidas em todas as novas DANFEs geradas com este modelo;
- Em determinadas situações, essas informações podem estar **estabelecidas diretamente no modelo do relatório (JRXML)**. Isso acontece quando o desenvolvedor do modelo configurou os dados de maneira fixa no layout, em vez de utilizar os campos dinâmicos do sistema. Nessa circunstância, o desenvolvedor do modelo ou a unidade deve colaborar na modificação do modelo.

**CAUSA:**

As informações apresentadas no cabeçalho da DANFE, tais como **telefone, endereço, razão social e CNPJ**, são, em regra, extraídas do **cadastro da empresa** (tabela TSIEMP) no Sankhya.
