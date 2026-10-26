---
id: "360043715434"
titulo: "Agrupar pagamentos na Remessa para um Parceiro não esta funcionando"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043715434-Agrupar-pagamentos-na-Remessa-para-um-Parceiro-n%C3%A3o-esta-funcionando"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T16:00:23Z"
rotulos: ["Configuração", "Parceiro", "Movimentação Financeira", "Financeiro", "Remessa Bancária", "Problema de agrupamento", "configurações específicas", "Verificação e marcação adequada"]
---

# Agrupar pagamentos na Remessa para um Parceiro não esta funcionando

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17175716336023) SITUAÇÃO:**

Na geração do Arquivo de Remessa Bancária, ao marcar a opção: 'Agrupar pagamentos', não está agrupando os títulos de um determinado parceiro.

**![Imagem 2: SOLUÇÃO: Considere o Comportamento da Aplicação, conforme abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/17175748776215) SOLUÇÃO:**
Considere o Comportamento da Aplicação, conforme abaixo:

O Sistema considera as seguintes regras para agrupar:

Mesmo Parceiro, Vencimento, Banco, Agência, Conta, radical do CGC e opção: Marque a opção **"Agrupar Pagamentos na geração p/Banco"**, da aba: **"Identificação do Cadastro do Parceiro".**

![Imagem 3: Acesse: Configurações » Cadastros » Parceiros](https://ajuda.sankhya.com.br/hc/article_attachments/17175748777111) Acesse: Configurações » Cadastros » Parceiros

Aba: **"Identificação"**

Campo **"Agrupar Pagamentos na geração p/Banco"**: marque

Banco: informe um banco, válido

![Imagem 4: Acesse: Financeiro » EDI Bancário » Geração Arquivo de Remessa](https://ajuda.sankhya.com.br/hc/article_attachments/17175748777751) Acesse: Financeiro » EDI Bancário » Geração Arquivo de Remessa

- Configurações Geração do Arquivo:
- **"Agrupar Pagamento"**: marque
- Gere novamente o arquivo de Remessa Bancaria

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17175748781079) CAUSA:**

Quando o Vencimento, Banco, Conta, Agência ou a marcação de Agrupar Pagamentos na geração p/ Banco não esta marcado, não agrupa os títulos na remessa.
