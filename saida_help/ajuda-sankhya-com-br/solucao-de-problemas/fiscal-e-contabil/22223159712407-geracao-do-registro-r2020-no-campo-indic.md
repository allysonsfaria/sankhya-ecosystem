---
id: "22223159712407"
titulo: "Geração do registro R2020 no campo \"Indicativo de prestação de serviço em obra\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/22223159712407-Gera%C3%A7%C3%A3o-do-registro-R2020-no-campo-Indicativo-de-presta%C3%A7%C3%A3o-de-servi%C3%A7o-em-obra"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:49:34Z"
rotulos: ["Configuração", "Fiscal", "Impostos", "Reinf"]
---

# Geração do registro R2020 no campo "Indicativo de prestação de serviço em obra"

**SOLUÇÃO**

Para garantir a geração correta do **REINF R2020** com o campo **"Indicativo de prestação de serviço em obra"** = 0 (Não é obra de construção civil), siga os passos abaixo:

**(1)**  Acesse o cabeçalho da nota fiscal e verifique o campo **"CNO"**. Este campo deve estar em branco.

![Imagem 1: (1) Acesse o cabeçalho da nota fiscal e verifique o campo "CNO" . Este campo deve estar em branco.](https://ajuda.sankhya.com.br/hc/article_attachments/22235872167447)

 **(2)**  Acesse o cadastro de **"Serviços"** (Configurações » Cadastros » Produtos » Serviço) e localize o serviço utilizado na nota fiscal.

**(3)**  Verifique o campo **"Obra de Construção Civil"**. Certifique-se de que este campo esteja sem nenhuma opção selecionada.

![Imagem 2: (3) Verifique o campo "Obra de Construção Civil" . Certifique-se de que este campo esteja sem nenhuma opção selecionada.](https://ajuda.sankhya.com.br/hc/article_attachments/22235855624471)

**Observação importante:** Se algum dos dois campos (CNO no cabeçalho da nota ou "Obra de Construção Civil" no cadastro de Serviços) estiver preenchido, o sistema sempre utilizará a informação do campo **"Obra de Construção Civil"** do cadastro de **"Serviços"** como **"Indicativo de prestação de serviço em obra"**.

Para garantir a correta validação do documento, o campo **"Cód. da Obra"** no pedido/nota deve ser preenchido obrigatoriamente com o **CNO** (Cadastro Nacional de Obras). Atente-se aos seguintes pontos:

- O código CNO é composto por **12 dígitos**;
- O fornecimento deste número é de inteira responsabilidade do cliente, seja ele o Dono da Obra ou a Construtora contratante;
- Caso a Nota Fiscal de Serviço seja recusada ou rejeitada devido à obrigatoriedade deste código, oriente o cliente a realizar o cadastro e obter o número através do **Portal e-CAC**.
