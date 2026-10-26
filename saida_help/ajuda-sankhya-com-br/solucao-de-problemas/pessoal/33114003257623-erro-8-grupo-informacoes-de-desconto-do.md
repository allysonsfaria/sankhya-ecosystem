---
id: "33114003257623"
titulo: "Erro 8 - Grupo 'Informações de desconto do empréstimo em folha' deve ser preenchido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33114003257623-Erro-8-Grupo-Informa%C3%A7%C3%B5es-de-desconto-do-empr%C3%A9stimo-em-folha-deve-ser-preenchido"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:20:09Z"
rotulos: ["eSocial", "Folha de Pagamento", "Erro", "Desligamento", "Artigo atualizado KCS", "Sankhya RH - KCS", "Remuneração", "Crédito Trabalhador"]
---

# Erro 8 - Grupo 'Informações de desconto do empréstimo em folha' deve ser preenchido

**SITUAÇÃO:**

Ao tentar enviar o evento S-2299 Desligamento ou S-1200 Remuneração, é apresentada a seguinte mensagem de erro: Erro 8 - Grupo 'Informações de desconto do empréstimo em folha' deve ser preenchido. 

**CAUSA:**

Esse erro ocorre quando o colaborador possui o evento de Desconto do Crédito Trabalhador calculado com a natureza de rubrica 9253, mas não levou as informações cadastradas da instituição financeira e número do contrato associadas a esse crédito.
 

**SOLUÇÃO:**

**(1)** Identifique o evento na folha do colaborador que corresponde ao Desconto do Crédito Trabalhador.

**(2)** Verifique se o lançamento desse evento contém as seguintes informações obrigatórias de acordo com os dados informados no arquivo retirado pelo [Portal Emprega Brasil](https://servicos.mte.gov.br/spme-v2/#/login): 

- Valor da Parcela do desconto crédito do trabalhador;
- Número do contrato;
- Código da instituição financeira.

Caso as informações estejam corretas será necessário reprocessar o Crédito do Trabalhador para isso basta seguir o passo a passo do artigo [**Reprocessamento do Crédito do Trabalhador**](https://ajuda.sankhya.com.br/hc/pt-br/articles/36386300103063-Reprocessamento-do-Cr%C3%A9dito-do-Trabalhador).

### Atenção:

O **erro também ocorre devido à edição manual do valor do desconto do empréstimo na folha de pagamento**. Uma vez que o sistema realiza o cálculo do desconto com base na seguinte regra:

- O valor do **desconto não pode ultrapassar 35% da remuneração disponível**, ou seja, da base margem de Crédito do Trabalhador (Base Margem Créd. Trab.).
- Quando o valor da parcela está dentro desse limite (até 35%), o desconto aplicado será igual ao valor da parcela. **Porém, ao ajustar manualmente** **para um valor superior ao permitido, o sistema não reconhece essa informação e, consequentemente, não o envia ao eSocial.**
