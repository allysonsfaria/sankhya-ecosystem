---
id: "33517227869591"
titulo: "310 Rejeição: Informação indevida de Guia de Trânsito Animal"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33517227869591-310-Rejei%C3%A7%C3%A3o-Informa%C3%A7%C3%A3o-indevida-de-Guia-de-Tr%C3%A2nsito-Animal"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:28:56Z"
rotulos: ["Produtos", "Configuração", "NF-e", "SEFAZ", "Impostos", "NCM", "Cadastro de Produtos", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Regra de validação", "Informação indevida de Guia de Trânsito Animal", "Rejeição 310", "Erro", "310 Rejeição"]
---

# 310 Rejeição: Informação indevida de Guia de Trânsito Animal

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/33517257196951) **MENSAGEM:**

310 Rejeição: Informação indevida de Guia de Trânsito Animal

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/33517257198743) SOLUÇÃO:**

Para a correção da rejeição, é imprescindível validar as informações referentes ao NCM do produto.

**(1)** Acesse a tela de **''Cadastro de Produtos''** (Configurações» Cadastros» Produtos» Cadastro de Produtos) na aba **''Impostos''** e verifique o campo ''**NCM''**;

![Imagem 3: (1) Acesse a tela de ''Cadastro de Produtos'' (Configurações» Cadastros» Produtos» Cadastro de Produtos) na aba…](https://ajuda.sankhya.com.br/hc/article_attachments/33568588631703)

**(2)** Valide as seguintes condições:

- Se o NCM estiver incorreto e realmente precisar ser classificado como Animal Vivo;
- Se o NCM estiver correto e a operação não exigir a inclusão de dados da Guia de Trânsito.

**(3)** Após a atualização do cadastro do NCM, retorne à Nota Fiscal Eletrônica gerada e tente gerar o lote novamente.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/33517227864983) CAUSA:**

Esta rejeição ocorre quando há informações referentes à Guia de Trânsito Animal, mas nenhum dos itens da Nota Fiscal Eletrônica (NF-e) apresenta NCMs correspondentes a Animais Vivos.

#### Exceção e Considerações:

- Essa regra de validação é opcional e pode ser implementada a critério de cada UF;
- Vigor em produção a partir de 01/04/2025, conforme estabelecido na NT 2024.003.

Confira a [Regra de validação](https://www.bing.com/ck/a?!&&p=eeb54c72a95dbdd328bd6d40a64b39f22867f50a37e18f5f3c375e9214f35af4JmltdHM9MTczOTQwNDgwMA&ptn=3&ver=2&hsh=4&fclid=1d04a6cb-f11f-6e81-2bb8-b3e1f0336f71&psq=NT+2024.003&u=a1aHR0cHM6Ly93d3cubmZlLmZhemVuZGEuZ292LmJyL3BvcnRhbC9leGliaXJBcnF1aXZvLmFzcHg_Y29udGV1ZG89ZE1pTVpRaWwlMjBCOD0&ntb=1) da SEFAZ:

![Imagem 5: Confira a Regra de validação da SEFAZ:](https://downloads.intercomcdn.com/i/o/iirbswk2/1378809392/63a2426a9d62e4f24c4785de9bfd/image.png?expires=1752697800&signature=f0a30daf6b16c4359e8acca92d455e2368ea7c9753b21082fb90a97db62cd81e&req=dSMgHsF%2BlIJWW%2FMW1HO4zbiZIbHsCFEjaATY4bF7HrnA0bVdNxDoX97NZJUs%0A83ZH%0A)
