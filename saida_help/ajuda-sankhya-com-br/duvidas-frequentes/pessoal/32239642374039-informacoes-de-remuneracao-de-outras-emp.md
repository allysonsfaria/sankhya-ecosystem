---
id: "32239642374039"
titulo: "Informações de remuneração de outras empresas não estão sendo consideradas para cálculos do 13º salário"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32239642374039-Informa%C3%A7%C3%B5es-de-remunera%C3%A7%C3%A3o-de-outras-empresas-n%C3%A3o-est%C3%A3o-sendo-consideradas-para-c%C3%A1lculos-do-13%C2%BA-sal%C3%A1rio"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-07-29T13:26:38Z"
rotulos: ["Eventos", "Impostos", "INSS", "Folha de Pagamento", "13º Salário", "Informações de remuneração de outras empresas", "INSS 13º Retido Outras Fontes ", "Base INSS 13º Outras Fontes ", "Base IRRF Outras Fontes", "não estão sendo consideradas", "cálculos do 13º salário", "IRRF Retido Outras Fontes ", "IRRF"]
---

# Informações de remuneração de outras empresas não estão sendo consideradas para cálculos do 13º salário

**SITUAÇÃO:**

O colaborador possui informações de **remuneração de outras empresas**, mas essas informações não foram consideradas corretamente no **cálculo do 13º salário** para os valores do **INSS** e **IRRF**.

**SOLUÇÃO:**

Para que os valores de remuneração de outras fontes sejam corretamente considerados nos cálculos de 13º salário, os valores de INSS e IRRF de outras fontes de 13º salário precisam ser lançados usando os seguintes **eventos**:

**![Imagem 1: 502: INSS 13º Retido Outras Fontes](https://ajuda.sankhya.com.br/hc/article_attachments/32401053762327)502:** INSS 13º Retido Outras Fontes 

(2)**Característica:** INSS13RETIDOOUTRASFONTES

**![Imagem 2: 503: Base INSS 13º Outras Fontes](https://ajuda.sankhya.com.br/hc/article_attachments/32401053762327)503:** Base INSS 13º Outras Fontes 

(2)**Característica:** BASEINSS13OUTRASFONTES

**![Imagem 3: 509: IRRF Retido Outras Fontes](https://ajuda.sankhya.com.br/hc/article_attachments/32401053762327)509:** IRRF Retido Outras Fontes 

(2)**Característica:** IRRFRETIDOOUTRASFONTES

**![Imagem 4: 510: Base IRRF Outras Fontes](https://ajuda.sankhya.com.br/hc/article_attachments/32401053762327)510:** Base IRRF Outras Fontes 

(2)**Característica:** BASEIRRFOUTRASFONTES

Após a realização dos lançamentos na tela **"Lançamento de movimento"** (Pessoal+» Rotinas Folha» Lançamento de Movimento), o cálculo do 13º salário poderá ser realizado.
