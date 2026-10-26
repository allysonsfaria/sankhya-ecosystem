---
id: "42427363714967"
titulo: "Como realizar um filtro usando o DDD de um contato em uma automação genérica de cliente?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427363714967-Como-realizar-um-filtro-usando-o-DDD-de-um-contato-em-uma-automa%C3%A7%C3%A3o-gen%C3%A9rica-de-cliente"
trilha: "PLOOMES: Automação de propostas  > Automações"
atualizado_em: "2026-08-10T18:00:18Z"
rotulos: ["sync_hc", "ploomes_5452390", "ploomes", "sync_hash_8603c10389aa"]
---

# Como realizar um filtro usando o DDD de um contato em uma automação genérica de cliente?

No Ploomes, é possível criar automações específicas para clientes, essas são as chamadas automações genéricas.

Usando o DDD dos telefones cadastrados, por exemplo, você consegue segmentar campanhas regionais, enviar mensagens personalizadas ou organizar contatos por localidade.

## Caso de Uso Prático

Imagine que você quer enviar uma promoção especial apenas para clientes de São Paulo (DDD 11).

Utilize essa automação para segmentar o público regional e aumentar as chances de conversão com mensagens personalizadas.

---

## Configuração

## 1. Criar automação

- Acesse **Administração > Automações > Cliente > Nova automação**
- Clique em **Filtro**.

[GIF animado: Imagem 1: Clique em Filtro .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2086791816/ef0597876615cb2a98344dac591e/DDD+artigo+.gif?expires=1786536000&signature=5dbf2a617d7017fa620ec7ec136177d330885454d34a60f9824395d124719392&req=diAvEM53nIleX%2FMW3nq%2BgRzPHmDJMfmMuKe02xqxuJpYCJ6cPD0ebPQi6YMz%0As63ucYBb3Bo8dxbBE1aVTlLi%2Flw%3D%0A)

## 2. Configurar o Filtro

- Selecione **Telefones > Número > Contém**.
- No campo de valor, digite o DDD desejado entre parênteses. Por exemplo, para São Paulo, use **(11)**. Isso garantirá que apenas contatos com esse DDD sejam incluídos.

[GIF animado: Imagem 2: No campo de valor, digite o DDD desejado entre parênteses. Por exemplo, para São Paulo, use (11) . Isso garantirá que…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2086792872/407bc1b1c1464c44fd7c224f151e/DDD+artigo+2.gif?expires=1786536000&signature=400c17882b31bca2f10fabd9591c47a0892315fa2fc82758a3ec1e199d0438a4&req=diAvEM53n4lYW%2FMW3nq%2BgV%2FZYO2Up1Uq08dCtC6Ek80QkwbiiWi7dLloKOmM%0AQwJmR704XLk0EJqRVmM7%2BkTn8uc%3D%0A)

## 3. Escolher o Gatilho e a Ação

- Escolha um gatilho como **"Periodicamente"** para verificar novos contatos de tempos em tempos.
- Configure a ação desejada, como **"Enviar e-mail"**, **"Criar tarefa"** ou **"Criar negócio"**.

[GIF animado: Imagem 3: Configure a ação desejada, como "Enviar e-mail" , "Criar tarefa" ou "Criar negócio" .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2086793530/4df9a0e1c67375a2b14326c2498f/DDD+artigo+3.gif?expires=1786536000&signature=e4e37c74e6a9a40c60c1a150498695d42710f8d978817d03235b19928a110273&req=diAvEM53noRcWfMW3nq%2BgdOlJzKA%2F7svJpUb9X31eVnhtVyirP5MgzBt66AG%0AmAjVMf6%2FCkF3O586gpt9NyyXe1M%3D%0A)

⚠️**Atenção**: A descrição é obrigatória e o ideal é que descreva a automação para que seja fácil encontra-la para novas configurações ou correções.

---

**Este artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
