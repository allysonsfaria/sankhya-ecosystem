---
id: "9329869905943"
titulo: "A data de lançamento deve respeitar os parâmetros de Dias para Retroação e Dias para lançamentos futuros"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9329869905943-A-data-de-lan%C3%A7amento-deve-respeitar-os-par%C3%A2metros-de-Dias-para-Retroa%C3%A7%C3%A3o-e-Dias-para-lan%C3%A7amentos-futuros"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T15:08:37Z"
rotulos: ["Configuração", "Usuário", "Preferências", "Financeiro", "CORE_E04090", "Definir Limites", "Data Lançamento Permissões", "Parâmetros Usuário", "Retroação", "Lançamentos Futuros"]
---

# A data de lançamento deve respeitar os parâmetros de Dias para Retroação e Dias para lançamentos futuros

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16701430184727) MENSAGEM:**

[CORE\_E04090]: A data de lançamento deve respeitar os parâmetros de Dias para Retroação e Dias para lançamentos futuros.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16701430190743)SOLUÇÃO:**

![Imagem 3: A data limite para retroação da baixa de títulos e lançamentos futuros, podem ser definidas no campo "Dias para…](https://ajuda.sankhya.com.br/hc/article_attachments/16701430195351) A data limite para retroação da baixa de títulos e lançamentos futuros, podem ser definidas no campo **"Dias para retroação da baixa"** e **"Dias para lançamentos futuros"**, localizados na tela [**"Cadastro de Usuário"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874), botão [**"Outras Opções"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#outrasop%C3%A7%C3%B5es), opção **"Configurações do Usuário".**

![Imagem 4: A data limite para retroação da baixa de títulos e lançamentos futuros, podem ser definidas no campo "Dias para…](https://ajuda.sankhya.com.br/hc/article_attachments/14495156772631)

![Imagem 5: Ou ainda por meio dos parâmetros "Dias para retroação da Baixa - DIASRETROACAO" na tela "Preferências" (Caminho de…](https://ajuda.sankhya.com.br/hc/article_attachments/16701437504535) Ou ainda por meio dos parâmetros **"Dias para retroação da Baixa - DIASRETROACAO"**na tela **"Preferências"** (Caminho de acesso: Configurações » Avançado » Preferências).

Dias para retroação da Baixa - DIASRETROACAO: defina a data limite para retroação da baixa de títulos por meio deste parâmetro.

![Imagem 6: Dias para retroação da Baixa - DIASRETROACAO: defina a data limite para retroação da baixa de títulos por meio deste…](https://ajuda.sankhya.com.br/hc/article_attachments/14495159750679)

**![Imagem 7: "Dias para lançamentos futuros (ref. data hoje)-DIASFUTURO": este parâmetro é definido a partir do cadastro de…](https://ajuda.sankhya.com.br/hc/article_attachments/16701437509271) "Dias para lançamentos futuros (ref. data hoje)-DIASFUTURO":** este parâmetro é definido a partir do cadastro de usuários, campo "Dias para lançamentos futuros". Utilizado para informar o número máximo de dias em que será permitido ao usuário lançar baixas futuras. Para cada usuário será criado um parâmetro quando for informado um valor qualquer neste campo.

**Exemplo:**

Usuário baixando um título no dia 01/06/2004 e no campo **"Data da baixa"** informando 23/06/2004. Se os dias para lançamentos futuros forem menor que 24, o sistema não permitirá a confirmação da baixa.

![Imagem 8: Usuário baixando um título no dia 01/06/2004 e no campo "Data da baixa" informando 23/06/2004. Se os dias para…](https://ajuda.sankhya.com.br/hc/article_attachments/14495213214999)

**Observações:** **é fundamental a configuração dos valores padrões dos parâmetros DIASFUTURO e DIASRETROACAO no usuário SUP**, definindo uma configuração geral que atenda a todos os usuários responsáveis pelas baixas, com as permissões mínimas necessárias. **Usuários gestores, que podem precisar de limites mais amplos e personalizados, devem ter suas configurações ajustadas de forma individual.**

Os referidos parâmetros estão associados ao usuário SUP. Portanto, o valor configurado será aplicado como padrão geral para todos os usuários que realizam baixas, exceto para aqueles com configurações personalizadas.

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16701430211095) CAUSA:**

Quando usuário logado não possui permissão para fazer lançamentos com data retroativa ou baixa futura.
