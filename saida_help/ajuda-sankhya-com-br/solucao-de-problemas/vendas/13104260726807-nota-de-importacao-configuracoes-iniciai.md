---
id: "13104260726807"
titulo: "Nota de Importação. Configurações iniciais"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/13104260726807-Nota-de-Importa%C3%A7%C3%A3o-Configura%C3%A7%C3%B5es-iniciais"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:00:24Z"
rotulos: ["Configuração", "Fiscal", "Parceiro", "Importação", "Impostos", "Nota Fiscal", "Documento essencial: Necessário para legalizar importações", "Configurações: Cadastro da TOP Parceiros e valores corretos", "Lançamento: Preencher DI valores e despesas aduaneiras"]
---

# Nota de Importação. Configurações iniciais

**(1)** A Nota Fiscal de Importação é um documento indispensável para legalizar compras e vendas de mercadorias importadas. Para emitir esse tipo de nota, é necessário ter acesso à Declaração de Importação (**DI**) e à Invoice (ou fatura comercial), para que o recolhimento correto dos impostos seja garantido.

**![Imagem 1: Configurações Necessárias para o lançamento:](https://ajuda.sankhya.com.br/hc/article_attachments/17317851869719) Configurações Necessárias para o lançamento:**

![Imagem 2: Configurações Necessárias para o lançamento:](https://ajuda.sankhya.com.br/hc/article_attachments/17317818742807) Cadastro da TOP:

**(1)**Aba **"Impressão"**:

- Base numeração: Venda;
- Numeração somente automática: marcado;
- Tipo de Numeração: Empresa / Série

![Imagem 3: Tipo de Numeração: Empresa / Série](https://ajuda.sankhya.com.br/hc/article_attachments/17317818758039) Cadastro de Parceiros:

**Identificação de Estrangeiro:** Informa o número do passaporte ou outro documento legal para identificar a pessoa estrangeira. A informação deste campo deve ter entre 5 e 20 caracteres/números.

**(1)**Aba **"Endereço"**:

- Cadastre a cidade vinculada ao estado EX (e no cadastro deste estado deve ter o País Exterior respectivo);
- No cadastro de País, vincule corretamente o campo País domicilio Fiscal;
- Cadastro do Parceiro deve ter o CNPJ ou CPF com zeros e inscrição estadual Isento;
- Informe o campo Identificação de Estrangeiro no cadastro de Parceiro.

**(1)** Para lançamento pegue as informações:

- Valor dos produtos;
- Valor das Despesas Aduaneiras (Taxa SISCOMEX, Armazenagem, Marinha Mercante...);
- Valor do II;
- Valor do PIS Importação;
- Valor do COFINS Importação.

![Imagem 4: Valor do COFINS Importação.](https://ajuda.sankhya.com.br/hc/article_attachments/17317851901847) Lançamento no SankhyaW:

- Informe os itens e seus valores;
- Preencha a Declaração de Importação, botão **"Outras Opções"** (quando houver mais de um item realizar o devido rateio dos valores):

  - Base de Cálculo do Imposto de Importação
  - Valor das Despesas Aduaneiras
  - Valor do Imposto de Importação
  - Valor do IOF
- Preencha dados da importação, aba **"Geral"** (para cada item):
- Preencha Adições (para cada item);

  - No total da nota, campo **"Destaque"** (somar):
  - ICMS (quando **"VOUTITEMSEMICMS"** habilitado não precisa somar ICMS)
  - PIS/COFINS de importação
  - Despesas Aduaneiras

![Imagem 5: OBSERVAÇÕES:](https://ajuda.sankhya.com.br/hc/article_attachments/17317851906327) **OBSERVAÇÕES:**

**(1)** O que compõe o Valor das Despesas Aduaneiras?

- Taxa SISCOMEX
- Armazenagem
- Marinha Mercante

**(1)** Caso seja necessário que o valor do II some ao total da nota este valor deverá ser somado aos itens da nota e redigitar os valores dos impostos;

**(1)** A nota de importação é toda digitada, o que deve ser observado é onde está digitando os valores para que fique correta.

![Imagem 6: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/17317851910807) **IMPORTANTE:**

Na DI (Declaração de Importação) o campo **"Valor das Despesas Aduaneiras"** não soma ao total da nota. Caso tenha que somar informe o junto com algum campo que soma, exemplo: "Valor do Imposto de Importação" ou "Declaração de Importação" (dentro da DI).
