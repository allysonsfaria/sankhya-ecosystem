---
id: "33377183550103"
titulo: "CSOSN não preenchido automaticamente na emissão de notas para empresas do Simples Nacional"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33377183550103-CSOSN-n%C3%A3o-preenchido-automaticamente-na-emiss%C3%A3o-de-notas-para-empresas-do-Simples-Nacional"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:29:05Z"
rotulos: ["Configuração", "Fiscal", "NF-e", "Simples Nacional", "Impostos", "TOP", "Passos para resolver", "Razão do erro", "Detalhe do erro", "emissão de notas para empresas do Simples Nacional", "ódigo de Situação da Operação do Simples Nacional (CSOSN)", "CSOSN não preenchido automaticamente", "CSOSN vazio"]
---

# CSOSN não preenchido automaticamente na emissão de notas para empresas do Simples Nacional

**SITUAÇÃO**

O campo **"Código de Situação da Operação do Simples Nacional (CSOSN)"** **permanece vazio** durante a emissão de notas fiscais para empresas do Simples Nacional, **mesmo após o** **cadastro correto do código na alíquota de ICMS e o ajuste das Configurações do Simples Nacional.**

**Observação:** para saber mais sobre essas configurações, acesse o artigo: ["Quais as principais configurações para cálculo de ICMS Simples Nacional"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110154).

**SOLUÇÃO**

Siga o passo a passo para garantir o preenchimento automático do CSOSN:

**(1)**  Verifique se tanto a empresa quanto o parceiro estão configurados como optantes pelo Simples Nacional.

**(2)**  Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e analise o campo **"Base Numeração"** na aba **"Impressão":**

- **Para notas de Venda e Devolução de Venda:**
  A base de numeração deve ser do tipo **"Venda"** ou **"Devolução de Venda"**. Assim, o sistema buscará o CSOSN automaticamente, porém não permitirá a alteração do número da nota na central.

![Imagem 1: Para notas de Venda e Devolução de Venda: A base de numeração deve ser do tipo "Venda" ou "Devolução de Venda" . Assim,…](https://ajuda.sankhya.com.br/hc/article_attachments/34102683015191)

- **Para notas de Compra e Devolução de Compra:**
  A base de numeração deve ser do tipo **"Manual (Informada pelo Usuário)"**. Neste caso, será possível alterar o número da nota no cabeçalho da central, porém o CSOSN não será preenchido automaticamente nos itens, sendo necessário o preenchimento manual.

![Imagem 2: Para notas de Compra e Devolução de Compra: A base de numeração deve ser do tipo "Manual (Informada pelo Usuário)" .…](https://ajuda.sankhya.com.br/hc/article_attachments/34102652211735)

**(3)**  Confira as marcações adicionais:

- Na tela **"Empresa"** (Comercial » Preferências » Empresa), a opção **"Escriturar valor de ICMS de entrada para Empresa Simples?"** deve estar desmarcada. Se marcada, o sistema não preencherá o CSOSN nos itens.
- Na tela **"Empresas"** (Configurações » Cadastros » Empresas), marque a opção **"Tem convênio Simples Nacional no Estado"** para operações internas. Assim, o sistema considerará a empresa como Simples Nacional dentro do próprio estado e buscará o CSOSN automaticamente.

**CAUSA**

O CSOSN não é preenchido automaticamente quando as configurações de optante pelo Simples Nacional não estão devidamente ajustadas para empresa e parceiro, ou quando a base de numeração da TOP está configurada de forma incompatível com o tipo de operação. Além disso, marcações incorretas nas preferências da empresa podem impedir o preenchimento automático do CSOSN.
