---
id: "44012712294039"
titulo: "[TMS] - Nenhum conhecimento do tipo (Subcontratação) localizado para o CT-e informado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012712294039--TMS-Nenhum-conhecimento-do-tipo-Subcontrata%C3%A7%C3%A3o-localizado-para-o-CT-e-informado"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T19:36:40Z"
rotulos: ["sync_hc", "lincros", "lincros_13433343", "sync_hash_122acd81a29c"]
---

# [TMS] - Nenhum conhecimento do tipo (Subcontratação) localizado para o CT-e informado

**Menu**: Operacional > Importação > CT-e > Importação

**Objetivo**: Como corrigir a importação referente ao erro de nenhum conhecimento do tipo Subcontratação localizado.

**Considerações**:

- Possuir um arquivo XML de ct-e para importação;

Abaixo segue os procedimentos:

1. Abaixo segue exemplo da mensagem com o erro, a mensagem nos indica que ao ser importado o CT-e não foi possível identificar com qual o pré-conhecimento deveria ser feito o vínculo;
2. Isto pode ocorrer caso o tipo do conhecimento que existe para a nota fiscal não esteja correto, por não haver conhecimento para esta nota fiscal, ou por algum outro motivo que o sistema não consiga interpretar qual seria o pré-conhecimento correto a ser vinculado.

   ![Imagem 1: Isto pode ocorrer caso o tipo do conhecimento que existe para a nota fiscal não esteja correto, por não haver…](https://ajuda.sankhya.com.br/hc/article_attachments/44012692846999)
3. Neste caso acima, o sistema não identificou o conhecimento que deveria ser vinculado, portanto, o caminho a seguir será entrar na guia de Pré-conhecimento da nota fiscal e copiar o número do pré-conhecimento, para então depois movermos o CT-e para ele;

   ![Imagem 2: Neste caso acima, o sistema não identificou o conhecimento que deveria ser vinculado, portanto, o caminho a seguir será…](https://ajuda.sankhya.com.br/hc/article_attachments/44012708983959)
4. O próximo passo será entrar no CT-e e clicar em "Mover CT-e" e após, marcar a opção 'Mover para outro conhecimento' e colar o número do pré-conhecimento que foi copiado no passo anterior;

   ![Imagem 3: O próximo passo será entrar no CT-e e clicar em "Mover CT-e" e após, marcar a opção 'Mover para outro conhecimento' e…](https://ajuda.sankhya.com.br/hc/article_attachments/44012722811159)
5. Pronto, isso fará com que o CT-e seja vinculado a este pré-conhecimento e irá corrigir este erro de importação;

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
