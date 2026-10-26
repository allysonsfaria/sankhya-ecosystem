---
id: "26948563024151"
titulo: "Campo \"Atraso\" incorreto na baixa de um título na Movimentação Financeira"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26948563024151-Campo-Atraso-incorreto-na-baixa-de-um-t%C3%ADtulo-na-Movimenta%C3%A7%C3%A3o-Financeira"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T14:40:31Z"
rotulos: ["Configuração", "Movimentação Financeira", "Financeiro", "Passos para resolver", "Razão do erro", "Detalhe do erro", "baixa de um título na movimentação financeira", "valor incorreto", "campo \"Atraso\"", "Campo \"Atraso\" incorreto na baixa de um título na Movimentação Financeira", "Argumentos da VM", "Timezone"]
---

# Campo "Atraso" incorreto na baixa de um título na Movimentação Financeira

**(1)**Quando o campo **"Atraso"** dentro da baixa de um título na movimentação financeira apresenta seu valor incorreto (**com um dia a mais ou um dia a menos**), é necessário analisar os Argumentos da VM.

![Imagem 1: Acesse a Administração do Servidor e verifique se no texto do campo "Argumentos da VM" possui o argumento abaixo,…](https://ajuda.sankhya.com.br/hc/article_attachments/26948563016343)  Acesse a Administração do Servidor e verifique se no texto do campo **"Argumentos da VM"** possui o argumento abaixo, conforme cita no Help '[Configuração de argumentos para Wildfly](https://ajuda.sankhya.com.br/hc/pt-br/articles/8896725681943-Configura%C3%A7%C3%A3o-de-argumentos-para-Wildfly)'.

**(1)** **-JAVA\_OPTS="$JAVA\_OPTS -Duser.timezone=GMT-3"**

Esse argumento é responsável por ajustar o timezone do servidor de aplicação, que serve de referência para o campo Atraso.

**Observação:**se seu servidor é Local, esse processo é realizado pelo time de Infraestrutura da empresa. Por outro lado, caso seja em Nuvem, entre em contato com os responsáveis pela hospedagem. Qualquer dúvida na execução do processo, acione a unidade responsável.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/26948516842775)CAUSA:**

Ocorre quando não existe o argumento de timezone, causando a divergência da data/hora do servidor.
