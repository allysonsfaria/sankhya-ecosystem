---
id: "29442291383575"
titulo: "EFD Contribuições - Conta contábil para Filiais"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/29442291383575-EFD-Contribui%C3%A7%C3%B5es-Conta-cont%C3%A1bil-para-Filiais"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:37:05Z"
rotulos: ["Configuração", "Fiscal", "Filial", "Impostos", "Contabilidade", "EFD Contribuições"]
---

# EFD Contribuições - Conta contábil para Filiais

Durante a geração do EFD - Contribuições, conforme as regras de alguns registros, temos a obrigatoriedade de gerar a informação da Conta Contábil, que recebe os efeitos contábeis daquele movimento.

Hoje no SankhyaOm, temos a possibilidade de geração da geração dessa informação, porém, como esta geração é consolidada na empresa matriz, as filiais acabam não apresentando suas próprias declarações.

Temos como obrigação Fiscal, a apresentação do registro **F100**, para:

- Receitas recebidas sobre Juros e Multas;
- Descontos recebidos sobre despesas;

Vejamos na imagem a seguir, onde ficam essas configurações na aplicação:

Tela **Empresa** (Comercial > Preferências > Empresa)

![Imagem 1: Tela Empresa (Comercial > Preferências > Empresa)](https://ajuda.sankhya.com.br/hc/article_attachments/29557265144343)

**Quando estamos gerando esta obrigação acessória, as FILIAIS devem receber essas configurações, e NÃO as deixando apenas para a empresa MATRIZ, que é quem gera de fato o arquivo .txt que consolida todas as informações.**

Caso não seja realizada essa configuração em cada filial, ao gerar o arquivo, as movimentações das filiais, não terão as contas contábeis destes movimentos, no registro F100, geradas, causando erros de validação no programa validador da receita PVA.
