---
id: "44066991330455"
titulo: "Como configurar e consultar as Médias Especiais"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44066991330455-Como-configurar-e-consultar-as-M%C3%A9dias-Especiais"
trilha: "Manual do Produto > Pessoas+ > Folha Mensal > Adicionais, Horas e Médias da Folha"
atualizado_em: "2026-10-14T11:27:28Z"
rotulos: ["Cálculos", "FPMEDIAESPEVE", "Médias Especiais"]
---

# Como configurar e consultar as Médias Especiais

### O que é e como usar

As médias especiais permitem que um conjunto de eventos tenha a média calculada com regras próprias de período, dividendo e divisor, diferentes das regras da aba **Médias** da **Regra de Cálculo**.

Os eventos são ligados à média especial por um **Grupo de Médias**. Quando a média especial vale para o tipo de média que está sendo calculado (por exemplo, Férias), os eventos do grupo **saem da média padrão** e são calculados só pela regra especial. O valor resultante é somado ao da média padrão.

### Antes de começar

Habilite o parâmetro **Usa médias especiais - FPMEDIAESPEVE** na tela **Preferências** (Configurações > Avançado). Com ele desativado:

- a aba **Médias Especiais** não aparece na tela **Cálculos**;
- as médias especiais **não são calculadas**, mesmo que já existam configurações cadastradas.

### Como configurar

1. **Configure o evento (rubrica)**

Comece pelo evento, porque o **Grupo de Médias** usado na **Regra de Cálculo** é escolhido entre os grupos já informados nos eventos.

1. Acesse a tela **Eventos** (Pessoal+ > Cadastros) e abra o evento que deve compor a média especial.
2. Na aba **Avançado**, no campo **Incide sobre médias**, selecione uma das opções:
   - **Incide nas médias pelo valor**; ou
   - **Incide nas médias pelo índice**.
3. No campo **Grupo de Médias**, que aparece depois dessa escolha, informe o nome do grupo. Para usar um grupo que já existe, clique no botão **Adicionar Grupo de Médias** ao lado do campo e selecione-o.
4. Salve o evento.
5. Repita o processo para todos os eventos que devem fazer parte do mesmo grupo.

**2. Configure a Regra de Cálculo**

1. Acesse a tela **Regra de Cálculo** (Pessoal+ > Cadastros).
2. Selecione a regra desejada e acesse a aba **Médias Especiais**.
3. Clique em **Adicionar Média Especial**.
4. Em **Médias especiais para o período dos últimos X mês(es)**, defina quantos meses serão considerados, de **1 a 12**.
5. Em **Dividendo**, escolha o que considerar:
   - **período**;
   - **apenas meses com valor**;
   - **meses com maior valor**. Nesse caso, informe também a quantidade de meses.
6. Em **Divisor**, escolha o que considerar:
   - **período**;
   - **número de meses do dividendo**;
   - **Duodecimal**.
7. Em **Grupo de Médias**, clique na lupa e selecione o grupo informado nos eventos. **Este campo é obrigatório.**
8. Em **Tipos de Média**, selecione um ou mais tipos aos quais a configuração se aplica: **Férias**, **Décimo Terceiro**, **Rescisão**, **Férias (Rescisão)** ou **Décimo Terceiro (Rescisão)**. É preciso selecionar pelo menos um.
9. Se você marcou **Rescisão**, aparece o campo **Considera mês da rescisão nas médias quando:**. Escolha uma das opções:
   - **Sempre considera**;
   - **Não considera** (padrão);
   - **Considera quando dias trabalhados forem maior que 14 dias**;
   - **Considera se for benéfico ao funcionário**: o sistema calcula com e sem o mês da rescisão e usa o maior valor.
10. Confirme a configuração.

### Onde consultar

Depois de calculada a folha, acesse a tela **Cálculos** (Pessoal+ > Rotinas Folha), selecione o funcionário e abra a aba **Médias Especiais**, ao lado da aba **Médias**. Cada linha mostra o código e a descrição do evento e o tipo de média.

A aba fica desabilitada quando não há média especial calculada para aquele funcionário e aquela referência. As médias especiais também entram no **Relatório de Médias**, no menu **Documentos** da tela de Cálculos.

### Pontos de Atenção

- Sem o parâmetro **FPMEDIAESPEVE** ativo, a aba fica oculta e o cálculo ignora as médias especiais.
- Cada **Grupo de Médias** só pode ser usado em **uma** média especial por **Regra de Cálculo**.
- Um evento só entra na média especial se tiver **Incide sobre médias** igual a "pelo valor" ou "pelo índice" e um **Grupo de Médias** informado.
- Ao marcar **Férias**, a média especial vale também para férias **vencidas** e **proporcionais**.
- Para os tipos de média que a configuração não cobre, os eventos do grupo continuam sendo calculados normalmente pela média padrão.

### Artigos Relacionados

- [Parâmetros do Pessoas+](https://ajuda.sankhya.com.br/hc/pt-br/articles/38767444361239)
- [Como conferir o cálculo individual](https://ajuda.sankhya.com.br/hc/pt-br/articles/39318926935191)
- [Configuração das Regras de Cálculos](https://ajuda.sankhya.com.br/hc/pt-br/articles/39936375428503)
- [Cadastro de Eventos (Rubricas) da Folha de Pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/33041194565911)
- [Como alterar o período das médias do 13º de 6 para 12 meses?](https://ajuda.sankhya.com.br/hc/pt-br/articles/39354981257111)
