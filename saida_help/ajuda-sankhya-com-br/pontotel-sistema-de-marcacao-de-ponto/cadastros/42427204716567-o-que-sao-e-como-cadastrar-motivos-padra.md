---
id: "42427204716567"
titulo: "O que são e como cadastrar motivos padrão"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427204716567-O-que-s%C3%A3o-e-como-cadastrar-motivos-padr%C3%A3o"
trilha: "PONTOTEL: Sistema de marcação de ponto > Cadastros"
atualizado_em: "2026-08-03T13:29:56Z"
rotulos: ["sync_hc", "pontotel_6a33284efaa893c373a9acaa", "sync_hash_629c563d85db", "pontotel"]
---

# O que são e como cadastrar motivos padrão

Os motivos padrão são fundamentais para organizar e padronizar os lançamentos na Pontotel. Eles garantem que eventos, como dispensas, suspensões, observações, ajustes de ponto ou envio de arquivos, sejam registrados de forma consistente, evitando divergências e facilitando a gestão da jornada de trabalho.

---

## Como acessar os motivos padrão

1. No menu de navegação do[site Gestão](https://gestao.pontotel.com.br/), clique em **Regras** e selecione a opção **Motivos padrão**.
2. Na tela de motivos padrão, clique no botão **Criar novo motivo padrão**.

---

## Como preencher os campos do motivo

### Campos do topo

![Imagem 1: Campos do topo](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1qu2h1b.png)

- **Nome do motivo:** Escolha um nome claro e objetivo que descreva o motivo, como "atestado médico" ou "ajuste de ponto".
- **Código:** Insira um código identificador para facilitar a consulta no sistema.
- **Tipo:** Selecione a categoria correspondente:

  - **Eventos**: Para motivos relacionados a dispensas (atestados), suspensões ou observações. Ao escolher o tipo "Eventos", é possível configurar os campos de atestado e dispensa que podem ser solicitados ao registrar esse tipo de evento na folha de ponto. Outros campos, como profissional de saúde, número da classe, clínica, CNPJ, CID, declaração de comparecimento, entre outros, representam as informações que poderão ser preenchidas no momento do cadastro do evento.
  - **Correção de ponto**: Para ajustes manuais de registros de ponto.
  - **Gerenciamento de arquivos**: para utilizar como categoria na funcionalidade [Gerenciamento de Arquivos](https://sankhya.zendesk.com/hc/pt-br/articles/42427307486615).
- **visível para todos os usuários do sistema**: Ao desativar, é possível selecionar quais perfis de usuário poderão visualizar e escolher esse motivo.

### Colunas

![Imagem 2: Colunas](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1m7km2d.png)

- **Exibir**: liga/desliga o campo. Se desligado, o campo **não aparece** no formulário do lançamento.
- **Obrigatório**: torna o preenchimento **obrigatório** (impede salvar sem o dado).
- **Marcado como padrão**: quando aplicável, o campo/ação já vem **pré-selecionado** ao escolher esse motivo.

### Seções e opções

> ⚠️ Atenção: As seções abaixo aparecerão somente ao escolher o tipo "eventos (dispensa, suspensão ou observações)

**1) Configurações de dispensa**

Define dados gerais do lançamento de dispensa.

![Imagem 3: Define dados gerais do lançamento de dispensa.](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_tzs39e.png)

- **Selecionar todas**: ativa todos os campos dessa seção de uma vez.
- **Tempo de deslocamento**: mostra um campo para informar minutos/horas de deslocamento (se sua política considerar).
- **Anexar arquivo**: permite exigir/aceitar upload de documento (ex.: atestado médico).
- **Duração esperada da pausa**: este campo deve ser preenchido com o tempo de pausa que o colaborador tem direito no dia dispensado. Essa informação sobrepõe a pausa configurada na regra de cálculo ou na jornada esperada.
- **Motivo padrão referente a atestado médico**: Ao desativar, oculta todos os campos referentes à atestado do passo seguinte.

**2) Informações de atestado**
Coleta dados do atestado quando o motivo for médico.

![Imagem 4: 2) Informações de atestado Coleta dados do atestado quando o motivo for médico.](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_c43ttm.png)

- Profissional de saúde, nº da classe, classe do profissional, estado, especialidade
- Clínica, CNPJ, CID
- Declaração de comparecimento, Atestado de dispensa

**3) Configurações de cálculo**
Controla o efeito do evento no cálculo.

![Imagem 5: 3) Configurações de cálculo Controla o efeito do evento no cálculo.](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1m4dhe8.png)

- **Ignorar jornada de folga**: desconsidera folgas ao aplicar o evento.
- **Descontar DSR**: aplica impacto no DSR conforme sua política.
- **Forma de cálculo da dispensa**: desativa a opção de escolher o tipo de cálculo do motivo ao utilizá-lo para lançar uma dispensa.

**4) Forma de cálculo padrão da dispensa**
Define como a dispensa será calculada (escolha **uma** como padrão):

![Imagem 6: 4) Forma de cálculo padrão da dispensa Define como a dispensa será calculada (escolha uma como padrão):](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_h2kba5.png)

- **Abonar período dispensado da jornada esperada**: O tempo de dispensa não conta como hora trabalhada e reduz a duração da jornada.
- **Considerar como horas trabalhadas**: O tempo de dispensa conta como trabalhado e não altera a duração da jornada.
- **Considerar como falta**: O dia inteiro é tratado como falta.

**5) Campos customizados**
Permite adicionar campos personalizados no lançamento da dispensa, possibilitando a coleta de informações adicionais conforme a necessidade da empresa.
Para criar um novo campo customizável, clique em “Adicionar campo” e configure o nome, tipo de preenchimento e demais opções desejadas.

![Imagem 7: 5) Campos customizados Permite adicionar campos personalizados no lançamento da dispensa, possibilitando a coleta de…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1q8cs9m.png)

- **Nome do campo:** Informe o nome do campo personalizado que será exibido no cadastro.
- **Tipo do campo:** Define o formato da informação que será preenchida no campo personalizado.

  - **Lista de opções**: permite criar uma lista de alternativas para seleção. Preencha as alternativas no(s) campo(s) "Opção". Clique no botão "+" para adicionar novos campos
  - **Resposta direta**: preenchimento por texto.
- **Campo obrigatório:** Ao ativar essa opção, o preenchimento do campo se tornará obrigatório durante o lançamento da dispensa.
- **Botão “X”:** Remove o campo personalizado que está sendo configurado antes do salvamento.

5. Clique em **Salvar** para concluir o cadastro do motivo padrão.

---

> 💡 Dica: A Pontotel conta com o Tour Guiado, uma funcionalidade interativa disponível dentro do próprio site Pontotel Gestão, criada para auxiliar você na configuração de cadastros, parametrizações e utilização das principais ferramentas da plataforma. Com orientações passo a passo diretamente na tela, o Tour ajuda a tornar o processo mais simples, rápido e intuitivo, reduzindo dúvidas e evitando erros durante as configurações. Sempre que precisar, você poderá ativar a funcionalidade em: Admin > Tour. Para mais detalhes sobre como utilizar o recurso, confira o artigo: [Como utilizar o Tour Guiado](https://sankhya.zendesk.com/hc/pt-br/articles/42427249823127).

---

Criar motivos padrão é uma maneira eficiente de garantir a uniformidade nos lançamentos, otimizando a gestão no sistema.

Caso ainda tenha dúvidas ou precise de auxílio, entre em contato com o nosso time de Suporte pelo chat integrado ao [site Pontotel Gestão](https://gestao.pontotel.com.br/#/cognito/login) ou pelo [WhatsApp](https://api.whatsapp.com/send/?phone=551131852700&text&type=phone_number&app_absent=0).
