---
id: "360044512953"
titulo: "Como proceder quando o Registro R2010 (EFD-REINF)- Para Movimentos dos Portais, não está sendo gerado?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044512953-Como-proceder-quando-o-Registro-R2010-EFD-REINF-Para-Movimentos-dos-Portais-n%C3%A3o-est%C3%A1-sendo-gerado"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T15:56:20Z"
rotulos: ["#RevisadoJR", "Configuração", "Central de Compras", "Impostos", "INSS", "R2010-Retenção Contribuição Serviços Tomados", "Registro R2010 não está sendo gerado", "Configure corretamente a classificação do serviço", "EFD-REINF", "R2010"]
---

# Como proceder quando o Registro R2010 (EFD-REINF)- Para Movimentos dos Portais, não está sendo gerado?

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17115287259159) SITUAÇÃO:**

O evento R2010-Retenção Contribuição Serviços Tomados não é gerado quando uma das configurações informadas abaixo não estão devidamente configuradas.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17115270482455) SOLUÇÃO:**

Para correção siga as orientações:

![Imagem 3: Acesse: Comercial » Preferências » Empresa, aba "Propriedades", campo "Ativo": a empresa deve estar ativa. Aba:…](https://ajuda.sankhya.com.br/hc/article_attachments/17115287272215) Acesse: Comercial » Preferências » Empresa, aba **"Propriedades",** campo **"Ativo":** a empresa deve estar ativa. Aba: **"EFD-Reinf",** sub-aba **"Eventos periódicos",** campo **"Gerar Evento":** marque para o evento R2010;

![Imagem 4: Acesse: Configurações » Cadastros » Produtos » Serviço, aba "Impostos", campo "Classificação Cessão M.d.Obra": preencha…](https://ajuda.sankhya.com.br/hc/article_attachments/17115287279639) Acesse: Configurações » Cadastros » Produtos » Serviço, aba **"Impostos",** campo **"Classificação Cessão M.d.Obra":** preencha devidamente;

![Imagem 5: Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP, aba "Geral", campo "Tipo de movimento": C-Compra (a…](https://ajuda.sankhya.com.br/hc/article_attachments/17115270501399) Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP, aba **"Geral",** campo **"Tipo de movimento":** C-Compra (a Top utilizada no Lanç. de Compra, deve ser do tipo C-Compra) e na aba: **"Livro Fiscal",** campo **"Atualização livros de ISS":** marque a opção **"Aquisições";**

![Imagem 6: Acesse: Configurações » Cadastros » Parceiros, aba "Identificação", campo "CNPJ / CPF" : coloque um CNPJ válido;](https://ajuda.sankhya.com.br/hc/article_attachments/17115287288087) Acesse: Configurações » Cadastros » Parceiros, aba **"Identificação",** campo **"CNPJ / CPF"**: coloque um CNPJ válido;

![Imagem 7: Acesse: Comercial » Consulta » Portal de Compras - A Nota de compra deve estar 'CONFIRMADA';](https://ajuda.sankhya.com.br/hc/article_attachments/17115287292823) Acesse: Comercial » Consulta » Portal de Compras - A Nota de **compra** deve estar  **'CONFIRMADA';**

![Imagem 8: Possuir INSS calculado a uma alíquota de 3.5% ou 11%;](https://ajuda.sankhya.com.br/hc/article_attachments/17115270521751) Possuir INSS calculado a uma alíquota de 3.5% ou 11%;

**(1)** Via 'Central de Compras' com 'Tipo Retenção' igual a 'Retido', ou com o 'Tipo Retenção' igual a 'Não aplicado', e o parâmetro **"GERIMPINCREINF"** ativo;

**ou**

**(1)** Via 'Outros Impostos' com 'Tipo Imposto' igual a 'Retido' ou com 'Tipo Imposto' igual a 'Incluso', e o parâmetro GERIMPINCREINF ativo.

**![Imagem 9: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/17115287305367) IMPORTANTE:**

Segue recomendações quanto a configuração para calculo via 'Outros Impostos':

![Imagem 10: Acesse: Configurações » Cadastros » Impostos](https://ajuda.sankhya.com.br/hc/article_attachments/17115287272215) Acesse: Configurações » Cadastros » Impostos

Crie um imposto com 'Tipo Imposto' igual a 'INSS';
Alíquota igual a 3,5% ou 11%;
Abas: **"Parceiro" |"TOP" |"Empresa"**;
Configure os campos **"Alíquota", "Red. Base" e "Na Nota"**;

![Imagem 11: Acesse: Comercial » Rotinas » Central de Compras](https://ajuda.sankhya.com.br/hc/article_attachments/17115287279639) Acesse: Comercial » Rotinas » Central de Compras

Na grade 'Itens', no botão **"Outras Opções",** selecione a opção **"Outros Impostos"**

**(1)** Inclua o 'Outro Imposto' com o campo 'Tipo Imposto' igual a 'Retido';

**ou**

**(1)** Inclua o 'Outro Imposto' com o campo 'Tipo Imposto' igual a 'Incluso' e ative o parâmetro Gera Impostos inclusos no EFD-Reinf?' - GERIMPINCREINF;

**![Imagem 12: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17115287309079) OBSERVAÇÃO:**

Caso seja necessária a ativação do parâmetro Gera Impostos inclusos no EFD-Reinf?' - GERIMPINCREINF, acesse o menu 'Configurações » Avançado » Preferências' e faça a busca pela chave do parâmetro;
