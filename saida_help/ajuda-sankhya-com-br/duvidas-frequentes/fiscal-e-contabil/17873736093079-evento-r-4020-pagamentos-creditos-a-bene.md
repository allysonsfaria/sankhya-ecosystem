---
id: "17873736093079"
titulo: "Evento R-4020 - Pagamentos/Créditos a Beneficiário Pessoa Jurídica"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/17873736093079-Evento-R-4020-Pagamentos-Cr%C3%A9ditos-a-Benefici%C3%A1rio-Pessoa-Jur%C3%ADdica"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-08-07T13:22:28Z"
rotulos: ["Configuração", "Eventos", "Movimentação Financeira", "Impostos", "EFD"]
---

# Evento R-4020 - Pagamentos/Créditos a Beneficiário Pessoa Jurídica

(1)** Configurar imposto, para que seja levado ao campo de valor agregado do R-4020:**

![Imagem 1: Caso deseja informar os valores de impostos agregados (PIS, Cofins e CSLL) em um único lançamento de imposto no item da…](https://ajuda.sankhya.com.br/hc/article_attachments/17962083523735) Caso deseja informar os valores de impostos agregados (PIS, Cofins e CSLL) em um único lançamento de imposto no item da nota. Acesse:

- Tela: Impostos - campo 'tipo imposto' deverá ser selecionado a opção: 'Outros';
- Na grade de exceções, o campo 'Cód.Receita' deverá ser igual ao código DARF informado no cadastro da empresa.
- Após realizar os passos acima, o sistema vinculará o imposto configurado ao item da nota, e na geração do R-4020 esse valor irá alimentar os campos "valor total base agregado" e "valor agregado"

(1)** Configurações necessárias para geração dos eventos do R-4020**

![Imagem 2: Para que o sistema puxe as notas para o R-4020, elas precisam:](https://ajuda.sankhya.com.br/hc/article_attachments/17962083523735) Para que o sistema puxe as notas para o R-4020, elas precisam:

- Ser do tipo de Compra;
- Estar aprovada;
- O parceiro ser CNPJ;
- O cadastro da TOP tem que estar com a informação abaixo marcada:

![Imagem 3: O cadastro da TOP tem que estar com a informação abaixo marcada:](https://ajuda.sankhya.com.br/hc/article_attachments/17962083533463)

- Precisa ter os impostos retidos e todos terem o vinculo com um código de Natureza de rendimento.

![Imagem 4: Quando se tratar de lançamentos diretamente na movimentação financeira, siga os passos abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/17962083537175)
 
![Imagem 5: Quando se tratar de lançamentos diretamente na movimentação financeira, siga os passos abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/17962039320215) Quando se tratar de lançamentos diretamente na movimentação financeira, siga os passos abaixo:

- O lançamento não pode ter vinculo com uma nota, o campo abaixo deve estar vazio:

![Imagem 6: O lançamento não pode ter vinculo com uma nota, o campo abaixo deve estar vazio:](https://ajuda.sankhya.com.br/hc/article_attachments/17962039330455)

- Deverá ser informado um 'código natureza de rendimento', na aba EFD-REIINF:

![Imagem 7: Deverá ser informado um 'código natureza de rendimento', na aba EFD-REIINF:](https://ajuda.sankhya.com.br/hc/article_attachments/17962039340055)

- É necessário ter um imposto de renda retido, em 'outros impostos':

![Imagem 8: É necessário ter um imposto de renda retido, em 'outros impostos':](https://ajuda.sankhya.com.br/hc/article_attachments/17962039346071)

- O cadastro da TOP deverá estar com a opção 'Gerar informações do EFD Reinf Grupo 4000'.

![Imagem 9: Ao finalizar as configurações, as notas e financeiro serão levados corretamente.](https://ajuda.sankhya.com.br/hc/article_attachments/17962039360279) Ao finalizar as configurações,  as notas e financeiro serão levados corretamente.

![Imagem 10: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17962039369367) **OBSERVAÇÃO:**

[Configurações para geração dos eventos do REINF Grupo 4000](https://ajuda.sankhya.com.br/hc/pt-br/articles/11814510069271)
