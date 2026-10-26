---
id: "360053292233"
titulo: "Nota de Serviço não está sendo gerada no livro de ISS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360053292233-Nota-de-Servi%C3%A7o-n%C3%A3o-est%C3%A1-sendo-gerada-no-livro-de-ISS"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T15:29:14Z"
rotulos: ["ISS", "Configuração", "Alíquota de ISS", "Impostos", "TOP", "NFS-e", "Falta de \"Cód. Tributação ISS\" impede geração no livro de ISS", "Preencha campo automaticamente em serviço ou alíquotas de ISS", "Verifique \"Atualização livros de ISS\" no Tipo de Operação."]
---

# Nota de Serviço não está sendo gerada no livro de ISS

Esse é um dos questionamentos frequentes, que na grande maioria das vezes o motivo é a falta do "Cód. Tributação ISS:"  no serviço na grade itens da central dessa nota:

- Para notas de emissão própria, se detectada a ausência dessa informação, não são possíveis ajustes após aprovação. Nesse caso entre em contato com o Service Desk para avaliação do caso.
- Já para notas de terceiros, é possível editar essa informação na grade de itens, conforme abaixo:

![Imagem 1: Já para notas de terceiros, é possível editar essa informação na grade de itens, conforme abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/15917357625367)

O preenchimento automático desse campo pode ocorrer de duas formas no sistema:

![Imagem 2: Esse preenchimento pode ser automático a partir da configuração no serviço ( Configurações » Cadastros » Produtos »…](https://ajuda.sankhya.com.br/hc/article_attachments/15917381883415) Esse preenchimento pode ser automático a partir da configuração no serviço (Configurações » Cadastros » Produtos » Serviço) na Aba **'Alíquotas de ISS**':

![Imagem 3: Esse preenchimento pode ser automático a partir da configuração no serviço ( Configurações » Cadastros » Produtos »…](https://ajuda.sankhya.com.br/hc/article_attachments/15917355129879)

![Imagem 4: 0u ainda direto no cadastro de Alíquotas de ISS ( Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ISS )](https://ajuda.sankhya.com.br/hc/article_attachments/15917381889303) 0u ainda direto no cadastro de Alíquotas de ISS (Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ISS)

- Mesmo para os serviços que forem isentos ou não forem tributados é necessário acessar a tela Alíquotas de ISS(Comercial » Arquivo » Cadastros » Alíquotas » Alíquotas de ISS) e informar o Cód.Tributação correspondente, dentre as opções abaixo:

00 - Tributado
01 - Tributado com ISS Retido
06 - Isento
07 - Não Tributado

![Imagem 5: Importante:](https://ajuda.sankhya.com.br/hc/article_attachments/30060139259927)**Importante:**

Além da verificação acima, é importante que o Tipo de Operação utilizado possua em seu cadastro, na aba 'Livros Fiscais', o campo **'Atualização livros de ISS' diferente de 'Não atualiza'**.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/15917372944407) CAUSA:**

Isso pode ocorrer devido o campo **"Cód. Tributação ISS**" na grade itens estar vazio.

Não é possível gerar para um livro fiscal de ISS, uma nota de serviço sem informar qual é o código da situação tributária deste serviço.
