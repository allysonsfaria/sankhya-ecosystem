---
id: "22689146733591"
titulo: "Erro nas versões que estão com o linha \"@op.userid\" no cabeçalho gerando hard parse no banco de dados [Fechado]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/22689146733591-Erro-nas-vers%C3%B5es-que-est%C3%A3o-com-o-linha-op-userid-no-cabe%C3%A7alho-gerando-hard-parse-no-banco-de-dados-Fechado"
trilha: "Modalidade SaaS > Erros Conhecidos"
atualizado_em: "2026-07-22T14:48:53Z"
rotulos: ["SQL", "Configuração", "Atualização", "Erro", "Banco de Dados"]
---

# Erro nas versões que estão com o linha "@op.userid" no cabeçalho gerando hard parse no banco de dados [Fechado]

Status: Concluído

Responsável: Ysmaylyka Soares Macedo

Link (card ou ticket): <https://sankhya.kanbanize.com/ctrl_board/57/cards/29145/details/>

# Sintomas:

Conforme a leitura dos SQL's no banco, identificamos que a estrutura é a mesma para todas das execuções e que cada uma estava gerando um SQL\_ID diferente.

![Imagem 1: Conforme a leitura dos SQL's no banco, identificamos que a estrutura é a mesma para todas das execuções e que cada uma…](https://ajuda.sankhya.com.br/hc/article_attachments/22689130659863)

Cada consulta listada acima, possui a mesma estrutura com diferença da linha "@op.userid" no identificador do cabeçalho.

![Imagem 2: Cada consulta listada acima, possui a mesma estrutura com diferença da linha "@op.userid" no identificador do cabeçalho.](https://ajuda.sankhya.com.br/hc/article_attachments/22689146730391)

De acordo com o conceito de  banco relacional e não relacional, tudo que for descrito dentro dentro de um trecho de comentário, não deve ser interpretado como trecho de SQL. Contudo, a rotina via aplicação está sendo executada gerando hard parse e um novo SQL\_ID, ou seja, a cada vez que o valor da linha "@op.userid" é alterado, gera um novo SQL\_ID no banco impossibilitando o SQL de passar pela otimização do banco.

#

# Solução:

O problema foi corrigido nas seguintes versões abaixo:

4.21b206
4.22b254
4.23b247
4.24b194
4.25b146
4.26b48

21/06/24 - Fechado -

O problema foi corrigido nas seguintes versões abaixo:

4.21b206
4.22b254
4.23b247
4.24b194
4.25b146
4.26b48
