---
id: "360043179174"
titulo: "Conferência finalizada. Erro ao imprimir etiquetas: Impressão de etiquetas cancelada. Nenhuma página a apresentar"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043179174-Confer%C3%AAncia-finalizada-Erro-ao-imprimir-etiquetas-Impress%C3%A3o-de-etiquetas-cancelada-Nenhuma-p%C3%A1gina-a-apresentar"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:02:50Z"
rotulos: ["#PUBLIFER", "Conferência", "Configuração", "Impressão", "TOP", "Verifique configuração", "Opção incorreta selecionada", "Impressão cancelada", "Erro"]
---

# Conferência finalizada. Erro ao imprimir etiquetas: Impressão de etiquetas cancelada. Nenhuma página a apresentar

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16161833140503) MENSAGEM:**

Conferência finalizada. Erro ao imprimir etiquetas: Impressão de etiquetas cancelada. Nenhuma página a apresentar. Verifique o filtro e tente novamente.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16161819028887) SITUAÇÃO:**

Ao finalizar a conferência de um lançamento, está sendo apresentada a mensagem.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16161819030679) SOLUÇÃO:**

![Imagem 4: Acesse a tela " Tipo de Operação - TOP " , localize o "Tipo de Operação" utilizado no respectivo lançamento.](https://ajuda.sankhya.com.br/hc/article_attachments/16161833147159) Acesse a tela **"[Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP)"**, localize o **"Tipo de Operação"** utilizado no respectivo lançamento.

![Imagem 5: Na aba "Geral" , verifique o código informado no campo "Configuração p/ conferência" .](https://ajuda.sankhya.com.br/hc/article_attachments/16161819048599) Na aba **"Geral"**, verifique o código informado no campo **"Configuração p/ conferência"**.

![Imagem 6: Acesse a tela " Configuração de Conferência " (Caminho de acesso: Comercial » Configuração » Configuração de…](https://ajuda.sankhya.com.br/hc/article_attachments/16161833163159) Acesse a tela **"[Configuração de Conferência](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112073-Configura%C3%A7%C3%A3o-de-Confer%C3%AAncia)"** (Caminho de acesso: Comercial » Configuração » Configuração de Conferência), localizar a conferência conforme item 2.

![Imagem 7: Na aba "Formação de Volumes" o campo " Formação de Volumes" deve estar configurado: "Registro detalhado de volumes".](https://ajuda.sankhya.com.br/hc/article_attachments/16161833165719) Na aba **"Formação de Volumes"** o campo "**Formação de Volumes"** deve estar configurado: **"Registro detalhado de volumes".**

![Imagem 8: Na aba "Formação de Volumes" o campo " Formação de Volumes" deve estar configurado: "Registro detalhado de volumes".](https://ajuda.sankhya.com.br/hc/article_attachments/14705230591511)

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16161833166871) CAUSA:**

Mensagem apresentada ao realizar impressão de etiquetas após conferência, quando a configuração de Formação de volumes for configurada diferente de Registro detalhado de volumes, pois é essa opção que popula as tabelas TGFVCF e TGFIVC, que são utilizada pelo jrxml para imprimir as etiquetas.
