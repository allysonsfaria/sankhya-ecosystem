---
id: "360043227653"
titulo: "Informado idEstrangeiro em operação interestadual [NT2015/002]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043227653-Informado-idEstrangeiro-em-opera%C3%A7%C3%A3o-interestadual-NT2015-002"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:06:25Z"
rotulos: ["ERRONF", "#criadoRoger", "Configuração", "Parceiro", "NF-e", "SEFAZ", "CFOP", "771", "Rejeição [771] - idEstrangeiro em operação interestadual", "Use CPF/CNPJ; ajuste CFOP para operações com estrangeiros", "idEstrangeiro não permitido em operações interestaduais exceto CFOP 6.667", "Identificação de Estrangeiro"]
---

# Informado idEstrangeiro em operação interestadual [NT2015/002]

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16087478091415) MENSAGEM:**

771-Rejeição: Informado idEstrangeiro em operação interestadual.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16087478099351) SOLUÇÃO:**

Para correção, siga os passos abaixo:
Consideração SEFAZ:

A Sefaz pode não permitir que seja emitida uma NF-e de Operação Interestadual e com Identificador de Destinatário Estrangeiro informado. Uma sugestão de correção seria Identificar o Destinatário da NF-e por um CPF ou CNPJ, porém se o Consumidor for um Estrangeiro, ele provavelmente não terá esse Cadastro de Pessoa Física ou Jurídica. Caso essa rejeição ocorra, e não seja possível Identificar o Destinatário da NF-e com um CPF ou CNPJ, recomendo que entre em contato com a Sefaz do seu Estado para uma melhor orientação. 

![Imagem 3: Acesse: Configurações » Cadastros » Parceiros Aba: "Identificação" Campo "Identificação de Estrangeiro": informe o…](https://ajuda.sankhya.com.br/hc/article_attachments/16087478107159) Acesse: Configurações » Cadastros » Parceiros
Aba: **"Identificação"**
Campo **"Identificação de Estrangeiro":** informe o número do passaporte ou algum documento estrangeiro.

![Imagem 4: Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP Aba: "Livro Fiscal" Se for uma operação com parceiro…](https://ajuda.sankhya.com.br/hc/article_attachments/16087491270167) Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP
Aba: **"Livro Fiscal"**
Se for uma operação com parceiro do Exterior, considere verificar a CFOP de acordo com a operação.

CFOP'S:

**ENTRADA**

1.000 - ENTRADA E/OU AQUISIÇÕES DE SERVIÇOS DO ESTADO
2.000 - ENTRADA E/OU AQUISIÇÕES DE SERVIÇOS DE OUTROS ESTADOS
**3.000** - ENTRADA E/OU AQUISIÇÕES DE SERVIÇOS DO EXTERIOR

**SAÍDAS**

5.000 - SAÍDAS OU PRESTAÇÕES DE SERVIÇOS PARA O ESTADO
6.000 - SAÍDAS OU PRESTAÇÕES DE SERVIÇOS PARA OUTROS ESTADOS
**7.000** - SAÍDAS OU PRESTAÇÕES DE SERVIÇOS PARA O EXTERIOR

Consulte a tabela de CFOP com o Contador da empresa.

![Imagem 5: Após ajustes, faturar novamente a NF-e e gerar Lote.](https://ajuda.sankhya.com.br/hc/article_attachments/16087491276055) Após ajustes, faturar novamente a NF-e e gerar Lote.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16087491279767) CAUSA:**

Quando for emitida uma NF-e com Indicador de Destino da Operação igual a 2 - "Interestadual" e for informado o campo <idEstrangeiro> como identificador do Destinatário será retornada a rejeição "771 - Informado idEstrangeiro em operação interestadual".

**Exceção a regra:**

1. A regra 771 não se aplica para o CFOP igual a 6.667 - "Venda de combustível ou lubrificante a consumidor ou usuário final estabelecido em outra UF diferente da que ocorrer o consumo".

**![Imagem 7: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16087478131095) OBSERVAÇÃO:**

([NT2015/002](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=VNyyxYte6T4=)) - Nota Técnica
