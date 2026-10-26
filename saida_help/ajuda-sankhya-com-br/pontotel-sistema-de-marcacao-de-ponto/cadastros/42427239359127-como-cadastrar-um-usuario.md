---
id: "42427239359127"
titulo: "Como cadastrar um usuário"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427239359127-Como-cadastrar-um-usu%C3%A1rio"
trilha: "PONTOTEL: Sistema de marcação de ponto > Cadastros"
atualizado_em: "2026-08-03T13:29:53Z"
rotulos: ["sync_hc", "pontotel_6a332859996918bbf68b45fe", "sync_hash_2e19251c2fd7", "pontotel"]
---

# Como cadastrar um usuário

Cadastrar **usuários** na plataforma é um passo essencial para que cada colaborador tenha acesso às funcionalidades adequadas à sua função, garantindo segurança e eficiência na gestão e registro de ponto. Portanto, é importante que cada pessoa tenha seu próprio usuário.

Além disso, a plataforma utiliza **perfis** de acesso para definir os níveis de visibilidade e ação de cada perfil, permitindo que funções administrativas e operacionais sejam ajustadas conforme a necessidade. Assim, cada colaborador acessa apenas o que é relevante para sua rotina.

Neste artigo, veremos como cadastrar usuários para gestão e registro de ponto e acompanhamento da própria folha.

---

## Como cadastrar usuários para gestão do ponto

Usuários de gestão dão acesso a colaboradores com permissões para administrar e monitorar informações da equipe, como **supervisores,** gerentes **e profissionais de\*** RH.\*

1. No menu superior do site Gestão, clique em **Admin**. Depois selecione **Usuários**.
2. Para adicionar um novo usuário, clique em **Criar novo usuário**.
3. Preencha os campos:

![Imagem 1: Preencha os campos:](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1vtqyk5.png)

- **Nome do usuário:** Insira o nome completo (ou nome e sobrenome) do colaborador que utilizará o usuário.
- **E-mail:** Informe o endereço eletrônico que será utilizado para fazer login na plataforma. Pode ser um e-mail real para que o colaborador receba notificações, [comprovantes de ponto](https://sankhya.zendesk.com/hc/pt-br/articles/42427318874391) e consiga recuperar a senha, ou um e-mail fictício, caso não haja necessidade de comunicação direta. O campo será preenchido automaticamente, caso tenha adicionado o e-mail na seção "campos opcionais" do [cadastro de empregado](https://sankhya.zendesk.com/hc/pt-br/articles/42427347938839).
- **Senha de acesso ao sistema:** Cadastre uma senha de pelo menos 8 caracteres. Esta senha será utilizada para o acesso ao sistema e pode ser alterada posteriormente.
- **Telefone:** informe o número de telefone da pessoa que utilizará este usuário. Esse dado é indispensável quando o usuário for o ponto de contato com o suporte da Pontotel. A partir dessa informação, será possível identificá-lo como contato principal e utilizar esse telefone nos chamados que forem abertos.
- **CPF:** Número do CPF do usuário, usado como dado de identificação. Essa informação é obrigatória para usuários que precisam criar ou editar cadastros na plataforma.
- **Empregado associado a este usuário:** Permite vincular o usuário a um empregado já cadastrado no sistema. Esse vínculo é necessário quando o usuário será utilizado de forma pessoal pelo colaborador para realizar o registro de ponto.
- **Código:** Atribua um código único para organizar e identificar o usuário no sistema. Este campo pode facilitar a consulta e o gerenciamento dos registros.
- **Permissão geral:** Define o nível de acesso do usuário e controla quais funcionalidades estarão disponíveis para ele. Se o usuário exercer funções de gestão e, além disso, precisar registrar o ponto, configure neste campo a permissão de gestão e, em "permissão pessoal", atribua a permissão funcionário.
- **Permissão pessoal**: Permite atribuir regras específicas de acesso ao usuário, caso possua um empregado vinculado ao usuário. Se o usuário for exclusivo para gestão do ponto, mantenha esse campo em branco.

![Exemplo de cadastro de usuário que exerce função de gestão e também realiza registro de ponto](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_ljqrx7.png)

Exemplo de cadastro de usuário que exerce função de gestão e também realiza registro de ponto

- **Líder desse usuário**: Campo para vincular um líder responsável pelo colaborador, caso seja aplicável.
- **A quem esse usuário terá acesso:** Ao selecionar uma permissão geral que não dê acesso a todos os locais, esse campo aparecerá. Defina aqui os locais, grupos ou liderados aos quais este usuário terá permissão de acesso no sistema para realizar a gestão.

![Exemplo de preenchimento de um usuário](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1d5xn05.png)

Exemplo de preenchimento de um usuário

4. Configure as **opções avançadas** (opcional)

   - **Gerar senha aleatória e enviar por e-mail**: Quando selecionado, gera automaticamente uma senha e envia para o e-mail cadastrado do usuário.
   - **Exigir troca de senha no primeiro acesso**: Obriga o usuário a redefinir a senha assim que acessar a plataforma pela primeira vez.
   - **Ativar fator de dupla autenticação (MFA)**: Recurso de segurança adicional que exige um segundo fator de autenticação no login (como código enviado por e-mail ou app autenticador).
   - **Considerar este usuário como ponto de contato para o suporte:** ao ativar essa opção, o usuário passa a ser definido como o contato principal da empresa junto ao suporte da Pontotel. Isso significa que seus dados, como telefone e e-mail, poderão ser utilizados nos chamados abertos, facilitando a comunicação e agilizando o atendimento quando houver necessidade de suporte. Por ser um usuário coletivo, recomendamos não habilitar esta opção.

   ![Imagem 4: Considerar este usuário como ponto de contato para o suporte: ao ativar essa opção, o usuário passa a ser definido como…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_fygigh.png)
5. Clique no botão **Salvar** para finalizar a criação ou alteração.

---

## Cadastro de usuários para registro de ponto

Usuários para registro de ponto dão acesso a colaboradores para registrar os pontos e visualizar seus dados pessoais. Os perfis nessa categoria são de **funcionário** e \*\*cadastro de coletores.

### Cadastro de coletores

O usuário com permissão de **cadastro de coletores** é destinado exclusivamente ao acesso no [site](https://bateponto.pontotel.com.br/#/marcacao) ou aplicativo BatePonto. Ele funciona como um acesso compartilhado em dispositivos utilizados por vários colaboradores para registrar seus pontos, sendo conhecido como **usuário coletivo**. Caso ainda não possua um usuário com essa permissão, [neste artigo](https://sankhya.zendesk.com/hc/pt-br/articles/42427316408215) você encontrará uma seção onde orienta a criação desta permissão.

### Funcionário

Um usuário com permissão de **funcionario** tem acesso restrito às funcionalidades essenciais para o registro de ponto e consulta de dados pessoais. Esse tipo de usuário não tem permissões para gerenciar ou visualizar informações de outros colaboradores, garantindo a privacidade e segurança dos dados. Para saber mais sobre, consulte este artigo: [Como cadastrar um usuário com permissão de funcionário](https://sankhya.zendesk.com/hc/pt-br/articles/42427218638871).

> 💡Dica: Além desses dois, é possível criar novos perfis de usuário com outras configurações de acesso, que podem ser atríbuidos aos usuário. Para saber mais, consulte este artigo: [O que é perfil de usuário e como cadastrar novos perfis de permissões](https://sankhya.zendesk.com/hc/pt-br/articles/42427306327575).

---

## ✨ Novidade

Para auxiliar na auditoria e gestão dos usuários do sistema, a tabela de usuários agora conta com as seguintes colunas:

- **Última alteração**: data e hora da criação ou última alteração.
- **Origem da alteração**: por onde a operação foi feita: integração, manual (edição dentro do sistema) ou importador
  As colunas são preenchidas conforme criação do usuário e atualizadas na edição.

![Imagem 5: Origem da alteração : por onde a operação foi feita: integração, manual (edição dentro do sistema) ou importador As…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1atg5xz.png)
> ⚠️ Atenção: Para os cadastros que já existiam na plataforma antes dessa atualização, a origem será exibida como “desconhecido” (padrão do sistema).

---

> 💡 Dica: A Pontotel conta com o Tour Guiado, uma funcionalidade interativa disponível dentro do próprio site Pontotel Gestão, criada para auxiliar você na configuração de cadastros, parametrizações e utilização das principais ferramentas da plataforma. Com orientações passo a passo diretamente na tela, o Tour ajuda a tornar o processo mais simples, rápido e intuitivo, reduzindo dúvidas e evitando erros durante as configurações. Sempre que precisar, você poderá ativar a funcionalidade em: Admin > Tour. Para mais detalhes sobre como utilizar o recurso, confira o artigo: [Como utilizar o Tour Guiado](https://sankhya.zendesk.com/hc/pt-br/articles/42427249823127).

---

Agora o novo usuário está cadastrado e já pode acessar o sistema conforme a permissão atribuída. Com os acessos devidamente configurados, sua equipe terá um controle mais seguro e organizado do ponto, garantindo que cada colaborador esteja habilitado para registrar suas jornadas ou realizar as tarefas relacionadas à sua função.

Caso ainda tenha dúvidas ou precise de auxílio, entre em contato com o nosso time de Suporte pelo chat integrado ao [site Gestão](https://gestao.pontotel.com.br/#/cognito/login) ou pelo [WhatsApp](https://api.whatsapp.com/send/?phone=551131852700&text&type=phone_number&app_absent=0).
