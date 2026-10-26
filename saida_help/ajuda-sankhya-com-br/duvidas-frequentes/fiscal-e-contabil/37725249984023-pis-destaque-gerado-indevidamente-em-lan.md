---
id: "37725249984023"
titulo: "PIS Destaque gerado indevidamente em lançamentos com valor destaque"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37725249984023-PIS-Destaque-gerado-indevidamente-em-lan%C3%A7amentos-com-valor-destaque"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-08-24T15:26:00Z"
rotulos: ["Configuração", "Fiscal", "NF-e", "PIS", "Impostos", "TOP", "Artigo atualizado KCS", "Squad Fiscal/Contábil", "PIS destaque", "PIS destaque gerado indevidamente", "Fiscal/Contábil - KCS"]
---

# PIS Destaque gerado indevidamente em lançamentos com valor destaque

O sistema está gerando base e alíquota para **"PIS Destaque"** em notas de compra, mesmo com a parametrização correspondente desabilitada na **"TOP"** (Configurações » Cadastros » Tipos de Operação - TOP).

### SITUAÇÃO

Mesmo que a **"TOP"** (Comercial » Arquivos » Cadastros) não esteja parametrizada para ratear despesas acessórias no PIS, ao realizar lançamentos de uma nota fiscal que possui **"Despesas acessórias"** com valor destacado, o sistema gera registros de **"PIS Destaque"** na tabela **"TGFDIN"**, apresentando base e alíquota do imposto, sem gerar o valor do imposto. A opção **"PIS proporcional para Destaque"** não precisa estar marcada na configuração da **"TOP"** para que este comportamento ocorra.

### SOLUÇÃO

**(1)** Este comportamento é uma **funcionalidade padrão do sistema** e não pode ser desabilitado.

**(2)** O sistema grava linhas na tabela **"TGFDIN"** automaticamente sempre que há **"Despesas acessórias"** com valor maior que zero, independentemente da parametrização da **"TOP"** para ratear essas despesas no PIS.

**(3)** Verifique que o registro na **"TGFDIN"** disponibiliza o valor proporcional da despesa acessória para cada item da nota no campo **"BASE"**, enquanto os campos **"BASERED"**, **"VALOR"** e **"VLRCRED"** permanecem zerados.

![Imagem 1: (3) Verifique que o registro na "TGFDIN" disponibiliza o valor proporcional da despesa acessória para cada item da nota…](https://ajuda.sankhya.com.br/hc/article_attachments/37725249977111)

**(4)** Essa linha de registro não interfere na geração da nota fiscal, livros e nem no SPED, servindo apenas para representar a despesa acessória como uma linha de imposto para fins de destaque e livros fiscais, caso alguma rotina do sistema precise dessa informação. O registro só ocorre quando realmente existe despesa acessória a ser considerada.

### CAUSA

A gravação dos registros na tabela **"TGFDIN"** é um comportamento padrão do sistema para garantir o controle proporcional das despesas acessórias por item da nota fiscal, visando disponibilizar informações para rotinas internas que necessitem do valor proporcional da despesa, sem impactar a conformidade fiscal.
