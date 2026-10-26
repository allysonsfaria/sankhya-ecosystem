---
id: "4405592111511"
titulo: "Erro liberação de rescisão devido a S-2205 e S-2206 com data posterior à rescisão"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4405592111511-Erro-libera%C3%A7%C3%A3o-de-rescis%C3%A3o-devido-a-S-2205-e-S-2206-com-data-posterior-%C3%A0-rescis%C3%A3o"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:23:44Z"
rotulos: ["Eventos", "não apagar", "eSocial", "Configuração Funcionários", "Central do eSocial", "Erro ao liberar rescisão", "Excluir eventos pós-rescisão", "Envio de eventos após rescisão", "Erro"]
---

# Erro liberação de rescisão devido a S-2205 e S-2206 com data posterior à rescisão

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16370065855127) MENSAGEM:**

Ao acessar o menu **Avançado -> Liberar envio da folha para o eSocia**l, pesquisar pelo empregado e marcar a opção de rescisão, ao confirmar apresenta a seguinte mensagem:

![Imagem 2: Ao acessar o menu Avançado -> Liberar envio da folha para o eSocia l, pesquisar pelo empregado e marcar a opção de…](https://ajuda.sankhya.com.br/hc/article_attachments/4405957115543)

Para que seja possível liberar a rescisão, será necessário efetuar a exclusão dos eventos que foram enviados após a data da rescisão do contrato, pois para o eSocial a rescisão será sempre o último evento a ser enviado (S-2299).

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16370057437719) SOLUÇÃO:**

Para se realizar a correção , siga os passos abaixo:

![Imagem 4: Realize uma nova geração dos eventos e, assim que finalizar, não libere nenhum evento.](https://ajuda.sankhya.com.br/hc/article_attachments/16370065898135) Realize uma nova geração dos eventos e, assim que finalizar, não libere nenhum evento.

![Imagem 5: Acesse: MGEPessoal » Menu » Avançado » Consulta eventos por funcionários.](https://ajuda.sankhya.com.br/hc/article_attachments/16370057442455) Acesse: MGEPessoal » Menu » Avançado » Consulta eventos por funcionários.

Insira o código do funcionário, filtre a referência com a referência atual (Exemplo: de 08/2021 a 08/2021) e clique em aplicar.

![Erro](https://ajuda.sankhya.com.br/hc/article_attachments/15917789167383)

![Imagem 7: Localize o evento S-2205 ou S-2206, clique com o botão direito do mouse em cima dele, na opção "Gerar evento como…](https://ajuda.sankhya.com.br/hc/article_attachments/16370057448087) Localize o evento S-2205 ou S-2206, clique com o botão direito do mouse em cima dele, na opção **"Gerar evento como exclusão"** e confirme:

![Erro](https://ajuda.sankhya.com.br/hc/article_attachments/15917789174167)

![Imagem 9: Volte na Central do eSocial, clique em ''Selecionar eventos Disponíveis" e veja que o evento S-2205 ou S-2206 será…](https://ajuda.sankhya.com.br/hc/article_attachments/16370057452951) Volte na Central do eSocial, clique em **''Selecionar eventos Disponíveis"** e veja que o evento S-2205 ou S-2206 será apresentado na tela como exclusão, faça o envio.

![Erro](https://ajuda.sankhya.com.br/hc/article_attachments/15917789177623)

![Imagem 11: Acesse o cadastro do empregado, aba “Registro de envio para o eSocial” , clique com o botão direito, selecione a opção:…](https://ajuda.sankhya.com.br/hc/article_attachments/16370057459479) Acesse o cadastro do empregado, aba **“Registro de envio para o eSocial”**, clique com o botão direito, selecione a opção: **“Preencher data de alteração do S-2205 ou S-2206”**, informe a data anterior à rescisão.

![Erro](https://ajuda.sankhya.com.br/hc/article_attachments/15917781358231)

![Imagem 13: Gere novamente os eventos na Central do eSocial.](https://ajuda.sankhya.com.br/hc/article_attachments/16370057466263) Gere novamente os eventos na Central do eSocial.

![Imagem 14: Realize o envio do S-2205 ou S-2206 com a data alterada.](https://ajuda.sankhya.com.br/hc/article_attachments/16370057472407) Realize o envio do S-2205 ou S-2206 com a data alterada.

![Imagem 15: Acesse a tela Avançado -> Liberar envio da folha para o eSocial, pesquise pelo empregado e marque a opção de Rescisão e…](https://ajuda.sankhya.com.br/hc/article_attachments/16370057474711) Acesse a tela Avançado -> Liberar envio da folha para o eSocial, pesquise pelo empregado e marque a opção de Rescisão e faça a liberação da rescisão desejada.

![Erro](https://ajuda.sankhya.com.br/hc/article_attachments/15917781363351)

![Imagem 17: Gere novamente os eventos e realize o envio do S-2299 da rescisão.](https://ajuda.sankhya.com.br/hc/article_attachments/16370065930007) Gere novamente os eventos e realize o envio do S-2299 da rescisão.

**![Imagem 18: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16370057483543) CAUSA:**

Cliente realiza alterações cadastrais ou contratuais com data posterior a rescisão e realiza o envio dos eventos S-2205 e S-2206. Ao tentar liberar a rescisão para envio, apresenta erro, pois o eSocial não aceita nenhum evento com data superior a da rescisão.
