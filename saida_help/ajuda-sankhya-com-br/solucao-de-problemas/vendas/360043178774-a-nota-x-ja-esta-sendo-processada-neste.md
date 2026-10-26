---
id: "360043178774"
titulo: "A nota 'X' já está sendo processada neste momento por outro usuário"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043178774-A-nota-X-j%C3%A1-est%C3%A1-sendo-processada-neste-momento-por-outro-usu%C3%A1rio"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-08-20T17:10:08Z"
rotulos: ["#PUBLIFER", "CORE_E04830", "Configuração", "Cache", "NF-e", "Agendamento", "TOP", "Nota em processamento", "Verificar configurações", "Processo travado", "Erro"]
---

# A nota 'X' já está sendo processada neste momento por outro usuário

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16164691893783) MENSAGEM:**

[CORE\_E04830]  A nota 'X' já está sendo processada neste momento por outro usuário.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16164691898647) SITUAÇÃO:**

Mensagem apresentada ao tentar confirmar e/ou gerar lote de notas fiscais.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16164713481239) SOLUÇÃO:**

![Imagem 4: Verifique se existem URL'S de teste inseridas na tela " Console NF-e " , aba Status do Serviço .](https://ajuda.sankhya.com.br/hc/article_attachments/16164691907095) Verifique se existem URL'S de teste inseridas na tela **"[Console NF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597734)"**, aba **Status do Serviço**.

- Em caso positivo, remova as URLs de teste de internet, assim o SanNFe vai utilizar suas URLs padrões e o problema pode deixar de acontecer;

![Imagem 5: Em caso positivo, remova as URLs de teste de internet, assim o SanNFe vai utilizar suas URLs padrões e o problema pode…](https://ajuda.sankhya.com.br/hc/article_attachments/14713122653719)

![Imagem 6: Acesse a Tela " Agendador para confirmação de Pedido " Caso nesta tela possua algum Registro de agendamento…](https://ajuda.sankhya.com.br/hc/article_attachments/16164713493911) Acesse a Tela **"[Agendador para confirmação de Pedido](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044598714)"**
Caso nesta tela possua algum Registro de agendamento configurado, verifique na aba **Configurações** se o agendamento possui Filtro por TOP.
Caso não possua será necessário criar o Filtro para as TOP's de Pedidos que devem ser confirmados automaticamente, caso não possua filtro o sistema fará tentativas de confirmação de todos os registros lançados no portal e causará o erro.

![Imagem 7: Acesse a Tela " Agendador para confirmação de Pedido " Caso nesta tela possua algum Registro de agendamento…](https://ajuda.sankhya.com.br/hc/article_attachments/14713194158103)

![Imagem 8: Caso persista, através do usuário SUP execute os procedimentos abaixo. É importante reportar aos demais usuários que…](https://ajuda.sankhya.com.br/hc/article_attachments/16164691916951) Caso persista, através do usuário SUP execute os procedimentos abaixo. É importante reportar aos demais usuários que esse procedimento mencionado irá reinicializar o sistema, e o manterá**inoperante por um prazo médio de 15 minutos**. 

![Imagem 9: Caso persista, através do usuário SUP execute os procedimentos abaixo. É importante reportar aos demais usuários que…](https://ajuda.sankhya.com.br/hc/article_attachments/14713163929751)

- **"[Administração do Servidor](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045107833)"** (Caminho de acesso: Configurações » Avançado » Administração do Servidor), aba **Geral** » **"Descartar cache"**
- Administração do Servidor (Caminho de acesso: Configurações » Avançado » Administração do Servidor), aba Geral » **"Reinicializar Sistema"**

![Imagem 10: Executado o procedimento acima é esperado que o sistema retorne a operar normalmente após o prazo médio mencionado (15…](https://ajuda.sankhya.com.br/hc/article_attachments/16164691921815) Executado o procedimento acima é esperado que o sistema retorne a operar normalmente após o prazo médio mencionado (15 minutos), caso isso não ocorra acione o Service Desk para análises. Reinicializado o mesmo, teste a emissão das notas.

**![Imagem 11: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16164713504535) CAUSA:**

Ocorre quando há algum processo sendo executado entre o Sistema SankhyaW e o SanNFe e esse esteja travado.
