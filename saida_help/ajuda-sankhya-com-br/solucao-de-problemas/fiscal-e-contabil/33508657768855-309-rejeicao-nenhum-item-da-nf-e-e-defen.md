---
id: "33508657768855"
titulo: "309 Rejeição: Nenhum item da NF-e é defensivo agrícola e informada receita de agrotóxico"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33508657768855-309-Rejei%C3%A7%C3%A3o-Nenhum-item-da-NF-e-%C3%A9-defensivo-agr%C3%ADcola-e-informada-receita-de-agrot%C3%B3xico"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:29:00Z"
rotulos: ["Produtos", "Configuração", "Fiscal", "NF-e", "SEFAZ", "Impostos", "NCM", "Cadastro de Produtos", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Nenhum item da NF-e é defensivo agrícola", "e informada receita de agrotóxico", "Regra de validação", "309 Rejeição", "Rejeição 309"]
---

# 309 Rejeição: Nenhum item da NF-e é defensivo agrícola e informada receita de agrotóxico

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/33508674334359) **MENSAGEM:**

309 Rejeição: Nenhum item da NF-e é defensivo agrícola e informada receita de agrotóxico.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/33508674336151) SOLUÇÃO:**

Para a correção da rejeição, é imprescindível validar as informações referentes ao **NCM** do produto:

**(1)** Acesse a tela **''Cadastro de Produtos''** (Configurações > Cadastros> Cadastro de Produtos) na aba **''Impostos''** e verifique o campo ''**NCM''.**

![Imagem 3: (1) Acesse a tela ''Cadastro de Produtos'' (Configurações > Cadastros> Cadastro de Produtos) na aba ''Impostos'' e…](https://ajuda.sankhya.com.br/hc/article_attachments/33566461390871)

**(1)** Valide as seguintes condições:

- Se o NCM estiver incorreto e realmente precisar ser classificado como defensivo agrícola;
- Se o NCM estiver correto e a operação não exigir a inclusão de dados relacionados a defensivos agrícolas.

**(1)** Após a devida atualização no cadastro do NCM, retorne à NFe gerada e tente gerar o lote novamente.

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/33508657763479)CAUSA:**

Esta rejeição ocorre quando há informações relativas a receituário ou receita de agrotóxicos, mas nenhum dos itens da Nota Fiscal Eletrônica (NF-e) apresenta NCMs que correspondam a defensivos agrícolas.

#### Exceção e Considerações:

- Essa regra de validação é opcional e pode ser adotada conforme a escolha de cada UF;
- O início da produção está programado para o dia 01 de abril de 2025, conforme estipulado na NT 2024.003;

Confira a [Regra de validação](https://www.bing.com/ck/a?!&&p=eeb54c72a95dbdd328bd6d40a64b39f22867f50a37e18f5f3c375e9214f35af4JmltdHM9MTczOTQwNDgwMA&ptn=3&ver=2&hsh=4&fclid=1d04a6cb-f11f-6e81-2bb8-b3e1f0336f71&psq=NT+2024.003&u=a1aHR0cHM6Ly93d3cubmZlLmZhemVuZGEuZ292LmJyL3BvcnRhbC9leGliaXJBcnF1aXZvLmFzcHg_Y29udGV1ZG89ZE1pTVpRaWwlMjBCOD0&ntb=1) da SEFAZ:

![Imagem 5: Confira a Regra de validação da SEFAZ:](https://downloads.intercomcdn.com/i/o/iirbswk2/1378740445/7a9acf4a278d657848fa29e9dc23/image.png?expires=1752680700&signature=3d3931f8e293817036085f7b55968eafc4fd61ac5b3847f7a7f2dbb8ecaf71f9&req=dSMgHs56nYVbXPMW1HO4zUuGxTpOxt1rGDnpN%2BriZptgK1Ci3UgSQM%2B7yfVa%0ATZQQ%0A)
