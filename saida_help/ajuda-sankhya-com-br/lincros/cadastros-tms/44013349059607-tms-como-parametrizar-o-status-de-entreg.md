---
id: "44013349059607"
titulo: "[TMS] - Como parametrizar o status de entrega e notificar por e-mail"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013349059607--TMS-Como-parametrizar-o-status-de-entrega-e-notificar-por-e-mail"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T19:54:37Z"
rotulos: ["sync_hc", "lincros", "lincros_13432678", "sync_hash_fddf6f58084e"]
---

# [TMS] - Como parametrizar o status de entrega e notificar por e-mail

**Menu**: Cadastros Gerais > Configurações da empresa > Ocorrências

**Objetivo**: Como parametrizar o status de entrega e notificar por e-mail

## Configurações:

- Possui as ocorrências cadastradas na plataforma;

Abaixo segue os procedimentos de como realizar a configuração:

1. Para que as entregas sejam notificadas, o primeiro passo, é inserir a ação de 'NotificarRastreamento' na ocorrência desejada através do menu: Cadastros Gerais > Configurações da empresa > Ocorrências;
2. Localizar a ocorrência desejada, neste exemplo, iremos configurar na ocorrência de 'ENTREGUE';

![Imagem 1: Localizar a ocorrência desejada, neste exemplo, iremos configurar na ocorrência de 'ENTREGUE';](https://ajuda.sankhya.com.br/hc/article_attachments/44013343871255)

3. Na ocorrência desejada, acessa a opção '+ Outras Ações', conforme abaixo:

![Imagem 2: 3. Na ocorrência desejada, acessa a opção '+ Outras Ações', conforme abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/44013314613143)

4. Logo abaixo na coluna 'Disponíveis', localizar a opção 'NotificarRastreamento' e vincular a mesma para a coluna 'Selecionados', clicando com a setinha '>', ou, clicar duas vezes sobre a mesma, conforme abaixo:

![Imagem 3: 4. Logo abaixo na coluna 'Disponíveis', localizar a opção 'NotificarRastreamento' e vincular a mesma para a coluna…](https://ajuda.sankhya.com.br/hc/article_attachments/44013344050199)

5. Após, verificar se a ação ficou na coluna 'Selecionados':

![Imagem 4: 5. Após, verificar se a ação ficou na coluna 'Selecionados':](https://ajuda.sankhya.com.br/hc/article_attachments/44013319084823)

6. Após, clicar em 'Salvar';

7. Essa mesma ocorrência, deve estar vinculada a transportadora, pois uma vez recebida, a plataforma irá disparar o e-mail;

8. Para isso, acessar o  menu: Cadastros gerais > Transportadoras > Ocorrências > Transportadora;

9. A ocorrência deve estar vinculada a transportadora, alguns exemplos abaixo:

![Imagem 5: 9. A ocorrência deve estar vinculada a transportadora, alguns exemplos abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/44013333119255)

10. Caso a ocorrência não estiver vinculada, basta clicar em 'Novo' e realizar o vínculo, conforme exemplo abaixo:

![Imagem 6: 10. Caso a ocorrência não estiver vinculada, basta clicar em 'Novo' e realizar o vínculo, conforme exemplo abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/44013349901463)

11. O e-mail será disparado para o registrado no cadastro pessoas, vinculado ao documento em que foi emitida a NF, disponível em: Cadastros Gerais > Pessoas > Cadastros;

12. Este e-mail é também enviado no .xml da NF para o Lincros e atualizado automaticamente, conforme a recepção do arquivo:

![Imagem 7: 12. Este e-mail é também enviado no .xml da NF para o Lincros e atualizado automaticamente, conforme a recepção do…](https://ajuda.sankhya.com.br/hc/article_attachments/44013333417495)

**Obs.:**Os templates de e-mail, serão enviados conforme o layout padrão Lincros, porém, caso o cliente queira criar um layout próprio, poderá ser solicitado um novo HTML, normalmente quem faz isso é o marketing ou TI;

O Lincros irá notificar sobre qualquer alteração de prazo, caso as ocorrências estejam com a ação de 'NotificarRastreamento', 'Transporte iniciado' e  'Entregue';

Para que o TMS passe a enviar os e-mail´s, precisamos receber essa informação do cliente, assim iremos cadastrar os layouts padrão Lincros na base e ativar o envio do e-mail. Para isso é necessário solicitar ao suporte através da abertura de chamado ([atendimento@lincros.com](mailto:atendimento@lincros.com)).

 "Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
