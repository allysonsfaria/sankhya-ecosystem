---
id: "360044512913"
titulo: "Como proceder quando o Registro R2010 (EFD-REINF)- Para Movimentos Financeiro não esta sendo gerado?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044512913-Como-proceder-quando-o-Registro-R2010-EFD-REINF-Para-Movimentos-Financeiro-n%C3%A3o-esta-sendo-gerado"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T15:56:22Z"
rotulos: ["#RevisadoJR", "reinf", "nota de serviço", "serviço", "não gera", "Configuração", "Movimentação Financeira", "Impostos", "Financeiro", "Registro R2010 - Para Movimentos Financeiro não esta sendo gerado", "Preencha a classificação de Cessão de Mão de Obra", "Configure o tipo de movimento nos Tipos de Operação", "EFD-REINF", "R2010"]
---

# Como proceder quando o Registro R2010 (EFD-REINF)- Para Movimentos Financeiro não esta sendo gerado?

**(1)** O evento R2010-Retenção Contribuição Serviços Tomados não é gerado quando uma das configurações informadas abaixo não estão devidamente configuradas.

![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16817039710231) **SOLUÇÃO:**

Para correção, siga as orientações:

![Imagem 2: Acesse: Comercial » Preferências » Empresa](https://ajuda.sankhya.com.br/hc/article_attachments/16817039716631) Acesse: Comercial » Preferências » Empresa

Aba **"Propriedades"**, Campo **"Ativo"** (a empresa deve estar ativa)

Aba **"EFD-Reinf"**, sub-aba **"Eventos periódicos"**, campo **"Gerar Evento"**: marque para o evento R2010

![Imagem 3: Acesse: Financeiro » Rotinas » Movimentação Financeira](https://ajuda.sankhya.com.br/hc/article_attachments/16817039722007)  Acesse: Financeiro » Rotinas » Movimentação Financeira

Aba **"Outras Informações",** campo **"Classificação Cessão M.d.Obra":** preencha devidamente

![Imagem 4: Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/article_attachments/16817039733783)  Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP

Aba **"Geral",** campo **"Tipo de movimento"**: I-Financeiro (A Top utilizada no Mov. Financeiro, deve ser do tipo I-Financeiro)

Aba **"Livro Fiscal"**, campo **"Atualização livros de ISS"**:  Aquisições

![Imagem 5: Acesse: Configurações » Cadastros » Parceiros](https://ajuda.sankhya.com.br/hc/article_attachments/16817002781975) Acesse: Configurações » Cadastros » Parceiros

Aba **"Identificação"**, campo **"CNPJ / CPF"**: insira um CNPJ válido

![Imagem 6: Possuir INSS calculado a uma alíquota de 3.5% ou 11%, via "Outros Impostos" com "Tipo Imposto" igual a "Retido" , ou…](https://ajuda.sankhya.com.br/hc/article_attachments/16817002783895) Possuir INSS calculado a uma alíquota de 3.5% ou 11%, via **"Outros Impostos"** com **"Tipo Imposto"** igual a **"Retido"**, ou com Tipo Imposto igual a **"Incluso"** e o parâmetro **"GERIMPINCREINF"** ativo;

**(1)** Seguem recomendações quanto a configuração para o calculo via Outros Impostos:

a) Configurações » Cadastros » Impostos

Crie um imposto com Tipo Imposto igual a 'INSS';
Alíquota igual a 3,5% ou 11%;
Abas: **"Parceiro", "TOP", "Empresa"**;
Configure os campos **"Alíquota", "Red. Base"** e **"Financeiro Origem Financeiro";**

b) Financeiro » Rotinas » Movimentação Financeira

Botão: Outras Opções > Outros Impostos
 -Inclua o Outro Imposto com o campo Tipo Imposto igual a Retido;
OU
 -Inclua o Outro Imposto com o campo Tipo Imposto igual a Incluso e ative o parâmetro Gera Impostos inclusos no EFD-Reinf? chave GERIMPINCREINF;

![Imagem 7: NOTA: caso seja necessário a ativação do parâmetro Gera Impostos inclusos no EFD-Reinf? chave GERIMPINCREINF , acesse o…](https://ajuda.sankhya.com.br/hc/article_attachments/16817002785943) **NOTA:** caso seja necessário a ativação do parâmetro Gera Impostos inclusos no EFD-Reinf? chave GERIMPINCREINF, acesse o menu 'Configurações » Avançado » Preferências' e faça a busca pela chave do parâmetro;
