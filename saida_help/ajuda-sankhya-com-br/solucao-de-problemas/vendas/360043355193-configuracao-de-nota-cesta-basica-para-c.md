---
id: "360043355193"
titulo: "Configuração de Nota Cesta Básica para Colaboradores"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043355193-Configura%C3%A7%C3%A3o-de-Nota-Cesta-B%C3%A1sica-para-Colaboradores"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:05:50Z"
rotulos: ["Configuração", "Fiscal", "Parceiro", "Impostos", "CFOP", "Diversos - Distribuição", "Cesta Básica", "Configuração de Nota Cesta Básica para Colaboradores"]
---

# Configuração de Nota Cesta Básica para Colaboradores

**![Imagem 1: SOLUÇÃO: Considere as configurações pertinentes ao tipo de lançamento na aplicação, conforme abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/16090158266263) SOLUÇÃO:**
Considere as configurações pertinentes ao tipo de lançamento na aplicação, conforme abaixo:

![Imagem 2: Acesse a tela " Tipos de Operação - TOP " (Caminho para acesso: Comercial » Arquivo » Cadastros » Tipos de Operação -…](https://ajuda.sankhya.com.br/hc/article_attachments/16090158274071) Acesse a tela **"[Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)"** (Caminho para acesso: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP):

**(2)**Crie uma TOP com as seguintes configurações:

**(3)**Aba **"Livro Fiscal"**

**(3)**Campo **"Atualização e Livro de ICMS"**

**(3)**Campo **"Natureza da Operação (SPED)"**, preencha com **"Distribuição de mercadoria aos empregados"**

**(3)**CFOP's: 5949 e 6949 (confira com o Contador)

As demais configurações como atualização de estoque e financeiro, alinhe com o Contador, conforme o processo da empresa.

![Imagem 3: Acesse a tela de " Parceiros " (Caminho para acesso: Configurações » Cadastros » Parceiros), crie um parceiro com a…](https://ajuda.sankhya.com.br/hc/article_attachments/16090142581271) Acesse a tela de **"[Parceiros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros)"** (Caminho para acesso: Configurações » Cadastros » Parceiros), crie um parceiro com a Descrição de Nome/Razão social: Diversos - Distribuição de mercadoria a empregados.

![Imagem 4: No Lançamento da Nota de Distribuição de Cesta Básica, teremos no XML a informação da Natureza da Operação:](https://ajuda.sankhya.com.br/hc/article_attachments/16090158282263) No Lançamento da Nota de Distribuição de Cesta Básica, teremos no XML a informação da Natureza da Operação:

<natOp>Distribuição de mercadoria aos empregados</natOp>

E no cabeçalho da Nota, no que se refere a Destinatário/Remetente, teremos a informação do Parceiro:

<dest>
<CPF>99999999999999</CPF>
<xNome>**Diversos - Distribuição de mercadoria a empregados**</xNome>

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16090158286487) CAUSA:**

**Cesta Básica**

Tratamento dispensado nas operações relacionadas com mercadorias que, não constituindo objeto normal de sua atividade, são adquiridas com a finalidade exclusiva de distribuição, neste Estado a título oneroso ou gratuito, a seus empregados para consumo final, visando atender às suas necessidades básicas de alimentação, vestuário, higiene e saúde. No ato da entrada da mercadoria e correspondendo a cada documento fiscal de aquisição, será emitida Nota Fiscal de Saída, nela se incluindo, sobre o valor das mercadorias adquiridas, a parcela do Imposto sobre Produtos Industrializados eventualmente pago pelo fornecedor.

A Nota Fiscal, além dos requisitos exigidos conterá as seguintes observações:

![Imagem 6: No campo "Destinatário" : Emitida nos termos do art. 1º, inciso I, da Portaria CAT nº 32, de 30.07.87;](https://ajuda.sankhya.com.br/hc/article_attachments/16090158274071) No campo **"Destinatário"**: Emitida nos termos do art. 1º, inciso I, da Portaria CAT nº 32, de 30.07.87;

![Imagem 7: Em seu corpo: Mercadorias adquiridas, conforme Nota Fiscal nº...., serie.... de ../../..", indicando os elementos…](https://ajuda.sankhya.com.br/hc/article_attachments/16090142581271) Em seu corpo: Mercadorias adquiridas, conforme Nota Fiscal nº...., serie.... de ../../..", indicando os elementos referentes ao documento fiscal de aquisição. Deverá ser discriminado item a item na nota fiscal a ser emitida pelo estabelecimento adquirente. Quanto ao IPI não há incidência do imposto.

**(2)** Como preencher a nota fiscal:
Natureza da operação: Distribuição de Cesta Básica
CFOP : 5.949 (Operações Internas).

Fundamento Legal:
ICMS: "Nota fiscal emitida nos termos da Portaria CAT n.º 154/2008. Nota Fiscal de aquisição n.º \_\_\_ de \_\_\_/\_\_\_/\_\_\_ " 
IPI : Não mencionar
