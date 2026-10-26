---
id: "42427219985815"
titulo: "I05 - Como cadastrar ou atualizar jornadas em massa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427219985815-I05-Como-cadastrar-ou-atualizar-jornadas-em-massa"
trilha: "PONTOTEL: Sistema de marcação de ponto > Relatórios, Importadores e Exportadores"
atualizado_em: "2026-08-03T12:51:06Z"
rotulos: ["sync_hc", "pontotel_6a33285603ecb83cff1a88c8", "sync_hash_55dec95465ca", "pontotel"]
---

# I05 - Como cadastrar ou atualizar jornadas em massa

O importador I05 é uma funcionalidade que permite realizar cadastros em massa dentro da plataforma Pontotel, de forma prática e segura. Agora, além de usuários, empregados, empregadores, locais de trabalho e férias, também é possível **importar jornadas** diretamente através de uma planilha modelo.

Essa funcionalidade é ideal para empresas que trabalham com múltiplos tipos de jornada e desejam agilizar a configuração inicial ou realizar atualizações com mais eficiência.

---

## Como baixar a planilha modelo

1. No menu de navegação do [site Gestão](https://gestao.pontotel.com.br/), selecione a opção **Relatórios e Registros**.
2. Na lista de "importadores", selecione a opção **I05 - Importadores de arquivos.**
3. Preencha os **filtros** do importador

   - Em "tipo de importação", selecione a opção **Jornadas.**

   ![Imagem 1: Em "tipo de importação", selecione a opção Jornadas.](https://storage.crisp.chat/users/helpdesk/website/-/f/7/b/6/f7b635117aa9f800/b3705c97-9849-4c2c-a229-51b652_10msc6z.png)

- Logo abaixo, selecione a extensão do arquivo desejada para fazer o download da planilha modelo para preenchimento das informações.

![Imagem 2: Logo abaixo, selecione a extensão do arquivo desejada para fazer o download da planilha modelo para preenchimento das…](https://storage.crisp.chat/users/helpdesk/website/-/5/4/9/e/549e29d4eb740800/a5806108-0186-4c86-a771-c3b359_1xmi6kw.png)
> 💡 **Dica:** Escolha a extensão **.xlsx**. Ela é a mais segura, pois dispensa a configuração manual de células e evita erros na importação. O formato CSV não possui formatação visual e o antigo .xls exige ajustes que, se ignorados, podem desconfigurar seus dados.

---

## Como preencher a planilha modelo

### Para cadastrar jornada(s) de trabalho

![Imagem 3: Para cadastrar jornada(s) de trabalho](https://storage.crisp.chat/users/helpdesk/website/-/b/3/d/0/b3d0dc43b8aa6000/54afcb58-f98b-44c6-ab16-f6e7f0_1hzfbzf.png)

1. Selecione a aba "Cadastrar Jornada de Trabalho".

   ![Imagem 4: Selecione a aba "Cadastrar Jornada de Trabalho".](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_xk60oz.png)
2. Preencha a planilha a partir da linha 4 da planilha. Veja o que significa cada coluna:

**Campos obrigatórios:**

- **Nome:** nome completo da jornada para fácil identificação no sistema.
- **Código:** identificador único da jornada (não pode se repetir). Serve para controle interno.
- **Entrada:** horário de início da jornada no formato HH:MM (ex: 08:00).
- **Pausa:** horário de início da pausa principal (ex: 12:00).
- **Retorno:** horário de retorno da pausa principal (ex: 13:00).
- **Saída:** horário de fim da jornada (ex: 18:00).

**Campos opcionais** (caso não seja preenchido, o campo ficará em brando ou será preenchido com o padrão do sistema):

- **Primeira pausa descanso:** pausa adicional prevista pela NR17 (a funcionalidade NR17 deve estar ativa).
- **Primeiro retorno descanso:** retorno da primeira pausa NR17 (a funcionalidade NR17 deve estar ativa).
- **Segunda pausa descanso:** segunda pausa adicional NR17 (a funcionalidade NR17 deve estar ativa).
- **Segundo retorno descanso:** retorno da segunda pausa NR17 (a funcionalidade NR17 deve estar ativa).
- **Tipo de pagamento:** define o tipo de jornada. Pode ser: Normal, Extraordinária ou Especial. Se deixar em branco, será considerada "Normal".
- **Regra de cálculo:** nome da regra de cálculo que será aplicada. Deve estar exatamente igual ao cadastro do sistema.
- **Duração legal:** duração legal da jornada (ex: 08:00).
- **Presença obrigatória:** define se o colaborador precisa cumprir obrigatoriamente essa jornada. Preencha com S para sim e N para não. Se deixado em branco, será considerado "sim".

### Para cadastrar jornada(s) de folga

![Imagem 5: Para cadastrar jornada(s) de folga](https://storage.crisp.chat/users/helpdesk/website/-/9/2/5/a/925a2f933ebf4800/53a3878d-6828-4c6d-9376-050d33_mkabmr.png)

1. Selecione a aba "Cadastrar Jornada de folga".

   ![Imagem 6: Selecione a aba "Cadastrar Jornada de folga".](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_18u5d8b.png)
2. Preencha a planilha a partir da linha 4 da planilha. Veja o que significa cada coluna:

**Campos obrigatórios:**

- **Nome:** nome completo da jornada para fácil identificação no sistema.
- **Código:** identificador único da jornada (não pode se repetir). Serve para controle interno.

**Campos opcionais** (caso não seja preenchido, o campo ficará em brando ou será preenchido com o padrão do sistema):

- **Descrição:** adicione uma breve descrição sobre a jornada
- **Característica:** defina a característica da jornada: normal, compensatória ou DSR. Se não houver uma necessidade específica, deixe em branco, para que ela seja considerada "normal". Esse campo serve para identificar a característica da jornada no AEJ - Arquivo Eletrônico de Jornada, e não terá impacto nos cálculos dos apontamentos do dia.
- **Tipo de pagamento:** define o tipo de jornada. Pode ser: Normal, Extraordinária ou Especial. Se deixar em branco, será considerada "Normal".
- **Regra de cálculo:** nome da regra de cálculo que será aplicada. Deve estar exatamente igual ao cadastro do sistema.
- **Cor:** defina a cor que a jornada terá na folha de ponto dentro da plataforma, podendo ser: verde, vermelha, azul, amarela ou cinza.

3. Depois de preencher a planilha de acordo com o objetivo definido, salve o arquivo. Se estiver utilizando o programa Excel, clique em "Arquivo", e depois em "Salvar", ou aperte as teclas CTRL + S.

---

## Como fazer o upload da planilha preenchida

1. Retorne ao [site Gestão](https://gestao.pontotel.com.br/#/cognito/login), no mesmo local instruído no item 1, e selecione novamente a opção**I05 - Importadores de arquivos.** Clique no botão "**anexar**", e selecione o arquivo no seu computador com as informações preenchidas.

   ![Imagem 7: Retorne ao site Gestão , no mesmo local instruído no item 1, e selecione novamente a opção I05 - Importadores de…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1kzbzu5.png)
2. Finalize clicando em **importar.**

   ![Imagem 8: Finalize clicando em importar.](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_10zvhk1.png)
3. Aguarde o processo de importação da planilha ser finalizado.
4. Quando o processo for concluído, será gerado um relatório com o feedback da importação. Certifique-se de que o usuário foi criado, atualizado ou desativado.

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

Com o Importador I05, cadastrar jornadas em lote se torna muito mais rápido e prático. Essa funcionalidade contribui para uma gestão mais eficiente e padronizada da jornada de trabalho de seus colaboradores.

Caso ainda tenha dúvidas ou precise de auxílio, entre em contato com o nosso time de Suporte pelo chat integrado ao [site Pontotel Gestão](https://gestao.pontotel.com.br/#/cognito/login) ou pelo [WhatsApp](https://api.whatsapp.com/send/?phone=551131852700&text&type=phone_number&app_absent=0)!
