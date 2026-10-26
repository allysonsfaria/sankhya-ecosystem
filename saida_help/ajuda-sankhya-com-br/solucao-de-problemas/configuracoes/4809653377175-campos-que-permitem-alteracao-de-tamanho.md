---
id: "4809653377175"
titulo: "Campos que permitem alteração de tamanho"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4809653377175-Campos-que-permitem-altera%C3%A7%C3%A3o-de-tamanho"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:18:35Z"
rotulos: ["Produtos", "Configuração", "Parceiro", "Cidades", "Controle", "CFOP", "não apagar", "Ajustes de Tamanho em Campos Específicos", "Tamanho do campo", "Banco de dados"]
---

# Campos que permitem alteração de tamanho

Alguns campos terão o seu tamanho definido de acordo com o tamanho do campo criado no banco de dados. Caso ocorra a necessidade de aumentar o tamanho de algum desses campos, execute o comando diretamente no banco de dados. Consulte abaixo os campos:

- Nome do Parceiro e Razão Social (TGFPAR.NOMEPARC E TGFPAR,RAZAOSOCIAL) apresentam-se juntos;
- Nome da Cidade (TSICID.NOMECID);
- Nome do Bairro (TSIBAI.NOMEBAI);
- Controle (TGFITE.CONTROLE);
- Nome do Usuário (TSIUSU.NOMEUSU);
- Descrição Padrão do Laudo (TGACLT.DESCRCLT);
- Características Analisáveis (TGACLC.NOMECLC);
- Descrição Abreviada do Bem (TCIBEM.DESCRABREV);
- Descrição do Produto (TGFPRO.DESCRPROD);
- Complemento do Produto (TGFPRO.COMPLDESC);
- Marca do Produto (TGFPRO.MARCA);
- Nome do Vendedor (TGFVEN.APELIDO);
- Histórico (TGFMBC.HISTORICO);
- Expressão (TSIRHI.EXPRESSAO);
- Descrição da TOP (TGFTOP.DESCROPER);
- Descrição da CFOP (TGFCFO.DESCRCFO);
- Desdob. e Desdob. Duplicata (TGFFIN.DESDOBRAMENTO e TGFFIN.DESDOBDUPL);
- Desdobramento e Desdobramento duplicata (TGFFIN\_EXC.DESDOBRAMENTO e TGFFIN\_EXC.DESDOBDUPL).

| Para aumentar o tamanho dos campos citados acima, solicite o DBA da sua Unidade que realize a criação de um script que percorra todas as tabelas que possuam o determinado campo e assim, realizar a devida alteração. Existe ainda a alternativa de solicitar para a Indústria Sankhya tal procedimento, uma vez que esta orçará a criação deste SCRIPT. |
| --- |
