---
id: "360044086153"
titulo: "Nota de CT-e precisa que os campos 'Cód.Cid.Início CT-e' e 'Cód.Cid.Fim CT-e' na aba Impostos sejam informados por causa do SPED"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044086153-Nota-de-CT-e-precisa-que-os-campos-C%C3%B3d-Cid-In%C3%ADcio-CT-e-e-C%C3%B3d-Cid-Fim-CT-e-na-aba-Impostos-sejam-informados-por-causa-do-SPED"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-22T16:02:01Z"
rotulos: ["#criadoRoger", "CORE_E04419", "CT-e", "Configuração", "SPED", "Cidades", "Impostos", "TOP", "Requisitos do SPED para CT-e: Informação de Códigos de Cidades"]
---

# Nota de CT-e precisa que os campos 'Cód.Cid.Início CT-e' e 'Cód.Cid.Fim CT-e' na aba Impostos sejam informados por causa do SPED

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16172808611223) MENSAGEM:**

[CORE\_E04419]  Nota de CT-e precisa que os campos 'Cód.Cid.Início CT-e' e 'Cód.Cid.Fim CT-e' na aba Impostos sejam informados por causa do SPED.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16172791930263) SOLUÇÃO:**

![Imagem 3: Insira, através da tela " Configurador de Layout da nota " , os campos "Cód.Cid.Início CT-e" e "Cód.Cid.Fim CT-e" para…](https://ajuda.sankhya.com.br/hc/article_attachments/16172791936151) Insira, através da tela **"[Configurador de Layout da nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634)"**, os campos **"Cód.Cid.Início CT-e"** e **"Cód.Cid.Fim CT-e"** para o Tipo de Movimento/TOP utilizados no lançamento do respectivo CT-e.

![Imagem 4: Insira, através da tela " Configurador de Layout da nota " , os campos "Cód.Cid.Início CT-e" e "Cód.Cid.Fim CT-e" para…](https://ajuda.sankhya.com.br/hc/article_attachments/14690424919703)

**(2)** Caso tenha dúvidas na inserção de campos através dessa rotina, utilize o documento a seguir para apoio:

[Configurador de Layout da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634)

![Imagem 5: Abra o lançamento na Central de Vendas/Compras e preencha os campos "Cód.Cid.Início CT-e' e 'Cód.Cid.Fim CT-e" de…](https://ajuda.sankhya.com.br/hc/article_attachments/16172791947671) Abra o lançamento na Central de Vendas/Compras e preencha os campos **"Cód.Cid.Início CT-e'** e **'Cód.Cid.Fim CT-e"** de acordo com a Cidade Início e Cidade FIM do Conhecimento de Transporte lançado e/ou emitido.

![Imagem 6: Preenchidos tais campos, ao realizar a confirmação a mensagem não será mais apresentada.](https://ajuda.sankhya.com.br/hc/article_attachments/16172808639639) Preenchidos tais campos, ao realizar a confirmação a mensagem não será mais apresentada.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16172791957783) CAUSA:**

Ao tentar confirmar um CT-e nos portais de compras/vendas, utilizando TOP com Modelo 57 - Conhecimento de Transporte Eletrônico, onde as informações Cód.Cid.Início CT-e e Cód.Cid.Fim CT-e não estiverem preenchidas, será retornada a mensagem.
