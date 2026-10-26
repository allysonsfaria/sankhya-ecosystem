---
id: "360059539993"
titulo: "A conta XX, é exclusiva da empresa YY"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360059539993-A-conta-XX-%C3%A9-exclusiva-da-empresa-YY"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:26:46Z"
rotulos: ["#criadoroger", "Configuração", "Contas", "Financeiro", "CORE_E02804", "Verificação de Configuração", "Conta Exclusiva Empresa", "Ajuste de Vínculos", "Erro"]
---

# A conta XX, é exclusiva da empresa YY

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16252821767575) MENSAGEM**:

[CORE\_E02804]  A conta XX, é exclusiva da empresa YY.

**![Imagem 2: SOLUÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/16252821771799) SOLUÇÃO**:

Veja um exemplo, para explanar a solução do problema

![Imagem 3: Acesse o cadastro de "Conta" Bancaria em: Configurações » Cadastros » Bancários » Contas](https://ajuda.sankhya.com.br/hc/article_attachments/16252821775127) Acesse o cadastro de **["Conta"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas)** Bancaria em: Configurações » Cadastros » Bancários » Contas

Identifique o código da conta bancaria vinculado à parcelas do Tipo de Negociação

![Imagem 4: Identifique o código da conta bancaria vinculado à parcelas do Tipo de Negociação](https://ajuda.sankhya.com.br/hc/article_attachments/14606130114711)

![Imagem 5: Acesse o cadastro de " Tipo de Negociação" em: Comercial » Arquivo » Cadastros » Tipos de Negociação Aba: "Parcelas"](https://ajuda.sankhya.com.br/hc/article_attachments/16252797363607) Acesse o cadastro de ["**Tipo de Negociação"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109173-Tipos-de-Negocia%C3%A7%C3%A3o) em: Comercial » Arquivo » Cadastros » Tipos de Negociação
Aba: **"Parcelas"**

![Imagem 6: Acesse o cadastro de " Tipo de Negociação" em: Comercial » Arquivo » Cadastros » Tipos de Negociação Aba: "Parcelas"](https://ajuda.sankhya.com.br/hc/article_attachments/14606138833815)

![Imagem 7: Acesse a Nota em: Comercial » Rotinas » Central de Vendas](https://ajuda.sankhya.com.br/hc/article_attachments/16252821787415) Acesse a Nota em: Comercial » Rotinas » Central de Vendas

Verifique a empresa do cabeçalho da nota, e caso esteja diferente da empresa exclusiva da conta bancária, considere ajustar as Parcelas do Tipo de Negociação.

![Imagem 8: Verifique a empresa do cabeçalho da nota, e caso esteja diferente da empresa exclusiva da conta bancária, considere…](https://ajuda.sankhya.com.br/hc/article_attachments/14606396630679)

Ou Seja:
Empresa da Conta Bancaria: Empresa 6 - Conta marcada como Exclusiva
Empresa da parcela do Tipo de Negociação como X-Constante Exclusiva = 6 
Empresa do cabeçalho da Nota = Empresa 6

Dessa forma, o cabeçalho da nota será salvo com sucesso.

[GIF animado: Imagem 9: Ou Seja: Empresa da Conta Bancaria: Empresa 6 - Conta marcada como Exclusiva Empresa da parcela do Tipo de Negociação…](https://ajuda.sankhya.com.br/hc/article_attachments/360097849214)

**![Imagem 10: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/16252821789975) CAUSA**:

Ocorre quando a Conta Bancaria, vinculada a uma das parcelas do Tipo de Negociação, é exclusiva da Empresa diferente da empresa do cabeçalho da nota, quando o Tipo de Negociação, está configurado na aba: **"Parcelas a opção"**
Campo **"Tipo de Empresa":** X-Constante Exclusiva e
Empresa: Código da empresa diferente do código vinculado a conta bancaria
