---
id: "33517587703575"
titulo: "312 Rejeição: Informação Indevida de Guia de Trânsito Vegetal"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33517587703575-312-Rejei%C3%A7%C3%A3o-Informa%C3%A7%C3%A3o-Indevida-de-Guia-de-Tr%C3%A2nsito-Vegetal"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:28:54Z"
rotulos: ["Produtos", "Configuração", "NF-e", "SEFAZ", "Impostos", "NCM", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Regra de validação", "Informação Indevida", "Guia de Trânsito Vegetal", "Rejeição 312", "312 Rejeição"]
---

# 312 Rejeição: Informação Indevida de Guia de Trânsito Vegetal

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/33517587693207) **MENSAGEM:**

312 Rejeição: Informação Indevida de Guia de Trânsito Vegetal

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/33517587694743) SOLUÇÃO:**

Para a correção da rejeição, é imprescindível validar as informações referentes ao NCM do produto:

**(1)** Acesse a tela de **''Cadastro de Produtos''** (Configurações» Cadastros» Produtos» Cadastro de Produtos) na aba **''Impostos''** e verifique o campo ''**NCM''**;

![Imagem 3: (1) Acesse a tela de ''Cadastro de Produtos'' (Configurações» Cadastros» Produtos» Cadastro de Produtos) na aba…](https://ajuda.sankhya.com.br/hc/article_attachments/33569711754007)

**(2)** Valide as seguintes condições:

- Se o NCM estiver incorreto e realmente precisar ser classificado como Produto Vegetal;
- Caso o NCM esteja correto, a operação não deve incluir dados da Guia de Trânsito.

**(3)** Retorne a NFe gerada e tente gerar o lote novamente.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/33517587697431) CAUSA:**

Essa rejeição ocorre quando há informações relacionadas à Guia de Trânsito Vegetal, mas nenhum dos itens da Nota Fiscal Eletrônica (NF-e) apresenta NCMs correspondentes a Produtos Vegetais.

#### Exceções e Observações:

- Esta regra de validação é opcional e pode ser implementada conforme a conveniência de cada Unidade da Federação (UF);
- Vigor em produção a partir de 01/04/2025, conforme estabelecido na NT 2024.003.

Confira a [Regra de validação](https://www.bing.com/ck/a?!&&p=eeb54c72a95dbdd328bd6d40a64b39f22867f50a37e18f5f3c375e9214f35af4JmltdHM9MTczOTQwNDgwMA&ptn=3&ver=2&hsh=4&fclid=1d04a6cb-f11f-6e81-2bb8-b3e1f0336f71&psq=NT+2024.003&u=a1aHR0cHM6Ly93d3cubmZlLmZhemVuZGEuZ292LmJyL3BvcnRhbC9leGliaXJBcnF1aXZvLmFzcHg_Y29udGV1ZG89ZE1pTVpRaWwlMjBCOD0&ntb=1) da SEFAZ:

![Imagem 5: Confira a Regra de validação da SEFAZ:](https://downloads.intercomcdn.com/i/o/iirbswk2/1378830674/15882bf1b074e66a25a069d96ce5/image.png?expires=1752698700&signature=3f7e4dbcbe43ca733f51314d0ba58d7cc4dd67df3dca21986972ac967707f22a&req=dSMgHsF9nYdYXfMW1HO4zUYPsq2z7aw6RdEnIKkZRuDDVCPdeR6mui90BlW%2B%0ANiWy%0A)
