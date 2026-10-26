---
id: "44455764539287"
titulo: "Destinatário cadastrado não aparece ao agendar relatório formatado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44455764539287-Destinat%C3%A1rio-cadastrado-n%C3%A3o-aparece-ao-agendar-relat%C3%B3rio-formatado"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-10-22T21:08:54Z"
rotulos: ["Produtos", "Configuração", "Fiscal", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Erro", "Documentos Eletrônicos", "agendar relatorio", "agendamento relatorio", "relatorio formatado", "destinatário"]
---

# Destinatário cadastrado não aparece ao agendar relatório formatado

**SITUAÇÃO**

Ao agendar um relatório formatado, na etapa **Defina os destinatários**, um destinatário não aparece na lista, nem quando é pesquisado pelo nome. O cadastro existe e está ativo na tela **Destinatários**.

A situação ocorre em bases com muitos destinatários ativos, normalmente acima de 1.000. Ela não tem relação com o usuário, o vendedor ou o parceiro vinculado ao destinatário, então não é preciso alterar esses cadastros.

**SOLUÇÃO**

Aumente a quantidade de destinatários que a tela de agendamento carrega. Essa quantidade é definida pelo parâmetro **AGDRELPAGSZ**.

**(1)**  Acesse a tela **Destinatários**, filtre os registros com o campo **Ativo** ligado e anote a quantidade de destinatários apresentada.

**(2)**  Acesse a tela **Preferências** e pesquise pelo parâmetro **AGDRELPAGSZ**, descrito como "Qtd registros carregados destinatário agendamento relatório". O valor padrão é **1000**.

**(3)**  Informe um valor maior que a quantidade anotada no passo 1, com uma margem para os próximos cadastros, e salve. Por exemplo: para 1.300 destinatários ativos, informe **2000**.

**(4)**  Feche a tela **Relatórios Formatados**, abra novamente e refaça o agendamento. O destinatário passa a aparecer na lista e na pesquisa.

| **Não informe um valor muito acima do necessário**  A lista de destinatários é carregada inteira ao entrar na etapa **Defina os destinatários**. Quanto maior o valor do parâmetro, mais tempo essa etapa leva para abrir. Use a quantidade de destinatários ativos com uma margem razoável. |
| --- |

#### Alternativa: inative os destinatários que não são mais usados

Se a base tem destinatários que não recebem mais relatórios, como clientes antigos, desligue o campo **Ativo** no cadastro deles. Destinatários inativos não entram na lista do agendamento, e assim a quantidade carregada pode ficar dentro do limite atual.

| **Atenção**  Um destinatário inativo deixa de receber todos os relatórios agendados em que já estiver incluído. Antes de inativar, confirme que ele não deve mais receber nenhum envio. |
| --- |

**CAUSA**

Ao entrar na etapa **Defina os destinatários**, o sistema carrega de uma só vez a lista de destinatários ativos, limitada pela quantidade definida no parâmetro **AGDRELPAGSZ**. O campo de pesquisa da etapa procura somente dentro dessa lista já carregada.

Quando a base tem mais destinatários ativos do que esse limite, os que excedem não são carregados e, por isso, não aparecem na lista nem na pesquisa, mesmo estando cadastrados e ativos. Os destinatários que ficam de fora não são necessariamente os cadastrados mais recentemente.
