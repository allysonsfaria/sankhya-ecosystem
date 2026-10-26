---
id: "42427218638871"
titulo: "Como cadastrar um usuário individual (com perfil de funcionário)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427218638871-Como-cadastrar-um-usu%C3%A1rio-individual-com-perfil-de-funcion%C3%A1rio"
trilha: "PONTOTEL: Sistema de marcação de ponto > Cadastros"
atualizado_em: "2026-08-03T13:29:59Z"
rotulos: ["sync_hc", "pontotel_6a33ee3726e8f95c269ec829", "sync_hash_3a7b74f62892", "pontotel"]
---

# Como cadastrar um usuário individual (com perfil de funcionário)

Cadastrar um usuário individual (com permissão de funcionário) é um passo essencial para garantir que cada empregado tenha acesso à plataforma de forma segura e restrita.
Com esse usuário, o colaborador poderá registrar seu ponto, consultar suas informações cadastrais e acessar dados relacionados ao seu próprio desempenho, sem ter acesso a configurações ou informações de outros membros da equipe.

Neste artigo, você aprenderá como realizar esse cadastro, garantindo a gestão eficiente do seu time.

---

## Como cadastrar um usuário individual:

1. No menu de navegação do[site Gestão](https://gestao.pontotel.com.br/), clique em **Cadastros**. Depois selecione a opção **Empregados**.
2. Selecione o empregado já criado na listagem.
3. Selecione a opção "**Criar/Editar usuário**".

![Imagem 1: Selecione a opção " Criar/Editar usuário ".](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1v4d17o.png)
> 💡 Dica: Você também pode criar o usuário acessando o caminho admin > usuários e vinculando um empregado no campo "empregado associado a este usuário". No entanto, por esse caminho, os campos não serão preenchidos automaticamente com os dados já cadastrados **do empregado.**

4. Preencha os campos do cadastro de usuário:

   - **Nome do usuário:** Insira o nome completo (ou nome e sobrenome) do colaborador que utilizará o usuário.
   - **E-mail:** Informe o endereço eletrônico que será utilizado para fazer login na plataforma. Pode ser um e-mail real para que o colaborador receba notificações, [comprovantes de ponto](https://sankhya.zendesk.com/hc/pt-br/articles/42427318874391) e consiga recuperar a senha, ou um e-mail fictício, caso não haja necessidade de comunicação direta. O campo será preenchido automaticamente, caso tenha adicionado o e-mail na seção "campos opcionais" do [cadastro de empregado](https://sankhya.zendesk.com/hc/pt-br/articles/42427347938839).
   - **Senha de acesso ao sistema:** Cadastre uma senha de pelo menos 8 caracteres. Esta senha será utilizada para o acesso ao sistema e pode ser alterada posteriormente.
   - **Telefone:** informe o número de telefone da pessoa que utilizará este usuário. Esse dado é indispensável quando o usuário for o ponto de contato com o suporte da Pontotel. A partir dessa informação, será possível identificá-lo como contato principal e utilizar esse telefone nos chamados que forem abertos.
   - **CPF:** Número do CPF do usuário, usado como dado de identificação. Essa informação é obrigatória para usuários que precisam criar ou editar cadastros na plataforma.
   - **Empregado associado a este usuário:** Permite vincular o usuário a um empregado já cadastrado no sistema. Esse vínculo é necessário quando o usuário será utilizado de forma pessoal pelo colaborador para realizar o registro de ponto.
   - **Código:** Atribua um código único para organizar e identificar o usuário no sistema. Este campo pode facilitar a consulta e o gerenciamento dos registros.
   - **Permissão geral:** Define o nível de acesso do usuário e controla quais funcionalidade estarão disponíveis. Ao selecionar a opção funcionário, o campo "permissão pessoal" não aparecerá. Porém, se o usuário também exercer funções de gestão e, além disso, precisar registrar o ponto, configure neste campo a permissão de gestão e, em "permissão pessoal", atribua a permissão funcionário.
   - Caso queira criar somente um usuário individual sem funções de gestão, selecione a opção "**funcionario**" neste campo.
   - **Permissão pessoal**: Permite atribuir regras específicas de acesso ao usuário, caso possua um empregado vinculado ao usuário. Se o usuário for exclusivo para gestão do ponto, mantenha esse campo em branco.

   ![Exemplo de cadastro de usuário que exerce função de gestão e também realiza registro de ponto](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_ljqrx7.png)

   Exemplo de cadastro de usuário que exerce função de gestão e também realiza registro de ponto

- **Líder desse usuário**: Campo para vincular um líder responsável pelo colaborador, caso seja aplicável.
- **A quem esse usuário terá acesso:** Ao selecionar uma permissão geral que não dê acesso a todos os locais, esse campo aparecerá. Defina aqui os locais, grupos ou liderados aos quais este usuário terá permissão de acesso no sistema para realizar a gestão.

**Exemplo de preenchimento de um usuário individual (sem funções de gestão):**

![Imagem 3: Exemplo de preenchimento de um usuário individual (sem funções de gestão):](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1qz2xf5.png)

5. Configure as **opções avançadas** (opcional):

   - **Gerar senha aleatória e enviar por e-mail**: Quando selecionado, gera automaticamente uma senha e envia para o e-mail cadastrado do usuário.
   - **Exigir troca de senha no primeiro acesso**: Obriga o usuário a redefinir a senha assim que acessar a plataforma pela primeira vez.
   - **Ativar fator de dupla autenticação (MFA)**: Recurso de segurança adicional que exige um segundo fator de autenticação no login (como código enviado por e-mail ou app autenticador).
   - **Considerar este usuário como ponto de contato para o suporte:** ao ativar essa opção, o usuário passa a ser definido como o contato principal da empresa junto ao suporte da Pontotel. Isso significa que seus dados, como telefone e e-mail, poderão ser utilizados nos chamados abertos, facilitando a comunicação e agilizando o atendimento quando houver necessidade de suporte. Por ser um usuário pessoal de funcionário, recomendamos não habilitar esta opção.

   ![Imagem 4: Considerar este usuário como ponto de contato para o suporte: ao ativar essa opção, o usuário passa a ser definido como…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_fygigh.png)
6. Clique no botão **Salvar** para finalizar a criação ou alteração.

---

> ⚠️ Atenção:

- Se a permissão de "funcionario" não estiver aparecendo para ser selecionada, significa que você não iniciou o cadastro pelo caminho correto. Reveja o passo 1 instruído acima.
- Se o colaborador não precisar registrar o ponto em um dispositivo pessoal, nem acessar sua folha ou dados, não há necessidade de criar um usuário com permissão de "funcionario". Nesse caso, o registro de ponto deve ser feito em um dispositivo compartilhado. O login nesse dispositivo deve ser feito com um [usuário coletivo](https://sankhya.zendesk.com/hc/pt-br/articles/42427316408215). Entenda mais sobre permissões [neste artigo](https://sankhya.zendesk.com/hc/pt-br/articles/42427306327575).

---

Cadastrar um usuário com perfil/permissão de funcionário é um processo importante para garantir que cada colaborador tenha acesso adequado às funcionalidades da plataforma. Ao entender como atribuir as permissões corretas, é possível otimizar a gestão de ponto, assegurando que os colaboradores possam registrar suas jornadas de trabalho de maneira eficiente, sem comprometer a segurança das informações.

Caso ainda tenha dúvidas ou precise de auxílio, entre em contato com o nosso time de Suporte pelo chat integrado ao [site Pontotel Gestão](https://gestao.pontotel.com.br/#/cognito/login) ou pelo [WhatsApp](https://api.whatsapp.com/send/?phone=551131852700&text&type=phone_number&app_absent=0).
