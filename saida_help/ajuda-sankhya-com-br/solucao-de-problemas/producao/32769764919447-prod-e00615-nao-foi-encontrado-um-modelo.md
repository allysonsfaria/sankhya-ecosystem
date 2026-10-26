---
id: "32769764919447"
titulo: "[PROD_E00615] Não foi encontrado um modelo de etiqueta para realizar a pesagem. O modelo de etiqueta pode ser configurado no cadastro do produto, no cadastro da empresa da planta de manufatura ou no parâmetro \"MODETIPES\"."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32769764919447--PROD-E00615-N%C3%A3o-foi-encontrado-um-modelo-de-etiqueta-para-realizar-a-pesagem-O-modelo-de-etiqueta-pode-ser-configurado-no-cadastro-do-produto-no-cadastro-da-empresa-da-planta-de-manufatura-ou-no-par%C3%A2metro-MODETIPES"
trilha: "Solução de Problemas > Produção"
atualizado_em: "2026-07-22T14:30:25Z"
rotulos: ["Produtos", "Configuração", "Preferências", "Manufatura", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Erro", "cadastro da empresa", "planta de manufatura", "Modelo de etiqueta", "MODETIPES", "Squad WMS", "PROD_E00615"]
---

# [PROD_E00615] Não foi encontrado um modelo de etiqueta para realizar a pesagem. O modelo de etiqueta pode ser configurado no cadastro do produto, no cadastro da empresa da planta de manufatura ou no parâmetro "MODETIPES".

![Imagem 1: MENSAGEM](https://ajuda.sankhya.com.br/hc/article_attachments/32769771008151) **MENSAGEM**

[PROD\_E00615] Não foi encontrado um modelo de etiqueta para realizar a pesagem. O modelo de etiqueta pode ser configurado no cadastro do produto, no cadastro da empresa da planta de manufatura ou no parâmetro "MODETIPES".

**![Imagem 2: SOLUÇÃO](https://ajuda.sankhya.com.br/hc/article_attachments/32769764912919)SOLUÇÃO**

O sistema verifica o **modelo de etiqueta para pesagem** seguindo uma ordem de prioridade. Para resolver a mensagem, é necessário garantir que pelo menos um dos locais abaixo esteja configurado:

**1. Verifique o modelo de etiqueta no Produto**

**(1)** Acesse a tela [**''Produto''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608254-Empresa) (Configurações» Cadastros» Produtos» Produtos).

**(2)** Na aba **''Manufatura''**, sub aba **''Pesagem''.**

**(3)** Verifique se existe um modelo configurado no campo **''Modelo de Etiqueta''**.

**(4)** Caso esteja vazio, **inclua** o modelo desejado.

##### 2. Verifique o modelo de etiqueta na Empresa

**(1)** Acesse a tela [**''Empresa''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608254-Empresa) (Comercial » Preferências » Empresa).

**(2)** Abra a aba ''Manufatura'' e verifique se o campo ''Modelo de Etiqueta'' está preenchido.

**(3)** Confira se o campo ''Modelo de Etiqueta'' está preenchido na aba Manufatura. Se não houver nenhum modelo configurado, **cadastre** o modelo que deverá ser utilizado.

##### 3. Verifique o parâmetro MODETIPES

**(1)** Acesse a tela **"Preferências"** (Configurações » Avançado » Preferências).

**(2)** No campo ''**Chave ou descrição''**, pesquise pelo parâmetro **''MODETIPES - Modelo de etiqueta pesagem''.**

**(3)** Caso esteja vazio, **configure** um modelo para que o sistema possa utilizá-lo.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/32769771010199)CAUSA:**

A mensagem aparece quando **nenhum modelo de etiqueta** está configurado no produto, na empresa ou no parâmetro.

Como o sistema não encontra nenhum modelo para usar na pesagem, ele mostra esse aviso.
