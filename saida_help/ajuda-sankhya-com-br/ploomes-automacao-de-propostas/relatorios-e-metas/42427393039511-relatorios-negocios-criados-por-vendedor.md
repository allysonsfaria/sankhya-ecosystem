---
id: "42427393039511"
titulo: "Relatórios: Negócios criados por vendedor"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427393039511-Relat%C3%B3rios-Neg%C3%B3cios-criados-por-vendedor"
trilha: "PLOOMES: Automação de propostas  > Relatórios e metas"
atualizado_em: "2026-08-11T16:15:01Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452211", "sync_hash_0903b36e42ce"]
---

# Relatórios: Negócios criados por vendedor

Nesse artigo, você aprende a criar um relatório que nos mostrará quantos negócios foram criados por cada vendedor/usuário, com o objetivo de quantificar o esforço de abertura de frentes de venda.

⚠️ **Atenção:** para montar este relatório, sua conta precisa ter o módulo **Analytics** contratado.

## Como acessar e configurar

Acesse o módulo de **Relatórios** (pelo menu lateral esquerdo).

![Imagem 1: Acesse o módulo de Relatórios (pelo menu lateral esquerdo).](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2577512189/e7cac473135dd66f783dd21342d3/image.png?expires=1786536000&signature=ef2462486cbd4673ff8825d20aede3e73ab48044f8f3a64c5ca5efd931b2fb2a&req=diUgEcx%2Fn4BXUPMW3nq%2BgagZUM51Zco2LUIx%2FUaWUo1ZMJ2KZH83QAbEctMw%0AsLoMUoVEN2od47jDdSgZzhhVkEk%3D%0A)

Escolha o painel onde o gráfico deve ficar, clique em **Novo Gráfico** e selecione o tipo **Tabela**.

![Imagem 2: Escolha o painel onde o gráfico deve ficar, clique em Novo Gráfico e selecione o tipo Tabela .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2577516627/9d788f2409138ca89915a1dc44d5/image.png?expires=1786536000&signature=465b93df0e2fe3d2b9f7c1aff5d68607c53a9e857d0bc75228eb66c90b07991e&req=diUgEcx%2Fm4ddXvMW3nq%2BgcOjLkVYiDstxCJHNBywqUWmlEhyzRvFV%2BkUVRDe%0AeFmZ%2B3ApelMLbnXe3QVhIxmrv4g%3D%0A)

💡 **Dica:** se você ainda não conhece a tela de Relatórios (criação de painéis, permissões de Leitor/Editor/Administrador e os tipos de gráfico disponíveis), veja também: **[Como criar relatórios no Ploomes (nova tela)](https://sankhya.zendesk.com/hc/pt-br/articles/42427389079447)**.

## Métrica de Negócio

1. Em **Objeto da Análise/Entidade**, selecione **Negócio > Contagem**.

   ![configuração da métrica com Módulo = Negócio e Operador = Contagem](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2577524089/4aafa57e660ee20c3fdb09dd6a43/Captura-2Bde-2Btela-2B2026-04-07-2B163437.png?expires=1786536000&signature=e15ae1e6082a724911435bbff214e591ac7e0750f51df7cd7086b428150235c9&req=diUgEcx8mYFXUPMW3nq%2BgUGdyXrBHK2VbSrIsf5c1MhvaW9pWqGs1JR0qZSJ%0Aw4FKFgGrjQAslYm92Pb6SNn7%2Bk4%3D%0A)
2. (Opcional) Aplique filtros para refinar os dados, como **Data de criação** ou **Funil**.

   ![tela de configuração do gráfico com Filtros em destaque](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2577526889/36953ea99c1476a7d292a6e49ed6/Captura-2Bde-2Btela-2B2026-04-07-2B1634371.png?expires=1786536000&signature=f12f2703e917c75a26698946535c53e6f284a7d267906c01c2249c839517ef7f&req=diUgEcx8m4lXUPMW3nq%2BgYJFz5P2m6oPOacSR%2B%2BZNWGgtFO1uDyRt7AECvas%0AxkW08sOvrw%2Bah4CHnmoDfMoMUFM%3D%0A)

   💡 **Dica:** aplicar filtros reduz o escopo do que está sendo medido — o gráfico passa a mostrar o volume apenas do recorte filtrado, não o volume total de Negócios da conta. Se quiser ver apenas os negócios criados que já foram ganhos, adicione a condição **Status igual a Ganho**.
3. Em **Escolha como agrupar os dados**, selecione o campo **Criador**.

   ![configuração do campo de agrupamento como Criador (Negócio)](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2577528297/d5d3d4dab8814f6309d081075177/Captura-2Bde-2Btela-2B2026-04-07-2B16343711.png?expires=1786536000&signature=df4853c8922a46dffd2dd554b4298b6122452870c2916e6d68ae0bb123937863&req=diUgEcx8lYNWXvMW3nq%2BgQAygS6PrFjmyuJb%2Bw2E2vHLaE4jp9QVIXXrWECU%0AldFJkwzW0JxHUADpE4GaCue0me0%3D%0A)

   💡 **Dica:** se, no seu processo, a criação do negócio não é feita pelo próprio vendedor (por exemplo, quando um gestor ou uma integração cadastra o negócio), mas o vendedor fica registrado no campo **Responsável**, utilize esse campo no agrupamento em vez de **Criador**.
4. Clique em **Salvar**.

## Resultado

Depois de salvar a métrica, clique em **Salvar gráfico.**

O relatório exibe uma tabela com o usuário Criador e a quantidade de Negócios de cada usuário.

![resultado final do gráfico em tabela, agrupado por criador](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2576371738/aacfc80597947c33a53541351b0c/Captura%2Bde%2Btela%2B2026-04-07%2B164133.png?expires=1786536000&signature=587db5865bf261482f2272524421a5d6ed20e8736c3cfccacb17a57ad64ae584&req=diUgEMp5nIZcUfMW3nq%2BgZ%2BQExbxjNGb7WSTm9r5vyIUelb8p8vbyDMY%2F3Dr%0AizfZ6j6OKroXmAFRkoatBNPJdsE%3D%0A)

---

**Esse artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
