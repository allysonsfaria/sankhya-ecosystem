---
id: "360044463433"
titulo: "Como manter Natureza, Centro de Resultado e Projeto do financeiro iguais ao cabeçalho da nota"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044463433-Como-manter-Natureza-Centro-de-Resultado-e-Projeto-do-financeiro-iguais-ao-cabe%C3%A7alho-da-nota"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-07-22T15:57:26Z"
rotulos: ["Configuração", "Projeto", "Centro de Resultado", "Nota Fiscal", "Preferências", "Financeiro", "Natureza", "Sincronização de Dados Financeiros"]
---

# Como manter Natureza, Centro de Resultado e Projeto do financeiro iguais ao cabeçalho da nota

**(1)** Quando o parâmetro **"Usar o mesmo CR/Projeto/Natureza da nota? - USACRPROJNATCAB"** estiver habilitado, os campos Projeto, Natureza e Centro de Resultado sempre estarão iguais ao cabeçalho da nota. Alterando qualquer campo, o financeiro será alterado também. Se estiver desabilitado, o sistema não altera os dados desses campos, caso haja uma alteração no cabeçalho da nota.

- Tela **"Preferências"** (Caminho de acesso: Configurações » Avançado)
- Chave **"Usar o mesmo CR/Projeto/Natureza da nota? - USACRPROJNATCAB"**

**(1)** Com o parâmetro acima mencionado desativado, o Centro de Resultado, Natureza e Projeto do Financeiro da Nota serão alimentados com esta informação correspondente, na aba **"Parcelas"** do **"Tipo de Negociação"**. Caso estes campos não estejam preenchidos no Tipo de Negociação, os três campos no Financeiro da Nota serão alimentados com os mesmos informados no Cabeçalho da Nota.

**Informações adicionais sobre os campos Centro Resultado Padrão, Natureza Padrão e Projeto**:

- Se houver Centro Resultado Padrão, Natureza Padrão  e/ou **"Projeto"** informados na parcela, estes serão utilizados; caso contrário, o sistema irá utilizar o **"Centro Resultado**", **"Natureza"** e **"Projeto"** da nota, porém, quando o parâmetro **"Usar o mesmo CR/Projeto/Natureza da nota? - USACRPROJNATCAB"** estiver ativado, os campos Centro Resultado, Projeto e Natureza do cabeçalho da nota que serão considerados na geração do movimento financeiro.
- Além disso, pode-se ainda, informar no parâmetro**"Considerar CR/Proj/Nat da parcela p/tipo de título - CRPRONATPARCTIT"** o Tipo de Título configurado na aba Parcela do Tipo de Negociação do título para a geração e, caso não tenha essa informação, o sistema irá verificar a definição do parâmetro USACRPROJNATCAB.
