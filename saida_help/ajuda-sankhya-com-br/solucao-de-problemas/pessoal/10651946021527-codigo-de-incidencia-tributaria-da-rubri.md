---
id: "10651946021527"
titulo: "Código de incidência tributária da rubrica para o IRRF inválido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10651946021527-C%C3%B3digo-de-incid%C3%AAncia-tribut%C3%A1ria-da-rubrica-para-o-IRRF-inv%C3%A1lido"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:16:35Z"
rotulos: ["Configuração", "Eventos", "Impostos", "eSocial", "#folha", "Erro 1352", "Alterar incidência no cadastro", "Código IRRF inválido", "Corrigir incidência no cadastro", "Alterar conforme Tabela 21", "Salvar e gerar evento S-1010", "IRRF"]
---

# Código de incidência tributária da rubrica para o IRRF inválido

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18976283830167) MENSAGEM:**

Erro 1352 - Código de incidência tributária da rubrica para o IRRF inválido. Ação Sugerida: O valor informado no campo deverá existir na Tabela 21 - Códigos de Incidência Tributária da Rubrica para o IRRF.'

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18976283844503) SITUAÇÃO:**

Ao realizar o envio da rescisão, evento  S-2299 a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18976283857175) CAUSA:**

Ocorre quando o cadastro do evento está incorreto.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18976281059863) SOLUÇÃO:**

Conforme [Tabela 21 - Códigos de Incidência Tributária da Rubrica para o IRRF](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-html/tabelas.html#21) do e-Social, a incidência de IRRF '00 - Não é base do IRRF', **não é mais válida**, sendo assim, caso a rubrica esteja com essa informação, deve ser alterada: 

![Imagem 5: Conforme Tabela 21 - Códigos de Incidência Tributária da Rubrica para o IRRF do e-Social, a incidência de IRRF '00 -…](https://ajuda.sankhya.com.br/hc/article_attachments/18976281069335) Acesse o cadastro do evento que apresentou o erro;
![Imagem 6: Conforme Tabela 21 - Códigos de Incidência Tributária da Rubrica para o IRRF do e-Social, a incidência de IRRF '00 -…](https://ajuda.sankhya.com.br/hc/article_attachments/18976281074199) Na guia ESOCIAL, no quadro INCIDÊNCIAS, no campo  "Incidência para IRRF", altere o código para um que seja válido, de acordo a Tabela 21 do eSocial.
![Imagem 7: Conforme Tabela 21 - Códigos de Incidência Tributária da Rubrica para o IRRF do e-Social, a incidência de IRRF '00 -…](https://ajuda.sankhya.com.br/hc/article_attachments/18976283879319) Clique em Salvar;
![Imagem 8: Conforme Tabela 21 - Códigos de Incidência Tributária da Rubrica para o IRRF do e-Social, a incidência de IRRF '00 -…](https://ajuda.sankhya.com.br/hc/article_attachments/18976283887639) Após, gere novamente o evento S-1010;
![Imagem 9: Conforme Tabela 21 - Códigos de Incidência Tributária da Rubrica para o IRRF do e-Social, a incidência de IRRF '00 -…](https://ajuda.sankhya.com.br/hc/article_attachments/18976283894935) Acompanhe a validação do evento no eSocial.
