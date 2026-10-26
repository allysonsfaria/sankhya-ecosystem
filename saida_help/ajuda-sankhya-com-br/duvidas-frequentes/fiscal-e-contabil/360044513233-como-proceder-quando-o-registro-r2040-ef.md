---
id: "360044513233"
titulo: "Como proceder quando o Registro R2040 (EFD-REINF)- Para Movimentos Financeiro não está sendo gerado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044513233-Como-proceder-quando-o-Registro-R2040-EFD-REINF-Para-Movimentos-Financeiro-n%C3%A3o-est%C3%A1-sendo-gerado"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T15:56:17Z"
rotulos: ["Configuração", "Movimentação Financeira", "Impostos", "TOP", "Financeiro", "Registro R2040 - Para Movimentos Financeiro não está sendo gerado", "Verifique o CNPJ válido", "Configure movimento e impostos corretamente", "EFD-REINF"]
---

# Como proceder quando o Registro R2040 (EFD-REINF)- Para Movimentos Financeiro não está sendo gerado

O evento R2040-Recursos Repassados para Associação Desportiva não é gerado quando uma das configurações informadas abaixo não está devidamente configurada.

Para correção, siga as orientações:

![Imagem 1: Comercial » Preferências » Empresa](https://ajuda.sankhya.com.br/hc/article_attachments/16414923917335) Comercial » Preferências » Empresa

Aba: **"Propriedades"**

Campo **"Ativo":** a empresa deve estar ativa

![Imagem 2: Configurações » Cadastros » Empresas](https://ajuda.sankhya.com.br/hc/article_attachments/16414923918615) Configurações » Cadastros » Empresas

Aba: **"Geral"**

Campo **"CNPJ/CPF":** possui um CNPJ valido

![Imagem 3: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/article_attachments/16414923919127) Comercial » Arquivo » Cadastros » Tipos de Operação - TOP

Aba: **"Geral"**

Campo **"Tipo de movimento"**: I-Financeiro (Documentos de origem na Mov. Financeira) >OU< C-Compra (Documentos de origem nos Portais)

Aba: **"Livro Fiscal"**

Campo **"Atualização livros de ISS"**: aquisições

![Imagem 4: Configurações » Cadastros » Parceiros](https://ajuda.sankhya.com.br/hc/article_attachments/16414923921687) Configurações » Cadastros » Parceiros

Aba: **"Fiscal"**

Campo **"Associação Desportiva"**: marcado

![Imagem 5: Comercial » Arquivo » Cadastros » Lista de Serviços](https://ajuda.sankhya.com.br/hc/article_attachments/16414907985431) Comercial » Arquivo » Cadastros » Lista de Serviços

O tipo de Serviço deve estar **ativo**.

Opção **"Tipo de repasse"**: devidamente configurado e o cadastro dessa tela deve estar devidamente vinculado ao cadastro do **produto/serviço** para documentos de origem nos Portais e, para documentos de origem Financeira, deve ser feito o vínculo direto na tela de Mov. Financeira.

![Imagem 6: Possuir INSS calculado a uma alíquota de 3.5% ou 11% via 'Outros Impostos' com 'Tipo Imposto' igual a 'Retido', ou com…](https://ajuda.sankhya.com.br/hc/article_attachments/16414923923351) Possuir INSS calculado a uma alíquota de 3.5% ou 11% via 'Outros Impostos' com 'Tipo Imposto' igual a 'Retido', ou com 'Tipo Imposto' igual a 'Incluso' e o parâmetro **"GERIMPINCREINF"** ativo;

Segue recomendações quanto a configuração para o cálculo via 'Outros Impostos':

**(2)** Configurações » Cadastros » Impostos

Criar um imposto com **"Tipo Imposto"** igual a **"INSS"**;
Alíquota igual a 3,5% ou 11%;
Abas: **"Parceiro" |"TOP" | "Empresa**";
Configurar os campos **"Alíquota"**, **"Red. Base"** e **"Financeiro Origem Financeiro"**;

**(2)** Financeiro » Rotinas » Movimentação Financeira

Botão: Outras Opções » Outros Impostos
 - Inclua o **"Outro Imposto"** com o campo **"Tipo Imposto"** igual a **"Retido"**;
Ou
 - Inclua o **"Outro Imposto"** com o campo **"Tipo Imposto"** igual a **"Incluso"** e ative o parâmetro **"Gera Impostos inclusos no EFD-Reinf?"** chave **"GERIMPINCREINF"**;

![Imagem 7: Financeiro » Rotinas » Movimentação Financeira](https://ajuda.sankhya.com.br/hc/article_attachments/16414907988631) Financeiro » Rotinas » Movimentação Financeira

- O campo **"Origem"** deve ser igual a **"Financeiro"** (financeiro lançado diretamente via Mov. Financeira);
- O campo **"Tipo Operação"** deve estar preenchido (informe uma TOP do Tipo 'Financeiro');
- O campo **"Classificação Cessão M.d.Obra"** na aba **"Geral"** **não** deve estar preenchido;
- O campo **"Tipo de Serviço"**, na aba **"Geral"**, **deve** estar preenchido;

![Imagem 8: Configurações » Cadastros » Produtos » Serviço](https://ajuda.sankhya.com.br/hc/article_attachments/16414907990935) Configurações » Cadastros » Produtos » Serviço

Aba: **"Impostos"**

Campo **"Classificação Cessão"**: não deve ser preenchido.

![Imagem 9: Documentos de origem nos portais, devem estar confirmados.](https://ajuda.sankhya.com.br/hc/article_attachments/16414923925143) Documentos de origem nos portais, devem estar confirmados.

![Imagem 10: Independente da origem, se Portais ou Mov. Financeira, deve haver valores de INSS calculados maiores que zero, tanto na…](https://ajuda.sankhya.com.br/hc/article_attachments/16414923926167) Independente da origem, se Portais ou Mov. Financeira, deve haver valores de INSS calculados maiores que zero, tanto na tabela de impostos da nota ou outros impostos, quando origem portais, quanto financeiros de origem financeira, em outros impostos."
