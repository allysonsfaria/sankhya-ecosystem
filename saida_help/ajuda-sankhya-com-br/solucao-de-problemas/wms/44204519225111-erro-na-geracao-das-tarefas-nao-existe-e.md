---
id: "44204519225111"
titulo: "Erro na geração das tarefas. Não existe endereço de movimentação vertical disponível para o Endereço: ' ' Código: CORE_E05102"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44204519225111-Erro-na-gera%C3%A7%C3%A3o-das-tarefas-N%C3%A3o-existe-endere%C3%A7o-de-movimenta%C3%A7%C3%A3o-vertical-dispon%C3%ADvel-para-o-Endere%C3%A7o-C%C3%B3digo-CORE-E05102"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-10-19T19:53:47Z"
rotulos: ["Movimentação Vertical não alterável com estoque", "WMS - KCS", "geração das tarefas", "separação para a Expedição"]
---

# Erro na geração das tarefas. Não existe endereço de movimentação vertical disponível para o Endereço: ' ' Código: CORE_E05102

**MENSAGEM**

Erro na geração das tarefas. Não existe endereço de movimentação vertical disponível para o Endereço: ' ' Código: CORE\_E05102

**SITUAÇÃO**

Ao acionar as opções dos botões “Gerar Tarefas” ou “Pré-visualizar”, na tela Tarefas de Recebimento, o sistema exibe a mensagem acima e não gera as tarefas.

O endereço citado na mensagem é o destino da tarefa. Ele utiliza movimentação vertical, ou seja, está com a opção “Utiliza endereço de conexão para Entrada” e/ou “para Saída” marcada. Porém, o sistema não encontrou nenhum endereço de conexão livre para ele.

**SOLUÇÃO**

**(1)** Acesse WMS » Cadastros » Endereço de Armazenamento e localize o endereço citado na mensagem.

**(2)** Na aba Movimentação Vertical, anote o Endereço Preferencial e o Endereço Secundário.

**(3)** Verifique o Endereço Preferencial. Para ser usado, ele precisa estar ativo e sem estoque, inclusive sem entrada pendente. Se estiver ocupado, conclua ou cancele as tarefas pendentes que usam essa conexão.

**(4)** Verifique o Endereço Secundário (endereço pai). Ele precisa ter pelo menos um endereço de conexão filho com:

- “Ativo” marcado;
- “Analítico” marcado;
- “Movimentação Vertical?” marcado;
- Sem estoque, se o parâmetro “Utiliza multiprodutos nos endereços de conexão? - UTIMULPROENDCON” estiver desligado.

Se não houver nenhum filho assim, cadastre um novo endereço de conexão dentro do endereço pai.

**(5)** Se desejar que mais de um produto utilize a mesma conexão, habilite o parâmetro "UTIMULPROENDCON". Esse parâmetro se aplica somente às conexões filhas do Endereço Secundário. O Endereço Preferencial continua sendo descartado quando possui estoque.

**(6)** Gere as tarefas novamente.

**CAUSA**

Quando uma tarefa passa por um endereço que utiliza conexão, o sistema procura um endereço de conexão na seguinte ordem:

**(1)**  Utiliza o Endereço Preferencial, caso esteja ativo e sem estoque ou entrada pendente.

**(2)**  Se não for possível utilizar o Endereço Preferencial, procura, entre os endereços filhos do Endereço Secundário, um que esteja ativo, seja analítico e esteja marcado como “Movimentação Vertical?”. Com o parâmetro UTIMULPROENDCON desligado, o endereço filho também precisa estar sem estoque.

Se nenhuma das duas opções estiver disponível, as tarefas não serão geradas e a mensagem será exibida. É comum que isso aconteça de forma intermitente: o primeiro recebimento ocupa a conexão preferencial, e o seguinte não encontra uma alternativa no endereço pai.

 **ATENÇÃO:**

- Se o Endereço Preferencial ou o Endereço Secundário estiver em branco, será exibida outra mensagem. Consulte o artigo “O endereço ‘’ está configurado para ter conexão mas não tem o endereço de conexão principal e/ou secundário informados”.
- Essa verificação só ocorre quando a movimentação vertical está ativa para a empresa, ou seja, quando a opção “Utiliza Movimentação Vertical” está marcada em Preferências da Empresa, na aba WMS.
