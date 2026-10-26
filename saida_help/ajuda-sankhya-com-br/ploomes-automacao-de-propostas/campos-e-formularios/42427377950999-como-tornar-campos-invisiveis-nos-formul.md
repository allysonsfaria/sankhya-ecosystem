---
id: "42427377950999"
titulo: "Como tornar campos invisíveis nos formulários"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427377950999-Como-tornar-campos-invis%C3%ADveis-nos-formul%C3%A1rios"
trilha: "PLOOMES: Automação de propostas  > Campos e formulários"
atualizado_em: "2026-08-10T18:00:04Z"
rotulos: ["sync_hc", "ploomes_5452348", "ploomes", "sync_hash_5e629f9b2348"]
---

# Como tornar campos invisíveis nos formulários

Este artigo tem por finalidade explicar como tornar um campo invisível nos formulários. Fazer o procedimento é bastante simples, mas o interessante mesmo é o que pode ser realizado através desta possibilidade.

## Exemplos práticos

### Caso de uso 1:

**Necessidade**: é necessário puxar o limite de crédito de um cliente por uma integração com um ERP e esta informação precisa ser exibida no cadastro do cliente

**Problema**: não desejamos que o campo "Limite de crédito" esteja no formulário de contato porque não faria sentido perguntar esta informação ao usuário no momento do cadastro.

**Solução**: deixar este campo disponível no formulário para ser exibida no perfil do cliente, porém sem que o usuário veja e tenha que preencher.

### Caso de uso 2:

**Necessidade**: criação de campos para armazenar valores intermediários que servirão para compor o resultado de uma fórmula.

**Problema**: os campos poluiriam o formulário.

**Solução**: escondê-los no formulário de criação e/ou edição de propostas, vendas, negócios e documentos.

## Como fazer

Para esconder um campo no formulário basta seguir os passos:

1. Vá até a tela de configuração de formulário em **Administração > Campos** **e formulários**;

   ![Imagem 1: Vá até a tela de configuração de formulário em Administração > Campos e formulários ;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1390823285/61bcc46b39a41dcb544c0ff3a023/image.png?expires=1786536000&signature=44deb979b30f90f367aeb27ca0362d0502902380b4957b3cd089afdf8e962915&req=dSMuFsF8noNXXPMW3nq%2BgQgEKkmYE8RaGZtjuDLY5wGvZ5bQQTLnrFPFrH6w%0Ac4pOJdTWjBP1OIG%2F4utTZtiXWEk%3D%0A)
2. Selecione o formulário desejado;
3. Localize ou insira o campo que deseja deixar oculto no formulário;
4. Passe o mouse sobre ele e clique no ícone ✏️ para editar o campo;
5. Localize a seção "Configurações de visualização do campo" e clique sobre ela para expandir;

   ![Imagem 2: Localize a seção "Configurações de visualização do campo" e clique sobre ela para expandir;](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1390825782/61b4de676419d5a2ea582c1ad3d1/image.png?expires=1786536000&signature=2dfb91ecedb03322458230c8a3d375ab0ea1de1de88abc0271b2370d51afbbd7&req=dSMuFsF8mIZXW%2FMW3nq%2BgbZGDPQXjVQfWup3BrtOwkbdeCXMeGpxBijiu%2BuW%0AZduFulKE8Y97Blj9%2BlRRBnQXWNA%3D%0A)
6. ative o checkbox "Ocultar por padrão":

Ao marcar esta opção, o campo será automaticamente ocultado no seu formulário de edição e criação, porém continuará disponível para ser manipulado via API ou pelas fórmulas.

**Obs.:** o campo ainda fica visível na tela de configuração de formulários, porém não mais no formulário de cadastro/edição da entidade em questão. Usuários Administradores podem ver os campos ocultos no formulário utilizando o atalho do teclado Shift + F
