---
id: "17033329185687"
titulo: "ORA-01400: não é possível inserir NULL em (SANKHYA , TGFIDI, DTDESEMBARACO"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/17033329185687-ORA-01400-n%C3%A3o-%C3%A9-poss%C3%ADvel-inserir-NULL-em-SANKHYA-TGFIDI-DTDESEMBARACO"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:53:55Z"
rotulos: ["XML", "Importação", "Financeiro", "Solução para Erro de Inserção Nulo em Data de Desembaraço", "ORA-01400", "Erro", "Sankhya"]
---

# ORA-01400: não é possível inserir NULL em (SANKHYA , TGFIDI, DTDESEMBARACO

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/17033271381271) **MENSAGEM:**

ORA-01400: não é possível inserir NULL em (SANKHYA , TGFIDI, DTDESEMBARACO.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17033313349143)CAUSA:**

Ocorre na ausência da tag  <dDesemb> no xml utilizado.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17033284905367)SOLUÇÃO:**

O XML precisa ter a tag <dDesemb> conforme evidência abaixo:
 
![Imagem 4: O XML precisa ter a tag <dDesemb> conforme evidência abaixo: Se o XML importado estiver sem essa TAG o sistema tenta…](https://ajuda.sankhya.com.br/hc/article_attachments/17033941131159)
 
Se o XML importado estiver sem essa TAG o sistema tenta inserir NULL, porém esse campo não é aceito com valor nulo na base.
 
Segue abaixo XML de exemplo com valor nulo.

![Imagem 5: Temos o artigo abaixo que descreve esse processo: Importar dados da DI-Declaração da Importação via XML - Nota de…](https://ajuda.sankhya.com.br/hc/article_attachments/17033963720727)

Temos o artigo abaixo que descreve esse processo: 
[Importar dados da DI-Declaração da Importação via XML - Nota de Nacionalização](https://ajuda.sankhya.com.br/hc/pt-br/articles/360043796574-Importar-dados-da-DI-Declara%C3%A7%C3%A3o-da-Importa%C3%A7%C3%A3o-via-XML-Nota-de-Nacionaliza%C3%A7%C3%A3o)
 
Outra alternativa seria diretamente na central de compras, necessário selecionar o produto em outras opções e em seguida clicar em "Declaração de Importação e Adições ".
 
![Imagem 6: Temos o artigo abaixo que descreve esse processo: Importar dados da DI-Declaração da Importação via XML - Nota de…](https://ajuda.sankhya.com.br/hc/article_attachments/17034014532503)
 
Clique para inserir os dados da DI manual, campo da data do desembaraço.
 
![Imagem 7: Temos o artigo abaixo que descreve esse processo: Importar dados da DI-Declaração da Importação via XML - Nota de…](https://ajuda.sankhya.com.br/attachments/token/OWv4dbtpr8asrAZXIucF9XtYR/?name=image.png)
 
Segue o passo a passo que valida a orientação: [Central de Compras | Grade Itens > Botão Outras Opções](https://ajuda.sankhya.com.br/hc/pt-br/articles/Central%20de%20Compras%20|%20Grade%20Itens%20>%20Bot%C3%A3o%20Outras%20Op%C3%A7%C3%B5es)
