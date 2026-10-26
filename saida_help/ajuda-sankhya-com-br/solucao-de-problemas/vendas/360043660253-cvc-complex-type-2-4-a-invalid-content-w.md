---
id: "360043660253"
titulo: "cvc-complex-type.2.4.a: Invalid content was found starting with element 'ISSQN'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043660253-cvc-complex-type-2-4-a-Invalid-content-was-found-starting-with-element-ISSQN"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:04:17Z"
rotulos: ["#criadoRoger", "#revisadohugo", "Configuração", "SEFAZ", "ICMS", "Impostos", "NFS-e", "ISSQN", "Acesse configurações de serviço", "Desmarque calcular ICMS", "Reenvie a nota"]
---

# cvc-complex-type.2.4.a: Invalid content was found starting with element 'ISSQN'

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16143851871511) MENSAGEM**:

cvc-complex-type.2.4.a: Invalid content was found starting with element 'ISSQN'. One of '{"http://www.portalfiscal.inf.br/nfe":IPI, "http://www.portalfiscal.inf.br/nfe":II, "http://www.portalfiscal.inf.br/nfe":PIS, "http://www.portalfiscal.inf.br/nfe":PISST, "http://www.portalfiscal.inf.br/nfe":COFINS, "http://www.portalfiscal.inf.br/nfe":COFINSST, "http://www.portalfiscal.inf.br/nfe":ICMSUFDest}' is expected.

**![Imagem 2: SOLUÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/16143851873687) SOLUÇÃO**:

Para correção, siga os passos abaixo:

![Imagem 3: Acesse: Configurações » Cadastros » Produtos » Serviço Aba: Impostos Opção "Calcular ICMS" : marcado. Caso este campo…](https://ajuda.sankhya.com.br/hc/article_attachments/16143851875991) Acesse: Configurações » Cadastros » Produtos » Serviço
Aba: **Impostos**
Opção **"Calcular ICMS"**: marcado. Caso este campo esteja marcado, salvo a exceção de Nota Mista para 'Brasília-DF', deverá verificar a incidência deste imposto em uma nota de Serviço, e considerar **desmarcar** este campo no cadastro do serviço.

![Imagem 4: Acesse: Configurações » Cadastros » Produtos » Serviço Aba: Impostos Opção "Calcular ICMS" : marcado. Caso este campo…](https://ajuda.sankhya.com.br/hc/article_attachments/14634160328727)

![Imagem 5: Após o ajuste, exclua o serviço da nota, lance novamente e transmita a nota de Serviço.](https://ajuda.sankhya.com.br/hc/article_attachments/16143851878167) Após o ajuste, exclua o serviço da nota, lance novamente e transmita a nota de Serviço.

**![Imagem 6: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/16143851879831) CAUSA**:

Ocorre quando a Nota de Serviço está configurada para calcular ISS e ICMS ao mesmo tempo, salvo a nota Mista para Brasília-DF, deverá verificar a incidência de ICMS em uma Nota de Serviço e desmarcar a opção.
