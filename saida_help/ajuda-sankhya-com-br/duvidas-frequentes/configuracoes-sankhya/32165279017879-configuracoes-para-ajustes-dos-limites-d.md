---
id: "32165279017879"
titulo: "Configurações para ajustes dos limites de carregamento de linhas por tela"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32165279017879-Configura%C3%A7%C3%B5es-para-ajustes-dos-limites-de-carregamento-de-linhas-por-tela"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-07-24T12:43:16Z"
rotulos: ["Configuração", "Relatórios", "Portal de Vendas", "Parâmetro", "ajustes dos limites", "carregamento de linhas por tela", "MAXRSLTSIZE - Qtd. máx. linhas result. consultas", "MAXLINHASCUBO - Máximo de linhas em cubos de decisão", "MAXPAGRELATORIO - Máximo de páginas por relatório", "LIMLINHASDSTELA - Limite carregamento linhas por tela (resourceID)", "configurações", "MAXLINTELADIC - Máximo de linhas para telas adicionais", "QTDMAXREGEXPORT - Qtd. máx. de reg. para export. de PDF XLS e Cubo", "Desempenho"]
---

# Configurações para ajustes dos limites de carregamento de linhas por tela

Conheça as configurações que influenciam na quantidade de linhas carregadas nas telas do sistema, permitindo sua modificação para aumentar ou limitar esse número conforme a necessidade.

**(1)** **MAXRSLTSIZE - Qtd. máx. linhas result. consultas;**

Com este parâmetro é possível determinar a quantidade de linhas apresentadas nas telas do sistema.

**(1)** **MAXLINHASCUBO - Máximo de linhas em cubos de decisão;**

Quando a quantidade de linhas processadas no cubo de decisão excede o limite permitido, o sistema exibe uma mensagem informando o usuário sobre o excesso. Esse limite é configurado por meio do parâmetro "Máximo de linhas em cubos de decisão", identificado pela chave MAXLINHASCUBO.

**(1)** **MAXLINTELADIC - Máximo de linhas para telas adicionais;**

Com este parâmetro é possível determinar a quantidade de linhas apresentadas em telas adicionais.

**(1)** **MAXPAGRELATORIO - Máximo de páginas por relatório;**

Esse parâmetro possibilita limitar a quantidade de páginas por relatório, impedindo que relatórios com grande volume de informações prejudiquem o desempenho do servidor de aplicação.

**(1)** **QTDMAXREGEXPORT - Qtd. máx. de reg. para export. de PDF, XLS e Cubo;**

Por meio desse parâmetro, você poderá limitar a quantidade máxima de registros que serão exportados na utilização das funcionalidades, como Exportar em PDF, Exportar como planilha ou mesmo Visualizar em cubo, idependente da tela. Informe um número inteiro, que representa o limite de registro que serão exportados, por exemplo, 50 registros, 100 registros; conforme a necessidade da Empresa.

**(1)** **DESABPAGINA – Desabilitação de paginação no Portal de Vendas**

O parâmetro DESABPAGINA controla o comportamento de paginação exclusivamente no Portal de Vendas, identificado pelo seguinte resource ID (**br.com.sankhya.mgecom.mov.selecaodocumento**).

- **Funcionamento quando o DESABPAGINA está LIGADO:**

A paginação do Portal de Vendas é totalmente desabilitada. Todos os registros disponíveis são carregados de uma única vez. O parâmetro **LIMLINHASDSTELA** é completamente ignorado, mesmo que esteja configurado

- **Funcionamento quando o DESABPAGINA está DESLIGADO (configuração recomendada):**

A paginação do Portal de Vendas funciona normalmente, e o parâmetro **LIMLINHASDSTELA** passa a ser respeitado. O carregamento ocorre de forma paginada, reduzindo consumo de memória e risco de lentidão

**Observação:**O impacto do **DESABPAGINA** ocorre apenas no Portal de Vendas e outras telas do sistema não são afetadas por este parâmetro.

Manter o **DESABPAGINA** ligado em ambientes com grande volume de dados pode causar lentidão, travamentos e um alto consumo de recursos do servidor de aplicação.

**(1)** **LIMLINHASDSTELA - Limite carregamento linhas por tela (resourceID)**

O parâmetro LIMLINHASDSTELA é usado para limitar ou aumentar a quantidade de registros carregados em telas específicas, ou seja, se apenas na tela 'X' deseja limitar os registros, pode ser preenchido usando o seguinte exemplo:

```
br.com.sankhya.mgecom.mov.PortalCompras=500
```

Neste caso, foi limitado o carregamento, apenas da tela **"Portal de Compras",** em 500 registros. Se for necessário informar mais de uma tela, separe por ";".

**Observação:** uma vez ligado o parâmetro **DESABPAGINA**, a **funcionalidade do parâmetro LIMLINHASDSTELA,** para os **Portais**, **é ignorada.**

**Observação:** para obter o ID citado acima, abra a tela para a qual deseja fazer o ajuste do carregamento de registros. Em seguida, nesta tela, clique no botão **"Configurar tela"** e copie o ID.

![Imagem 1: Observação: para obter o ID citado acima, abra a tela para a qual deseja fazer o ajuste do carregamento de registros.…](https://ajuda.sankhya.com.br/hc/article_attachments/32475943372567)

![Imagem 2: Observação: para obter o ID citado acima, abra a tela para a qual deseja fazer o ajuste do carregamento de registros.…](https://ajuda.sankhya.com.br/hc/article_attachments/32475943375511)

**Importante:** **o aumento da quantidade de linhas para carregamento em telas pode ocasionar lentidão no sistema, visto que todos os parâmetros são globais, exceto o LIMLINHASDSTELA. Então, antes de realizar qualquer alteração, faça a devida validação em base de testes e só depois replique em produção.**
