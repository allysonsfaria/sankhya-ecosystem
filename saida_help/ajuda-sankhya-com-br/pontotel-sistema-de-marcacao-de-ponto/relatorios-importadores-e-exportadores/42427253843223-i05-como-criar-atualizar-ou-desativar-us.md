---
id: "42427253843223"
titulo: "I05 - Como criar, atualizar ou desativar usuários em massa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427253843223-I05-Como-criar-atualizar-ou-desativar-usu%C3%A1rios-em-massa"
trilha: "PONTOTEL: Sistema de marcação de ponto > Relatórios, Importadores e Exportadores"
atualizado_em: "2026-08-03T13:29:53Z"
rotulos: ["sync_hc", "pontotel", "pontotel_6a332857c832f66ee4526db5", "sync_hash_e3fd85577940"]
---

# I05 - Como criar, atualizar ou desativar usuários em massa

Cadastrar ou atualizar múltiplos usuários manualmente pode ser um processo demorado. Para simplificar essa tarefa, a Pontotel oferece a funcionalidade **I05 - Importadores de Arquivos**, que permite realizar a criação e atualização em massa de cadastros de empregados e usuários de forma ágil e eficiente. Neste artigo, vamos explicar como usar essa ferramenta para otimizar o seu processo de importação.

---

> ⚠️ Aviso: Este importador não é aplicável caso sua empresa possua integração de cadastros ativa com outros sistemas, como Sankhya ou similares.

---

## Como baixar a planilha modelo

1. No menu de navegação do [site Gestão](https://gestao.pontotel.com.br/), selecione a opção **Relatórios e Registros**.
2. Na lista de "importadores", selecione a opção **I05 - Importadores de arquivos.**
3. Preencha os **filtros** do importador

   - Em "tipo de importação", selecione a opção **Usuários.**

   ![Imagem 1: Em "tipo de importação", selecione a opção Usuários.](https://storage.crisp.chat/users/helpdesk/website/-/e/9/4/9/e949308043326000/d3e82ea4-078b-450a-81a5-b2a496_yqiu4c.png)

- Logo abaixo, selecione a extensão do arquivo desejada para fazer o download da planilha modelo para preenchimento das informações.

![Imagem 2: Logo abaixo, selecione a extensão do arquivo desejada para fazer o download da planilha modelo para preenchimento das…](https://storage.crisp.chat/users/helpdesk/website/-/5/4/9/e/549e29d4eb740800/a5806108-0186-4c86-a771-c3b359_1xmi6kw.png)
> 💡 **Dica:** Escolha a extensão **.xlsx**. Ela é a mais segura, pois dispensa a configuração manual de células e evita erros na importação. O formato CSV não possui formatação visual e o antigo .xls exige ajustes que, se ignorados, podem desconfigurar seus dados.

4. **Preencha os campos** da planilha modelo

   - A planilha conta com três abas de navegação: **Cadastrar**, **Atualizar** e **Desativar**. Selecione a aba correspondente à ação que deseja realizar.

   ![Imagem 3: A planilha conta com três abas de navegação: Cadastrar , Atualizar e Desativar . Selecione a aba correspondente à ação…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1rjomlx.png)

- Na primeira linha de cada planilha, será indicado se a coluna corresponde a um campo **obrigatório** ou **opcional**. Todas as colunas obrigatórias devem ser devidamente preenchidas. Caso contrário, a importação não será realizada.
- Na segunda linha da planilha, há uma descrição detalhada com orientações sobre como o campo deve ser preenchido.

![Primeiros campos da planilha da aba "Cadastrar"](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1j35rsv.png)

Primeiros campos da planilha da aba "Cadastrar"

---

## Como preencher a aba "Cadastrar"

Para criar novos usuários, utilize a aba "Cadastrar" da planilha. Nessa aba, insira as informações dos acessos de colaboradores que precisam acessar a plataforma. Preencha todos os campos necessários, garantindo que as informações estejam corretas para que o cadastro seja realizado com sucesso.

1. As colunas **A**, **B** e **D** são campos de **preenchimento obrigatório**. Sem as informações nas células dessas colunas, a criação do cadastro não ocorrerá.

![Imagem 5: As colunas A , B e D são campos de preenchimento obrigatório . Sem as informações nas células dessas colunas, a criação…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_9cerwg.png)

- Coluna A | **Nome:** Insira o nome completo (ou nome e sobrenome) do colaborador que utilizará o usuário.
- Coluna B | **E-mail:** Informe o e-mail do usuário que será usado para fazer login na plataforma. Pode ser um e-mail real para que o colaborador receba notificações e consiga recuperar a senha, ou um e-mail fictício, caso não haja necessidade de comunicação direta.
- Coluna D | **Permissões:** Defina o nível de acesso que o usuário terá dentro do sistema, selecionando umas das permissões previamente cadastradas. Inicialmente, você terá as seguintes permissões para uso: RH, Funcionario, Gerente e Supervisor. Entenda mais sobre as permissões [nesse artigo](https://sankhya.zendesk.com/hc/pt-br/articles/42427306327575).

2. As colunas **C**, **E**, **F** e **G** são campos opcionais, mas fornecem dicas valiosas para a correta inserção dos dados, especialmente no que diz respeito às permissões de gestores (que só tem acesso a um ou mais locais de trabalho, mas não todos). Vale ressaltar que, embora sejam opcionais, alguns campos podem se tornar obrigatórios, dependendo da permissão que o usuário terá dentro do sistema.

   ![Imagem 6: As colunas C , E , F e G são campos opcionais, mas fornecem dicas valiosas para a correta inserção dos dados,…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_xfoh8s.png)
3. As colunas **H** a **N** também são campos opcionais, mas alguns pontos são importante serem mencionados:

![Imagem 7: As colunas H a N também são campos opcionais, mas alguns pontos são importante serem mencionados:](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1gleh6t.png)

- O PIN (coluna H) deve ser preenchido se o colaborador já tiver um cadastro de empregado no sistema.
- Embora não seja obrigatório, recomendamos preencher o CPF (coluna I), especialmente se o usuário já tiver um cadastro de empregado ou for desempenhar funções de gestão na plataforma.

---

## Como preencher a aba "Atualizar"

Para atualizar os cadastros dos usuários em lote, utilize a aba "Atualizar" da planilha. Nela, insira os dados dos colaboradores que precisam ser modificados.

> 💡 Dica: Essa funcionalidade é especialmente útil quando você cria uma nova permissão e deseja aplicá-la a vários usuários já cadastrados.

1. A coluna **B** é um campo de preenchimento obrigatório. Sem a informação na célula corespondente, a atualização do cadastro não ocorrerá.

   ![Imagem 8: A coluna B é um campo de preenchimento obrigatório. Sem a informação na célula corespondente, a atualização do cadastro…](https://d33v4339jhl8k0.cloudfront.net/docs/assets/574ca4e4c6979138ff609a77/images/673b538a442d517d60d26bc7/file-Lwn4mfzfwv.png)
2. As demais colunas possuem preenchimento opcional. Caso sejam preenchidas, as novas informações substituirão os dados existentes no cadastro. Certifique-se de seguir as mesmas orientações apresentadas na seção "Para cadastrar".

---

## Como para preencher a aba "Desativar"

Para desativar usuários em massa, utilize a aba "Desativar" na planilha. Dessa forma, os usuários indicados serão desabilitados e não terão mais acesso ao sistema.

1. No único campo obrigatório (coluna A), insira o e-mail do usuário que deseja desativar. Certifique-se de que a informação esteja exatamente como registrada no sistema, incluindo pontos e outros caracteres. Qualquer divergência poderá resultar em falha na importação da linha correspondente.

![Imagem 9: No único campo obrigatório (coluna A), insira o e-mail do usuário que deseja desativar. Certifique-se de que a…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_cwa5an.png)

---

## Como fazer o upload da planilha preenchida

1. Depois de preencher a planilha de acordo com o objetivo definido, salve o arquivo. Se estiver utilizando o programa Excel, clique em "Arquivo", e depois em "Salvar", ou aperte as teclas CTRL + S.
2. Retorne ao [site Gestão](https://gestao.pontotel.com.br/#/cognito/login), no mesmo local instruído no item 1, e selecione novamente a opção**I05 - Importadores de arquivos.** Clique no botão "**anexar**", e selecione o arquivo no seu computador com as informações preenchidas.

   ![Imagem 10: Retorne ao site Gestão , no mesmo local instruído no item 1, e selecione novamente a opção I05 - Importadores de…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1kzbzu5.png)
3. Finalize clicando em **importar.**

   ![Imagem 11: Finalize clicando em importar.](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_10zvhk1.png)
4. Aguarde o processo de importação da planilha ser finalizado.
5. Quando o processo for concluído, será gerado um relatório com o feedback da importação. Certifique-se de que o usuário foi criado, atualizado ou desativado.

---

## 🆕 Novidade: limpeza de campos opcionais via importador I05

O importador I05 agora permite **remover informações opcionais já cadastradas** diretamente pela planilha, sem precisar de ajuste manual na plataforma.
Para isso, basta utilizar a palavra reservada **`<APAGAR>`** na célula correspondente ao campo que deseja limpar, dentro da aba **Atualizar** da planilha.
**Como funciona:**

- **Célula em branco:** o sistema interpreta como "não alterar". O valor existente é mantido.
- **`<APAGAR>` em campo opcional:** o sistema remove o valor cadastrado naquele campo.
- **`<APAGAR>` em campo obrigatório:** a importação retorna uma mensagem de erro. Campos obrigatórios não podem ser apagados.

> 💡 Dica: essa funcionalidade está disponível apenas na aba Atualizar da planilha do I05. Utilize com atenção para não remover informações de forma não intencional.

---

Agora que você aprendeu como criar, atualizar e desativar usuários de forma rápida e eficiente através da importação do I05, a gestão de acessos na plataforma Pontotel se torna mais prática e otimizada. Seguindo os passos corretamente e preenchendo as informações com atenção, você evita erros e garante que os acessos sejam configurados com precisão no sistema.

Caso ainda tenha dúvidas ou precise de auxílio, entre em contato com o nosso time de Suporte pelo chat integrado ao [site Pontotel Gestão](https://gestao.pontotel.com.br/#/cognito/login) ou pelo [WhatsApp](https://api.whatsapp.com/send/?phone=551131852700&text&type=phone_number&app_absent=0)!
