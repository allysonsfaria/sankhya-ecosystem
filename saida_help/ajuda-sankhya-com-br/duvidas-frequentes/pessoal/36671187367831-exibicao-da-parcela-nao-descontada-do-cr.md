---
id: "36671187367831"
titulo: "Exibição da Parcela Não Descontada do Crédito do Trabalhador no Holerite e na TRCT"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36671187367831-Exibi%C3%A7%C3%A3o-da-Parcela-N%C3%A3o-Descontada-do-Cr%C3%A9dito-do-Trabalhador-no-Holerite-e-na-TRCT"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-08-27T18:34:39Z"
rotulos: ["Configuração", "Preferências", "Folha de Pagamento", "Regras de Cálculo", "Crédito do Trabalhador", "TRCT", "Parcela Não Descontada", "Holerite mensal", "FPRELATHOLERITE", "Holerite", "Crédito Consignado"]
---

# Exibição da Parcela Não Descontada do Crédito do Trabalhador no Holerite e na TRCT

A **parcela não descontada** do crédito do trabalhador corresponde ao valor de empréstimos consignados que não pôde ser abatido da remuneração do empregador por **falta de saldo**, **afastamento** ou **rescisão contratual**.

Essa informação deve aparecer tanto no **holerite mensal** quanto na **TRCT (Termo de Rescisão do Contrato de Trabalho),** garantindo transparência e evitando divergências.

## Procedimento:

### 1. Holerite Mensal

Para que o holerite exiba corretamente essa parcela não descontada, siga os passos:

**(1)** Acesse a tela [**''Preferências''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias) (Configurações » Avançado » Preferências).

**(2)** No campo **''Chave ou descrição''**, pesquise pelo parâmetro **''FPRELATHOLERITE'' - Holerite Mensal''**.

**(3)** No campo **''Inteiro''** preencha os parâmetros com **0** ou deixe em **branco**.

### 2. TRCT (Termo de Rescisão do Contrato de Trabalho)

A TRCT deve mostrar a parcela não descontada para registrar o saldo pendente do crédito consignado e garantir transparência no desligamento.

#### Como ajustar:

**(1)** Acesse a tela ''Preferências'' (Configurações » Avançado » Preferências).

**(2)** No campo ''Chave ou descrição'', busque separadamente pelos seguintes parâmetros:

- **FPRELATHOLRESC**
- **FPRELATQUIRESC**
- **FPRELATRESCISAO**

**(3)** Nos três parâmetros, no campo ''Inteiro'' preencha os parâmetros com **0** ou deixe em **branco**.

**(4)** Em seguida, acesse a tela [**''Regras de Cálculo''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405310442007-Regras-de-C%C3%A1lculo) (Pessoal+ » Cadastros » Regras de Cálculo).

**(5)** Na aba **''TRCT''** sub-aba **''Eventos'',** associe o **evento da parcela não descontada** ao campo correspondente da TRCT.

- Essa configuração é necessária para que o sistema saiba **qual valor deve ser exibido na TRCT**.
- Mesmo com os parâmetros corretos de ''Preferências'', sem essa associação o evento não aparecerá no documento.
