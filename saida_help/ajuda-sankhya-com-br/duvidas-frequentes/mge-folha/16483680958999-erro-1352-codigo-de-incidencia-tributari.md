---
id: "16483680958999"
titulo: "Erro 1352 - Código de incidência tributária da rubrica para o IRRF inválido  Pessoal G"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/16483680958999-Erro-1352-C%C3%B3digo-de-incid%C3%AAncia-tribut%C3%A1ria-da-rubrica-para-o-IRRF-inv%C3%A1lido-Pessoal-G"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:31:24Z"
rotulos: ["Configuração", "eSocial", "Folha de Pagamento", "Erro 1352", "Corrigir incidência conforme Tabela 21 e reenviar", "Incidência IRRF inválida", "Campo \"Incidência para IRRF\" incorreto", "Erro", "IRRF"]
---

# Erro 1352 - Código de incidência tributária da rubrica para o IRRF inválido  Pessoal G

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16483680927639) MENSAGEM:**

Erro 1352 - Código de incidência tributária da rubrica para o IRRF inválido. Ação Sugerida: O valor informado no campo deverá existir na Tabela 21 - Códigos de Incidência Tributária da Rubrica para o IRRF.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16483689175703) CAUSA:**

Ao enviar o evento S-1010, o sistema retorna com a mensagem supracitada devido ao preenchimento errado do campo “Incidência para IRRF”.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16483705511063) SOLUÇÃO:**

Para a resolução do erro, siga os passos abaixo:

![Imagem 4: Acesse a tela Eventos (Arquivos > Eventos), aba “Incidência” do evento que apresentou o erro;](https://ajuda.sankhya.com.br/hc/article_attachments/16483680932503) Acesse a tela Eventos (Arquivos > Eventos), aba “Incidência” do evento que apresentou o erro;

![Imagem 5: No campo “Incidência para IRRF”, altere para uma incidência válida conforme Tabela 21 - Códigos de Incidência…](https://ajuda.sankhya.com.br/hc/article_attachments/16483689181975) No campo “Incidência para IRRF”, altere para uma incidência válida conforme [Tabela 21 - Códigos de Incidência Tributária da Rubrica para o IRRF](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/leiautes-esocial-v-1-1-beta/tabelas.html#21) do eSocial: 

![Imagem 6: No campo “Incidência para IRRF”, altere para uma incidência válida conforme Tabela 21 - Códigos de Incidência…](https://ajuda.sankhya.com.br/hc/article_attachments/16483620841751)

![Imagem 7: Importante:](https://ajuda.sankhya.com.br/hc/article_attachments/16533929900439) **Importante:**

**Observar se o código utilizado não está com a vigência finalizada. Só serão válidos os códigos sem data de término.**

![Imagem 8: Observar se o código utilizado não está com a vigência finalizada. Só serão válidos os códigos sem data de término.](https://ajuda.sankhya.com.br/hc/article_attachments/16533929902999)

![Imagem 9: Salve as alterações;](https://ajuda.sankhya.com.br/hc/article_attachments/16483705524375) Salve as alterações;

![Imagem 10: Após ajuste, na Central do eSocial, gere novamente o evento S-1010 e envie o mesmo preenchendo o campo “Início de…](https://ajuda.sankhya.com.br/hc/article_attachments/16483680943767) Após ajuste, na Central do eSocial, gere novamente o evento S-1010 e envie o mesmo preenchendo o campo “Início de Validade”:

![Imagem 11: Após ajuste, na Central do eSocial, gere novamente o evento S-1010 e envie o mesmo preenchendo o campo “Início de…](https://ajuda.sankhya.com.br/hc/article_attachments/16483660156823)

Ou utilize o comando CTRL + SHIFT + F9 e informe a data desejada no poup-up que aparecerá:

**![Imagem 12: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16483689196055) OBSERVAÇÃO:**

Recomendamos sempre informar o primeiro dia da referência.

![Imagem 13: Recomendamos sempre informar o primeiro dia da referência.](https://ajuda.sankhya.com.br/hc/article_attachments/16483694248727)

![Imagem 14: Acompanhe a validação do evento no eSocial.](https://ajuda.sankhya.com.br/hc/article_attachments/16483697588247) Acompanhe a validação do evento no eSocial.
