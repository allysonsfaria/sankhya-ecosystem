---
id: "360051398253"
titulo: "O registro I051 é obrigatório quando existe código do plano de contas referencial informado no registro 0000 (COD_PLAN_REF)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360051398253-O-registro-I051-%C3%A9-obrigat%C3%B3rio-quando-existe-c%C3%B3digo-do-plano-de-contas-referencial-informado-no-registro-0000-COD-PLAN-REF"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:30:43Z"
rotulos: ["#criadoRoger", "Configuração", "ECD", "Impostos", "Contabilidade", "Plano de Contas", "Registro I051 obrigatório: Se COD_PLAN_REF no 0000", "Causa: Campo \"Instituição Resp. Man.\" preenchido", "Solução: Verificar e configurar Plano de Contas gerar arquivo I051"]
---

# O registro I051 é obrigatório quando existe código do plano de contas referencial informado no registro 0000 (COD_PLAN_REF)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18666096124311) MENSAGEM:**

O registro **I051**é obrigatório quando existe código do plano de contas referencial informado no registro 0000 **(COD\_PLAN\_REF).**

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18666079470231) CAUSA:**

Esse campo torna-se obrigatório a partir do momento que o campo "Instituição Resp. Man. Plano Contas Referencial", da aba Plano de Contas, está com valor informado.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18666079476631) SOLUÇÃO:**

![Imagem 4: Contabilidade » Preferências » Empresa](https://ajuda.sankhya.com.br/hc/article_attachments/18666096149143) Contabilidade » Preferências » Empresa

- Aba: Plano de Contas.
- Campo: Instituição Resp. Man. Plano Contas Referencial = [Caso esteja com um valor diferente de 'Nenhuma'], devera efetuar a marcação e geração do **I051** (Blocos e Registros, então acesse a aba: **ECD-Escrituração Contábil Digital**

![Imagem 5: Campo: Instituição Resp. Man. Plano Contas Referencial = (Caso esteja com um valor diferente de 'Nenhuma'), devera…](https://ajuda.sankhya.com.br/hc/article_attachments/18666096153111)

![Imagem 6: Contabilidade » Cadastros » Plano de Contas:](https://ajuda.sankhya.com.br/hc/article_attachments/18666096159127)Contabilidade » Cadastros » Plano de Contas:

- Verifique se a referida empresa já fez a importação do Plano de Contas Referencial.
- Maiores detalhes do processo, acesse o artigo [Plano de Contas Referencial](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116353)

![Imagem 7: Após os devidos ajustes e manutenções no Plano de Contas, gere o arquivo novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/18666096165143)Após os devidos ajustes e manutenções no Plano de Contas, gere o arquivo novamente.
