---
id: "42427415233303"
titulo: "Como criar uma automação para enviar e-mail quando um negócio for ganho"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427415233303-Como-criar-uma-automa%C3%A7%C3%A3o-para-enviar-e-mail-quando-um-neg%C3%B3cio-for-ganho"
trilha: "PLOOMES: Automação de propostas  > Automações"
atualizado_em: "2026-08-10T18:00:46Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452249", "sync_hash_c0896de665b7"]
---

# Como criar uma automação para enviar e-mail quando um negócio for ganho

Enviar automaticamente um e-mail quando um negócio é ganho é essencial para garantir agilidade na comunicação e manter o time sempre alinhado. Com as automações do Ploomes, é possível configurar esse envio de forma automática, incluindo um link direto para o card do negócio, facilitando o acesso às informações e evitando processos manuais.

## Configuração

## 1. Criar uma nova automação

- Acesse **Administração > Automações**
- Selecione a entidade **Cliente**
- Clique em **Nova automação**

[GIF animado: Imagem 1: Clique em Nova automação](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2327519050/cb52b93699185bfbe326f45daef9/vivaldi_qydchzfW41.gif?expires=1786536000&signature=8e8a9914ca41607bad6a503ebaa6930996eebdc6cc170447a85d40c37ebcdbd7&req=diMlEcx%2FlIFaWfMW3nq%2BgQ0VRGgRGQANqxEB4RS9FdLuXgTRKCjPo%2BwLeZKR%0AU0eoejqkau7EA8K6ODPesgAGvaI%3D%0A)

## 2. Configurar descrição, gatilho e filtros

- No campo **Descrição da automação**, informe um nome que identifique a ação
  Exemplo: Disparar e-mail ao ganhar um negócio

- Em **Quando a automação deve ser disparada**, selecione **Quando o negócio for ganho**

- Em seguida, clique no ícone **+** para adicionar os filtros e aplique alguma restrição se achar necessário. (Opcional)
  Neste caso, será aplicado um filtro restringindo o funil, pois é desejado que o e-mail seja disparado somente quando o Negócio for ganho no funil de vendas.

  Filtro
  **Funil (Negócio) - igual a - Funil de vendas**

[GIF animado: Imagem 2: Em seguida, clique no ícone + para adicionar os filtros e aplique alguma restrição se achar necessário. (Opcional)…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2327527782/8275812a68685986e47a9bc5366f/vivaldi_bmuzmyfLkl.gif?expires=1786536000&signature=6ce17a51e8a822b2be86e7c3e8d4a1f684f92936e337ecc587b13e4603cac6b9&req=diMlEcx8moZXW%2FMW3nq%2BgRxSHiEXjM3FX1vbWN9bYP2c5bQ2R%2Bp3cD9%2BZASF%0AO8dw4pGOopun5pJ4kpSR2AK80N8%3D%0A)

## 3. Definir a primeira ação

- Em **Ao ser disparada, o que a automação deve fazer?**, selecione:

  - **Editar dados**
- Em **Selecione um campo**, clique em:

  - **Criação rápida**
  - Crie um novo campo chamado **Url do Negócio** do tipo **texto simples** que será responsável por armazenar o link do Negócio.
  - Em **Tipo de preenchimento** troca para **Fórmula** e clique em **Adicionar**.
  - Na tela que será aberta copie e cole a fórmula que será disponibilizada abaixo.
  - Apague o campo **[Negócio.Id]** e insira novamente pelo botão **Campos** para que a variável seja adicionada e a fórmula funcione corretamente.
  - Clique em **Salvar fórmula**

[GIF animado: Imagem 3: Clique em Salvar fórmula](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2327557967/5940e8087ad5de85c295b0352fde/vivaldi_37b2pgQ12U.gif?expires=1786536000&signature=ca0ec71b8d129824548b7255357ecb5fee50d49692d20b57a871412dd1665a77&req=diMlEcx7mohZXvMW3nq%2BgYPpcinyT2oeDzZj24fPxCd1HJqA5BYks%2FJVwsKa%0AgYMBuHovkCUpOlnSNyePTLXi5Yg%3D%0A)

**Fórmula**

(function(){

return "<a href='<https://app10.ploomes.com/deal/>" + [Negócio.Id] + "'>URL do Negócio</a>";

})();

## 4. Definir a segunda ação

- Após configurar a primeira ação, clique em **Adicionar nova ação**.
- Escolha a nova ação para **Enviar e-mail**:

  - Selecione o **tipo de remetente**
  - Selecione **um** **usuário para ser avisado caso o envio do e-mail falhe**
  - Selecione **um** **campo de e-mail para o destinatário ou escreva e-mails separados por ponto e vírgula**
  - Preencha o **assunto do e-mail**
  - Insira no corpo do e-mail o campo **Url do Negócio** criado anteriormente na primeira ação.
- Clique em **Salvar**, para salvar a automação.

[GIF animado: Imagem 4: Clique em Salvar , para salvar a automação.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2327588325/f7c132c73b11f1914dfa534ef476/vivaldi_edTHZ9WWIk.gif?expires=1786536000&signature=946572bd2959e2bb1c4bc2d8156a6a35216a08cbd9a0225bb5c410681b85b8eb&req=diMlEcx2lYJdXPMW3nq%2BgXFaIfTxmPCxLlc9o2IVQ2ydCEob%2FnPykiKL3F7l%0AsxnWiwwWxmr0TyadTu3PVBapgso%3D%0A)

---

**Este artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
