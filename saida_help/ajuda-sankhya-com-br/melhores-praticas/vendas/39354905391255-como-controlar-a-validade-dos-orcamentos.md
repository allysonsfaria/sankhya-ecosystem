---
id: "39354905391255"
titulo: "Como controlar a validade dos orçamentos pelo agendador"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39354905391255-Como-controlar-a-validade-dos-or%C3%A7amentos-pelo-agendador"
trilha: "Melhores Práticas > Vendas"
atualizado_em: "2026-10-02T18:22:58Z"
rotulos: ["Configuração", "Agendamento", "Financeiro", "Sankhya", "Artigo criado KCS", "CVE - KCS", "Orçamentos"]
---

# Como controlar a validade dos orçamentos pelo agendador

Este artigo orienta sobre como definir ou ajustar o prazo de fechamento automático de orçamentos no sistema Sankhya.

Para controlar a validade dos orçamentos, ou seja, por quanto tempo eles ficam em aberto, pode ser usada a tela **"Agendador para marcar pedidos como não pendentes"**. Ela marca automaticamente como não pendentes os orçamentos que passarem do prazo definido pela empresa. Se a empresa já usa esse agendador e os orçamentos estão sendo fechados antes do tempo, basta aumentar o prazo configurado nele.

### Localização da Configuração do Agendador

O fechamento automático dos orçamentos é feito pela tela **"Agendador para marcar pedidos como não pendentes"** (Comercial » Avançado » Agendadores). Ela marca como **"Não pendente"** os pedidos e orçamentos das TOPs selecionadas no agendamento.

Essa tela não tem um campo de prazo em dias. A programação do agendamento define **quando** ele roda (dias e horários), e o **"Filtro"** da aba **"Configurações"** define **quais** orçamentos são fechados, por exemplo, apenas os lançados há mais de 30 dias.

### Como Ajustar o Prazo de Fechamento

Para modificar o prazo de fechamento automático dos orçamentos, siga os passos abaixo:

**(1)**  Acesse a tela **"Agendador para marcar pedidos como não pendentes"** (Comercial » Avançado » Agendadores).
**(2)**  Localize o agendamento que tem a TOP do orçamento em **"Tops selecionadas"**, na aba **"TOP"**.
**(3)**  Na aba **"Configurações"**, verifique o campo **"Filtro"**. É nele que se define há quantos dias o orçamento precisa ter sido lançado para ser fechado. Atenção: o campo **"Qtd. dias para manter histórico"** não altera esse prazo. Ele só define por quantos dias o histórico de execuções fica guardado.
**(4)**  Crie ou ajuste o filtro pela data do orçamento com o novo prazo desejado e deixe-o ativo.
**(5)**  Salve as alterações realizadas.

### Considerações Importantes

Após o ajuste, o sistema passará a considerar o novo prazo configurado para marcar automaticamente os orçamentos como não pendentes. Certifique-se de que o prazo definido atenda às necessidades operacionais da sua empresa, evitando que orçamentos sejam fechados antes do tempo adequado para negociação com os clientes.

**Atenção:** se o agendamento não tiver filtro por data, cada execução fecha todos os orçamentos pendentes das TOPs selecionadas, independentemente do dia do lançamento, inclusive os lançados no mesmo dia.

O agendador só fecha orçamentos confirmados, das TOPs selecionadas e da empresa informada (quando houver), e não considera os que já têm itens enviados ao WMS.
