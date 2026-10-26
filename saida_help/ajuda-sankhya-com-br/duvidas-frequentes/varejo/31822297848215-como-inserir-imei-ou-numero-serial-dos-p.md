---
id: "31822297848215"
titulo: "Como inserir IMEI ou Número Serial dos produtos na DANFE?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/31822297848215-Como-inserir-IMEI-ou-N%C3%BAmero-Serial-dos-produtos-na-DANFE"
trilha: "Dúvidas Frequentes > Varejo"
atualizado_em: "2026-07-22T14:32:21Z"
rotulos: ["Produtos", "Configuração", "Fiscal", "NF-e", "XML", "DANFE", "Número Serial", "Passos para resolver", "Razão do erro", "Detalhe do erro", "inserir IMEI", "produtos DANFE"]
---

# Como inserir IMEI ou Número Serial dos produtos na DANFE?

Para que o IMEI seja incluído corretamente no XML da nota fiscal, execute os seguintes passos:

**![Imagem 1: Cadastro do Produto:](https://ajuda.sankhya.com.br/hc/article_attachments/31997012929815) Cadastro do Produto:**

Na tela **"Produtos"** (Configurações » Cadastros » Produtos » Produtos), na aba **"Geral"** configure os campos:

- **Qtd. Identificadores**: informe quantos identificadores o produto exige;
- **Tipo Identificador**: selecione a opção **"IMEI"**.

**![Imagem 2: Configuração do Parâmetro:](https://ajuda.sankhya.com.br/hc/article_attachments/31997004238999) Configuração do Parâmetro:**

Acesse a tela **"Preferências"** e configure o parâmetro **"QUEINFADCXMLNFE" (Consulta para informação adicional no XML da nota)**
Insira uma query que busque os valores dos IMEIs. Desta forma, na emissão do XML, o sistema irá gerar um grupo <obsCont> para cada linha retornada desta consulta, contendo as informações dentro das tags <xCampo> e <xTexto>.

**Exemplo:**

![Imagem 3: Exemplo:](https://ajuda.sankhya.com.br/hc/article_attachments/31822284999575)

(1)** Explicação:**

- `<infAdic>`: Bloco de informações adicionais da NF-e.
- `<obsCont>`: Observação do contribuinte (uso livre do emitente).

  - Atributo `xNome`: nome da informação personalizada (no caso, "IMEI").
- `<xCampo>`: Identificador do campo (pode ser repetido em várias observações).
- `<xTexto>`: O valor correspondente — aqui, o número do IMEI.

(1)** Observações Importantes:**

- O sistema gera um grupo <obsCont> para cada linha retornada da consulta;
- Se a consulta retornar valores vazios, a tag será gerada vazia e a NF-e será rejeitada;
- Esta configuração garante que os números de IMEI dos produtos sejam corretamente incluídos no XML da nota fiscal, atendendo às exigências fiscais.
