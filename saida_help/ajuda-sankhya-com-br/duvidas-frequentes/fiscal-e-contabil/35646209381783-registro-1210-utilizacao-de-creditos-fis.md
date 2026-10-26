---
id: "35646209381783"
titulo: "Registro 1210: Utilização de créditos fiscais - ICMS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35646209381783-Registro-1210-Utiliza%C3%A7%C3%A3o-de-cr%C3%A9ditos-fiscais-ICMS"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:24:57Z"
rotulos: ["Configuração", "SPED", "Ajuste da Apuração de ICMS e ICMS ST", "Livros Fiscais", "Crédito", "ICMS", "Impostos", "EFD", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Utilização de créditos fiscais - ICMS", "Registro 1210"]
---

# Registro 1210: Utilização de créditos fiscais - ICMS

**SITUAÇÃO**

REGISTRO 1210: UTILIZAÇÃO DE CRÉDITOS FISCAIS – ICMS. Este registro deve ser apresentado para detalhar a utilização de créditos fiscais de ICMS no período. O somatório dos valores do campo 04 deste registro deve corresponder ao informado no campo 06 do registro 1200.

**![Imagem 1: SOLUÇÃO](https://ajuda.sankhya.com.br/hc/article_attachments/35646209358743)SOLUÇÃO**

Para que o **registro seja gerado automaticamente**, é necessário que exista uma **linha de ajuste de apuração configurada**.

Os campos do **Registro 1210** são alimentados a partir da tela "**Ajuste da Apuração de ICMS e ICMS ST" exclusivamente** pela Aba "**Utilização de Créditos Fiscais",** conforme orientação abaixo:

**(1)** Acesse a tela Ajuste da Apuração de ICMS e ICMS ST (Livros Fiscais > Arquivos > Ajuste da Apuração de ICMS e ICMS ST)

**(2)** Vá até a aba **"Controle Créditos Fiscais"**

**(3)** Na sub-aba Utilização de Créditos Fiscais

**(4)** O sistema buscará automaticamente as notas relacionadas à empresa vinculada ao ajuste

**(5)** Os valores serão preenchidos com base nas informações das notas fiscais

Para mais informações sobre a tela da rotina, acesse o artigo: [Ajuste da Apuração de ICMS e ICMS ST](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607654-Ajuste-da-Apura%C3%A7%C3%A3o-de-ICMS-e-ICMS-ST#abacontrolecrditosfiscais)

![Imagem 2: Para mais informações sobre a tela da rotina, acesse o artigo: Ajuste da Apuração de ICMS e ICMS ST](https://ajuda.sankhya.com.br/hc/article_attachments/35646219226007)

**Geração dos valores:**

- Os valores são alimentados automaticamente no momento da geração do Livro de ICMS;
- O sistema buscará as informações das configurações de ajustes de apuração;
- Os campos serão preenchidos com base nos documentos fiscais vinculados.

**Importante:**

- Os valores gerados automaticamente serão utilizados para os registros 1200 e 1210 do SPED;
- O sistema considerará apenas registros relacionados à empresa vinculada ao ajuste;
- A busca é realizada na tabela de Nota/Pedido para vincular os documentos fiscais.

Esta. configurações permitem que o sistema gere automaticamente os valores necessários para o controle de créditos fiscais, baseando-se nos documentos fiscais existentes.
