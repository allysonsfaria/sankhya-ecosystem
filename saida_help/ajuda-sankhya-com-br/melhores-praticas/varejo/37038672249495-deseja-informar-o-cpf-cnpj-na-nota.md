---
id: "37038672249495"
titulo: "Deseja informar o CPF/CNPJ na nota?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37038672249495-Deseja-informar-o-CPF-CNPJ-na-nota"
trilha: "Melhores Práticas > Varejo"
atualizado_em: "2026-07-22T14:21:56Z"
rotulos: ["Configuração", "Fiscal", "Parceiro", "NF-e", "Preferências", "NFC-e", "CPF/CNPJ", "CPF/CNPJ na Nota", "Pop up", "Configurador do Layout da Nota", "Chave ou descrição", "Nota Fiscal Eletrônica (NFe) – Modelo 55"]
---

# Deseja informar o CPF/CNPJ na nota?

O sistema permite que o caixa decida, no momento da venda, se deseja ou não informar o **CPF/CNPJ do cliente**, por meio da exibição de um **pop-up** antes da finalização da transação.

Para que esse comportamento seja exibido corretamente, é necessário realizar as configurações descritas abaixo.

![Imagem 1: Para que esse comportamento seja exibido corretamente, é necessário realizar as configurações descritas abaixo.](https://ajuda.sankhya.com.br/hc/article_attachments/37038672220823)

#### Procedimento:

**(1)** Acesse a tela [**''Preferências''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601834-Prefer%C3%AAncias) (Configurações » Avançado » Preferências).

**(2)** No campo **''Chave ou descrição''** busque pelos parâmetros abaixo e verifique as configurações:

**EXIGECPFCNPJVLR**: deve estar **vazio**

**UFCAPTURACPF**: deve estar **preenchido com a UF (estado) da empresa**

- O parceiro utilizado nas vendas de balcão ou no PDV Web deve estar configurado corretamente.

**(3)** Em seguida, acesse a tela [**''Configurador do Layout da Nota''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Configurador-de-Layout-da-Nota) (Comercial » Configuração » Configurador de Layout da Nota).

**(4)** Habilite o campo para permitir a inserção do CPF/CNPJ após a exibição do pop-up.

**ATENÇÃO:** A partir de 2026, com a implementação da Reforma Tributária, as regras fiscais não permitirão a emissão de Nota Fiscal de Consumidor Eletrônica (NFC-e) para adquirentes identificados com CNPJ. A NFC-e será destinada exclusivamente ao consumidor final.

Se o cliente exigir a nota com CNPJ, será necessário emitir a **Nota Fiscal Eletrônica (NFe) – Modelo 55**.
