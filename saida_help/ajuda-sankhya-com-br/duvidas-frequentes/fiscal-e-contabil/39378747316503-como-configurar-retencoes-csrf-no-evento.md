---
id: "39378747316503"
titulo: "Como configurar retenções CSRF no evento R4020 da EFD-REINF?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39378747316503-Como-configurar-reten%C3%A7%C3%B5es-CSRF-no-evento-R4020-da-EFD-REINF"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-08-13T17:26:32Z"
rotulos: ["Configuração", "Impostos", "Artigo criado KCS", "Fiscal/Contábil - KCS", "Documentos Eletrônicos", "EFD-REINF", "R4020", "CSRF"]
---

# Como configurar retenções CSRF no evento R4020 da EFD-REINF?

O evento **R4020** da **EFD-REINF** é responsável por informar os pagamentos ou créditos realizados a beneficiários pessoas jurídicas.

Para que as **retenções CSRF** — **PIS, COFINS e CSLL** — sejam geradas corretamente nesse evento, é necessário realizar a configuração adequada no cadastro de impostos. A utilização incorreta do **Tipo de Imposto** ou do **Código de Receita** pode impedir a geração das retenções ou fazer com que os valores sejam apresentados de forma agregada no arquivo da REINF.

### Configuração do cadastro de impostos

Para que o sistema gere corretamente as retenções CSRF no evento R4020, configure o cadastro de impostos da seguinte forma:

**(1)** Acesse a tela **"Impostos"** (Configurações » Cadastros » Impostos).

**(2)** Crie **"cadastros separados"** para cada imposto: PIS, COFINS e CSLL.

**(3)** No campo **Tipo de Imposto**, selecione o imposto correspondente ao cadastro. Não utilize a opção **Outros** para esses impostos

**(4)** Detalhamento das configurações está [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599834-Impostos)

### Valores agregados x campos próprios

A apresentação das retenções CSRF no evento R-4020 depende da existência do **Código de Receita** configurado para os impostos.

**Com Código de Receita:** os valores das retenções de PIS, COFINS e CSLL podem ser considerados de forma agregada no evento R4020, conforme a regra de agrupamento aplicada pela EFD-REINF.

**Sem Código de Receita:** os valores das retenções permanecem individualizados, sendo apresentados nos respectivos campos do evento R4020 para cada imposto.

Dessa forma, a inclusão ou remoção do **Código de Receita** deve ser realizada de acordo com a forma de apresentação e agrupamento necessária para a escrituração da empresa.

Para agregar os impostos é necessário que nas abas **"Empresa"**, **"TOP"**, **"Parceiro"** e **"Serviço"**, informe o **"Código de receita"** correspondente ao imposto. A mesma informação definida na tela Empresa (Comercial » Preferências » Empresa) aba EFD-Reinf

![Imagem 1: Para agregar os impostos é necessário que nas abas "Empresa" , "TOP" , "Parceiro" e "Serviço" , informe o "Código de…](https://ajuda.sankhya.com.br/hc/article_attachments/42698147862935)

### Observações importantes

Se as notas fiscais já foram lançadas antes da configuração correta dos impostos, inclua manualmente o **"Código de receita"** nas notas para que as retenções sejam geradas corretamente no evento R4020.

Após realizar as configurações, gere novamente o evento R4020 para verificar se as retenções CSRF estão sendo informadas corretamente no arquivo da EFD-REINF.
