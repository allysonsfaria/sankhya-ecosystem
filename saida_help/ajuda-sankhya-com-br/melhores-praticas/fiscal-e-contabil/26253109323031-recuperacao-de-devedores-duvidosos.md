---
id: "26253109323031"
titulo: "Recuperação de Devedores Duvidosos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26253109323031-Recupera%C3%A7%C3%A3o-de-Devedores-Duvidosos"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-08-14T11:22:03Z"
rotulos: ["Configuração", "Movimentação Financeira", "PDD", "Recuperação de Devedores Duvidosos", "Crédito", "Contabilização", "Financeiro"]
---

# Recuperação de Devedores Duvidosos

A **contabilização da recuperação de devedores duvidosos** ocorre quando uma empresa consegue recuperar total ou parcialmente um valor que havia sido anteriormente classificado como incobrável ou de difícil recebimento.

Para essa contabilização é necessário que o título anteriormente já tenha sido marcado como PDD, e já tenha sido contabilizado como PDD.

**1° Passo** 

Tela **"Recuperação de Devedores Duvidosos":** Contabilização » Arquivos » Recuperação de Devedores Duvidosos

- Execute um filtro pelos os seguintes dados: Empresa, Número do Lote e contas de Débito e Crédito.

![Imagem 1: Execute um filtro pelos os seguintes dados: Empresa, Número do Lote e contas de Débito e Crédito.](https://ajuda.sankhya.com.br/hc/article_attachments/26427117142679)

**2° Passo**

Após Filtrar, trabalhe os botões **"Remover Selecionados"** e **"Remover NÃO selecionados"** para determinar as linhas que serão contabilizadas e recuperadas.

![Imagem 2: Após Filtrar, trabalhe os botões "Remover Selecionados" e "Remover NÃO selecionados" para determinar as linhas que…](https://ajuda.sankhya.com.br/hc/article_attachments/26427117146391)

- Ao clicar em recuperar acontecerá a contabilização recuperando o título marcado como PDD. Tanto que na movimentação financeira a marcação PDD é desfeita automaticamente.

![Imagem 3: Importante: o parâmetro "Apresentar tít. de PDD assumindo o Vlr. de Lanç - TITPDDVLRLANC" tem a função de definir qual…](https://ajuda.sankhya.com.br/hc/article_attachments/26427117150871)

**Importante:** o parâmetro **"Apresentar tít. de PDD assumindo o Vlr. de Lanç - TITPDDVLRLANC"** tem a função de definir qual valor será utilizado ao apresentar os títulos contabilizados como Devedores Duvidosos (PDD) na tela de Recuperação de Devedores Duvidosos. Quando este parâmetro está ativado, o sistema exibe os títulos com base no valor do lançamento contábil, em vez de usar o valor do desdobramento do título financeiro.

#### Comportamento do Parâmetro:

**![Imagem 4: Parâmetro ativado :](https://ajuda.sankhya.com.br/hc/article_attachments/26427113079319) Parâmetro ativado**:

Se os títulos já foram contabilizados como Devedores Duvidosos (seja pela rotina de Contabilização de Devedores Duvidosos ou via Agendamento), ao executar a rotina de Recuperação de Devedores Duvidosos o sistema irá mostrar o valor contabilizado originalmente como PDD, mantendo o valor do lançamento contábil.

**![Imagem 5: Parâmetro desativado :](https://ajuda.sankhya.com.br/hc/article_attachments/26427113083031) Parâmetro desativado**:

O sistema seguirá o comportamento padrão, ou seja, ao invés de exibir o valor do lançamento contábil, apresentará o valor do desdobramento do título conforme registrado no financeiro.
