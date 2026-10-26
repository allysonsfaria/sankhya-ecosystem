---
id: "4404429910679"
titulo: "O registro I051 é obrigatório quando existe código do plano de contas referencial informado no registro 0000 (COD_PLAN_REF)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4404429910679-O-registro-I051-%C3%A9-obrigat%C3%B3rio-quando-existe-c%C3%B3digo-do-plano-de-contas-referencial-informado-no-registro-0000-COD-PLAN-REF"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:23:14Z"
rotulos: ["Configuração", "ECD", "Fiscal", "Contabilidade", "Plano de Contas", "#publicadoHyago", "Solução: Importar plano referencial e vincular.", "Registro I051 obrigatório: Se COD_PLAN_REF no 0000.", "Configuração: Ajustar nas preferências da empresa."]
---

# O registro I051 é obrigatório quando existe código do plano de contas referencial informado no registro 0000 (COD_PLAN_REF)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16347353174295) MENSAGEM:**

O registro I051 é obrigatório quando existe código do plano de contas referencial informado no registro 0000 (COD\_PLAN\_REF).

![Imagem 2: O registro I051 é obrigatório quando existe código do plano de contas referencial informado no registro 0000…](https://ajuda.sankhya.com.br/attachments/token/pY2O3nremK4fsYloPsKETrjfp/?name=inline-38988359.png)

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16347336853783)SOLUÇÃO:**

![Imagem 4: Importe o plano de contas Referencial (ver Artigo Plano de Contas Referencial )](https://ajuda.sankhya.com.br/hc/article_attachments/16347353179031) Importe o plano de contas Referencial (ver Artigo [Plano de Contas Referencial](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116353-Plano-de-Contas-Referencial?source=search&auth_token=eyJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X2lkIjo5NjE4MTY4LCJ1c2VyX2lkIjoxNTA1MjQxMDA5NTIxLCJ0aWNrZXRfaWQiOjExMDI1NSwiY2hhbm5lbF9pZCI6NjMsInR5cGUiOiJTRUFSQ0giLCJleHAiOjE2MjkwNTg5NDl9.Rj1KFevoNjflPisXjHDCbWH60mFmXyzRHdytzVsSP_4))

![Imagem 5: Na tela "Plano de contas" , aba "Plano de contas referencial" , vincule o Plano de Contas referencial.](https://ajuda.sankhya.com.br/hc/article_attachments/16347353180567) Na tela **"Plano de contas"**, aba **"Plano de contas referencial"**, vincule o Plano de Contas referencial.

![O](https://ajuda.sankhya.com.br/hc/article_attachments/15673438105751)

![Imagem 7: Nas preferências da empresa (Caminho de acesso: Contabilidade » Preferências), na aba "ECD- Escrituração Contábil…](https://ajuda.sankhya.com.br/hc/article_attachments/16347353181975) Nas preferências da empresa (Caminho de acesso: Contabilidade » Preferências), na aba **"ECD- Escrituração Contábil Digital"** cadastre e marque para gerar.

![O](https://ajuda.sankhya.com.br/hc/article_attachments/15673438110103)

**OBSERVAÇÃO:** o tipo do plano Definido nas Preferências da Empresa é o mesmo tipo que irá utilizar no cadastro do plano de contas nas contas.

![Imagem 9: OBSERVAÇÃO: o tipo do plano Definido nas Preferências da Empresa é o mesmo tipo que irá utilizar no cadastro do plano…](https://ajuda.sankhya.com.br/attachments/token/QO6dynqzWZKnu8rlorQuK7VP7/?name=inline387450432.png)

![O](https://ajuda.sankhya.com.br/hc/article_attachments/15673428048407)

**![Imagem 11: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16347336867479)CAUSA:**

Nessa validação o sistema está validando a informação que tem no registro 0000 campo.

| |0000|LECD|01012020|31122020|FENIX PARTICIPAÇÕES E EMPREENDIMENTOS|26751895000190|DF|0779354500154|0000000|||0|0|0||0|0||N|N|0|0|2| |
| --- |

![Imagem 12: |0000|LECD|01012020|31122020|FENIX PARTICIPAÇÕES E…](https://ajuda.sankhya.com.br/attachments/token/xclWq5NkpB0GAbhXTlgiQOCzw/?name=inline-1194395463.png)

Essa informação está sendo gerada com base nas configurações das preferências da empresa (Caminho de acesso: Empresa » Contabilidade), aba **"Plano de Contas"**, campo **"Instituição Resp. Man. Plano Contas Referencial".**

![O](https://ajuda.sankhya.com.br/hc/article_attachments/15673428053015)
