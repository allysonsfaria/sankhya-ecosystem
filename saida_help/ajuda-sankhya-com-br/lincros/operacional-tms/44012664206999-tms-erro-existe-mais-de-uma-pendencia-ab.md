---
id: "44012664206999"
titulo: "[TMS] - Erro \"Existe mais de uma pendência aberta com a mesma classificação para o conhecimento\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012664206999--TMS-Erro-Existe-mais-de-uma-pend%C3%AAncia-aberta-com-a-mesma-classifica%C3%A7%C3%A3o-para-o-conhecimento"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T19:35:26Z"
rotulos: ["sync_hc", "lincros", "lincros_13433392", "sync_hash_bfd417fce836"]
---

# [TMS] - Erro "Existe mais de uma pendência aberta com a mesma classificação para o conhecimento"

**Menu**: Operacional > Importação > Ct-e > Importação

**Objetivo**: Como tratar o erro de importação quando existir mais de uma pendência aberta com a mesma classificação para o conhecimento

**Considerações**:

- Possui o conhecimento apresentado na mensagem do erro cadastrado do sistema;

Abaixo segue os procedimentos:

1. Ao importar o XML da nota fiscal está apresenta a seguinte mensagem: "ERROR: Existe mais de uma pendência aberta com a mesma classificação para o conhecimento 10820597171, pendência 264458564";

   ![Imagem 1: Ao importar o XML da nota fiscal está apresenta a seguinte mensagem: "ERROR: Existe mais de uma pendência aberta com a…](https://ajuda.sankhya.com.br/hc/article_attachments/44012650850327)
2. Acessar o pré-conhecimento que acusa na mensagem do erro, neste exemplo: 10820597171 no menu: Operacional > Cargas > Pré-Conhecimentos;
3. Verificar na aba 'Pendência' que está sem nenhuma pendência 'Pendência(0);

   ![Imagem 2: Verificar na aba 'Pendência' que está sem nenhuma pendência 'Pendência(0);](https://ajuda.sankhya.com.br/hc/article_attachments/44012650963479)
4. Clicar na opção 'Recalcular';

   ![Imagem 3: Clicar na opção 'Recalcular';](https://ajuda.sankhya.com.br/hc/article_attachments/44012657515927)
5. Verificar que agora na aba pendência, consta uma pendência (Pendência 1);

   ![Imagem 4: Verificar que agora na aba pendência, consta uma pendência (Pendência 1);](https://ajuda.sankhya.com.br/hc/article_attachments/44012664712087)
6. Clicar na opção 'Salvar';
7. Acessar o menu: Operacional > Importação > Ct-e > Importação e importar o XML novamente ou reprocessar o mesmo através do menu: Operacional > Importação > Ct-e > Log

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
