---
id: "360044607734"
titulo: "GIM - Guia de Informação Mensal (Recibo de Entrega)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607734-GIM-Guia-de-Informa%C3%A7%C3%A3o-Mensal-Recibo-de-Entrega"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Escriturações e Declarações   > Declarações estaduais e municipais"
atualizado_em: "2026-09-15T17:38:05Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Fiscal", "GIM", "Guia", "Informação", "Recibo de Entrega", "br.com.sankhya.mgeliv.cad.guiainformacaomensal", "GIM - Guia de Informação Mensal (Recibo de Entrega) manual", "Mensal", "Sintegra", "Paraíba", "\"Empresa\" \"Data Referência\" \"Nro. Recibo\"", "Decreto nº 32.017/2011", "Campos fixos após confirmação", "Documentos Eletrônicos"]
---

# GIM - Guia de Informação Mensal (Recibo de Entrega)

| ``` ![Imagem 1: Módulo: Livros Fiscais > Avançado](https://ajuda.sankhya.com.br/hc/article_attachments/42312982017431) Módulo: Livros Fiscais > Avançado ``` |
| --- |

---

Esta rotina segue as orientações do Decreto nº 32.017, de 23.02.2011 - DOE PB de 24.02.2011.

**Importante:** a princípio, esta tela atenderá apenas ao Estado da Paraíba (PB), contudo, nada impede que posteriormente esta rotina venha a ser adotada por outros estados.

Para o Sintegra da Paraíba, será necessário a geração do Registro **"88 Paraíba"**, cujas informações serão gravadas em tabela específica, alimentada por esta tela.

Na tela [Sintegra](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607534-Sintegra), aba [Filtros Adicionais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607534-Sintegra#abafiltrosadicionais) quando selecionada a marcação 88 Paraíba e a data inicial do registro for maior ou igual a **"01/05/2011"**, o sistema buscará nesta tela os dados para geração do registro.

Caso não existam dados nesta tela, na geração do Sintegra para o Registro 88 Paraíba, será emitida uma mensagem informando que os dados do recibo referente ao mês anterior são inexistentes e, neste caso, o registro não será gerado. Uma vez que esta tela tenha sido alimenta, o Registro 88 Paraíba será gerado conforme o layout oficial.

![Imagem 2: Caso não existam dados nesta tela, na geração do Sintegra para o Registro 88 Paraíba , será emitida uma mensagem…](https://ajuda.sankhya.com.br/hc/article_attachments/8769399328151)

Informe no campo **"Empresa"**, a empresa geradora do Arquivo Sintegra.

No campo **"Data Referência"**, preencha com o primeiro dia do mês da geração do Arquivo Sintegra; considera-se apenas mês e ano, mas é necessário preencher a data completa (dd/mm/aaa).

**Observação:** mesmo ao informar um dia diferente, o sistema considerará o dia 01 ao salvar, como exemplo: informando-se o dia 16/10/2014, ao clicar-se em salvar, o sistema terá gravado 01/10/2014.

No campo **"Nro. Recibo"** informe o Número do Código autenticador do recibo oficial da GIM (Guia de Informação Mensal) referente ao mês anterior; caso seja a primeira entrega da declaração correspondente ao início das atividades, este campo deverá ficar em branco. Por outro lado, caso seja a primeira entrega da declaração após um período inativo (baixa, cancelamento, suspensão de ofício ou suspensão a pedido), neste campo, deverá ser informado o número do código autenticador do recibo oficial da GIM referente ao último mês entregue antes do período de inatividade.

Defina no campo **"Situação"**, a situação no cadastro do contribuinte, sendo que, as opções para escolha são:

- Primeira entrega da declaração após um período de suspensão de ofício;
- Primeira entrega da declaração após um período inativo (baixa, cancelamento ou suspensão a pedido);
- Primeira entrega da declaração, pois o contribuinte está iniciando as suas atividades;
- Entrega mensal.

Através do campo **"Data Situação"**, informe a data em que ocorreu a situação (item acima) na forma dd/mm/aaaa (data do início das atividades, data da baixa, cancelamento ou suspensão).

Os campos Empresa e Data Referência são chamados campos **"chave"** desta tela e, portanto, uma vez informados e confirmados, não poderão mais serem alterados. Caso alguma tentativa de alteração seja feita, será apresentada a mensagem abaixo:

**"Não é possível alterar o valor de um campo chave do registro".**

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607734-GIM-Guia-de-Informa%C3%A7%C3%A3o-Mensal-Recibo-de-Entrega#top)
