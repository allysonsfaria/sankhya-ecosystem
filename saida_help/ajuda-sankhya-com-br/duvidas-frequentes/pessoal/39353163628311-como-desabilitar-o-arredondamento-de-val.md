---
id: "39353163628311"
titulo: "Como Desabilitar o Arredondamento de Valores na Folha de Pagamento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39353163628311-Como-Desabilitar-o-Arredondamento-de-Valores-na-Folha-de-Pagamento"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-07-29T13:28:51Z"
rotulos: ["Configuração", "Financeiro", "Folha de Pagamento", "Artigo criado KCS", "Sankhya RH - KCS", "Arredondamento", "Arquivo Bancário"]
---

# Como Desabilitar o Arredondamento de Valores na Folha de Pagamento

O arredondamento de valores na folha de pagamento é uma funcionalidade que ajusta automaticamente os centavos do salário líquido dos colaboradores. No entanto, quando os pagamentos são realizados por **"arquivo bancário"**, essa funcionalidade pode se tornar desnecessária, pois os valores precisam corresponder exatamente aos centavos calculados.

Este artigo orienta como desabilitar o arredondamento na folha de pagamento, garantindo que os valores sejam processados sem ajustes automáticos de centavos.

### Quando Desabilitar o Arredondamento

A desabilitação do arredondamento é recomendada nas seguintes situações:

- Os pagamentos são realizados exclusivamente por **"arquivo bancário"**.
- É necessário manter a precisão exata dos centavos calculados.
- O arredondamento está causando divergências entre o valor calculado e o valor pago.
- A empresa não utiliza pagamentos em dinheiro ou cheque que necessitem arredondamento.

### Como Desabilitar o Arredondamento na Folha Mensal

Para eliminar o arredondamento dos valores na folha mensal, siga os passos abaixo:

**(1)** Acesse a tela **"Regras de Cálculo"** (Pessoal+ » Cadastros » Regras de Cálculo).

**(2)** Localize o campo **"Arredondamento Salário Líquido"** na tela.

![Imagem 1: Altere o valor do campo para "0" , eliminando assim qualquer arredondamento. Clique no "Botão Salvar" para aplicar as…](https://ajuda.sankhya.com.br/hc/article_attachments/41273707685911)

**(3)** Altere o valor do campo para **"0"**, eliminando assim qualquer arredondamento.

**(4)** Clique no **"Botão Salvar"** para aplicar as alterações realizadas na tela.

Após realizar esse ajuste, a folha mensal será calculada sem arredondamento, mantendo os centavos exatos do cálculo.

### Observações Importantes

**Limitação do arredondamento:** O sistema não consegue lançar um provento negativo nem um desconto negativo. Portanto, não é possível configurar arredondamentos para baixo em determinados cenários, como no adiantamento salarial.

**Personalização avançada:** Caso seja necessário criar regras específicas de arredondamento (como arredondar para baixo em determinadas situações), será preciso criar um evento personalizado de desconto com condições específicas. Essa customização deve ser realizada pela equipe técnica da empresa, pois o **"Service Desk"** não atua com personalizações.

**Validação após alterações:** Sempre realize um cálculo de teste após desabilitar ou modificar as configurações de arredondamento para garantir que os valores estejam sendo processados conforme esperado.
