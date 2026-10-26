---
id: "30704225649559"
titulo: "Ao clicar em Visualizar NF-e/CT-e aparece o aviso 'sem mensagem de erro', o que fazer?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30704225649559-Ao-clicar-em-Visualizar-NF-e-CT-e-aparece-o-aviso-sem-mensagem-de-erro-o-que-fazer"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:35:00Z"
rotulos: ["CT-e", "Configuração", "NF-e", "XML", "SEFAZ", "Passos para resolver", "Razão do erro", "Detalhe do erro", "portal de importação de XML", "Visualizar NF-e/CT", "sem mensagem de erro", "Erro"]
---

# Ao clicar em Visualizar NF-e/CT-e aparece o aviso 'sem mensagem de erro', o que fazer?

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/30704225637655) **MENSAGEM:**

Sem mensagem de erro

![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30728404667927) **SITUAÇÃO:**

Na tela **Portal de Importação de XML** (Comercial » Rotinas » Portal de importação de XML), ao clicar no botão: **MD-e >> Visualizar NF-e/CT-e**

![Imagem 3: Na tela Portal de Importação de XML (Comercial » Rotinas » Portal de importação de XML), ao clicar no botão: MD-e >>…](https://ajuda.sankhya.com.br/hc/article_attachments/30728891984919)

Apresenta o seguinte Erro: **"Sem mensagem de erro"**

![Imagem 4: Apresenta o seguinte Erro: "Sem mensagem de erro"](https://ajuda.sankhya.com.br/hc/article_attachments/30704230276631)

**![Imagem 5: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30704225642135)SOLUÇÃO:**

Verifique se o conteúdo do parâmetro **CONFIGURACAOMDE** condiz com as configurações da tela **"Configuração MD-e/DF-e"**

**Exemplo:**

![Imagem 6: Exemplo:](https://ajuda.sankhya.com.br/hc/article_attachments/30728956388375)

![Imagem 7: Exemplo:](https://ajuda.sankhya.com.br/hc/article_attachments/30728891987223)

Pois o sistema verifica o caminho de impressão dos relatórios conforme definido no parâmetro. Uma vez que as configurações realizadas na tela Configuração MD-e/DF-e reflete no conteúdo inserido dentro do parâmetro. Porém, se realizado o ajuste manual direto no parâmetro, a informação inserida deve ser encontrada no sistema para que seja possível realizar a impressão.

**Importante:** caso tenha dúvida referente a configuração de impressão dessa rotina, veja a documentação: [**Configuração MD-e/DF-e**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599234-Configura%C3%A7%C3%A3o-MD-e-DF-e)

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/30704230283415)CAUSA:**

Divergência nas configurações de Impressão da rotina do MD-e / DF-e
