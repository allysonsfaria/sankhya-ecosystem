---
id: "360045975873"
titulo: "Suspensão 1/3 de férias - MP927. Saiba Mais !"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045975873-Suspens%C3%A3o-1-3-de-f%C3%A9rias-MP927-Saiba-Mais"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:34:36Z"
rotulos: ["Configuração", "Eventos", "#ancoragem", "Folha de Pagamento", "Férias", "MP927 Férias Suspensão", "Eventos Desconto Férias", "Parâmetros Versão Atual", "MP927"]
---

# Suspensão 1/3 de férias - MP927. Saiba Mais !

**[MEDIDA PROVISÓRIA Nº 927, DE 22 DE MARÇO DE 2020](http://legislacao.planalto.gov.br/legisla/legislacao.nsf/Viw_Identificacao/mpv%20927-2020?OpenDocument)**

|  | Dispõe sobre as medidas trabalhistas para enfrentamento do estado de calamidade pública reconhecido pelo Decreto Legislativo nº 6, de 20 de março de 2020, e da emergência de saúde pública de importância internacional decorrente do coronavírus (**covid-19**), e dá outras providências. |
| --- | --- |

Fonte: <http://www.planalto.gov.br/ccivil_03/_Ato2019-2022/2020/Mpv/mpv927.htm>

**Pré-Requisitos:**

- Versão 4.32.0.29 ou superior
- Versão 4.33.0.11 ou superior

Versões disponíveis em:

- Jiva  :<http://place.jiva.com.br/>
- Sankhya:  <http://place.sankhya.com.br/>

**![Imagem 1: Eventos e Fórmulas no caso da dispensa do pagamento de 1/3 de férias:](https://ajuda.sankhya.com.br/hc/article_attachments/19149779905175) Eventos e Fórmulas no caso da dispensa do pagamento de 1/3 de férias:**

 Foram criados eventos de desconto para suspender o pagamento de 1/3 de férias ou "zerar" as incidências de encargo do mesmo. Prudente manter os mesmos códigos utilizados.

**Importante:** Avalie as PRÓXIMAS parametrizações necessárias conforme uma das situações abaixo:

| [Clientes que os eventos de 1/3 de férias tem os códigos 402,404,414,416](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045975873-Suspens%C3%A3o-1-3-de-f%C3%A9rias-MP927-Saiba-Mais#Clientesevento402) | [Clientes que os eventos de 1/3 de férias tem os códigos: 4420,4040,4160](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045975873-Suspens%C3%A3o-1-3-de-f%C3%A9rias-MP927-Saiba-Mais#Clientesevento4420) |
| --- | --- |

**![Imagem 2: Alteração para clientes que utilizam a rotina ANTIGA de cálculo de férias ( Clientes que os eventos de 1/3 de férias…](https://ajuda.sankhya.com.br/hc/article_attachments/19149779916439) Alteração para clientes que utilizam a rotina ANTIGA de cálculo de férias [ Clientes que os eventos de 1/3 de férias tem os códigos** **402,404,414,416]:**

- **4502 - SUSPENSÃO 1/3 FÉRIAS MP927**

Aba Propriedades:

![Imagem 3: Aba Propriedades:](https://ajuda.sankhya.com.br/hc/article_attachments/360063410534)

Aba Incidência:

![Imagem 4: Aba Incidência:](https://ajuda.sankhya.com.br/hc/article_attachments/360063410714)

Aba Bases de Cálculo:

![Imagem 5: Aba Bases de Cálculo:](https://ajuda.sankhya.com.br/hc/article_attachments/360063410734)

**Fórmula:**

IF(PDESPARAM('ADERIMP927','TFPFUN','CODEMP = :INT\_CODEMP AND CODFUNC = :INT\_CODFUNC',STR(queFuncionario.CODEMP), STR(queFuncionario.CODFUNC)) <> 'S',&E402,0)

- **4504 - SUSPENSAO 1/3 ABONO  MP927**

Aba Propriedades:

![Imagem 6: Aba Propriedades:](https://ajuda.sankhya.com.br/hc/article_attachments/360064392633)

Aba Incidência:

![Imagem 7: Aba Incidência:](https://ajuda.sankhya.com.br/hc/article_attachments/360063410834)

Aba Bases de Cálculo:

![Imagem 8: Aba Bases de Cálculo:](https://ajuda.sankhya.com.br/hc/article_attachments/360063410954)

**Fórmula:**

IF(PDESPARAM('ADERIMP927','TFPFUN','CODEMP = :INT\_CODEMP AND CODFUNC = :INT\_CODFUNC',STR(queFuncionario.CODEMP), STR(queFuncionario.CODFUNC)) <> 'S',&E404,0)

- **4514 - SUSP 1/3 ADIANT FERIAS MP927**

Aba Propriedades:

![Imagem 9: Aba Propriedades:](https://ajuda.sankhya.com.br/hc/article_attachments/360063411034)

Aba Incidência:

![Imagem 10: Aba Incidência:](https://ajuda.sankhya.com.br/hc/article_attachments/360063411094)

Aba Bases de Cálculo:

![Imagem 11: Aba Bases de Cálculo:](https://ajuda.sankhya.com.br/hc/article_attachments/360063411154)

**Fórmula:**

IF(PDESPARAM('ADERIMP927','TFPFUN','CODEMP = :INT\_CODEMP AND CODFUNC = :INT\_CODFUNC',STR(queFuncionario.CODEMP), STR(queFuncionario.CODFUNC)) <> 'S',&E414,0)

- **4516 - SUSP 1/3 FERIAS MES COMP MP927**

Aba Propriedades:

![Imagem 12: Aba Propriedades:](https://ajuda.sankhya.com.br/hc/article_attachments/360064393173)

Aba Incidência:

![Imagem 13: Aba Incidência:](https://ajuda.sankhya.com.br/hc/article_attachments/360064393213)

Aba Bases de Cálculo:

![Imagem 14: Aba Bases de Cálculo:](https://ajuda.sankhya.com.br/hc/article_attachments/360063411694)

**Fórmula:**

IF(PDESPARAM('ADERIMP927','TFPFUN','CODEMP = :INT\_CODEMP AND CODFUNC = :INT\_CODFUNC',STR(queFuncionario.CODEMP), STR(queFuncionario.CODFUNC)) <> 'S',(FBE(QueFuncionario.CODEMP, QueFuncionario.CODFUNC, FSOMAMES(&Refere,-1),'F','4514') \* (-1)),0)

[Voltar ao topo](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045975873-Suspens%C3%A3o-1-3-de-f%C3%A9rias-MP927-Saiba-Mais#topo)

**![Imagem 15: Alteração para clientes que utilizam a NOVA rotina de cálculo de férias (Clientes que os eventos de ⅓ de férias tem os…](https://ajuda.sankhya.com.br/hc/article_attachments/19149783315479) Alteração para clientes que utilizam a NOVA rotina de cálculo de férias [Clientes que os eventos de  ⅓ de férias tem os códigos: 4420,4040,4160]:**

- **4520 - SUSPENSÃO 1/3 FÉRIAS MP927**

Aba Propriedades:

![Imagem 16: Aba Propriedades:](https://ajuda.sankhya.com.br/hc/article_attachments/360064393853)

Aba Incidência:

![Imagem 17: Aba Incidência:](https://ajuda.sankhya.com.br/hc/article_attachments/360063412154)

Aba Bases de Cálculo:

![Imagem 18: Aba Bases de Cálculo:](https://ajuda.sankhya.com.br/hc/article_attachments/360064393973)

**Fórmula:**

IF(PDESPARAM('ADERIMP927','TFPFUN','CODEMP = :INT\_CODEMP AND CODFUNC = :INT\_CODFUNC',STR(queFuncionario.CODEMP), STR(queFuncionario.CODFUNC)) <> 'S',&E4420,0)

**Fórmula índice:**

&DIAFERADI

- **4540 - SUSPENSÃO 1/3 ABONO MP927**

Aba Propriedades:

![Imagem 19: Aba Propriedades:](https://ajuda.sankhya.com.br/hc/article_attachments/360064394233)

Aba Incidência:

![Imagem 20: Aba Incidência:](https://ajuda.sankhya.com.br/hc/article_attachments/360063412394)

Aba Bases de Cálculo:

![Imagem 21: Aba Bases de Cálculo:](https://ajuda.sankhya.com.br/hc/article_attachments/360064394393)

**Fórmula:**

IF(PDESPARAM('ADERIMP927','TFPFUN','CODEMP = :INT\_CODEMP AND CODFUNC = :INT\_CODFUNC',STR(queFuncionario.CODEMP), STR(queFuncionario.CODFUNC)) <> 'S',&E4040,0)

- **4550 - SUSP 1/3 FERIAS MES COMP MP927:**

**Esse evento não incide no líquido, porque o valor pago no recibo já é descontado no evento 4110. Ele entrará somente para zerar a incidência de encargos (INSS e FGTS).**

Aba Propriedades:

![Imagem 22: Aba Propriedades:](https://ajuda.sankhya.com.br/hc/article_attachments/360065196573)

Aba Incidência:

![Imagem 23: Aba Incidência:](https://ajuda.sankhya.com.br/hc/article_attachments/360063413214)

Aba Bases de Cálculo:

![Imagem 24: Aba Bases de Cálculo:](https://ajuda.sankhya.com.br/hc/article_attachments/360064395653)

**Fórmula:**

IF(PDESPARAM('ADERIMP927','TFPFUN','CODEMP = :INT\_CODEMP AND CODFUNC = :INT\_CODFUNC',STR(queFuncionario.CODEMP), STR(queFuncionario.CODFUNC)) <> 'S',&E4160,0)

**Importante:**

Demais questões relativas a 1/3 que foram tratadas na MP927, serão liberadas posteriormente, e as informações devidamente atualizadas nesse artigo.

- **Artigos relacionados:**
- [Pagamento do 1/3 de férias suspenso - MP927. Saiba Mais!](https://ajuda.sankhya.com.br/hc/pt-br/articles/360048834473)
