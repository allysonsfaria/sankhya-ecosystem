---
id: "42427220226327"
titulo: "I05 - Como criar ou atualizar empregados em massa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427220226327-I05-Como-criar-ou-atualizar-empregados-em-massa"
trilha: "PONTOTEL: Sistema de marcação de ponto > Relatórios, Importadores e Exportadores"
atualizado_em: "2026-08-07T16:18:02Z"
rotulos: ["sync_hc", "pontotel_6a332858a2d67f1d9d83bcb9", "sync_hash_edfbf46bd731", "pontotel"]
---

# I05 - Como criar ou atualizar empregados em massa

Atualizar ou cadastrar vários empregados de forma manual pode ser trabalhoso. Para facilitar esse processo, a Pontotel conta com a fucionalidade **I05 - Importadores de Arquivos**, que permite a criação e atualização em massa dos cadastros de empregados e usuários de maneira rápida e prática. Neste artigo, vamos mostrar como utilizar essa ferramenta.

---

> ⚠️ Aviso: Este importador não é aplicável caso sua empresa possua integração de cadastros ativa com outros sistemas, como Sankhya ou similares.

---

## Como baixar a planilha modelo

1. No menu de navegação do [site Gestão](https://gestao.pontotel.com.br/), selecione a opção **Relatórios e Registros**.
2. Na lista de "importadores", selecione a opção **I05 - Importadores de arquivos.**
3. Preencha os **filtros** do importador

   - Em "tipo de importação", selecione a opção **Empregados.**

   ![Imagem 1: Em "tipo de importação", selecione a opção Empregados.](https://storage.crisp.chat/users/helpdesk/website/-/a/1/0/a/a10ad72e4f256800/6acfb2b3-7194-4bf8-b0bc-8ff4f0_19jcggm.png)

- Logo abaixo, selecione a extensão do arquivo desejada para fazer o download da planilha modelo para preenchimento das informações.

![Imagem 2: Logo abaixo, selecione a extensão do arquivo desejada para fazer o download da planilha modelo para preenchimento das…](https://storage.crisp.chat/users/helpdesk/website/-/5/4/9/e/549e29d4eb740800/a5806108-0186-4c86-a771-c3b359_1xmi6kw.png)
> 💡 **Dica:** Escolha a extensão **.xlsx**. Ela é a mais segura, pois dispensa a configuração manual de células e evita erros na importação. O formato CSV não possui formatação visual e o antigo .xls exige ajustes que, se ignorados, podem desconfigurar seus dados.

---

## Como preencher a planilha modelo

Na planilha, terão 3 abas de navegação: **Cadastrar**, **Atualizar** e **Demitir**.
Os dados deverão ser adicionados a partir da linha 4 da planilha.

![Imagem 3: Na planilha, terão 3 abas de navegação: Cadastrar , Atualizar e Demitir . Os dados deverão ser adicionados a partir da…](https://storage.crisp.chat/users/helpdesk/website/-/a/d/2/2/ad2232038bca7000/4056f896-61f0-460e-8cec-c88dfa_1ac35r0.png)

### Para cadastrar

Para criar novos cadastros de empregados, utilize a aba "Cadastrar" da planilha. Nessa aba, insira as informações dos colaboradores que precisam ser incluídos no sistema. Preencha todos os campos necessários, garantindo que as informações estejam corretas para que o cadastro seja realizado com sucesso.

> ⚠️ Atenção:

- O cadastro só será concluído se todos os campos forem preenchidos corretamente. Verifique os dados antes de iniciar a importação para evitar falhas no processo. Campos como Local de Trabalho (coluna E) e Empregador (coluna F) precisam ser preenchidos exatamente como estão registrados no sistema, incluindo pontos, espaços e demais caracteres. Qualquer divergência pode causar falha na importação da linha correspondente.
- Antes de inserir as informações, leia atentamente na linha 2 da planilha. Ela contém orientações importantes sobre como cada campo deve ser preenchido corretamente.

1. As colunas **A** a **L** (com exceção da coluna G), são campos de **preenchimento obrigatório**. Sem as informações nas células dessas colunas, a criação do cadastro não ocorrerá.
2. As colunas **G** e **M** a **AN** são de preenchimento opcional e não interferem diretamente na criação do cadastro. No entanto, quanto mais informações forem adicionadas, mais completo será o registro do colaborador. Vale destacar que alguns campos têm impacto em outras áreas da plataforma e, por isso, são importantes de serem preenchidos, como o **PIS** (coluna T) e a **Função** (coluna U).
   Atenção ao preenchimento de algumas colunas:

- **Coluna G:** este campo pode se tornar obrigatório caso o cadastro do empregador escolhido contenha a informação de CEI, CNO ou CAEPF.
- **Coluna J:** ela define o dia da semana em que a escala será iniciada. Por exemplo, o número 0 corresponde à segunda-feira, enquanto o número 6 representa o domingo. É essencial que o dia da semana seja corretamente associado ao número correspondente para garantir que a escala inicie no dia desejado.
- Colunas **Y** a **AN**: são configurações opcionais para o registro de ponto do colaborador. Algumas opções são recomendadas para uma gestão de ponto mais eficiente, no entanto, habilite apenas aquelas que atendam às necessidades específicas da empresa. Você poderá ver nossa recomendação no item 4.3 do artigo "Como cadastrar um empregado?"

3. As colunas **AO** a **AS** tem o preenchimento opcional, mas estratégico. Essas colunas estão relacionadas à **criação do usuário**, ou seja, ao acesso do colaborador à plataforma, seja para registrar o ponto ou realizar atividades de gestão. Ao inserir essas informações, o cadastro do empregado será automaticamente vinculado a um usuário para acesso ao sistema, facilitando o processo de integração e uso da plataforma.

   - Atenção ao preenchimento da coluna AO, pois é um campo de extrema importância. Para permitir que os colaboradores registrem o ponto nos aplicativos ou no sistema da Pontotel, insira "**S**" no campo "Sincronizar com REP-P".

### Para atualizar

Para atualizar os cadastros dos empregados em lote, utilize a aba "Atualizar" da planilha. Nela, insira os dados dos colaboradores que precisam ser modificados.

> ⚠️ Atenção:

- A atualização considera que os cadastros dos empregados já estão presentes no sistema Gestão.
- Certifique-se de preencher corretamente tanto os campos obrigatórios quanto os opcionais para evitar falhas no processo de importação.

1. Somente a coluna **A** é obrigatória para a inclusão, pois ela serve para identificar qual cadastro deve ser atualizado no sistema. Preencha esta coluna com o **PIN** do empregado, exatamente como está registrado no sistema.

   ![Imagem 4: Somente a coluna A é obrigatória para a inclusão, pois ela serve para identificar qual cadastro deve ser atualizado no…](https://storage.crisp.chat/users/helpdesk/website/-/7/e/4/a/7e4a17dd80c25000/08ef06ee-cea5-4e86-899d-61d81c_51v4r1.png)
2. As demais colunas possuem preenchimento opcional. Caso sejam preenchidas, as novas informações substituirão os dados existentes no cadastro. Certifique-se de seguir as mesmas orientações apresentadas na seção "Para cadastrar".

### Para desligar

Para realizar o desligamento de vários empregados, selecione a aba "Demitir" na planilha. Siga os passos abaixo para realizar o processo de desligamento sem erros.

1. Preencha as colunas **A** a **E,** para que a importação do desligamento do cadastro ocorra.

![Imagem 5: Preencha as colunas A a E, para que a importação do desligamento do cadastro ocorra.](https://storage.crisp.chat/users/helpdesk/website/-/d/1/2/2/d12201684bd66000/59ad86c3-11bd-4e0d-b912-e5de67_1y6sfd6.png)

- Coluna **A**: Preencha com o PIN do cadastro do empregado.
- Coluna **B**: Caso o desligamento deva ocorrer no dia da importação ou em dias posteriores, preencha com "S". Caso o desligamento tenha ocorrido em dias anteriores ao da importação da planilha, preencha com "N".
- Coluna **C**: Caso o colaborador trabalhou ou irá trabalhar no dia em que foi/será desligado, preencha com "S".
- Coluna **D**: Preencha o dia do desligamento, no formato dd/mm/aaaa.
- Coluna **E**: Preencha o motivo do desligamento, selecionando uma das opções predefinidas no sistema: "desligamento", "pediu desligamento", "falecimento" ou "outro".

---

## Como fazer o upload da planilha preenchida

1. Depois de preencher a planilha de acordo com o objetivo definido, salve o arquivo. Se estiver utilizando o programa Excel, clique em "Arquivo", e depois em "Salvar", ou aperte as teclas CTRL + S.
2. Retorne ao [site Gestão](https://gestao.pontotel.com.br/#/cognito/login), no mesmo local instruído no item 1, e selecione novamente a opção**I05 - Importadores de arquivos.** Clique no botão "**anexar**", e selecione o arquivo no seu computador com as informações preenchidas.

   ![Imagem 6: Retorne ao site Gestão , no mesmo local instruído no item 1, e selecione novamente a opção I05 - Importadores de…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1kzbzu5.png)
3. Finalize clicando em **importar.**

   ![Imagem 7: Finalize clicando em importar.](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_10zvhk1.png)
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

Agora que você aprendeu como criar, atualizar e desligar cadastros de empregados de forma rápida e eficiente através da importação do I05, o processo de gestão de registros de funcionários na plataforma Pontotel se torna muito mais ágil. Ao seguir os passos e garantir que os dados estejam corretamente preenchidos, você evita erros e assegura que todas as informações sejam refletidas com precisão no sistema.

Caso ainda tenha dúvidas ou precise de auxílio, entre em contato com o nosso time de Suporte pelo chat integrado ao [site Pontotel Gestão](https://gestao.pontotel.com.br/#/cognito/login) ou pelo [WhatsApp](https://api.whatsapp.com/send/?phone=551131852700&text&type=phone_number&app_absent=0)!
