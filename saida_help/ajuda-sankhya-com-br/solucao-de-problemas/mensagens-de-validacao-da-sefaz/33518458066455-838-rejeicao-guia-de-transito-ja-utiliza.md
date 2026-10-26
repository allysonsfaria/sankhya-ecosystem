---
id: "33518458066455"
titulo: "838 Rejeição: Guia de trânsito já utilizada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33518458066455-838-Rejei%C3%A7%C3%A3o-Guia-de-tr%C3%A2nsito-j%C3%A1-utilizada"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T14:28:52Z"
rotulos: ["NF-e", "Central de Vendas", "SEFAZ", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Regra de validação", "Guia de trânsito já utilizada", "Número da Guia", "guia de trânsito", "Erro", "838 Rejeição:", "Rejeição 838"]
---

# 838 Rejeição: Guia de trânsito já utilizada

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/33518425207063) **MENSAGEM:**

838 Rejeição: Guia de trânsito já utilizada

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/33518425209623) SOLUÇÃO:**

**(1)** Acesse a tela da **''Central de Vendas''** (Comercial» Rotinas» Central de Vendas), abra a NFe rejeitada e, em seguida, no campo **"Número da Guia"**, informe o número da Guia que não tenha sido utilizado anteriormente;

![Imagem 3: (1) Acesse a tela da ''Central de Vendas'' (Comercial» Rotinas» Central de Vendas), abra a NFe rejeitada e, em seguida,…](https://ajuda.sankhya.com.br/hc/article_attachments/33614516929943)

**Observação:** Em caso de dúvidas sobre qual número de guia utilizar, recomenda-se consultar as informações junto à sua contabilidade.

**(2)** Salve a alteração e gere lote da NFe novamente.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/33518458059031)CAUSA:**

A rejeição ocorre quando há registro de uma Guia de Trânsito que já foi utilizada.

#### Exceções e Considerações

- Será validado o número da guia de trânsito no banco de dados integrado da SEFAZ com o órgão de controle sanitário responsável pela emissão da GTA;
- Essa regra de validação é opcional e pode ser implementada a critério de cada UF;
- Vigor em produção a partir de 01/04/2025, conforme estabelecido na NT 2024.003.

Confira a [Regra de validação](https://www.bing.com/ck/a?!&&p=eeb54c72a95dbdd328bd6d40a64b39f22867f50a37e18f5f3c375e9214f35af4JmltdHM9MTczOTQwNDgwMA&ptn=3&ver=2&hsh=4&fclid=1d04a6cb-f11f-6e81-2bb8-b3e1f0336f71&psq=NT+2024.003&u=a1aHR0cHM6Ly93d3cubmZlLmZhemVuZGEuZ292LmJyL3BvcnRhbC9leGliaXJBcnF1aXZvLmFzcHg_Y29udGV1ZG89ZE1pTVpRaWwlMjBCOD0&ntb=1) da SEFAZ:

![Imagem 5: Confira a Regra de validação da SEFAZ:](https://downloads.intercomcdn.com/i/o/iirbswk2/1378854956/2805b63011d2dde7cddecd741463/image.png?expires=1752699600&signature=9d0eb51c496b0cf09f9f287b848ba347c4b6e200ce55fdee4aa08b13a47b8057&req=dSMgHsF7mYhaX%2FMW1HO4zftcHl0KDrCuRofcFrGTMu8czL2C0QCLxFD9vsN8%0A0naU%0A)
