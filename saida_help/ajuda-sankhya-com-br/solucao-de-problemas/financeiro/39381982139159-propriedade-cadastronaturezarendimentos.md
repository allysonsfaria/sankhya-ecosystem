---
id: "39381982139159"
titulo: "Propriedade 'CadastroNaturezaRendimentos' não existe para o ValueObject  'Financeiro.ValueObject'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39381982139159-Propriedade-CadastroNaturezaRendimentos-n%C3%A3o-existe-para-o-ValueObject-Financeiro-ValueObject"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T13:32:47Z"
rotulos: ["Configuração", "Relatórios", "Movimentação Financeira", "Financeiro", "Erro", "Artigo criado KCS", "Financeiro - KCS"]
---

# Propriedade 'CadastroNaturezaRendimentos' não existe para o ValueObject  'Financeiro.ValueObject'

**MENSAGEM**

Falha detectada

Propriedade 'CadastroNaturezaRendimentos' não existe para o ValueObject 
'Financeiro.ValueObject'

**SITUAÇÃO**

Ao tentar exportar dados da tela **"Movimentação Financeira"** (Financeiro > Rotinas > Movimentação Financeira) para uma planilha Excel (.xls), o sistema apresenta mensagens de erro e não permite a conclusão da exportação.

**SOLUÇÃO**

**Solução: Ajuste as colunas apresentadas na grade**

**(1)** Acesse a tela **"Movimentação Financeira"** (Financeiro > Rotinas > Movimentação Financeira).
**(2)** Clique no ícone de configurações (engrenagem) e posteriormente clique em **"Configurar Grade".**
**(3)** Em "Colunas Selecionadas" remova os campos **“Código Natureza Rendimento” e “Descrição Natureza Rendimento”** .

![Imagem 1: (1) Acesse a tela "Movimentação Financeira" (Financeiro > Rotinas > Movimentação Financeira). (2) Clique no ícone de…](https://ajuda.sankhya.com.br/hc/article_attachments/41865136539927)

**(4)** Realize novamente a exportação para Excel.

**CAUSA**

Campos como **"Natureza de Rendimento"** **e “Descrição Natureza Rendimento”** são calculados dinamicamente e não podem ser exportados para Excel, pois não possuem vínculo com a tabela TGFFIN.
