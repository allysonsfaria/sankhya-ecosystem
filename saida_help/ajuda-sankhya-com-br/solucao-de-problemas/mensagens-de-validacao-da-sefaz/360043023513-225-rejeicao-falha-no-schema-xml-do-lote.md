---
id: "360043023513"
titulo: "225 Rejeição: Falha no Schema XML do lote de NFe"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043023513-225-Rejei%C3%A7%C3%A3o-Falha-no-Schema-XML-do-lote-de-NFe"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:10:00Z"
rotulos: ["ERRONF", "ERROMDFE", "Configuração", "NF-e", "XML", "SEFAZ", "Nota Técnica", "225", "Atualize sistema e ajuste versão NT", "Configuração desatualizada da Nota Técnica", "Falha no Schema XML do lote de NFe", "225 Rejeição: Falha no Schema XML do lote de NFe", "225 Rejeição", "Rejeição 225"]
---

# 225 Rejeição: Falha no Schema XML do lote de NFe

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16456910007319) MENSAGEM:**

225 Rejeição: Falha no Schema XML do lote de NFe.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16456910012439) SOLUÇÃO:**

- Atualize a versão do seu sistema para últimas versões disponíveis em <http://downloads.sankhya.com.br/>
- Sintonize com seu contador se a NT mencionada (Nota Técnica 2018.005) já está sendo validada no seu Estado;

(1)** EM CASO NEGATIVO:**

Para as empresas/UF's em que a validação da NT citada ainda não esteja acontecendo, deverá manter a configuração abaixo:

![Imagem 3: Acesse a tela " EMPRESA" (Caminho de acesso: Comercial » Preferências » Empresa)](https://ajuda.sankhya.com.br/hc/article_attachments/16456910018839) Acesse a tela "**[EMPRESA"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893)** (Caminho de acesso: Comercial » Preferências » Empresa)

- Aba: "**NF-e/NFC-e"**

- Campo**: "Versão NT"= última (Nota Técnica 2018.005)**

 Acesse '**[Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834)**' (Caminho de acesso: Configurações » Avançado)

- Parâmetro "**DATINIULTNTNFE"** - Data Início da última nota técnica da NF-e' = 03/06/2019

![Imagem 4: Realizado esse ajuste, gere um novo lote da respectiva NF-e.](https://ajuda.sankhya.com.br/hc/article_attachments/16456958247191) Realizado esse ajuste, gere um novo lote da respectiva NF-e.

(1)** EM CASO POSITIVO:**

Para as empresas/UF's em que a validação da NT citada esteja acontecendo, realize as configurações abaixo:

![Imagem 5: Acesse Preferências (Caminho de acesso: Configurações » Avançado)](https://ajuda.sankhya.com.br/hc/article_attachments/16456910018839) Acesse Preferências (Caminho de acesso: Configurações » Avançado)

- Parâmetro "**DATINIULTNTNFE"** - Data Início da última nota técnica da NF-e' = 07/05/2019

![Imagem 6: Acesse EMPRESA (Caminho de acesso: Comercial » Preferências » Empresa )](https://ajuda.sankhya.com.br/hc/article_attachments/16456958250263) Acesse  EMPRESA (Caminho de acesso: Comercial » Preferências » Empresa)

- Aba: "**NF-e/NFC-e**"

- Campo: "**Versão NT" =** última (Nota Técnica 2018.005)

![Imagem 7: Realizado esse ajuste, gere um novo lote da respectiva NF-e.](https://ajuda.sankhya.com.br/hc/article_attachments/16456958247191) Realizado esse ajuste, gere um novo lote da respectiva NF-e.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16456910031895) CAUSA:**

Ocorre quando em casos em que a UF ainda não está validando a nova Nota Técnica 2018.005, se faz necessário configurar para não considerar a NT, nas Preferências da Empresa.
