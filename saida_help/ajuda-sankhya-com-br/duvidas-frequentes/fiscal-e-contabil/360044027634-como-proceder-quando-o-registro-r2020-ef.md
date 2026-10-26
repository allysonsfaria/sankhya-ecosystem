---
id: "360044027634"
titulo: "Como proceder quando o Registro R2020 (EFD-REINF) - Para Movimentos dos Portais, não está sendo gerado?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044027634-Como-proceder-quando-o-Registro-R2020-EFD-REINF-Para-Movimentos-dos-Portais-n%C3%A3o-est%C3%A1-sendo-gerado"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T15:56:24Z"
rotulos: ["#RevisadoJR", "Configuração", "Central de Vendas", "Impostos", "TOP", "Documentos Eletrônicos", "EFD-REINF"]
---

# Como proceder quando o Registro R2020 (EFD-REINF) - Para Movimentos dos Portais, não está sendo gerado?

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16415118052119) **MENSAGEM:**

O evento R2020-Retenção Contribuição Serviços Prestados não é gerado quando uma das configurações informadas abaixo não está devidamente configurada.

![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16415118054679) **SOLUÇÃO:**

Para correção, siga as orientações:

![Imagem 3: Comercial » Preferências » Empresa](https://ajuda.sankhya.com.br/hc/article_attachments/16415118055447) Comercial » Preferências » Empresa

Aba: **"Propriedades"**

Campo **"Ativo":** A empresa deve estar ativa

Aba: **"EFD-Reinf' sub-aba 'Eventos periódicos"**

Campo **"Gerar Evento":** Marcado para o evento R2020

![Imagem 4: Configurações » Cadastros » Produtos » Serviço (deve ser feito na tela de Serviço e não de Produtos)](https://ajuda.sankhya.com.br/hc/article_attachments/16415062798743) Configurações » Cadastros » Produtos » Serviço (deve ser feito na tela de Serviço e não de Produtos)

Aba: **"Impostos"**

Campo **"Classificação Cessão M.d.Obra"**: deve estar devidamente preenchido

![Imagem 5: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP](https://ajuda.sankhya.com.br/hc/article_attachments/16415062799511) Comercial » Arquivo » Cadastros » Tipos de Operação - TOP

Aba: **"Geral"**

Campo **"Tipo de movimento"**: V-Venda (A Top utilizada no Lanç. de Venda, deve ser do tipo V-Venda)

Aba: **"Livro Fiscal"**

Campo "Atualização livros de ISS": **"Prestações"**

![Imagem 6: Comercial » Consulta » Portal de Vendas A Nota de VENDA deve estar ' Confirmada '](https://ajuda.sankhya.com.br/hc/article_attachments/16415118058647) Comercial » Consulta » Portal de Vendas A Nota de VENDA deve estar '**Confirmada**'

![Imagem 7: Possui INSS calculado a uma alíquota de 3.5% ou 11%;](https://ajuda.sankhya.com.br/hc/article_attachments/16415118059671) Possui INSS calculado a uma alíquota de 3.5% ou 11%;

OU SEJA

5.1) Via **"Central de Vendas"** com **"Tipo Retenção"** igual a **"Retido",** ou com o **"Tipo Retenção"** igual a **"Não aplicado"** e o parâmetro **"GERIMPINCREINF"** ativo;
OU SEJA

5.2) Via **"Outros Impostos"** com **"Tipo Imposto"** igual a **"Retido"**, ou com **"Tipo Imposto"** igual a **"Incluso"** e o parâmetro **"GERIMPINCREINF**" ativo;

Segue recomendações quanto à configuração para calculo via **"Outros Impostos"**:

**(2)** Configurações » Cadastros » Impostos

Crie um imposto com **"Tipo Imposto"** igual a **"INSS"**;
Alíquota igual a 3,5% ou 11%;
Abas: **"Parceiro" |"TOP"|"Empresa"**;
Configure os campos "**Alíquota"**, **"Red. Base"** e **"Na Nota"**;

**(2)** Comercial » Rotinas » Central de Vendas

Na grade **"Itens"**, no botão **"Outras Opções"**, selecione a opção **"Outros Impostos**";
Inclua o **"Outro Imposto"** com o campo **"Tipo Imposto"** igual a **"Retido"**;
OU
Inclua o **"Outro Imposto",** com o campo **"Tipo Imposto"** igual a **"Incluso"** e ative o parâmetro **"Gera Impostos inclusos no EFD-Reinf? chave GERIMPINCREINF"**;

![Imagem 8: Na configuração da TOP, quando o modelo do documento for diferente de 67, o campo "Atualização livros de ISS" pode…](https://ajuda.sankhya.com.br/hc/article_attachments/16415118062615) Na configuração da TOP, quando o modelo do documento for diferente de 67, o campo **"Atualização livros de ISS"** pode estar como **"Prestações"**;
OU se o modelo do documento for 67, o campo **"Atualização de Livro ICMS"** deve estar marcado com uma das seguintes opções: Ambos ou Livro de saída e o campos **"Status CT-e"** deve estar aprovado;
OU se a UF da empresa gerador do REINF for DF, o modelo de documento pode ser 55 e na TOP o campo **"Atualização livros de ISS"** deve estar como **"Não atualiza"** ou o campo **"Atualização de Livro ICMS"** deve estar com uma das seguintes opções: Livro de entrada ou Ambos.

**Nota:** Caso seja necessário a ativação do parâmetro "Gera Impostos inclusos no EFD-Reinf?' chave GERIMPINCREINF", acesse o menu 'Configurações » Avançado » Preferências' e busque pela chave do parâmetro;
