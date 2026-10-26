---
id: "39354515537175"
titulo: "Por que eventos excluídos do fixo retornam automaticamente à folha de pagamento?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39354515537175-Por-que-eventos-exclu%C3%ADdos-do-fixo-retornam-automaticamente-%C3%A0-folha-de-pagamento"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-07-29T13:28:53Z"
rotulos: ["Configuração", "Eventos", "Parcelamento", "Folha de Pagamento", "Artigo criado KCS", "Sankhya RH - KCS", "Movimento Fixo"]
---

# Por que eventos excluídos do fixo retornam automaticamente à folha de pagamento?

Os eventos excluídos dos Lançamentos Fixos podem reaparecer nas competências seguintes, gerando descontos ou lançamentos indevidos na folha de pagamento.

Isso ocorre porque a exclusão remove apenas o lançamento da competência atual. Se já existirem registros do mesmo evento em competências futuras, eles permanecerão ativos e continuarão sendo considerados no cálculo da folha.

Além disso, em alguns cenários, parcelamentos ativos ou alterações de lotação que não foram atualizadas corretamente também podem fazer com que o evento seja recalculado nas competências posteriores.

### Comportamento do sistema com parcelamentos

Quando um evento é lançado como parcelamento (por exemplo, em 4 parcelas), a exclusão em uma competência não cancela automaticamente as parcelas futuras.

Dessa forma, o evento continuará sendo lançado nas competências seguintes até que todas as parcelas programadas sejam processadas, caracterizando o comportamento esperado do sistema.

Caso seja necessário interromper o desconto antes do término do parcelamento, é preciso verificar as competências futuras e excluir manualmente os lançamentos existentes.

##

### Como excluir corretamente um evento fixo

Para evitar que eventos excluídos retornem à folha de pagamento, siga o procedimento correto de exclusão:

**(1)** Acesse a tela **"Lançamento de Movimento"** (Pessoal+ » Rotinas Folha » Lançamento de Movimento).

**(2)** Selecione a **"Empresa"** e informe a **"Referência"** em que deseja realizar a exclusão. Clique no **"Botão Pesquisar"**.

**(3)** Acesse a aba **"Visualização"** para ver todos os movimentos lançados.

**(4)** Clique na linha do funcionário desejado e passe o mouse sobre o evento que deseja excluir.

**(5)** Clique no **"Botão Excluir Evento"** que aparecerá ao passar o mouse sobre o movimento.

**(6)** Confirme a exclusão clicando no **"Botão Sim"** no aviso apresentado.

### Observações importantes sobre exclusão de eventos

**Folha calculada:** Se a folha da referência já estiver calculada, não será possível excluir o movimento. Nesse caso, primeiro exclua o cálculo da folha e, em seguida, realize a exclusão do evento.

**Parcelamentos:** Quando um evento possui parcelamento ativo, sua exclusão em uma competência não cancela automaticamente as parcelas futuras. Verifique as próximas competências e, se necessário, exclua o evento novamente até o término do parcelamento.

**Movimento Fixo:** Esse recurso deve ser utilizado apenas para lançamentos recorrentes e que não sofrem alterações mensais. Para eventos variáveis, recomenda-se utilizar outro tipo de lançamento.

### Recomendações para evitar retorno de eventos

- Verifique se o evento possui parcelamento ativo antes de realizar a exclusão.
- Mantenha atualizados os dados cadastrais, como lotação, cargo e benefícios, para evitar recálculos indevidos.
- Valide os cálculos de colaboradores que passaram por alterações cadastrais antes do fechamento da folha.
- Utilize o Movimento Fixo apenas para eventos permanentes e recorrentes, evitando seu uso para lançamentos que variam entre competências.

## Pontos de Atenção

⚠️ A exclusão do movimento fixo afeta apenas as competências futuras. As competências já calculadas e fechadas permanecerão inalteradas.

⚠️ Excluir apenas o evento da folha calculada, sem remover o movimento fixo, fará com que ele seja lançado novamente no próximo cálculo.

⚠️ Para alterar ou excluir um movimento fixo, não pode existir folha calculada na referência. Caso exista, o cálculo deverá ser excluído antes da alteração.
