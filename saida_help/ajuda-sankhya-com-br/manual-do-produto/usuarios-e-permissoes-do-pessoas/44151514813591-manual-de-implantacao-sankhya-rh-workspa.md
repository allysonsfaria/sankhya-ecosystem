---
id: "44151514813591"
titulo: "Manual de Implantação — Sankhya RH Workspace 2.0"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44151514813591-Manual-de-Implanta%C3%A7%C3%A3o-Sankhya-RH-Workspace-2-0"
trilha: "Manual do Produto > Pessoas+ > Implantação e Acessos do Pessoas+ > Usuários e Permissões do Pessoas+"
atualizado_em: "2026-10-22T18:51:32Z"
---

# Manual de Implantação — Sankhya RH Workspace 2.0

**Público-alvo:** Consultores de implantação e equipes responsáveis pela ativação do Sankhya RH Workspace.

### Visão geral

O **Sankhya RH Workspace** centraliza o acesso às soluções contratadas de **Gestão de Pessoas** por meio de um único endereço e autenticação integrada com o **Sankhya Pass**. Conforme os produtos contratados, o ambiente pode disponibilizar soluções como **Portal RH**, **Pontotel**, **Mindsight** e **Vixting**.

Ele tem duas partes principais:

- **Widgets:** resumos com informações dos produtos integrados ao Workspace, que facilitam o acompanhamento de informações relevantes. Ao clicar em um widget, o colaborador é direcionado à tela correspondente no produto.
- **Pendências:** lista centralizada de tarefas que o colaborador precisa realizar nos produtos integrados, como responder a avaliações ou aprovar requisições. Conforme as tarefas são concluídas nos respectivos produtos, elas deixam de aparecer na lista.

A implantação deve considerar o ambiente do cliente, a utilização do Sankhya Om, a situação do Sankhya Pass e o método de autenticação adotado.

### Antes de começar

Antes de iniciar o processo, valide os requisitos a seguir.

#### 1. Contratação e ambiente

- O cliente deve ter contratado o **Pessoas+** e **pelo menos mais uma solução de Gestão de Pessoas**, como Pontotel, Mindsight ou Vixting.
- Se o cliente **não tiver o Pessoas+**, consulte o time Sankhya RH.
- O ambiente deve estar hospedado na **Sankhya Cloud**. O Workspace RH não está disponível para ambientes On-Premise.

#### 2. Versões e informações técnicas

- A versão mínima do Pessoas+ deve ser 5.85.0.
- O campo **E-mail Corporativo** deve estar preenchido no cadastro dos colaboradores.
- Se o cliente utilizar Sankhya Om, a versão mínima exigida é:
  - `4.36b78`, para ambientes na versão 4.36;
  - `4.35b814`, para ambientes na versão 4.35.
- O ambiente Sankhya Om deve utilizar HTTPS com certificado SSL válido.
- Solicite a URL do Sankhya Om e o código do parceiro (**CodParc**).

| **⚠️** **Atenção**  Valide a compatibilidade das versões antes de iniciar a configuração. |
| --- |

#### 3. Informações para o levantamento inicial

Identifique se o cliente é uma nova implantação ou se já possui uma base em funcionamento. Para registrar as informações iniciais, utilize o formulário **Formulário de levantamento — Sankhya RH Workspace**.

Após garantir o preenchimento do forms, analise as informações necessárias para identificar o cenário de implantação.

O levantamento deve permitir definir se será necessário ativar o Sankhya Pass no Sankhya Om, envolver o time responsável pela autenticação externa ou realizar diretamente a criação dos acessos dos colaboradores.

### Etapas da implantação

#### Etapa 1 — Preparar o cadastro dos colaboradores

Antes de criar os usuários e os acessos, confira se o cadastro de cada colaborador contém o endereço de e-mail corporativo.

- **Caminho de acesso:** Pessoas+ > Cadastros > Configuração Funcionários:
  - aba Pessoal > campo **Email Corporativo**.

O e-mail informado deve corresponder ao e-mail que será utilizado pelo colaborador na autenticação. Verifique se ele está correto e se não há divergências entre os cadastros e as soluções integradas. Exemplo: Pessoas+ e Pontotel.

Se a empresa utilizar uma integração de admissão que preencha esse campo automaticamente, confirme se o dado foi importado corretamente.

Quando o e-mail estiver armazenado em um campo personalizado ou em outro local, avalie a adequação do cadastro para que o processo de criação dos acessos utilize o campo **Email Corporativo**.

📚 Para conhecer as regras do campo, consulte [Uso do E-mail Corporativo no Sankhya Pass e no Workspace RH](https://ajuda.sankhya.com.br/hc/pt-br/articles/40497635266583-Uso-do-E-mail-Corporativo-no-Sankhya-Pass-e-no-Workspace-RH).

#### Etapa 2 — Identificar o cenário de autenticação

Com as informações levantadas, identifique o cenário do cliente e siga o procedimento correspondente.

**Cenário A — O cliente utiliza Sankhya Om e já possui Sankhya Pass ativo**

1. Confirme se os colaboradores que utilizarão o Workspace possuem acesso ao Sankhya Pass.
2. Prossiga para a criação do acesso ao Workspace RH.
3. Realize o teste de acesso.

**Cenário B — O cliente utiliza Sankhya Om, mas ainda não possui Sankhya Pass ativo**

1. Siga o [procedimento oficial de ativação do Sankhya Pass no Sankhya Om](https://ajuda.sankhya.com.br/hc/pt-br/articles/41182140813719).
2. Quando necessário, envolva o responsável pela ativação para concluir as configurações.
3. Depois de confirmar que o Sankhya Pass está ativo, confira os cadastros e os e-mails corporativos dos colaboradores.
4. Prossiga para a criação do acesso ao Workspace RH.
5. Realize o teste de acesso.

**Cenário C — O cliente utiliza autenticação externa por Google ou Microsoft**

Quando a implantação depender da integração de autenticação externa, alinhe a configuração com o **time responsável pelo Sankhya Pass**.

1. Confirme qual provedor de autenticação será utilizado.
2. Agende o alinhamento técnico necessário para ativar a integração.
3. Após a configuração, valide a autenticação e a disponibilidade dos acessos.
4. Prossiga para a criação do acesso ao Workspace RH.
5. Realize o teste de acesso.

A disponibilidade e o comportamento da autenticação externa devem ser confirmados conforme a configuração efetivamente adotada pelo cliente.

#### Etapa 3 — Incluir os usuários dos colaboradores no Sankhya Pass

Antes de liberar o acesso ao Workspace RH, os colaboradores precisam ter uma conta no Sankhya Pass ativa.

Para **clientes que contrataram somente a suíte Sankhya RH** e **não utilizam o Sankhya Om**, o consultor pode solicitar a criação dos usuários individualmente ou em lote diretamente pela tela **Configuração Funcionários** (Pessoas+ > Cadastros), no Pessoas+.

- **Para criar o usuário de um colaborador:**
  1. Acesse a tela [**Configuração Funcionários**](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639) (Pessoal+ > Cadastros).
  2. Localize e selecione o colaborador desejado.
  3. No menu **Outras opções**, selecione **Criar Sankhya Pass**.
  4. Verifique o resultado da operação pela opção **Consultar Integração com o Sankhya Pass**.
- **Para criar usuários de vários colaboradores:**
  1. Acesse a tela **Configuração Funcionários**.
  2. Selecione os colaboradores para os quais deseja criar usuários no Sankhya Pass.
  3. No menu **Outras opções**, selecione **Criar Sankhya Pass**.

Durante a criação, o sistema valida se o colaborador já possui acesso ao Sankhya Pass e se o CPF e o e-mail cadastrados são válidos. Se houver inconsistências, o acesso não será criado e o sistema informará o motivo.

Após a solicitação, o colaborador receberá um e-mail com as instruções para ativar a conta. **A ativação deve ser realizada pelo próprio colaborador.**

Quando o cliente utiliza autenticação externa, como Google ou Microsoft, siga o fluxo de autenticação configurado para esse ambiente.

📚 Para consultar o procedimento de acesso, veja [Sankhya RH Workspace: o que é e como acessar](https://ajuda.sankhya.com.br/hc/pt-br/articles/36777482253463-Sankhya-RH-Workspace-o-que-%C3%A9-e-como-acessar).

O consultor pode acompanhar o processamento pela opção **Consultar Integração com o Sankhya Pass**.

**Se o cliente utiliza Sankhya Om**, siga o procedimento de ativação correspondente descrito no artigo [Processo Ativação do Sankhya Pass](https://ajuda.sankhya.com.br/hc/pt-br/articles/41182140813719-Processo-Ativa%C3%A7%C3%A3o-do-Sankhya-Pass).

#### Etapa 4 — Validar o fluxo com um usuário de teste

Antes de executar o processo para todos os colaboradores, crie um usuário de teste e valide o fluxo completo de acesso ao Workspace RH.

1. Confirme a criação do usuário no Sankhya Pass.
2. Verifique o e-mail recebido e conclua a ativação da conta.
3. Confirme se o Sankhya Pass está ativo.

Após validar o fluxo, execute o procedimento para os demais colaboradores, orientando cada um a concluir a ativação da conta pelo e-mail recebido.

#### Etapa 5 — Criar o acesso ao Workspace RH no cadastro do colaborador

Após confirmar que o colaborador possui o Sankhya Pass ativo, crie o acesso ao Workspace RH.

1. Acesse a tela [**Configuração Funcionários**](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639) (Pessoas+ > Cadastros).
2. Localize o cadastro do colaborador.
3. Acesse a aba **Pessoal** e confira se o campo **Email Corporativo** está preenchido corretamente.
4. Clique no botão **Outras opções**, no canto superior direito da tela.
5. Selecione **Criar acesso ao Workspace RH**.
6. Aguarde o processamento da solicitação.

A criação do acesso é processada de forma assíncrona. Portanto, a solicitação pode não ser concluída imediatamente.

**Consultar a situação da ativação**

Para verificar o resultado do processamento:

1. Mantenha aberto o cadastro do colaborador na tela **Configuração Funcionários**.
2. Abra novamente o menu de opções adicionais do botão **Outras opções**.
3. Selecione **Consultar ativação de acesso ao Workspace RH**.
4. Verifique a situação apresentada pelo sistema e, se necessário, siga as orientações indicadas.

| **⚠️** **Atenção**  O colaborador precisa ter acesso ativo ao Sankhya Pass. A criação do acesso ao Workspace RH não substitui a ativação do Sankhya Pass. |
| --- |

#### Etapa 6 — Testar o acesso ao Sankhya RH Workspace

Depois de concluir as configurações, valide o acesso com um colaborador preparado para a autenticação.

1. Acesse o endereço do Workspace RH: <https://rh.sankhya.com.br/> pelo navegador.
2. Clique em **Entrar com Sankhya Pass**.
3. Informe o e-mail utilizado na autenticação.
4. Conclua o login conforme o método configurado para o cliente.
5. Após entrar, confira se as soluções esperadas estão disponíveis para o perfil do colaborador.
6. Selecione uma solução e confirme se o acesso funciona corretamente.

### Tratamento de falhas

Se o teste de acesso não funcionar, verifique os itens abaixo antes de abrir um chamado.

**O colaborador não consegue entrar**

- Confirme se o acesso ao Sankhya Pass está ativo.
- Confira se o e-mail utilizado no login corresponde ao cadastro do colaborador.
- Verifique se o E-mail Corporativo está preenchido corretamente.
- Confirme se a criação do acesso ao Workspace RH foi solicitada e se o processamento foi concluído.
- Verifique se a autenticação externa, quando utilizada, foi configurada corretamente.

**O colaborador consegue entrar, mas não visualiza uma solução**

O Workspace RH apresenta as soluções disponíveis conforme as permissões do usuário em cada produto.

Nesse caso:

1. Confirme quais soluções foram contratadas pelo cliente.
2. Verifique se o colaborador possui cadastro e permissões na solução que deseja acessar.
3. Confirme se o e-mail está corretamente cadastrado nos ambientes envolvidos.
4. Verifique se a solução está integrada ao fluxo de autenticação utilizado.

O Workspace RH não substitui o gerenciamento de usuários e permissões de cada solução. Essas configurações devem ser verificadas diretamente no produto correspondente.

#### Quando acionar o time Sankhya RH

Se as validações não resolverem o problema, entre em contato com o time Sankhya RH.

Informe:

- identificação do cliente e do ambiente;
- URL do ambiente Sankhya Om, quando aplicável;
- identificação do colaborador afetado;
- e-mail utilizado na autenticação;
- descrição do cenário e das etapas executadas;
- mensagem de erro, se houver;
- capturas de tela;
- logs disponíveis;
- resultado da consulta de ativação do acesso ao Workspace RH.

Essas informações ajudam a identificar se a falha está relacionada ao cadastro do colaborador, à ativação do Sankhya Pass, à criação do acesso ao Workspace ou às permissões das soluções.

### Perguntas frequentes

**1. O Sankhya Pass e o Workspace RH são ativados pela mesma opção?**

Não. A ativação do Sankhya Pass segue o procedimento próprio de integração e ativação. A criação do acesso ao Workspace RH é solicitada separadamente, pelo menu de opções adicionais da tela Configuração Funcionários.

**2. Onde crio o acesso de um colaborador ao Workspace RH?**

Acesse **Pessoas+ > Cadastros > Configuração Funcionários**, abra o cadastro do colaborador e, no botão Outras Opções, selecione **Criar acesso ao Workspace RH**.

**3. Como verifico se a ativação foi concluída?**

No mesmo menu, selecione **Consultar ativação de acesso ao Workspace RH**.

**4. O colaborador precisa ter o E-mail Corporativo preenchido?**

Sim. O campo E-mail Corporativo é utilizado na criação dos acessos ao Sankhya Pass e ao Workspace RH. Confira o preenchimento antes de solicitar a criação do acesso.

**5. O colaborador acessa o Workspace, mas não vê uma das soluções contratadas. O que devo verificar?**

Verifique se o colaborador possui permissões na solução e se seu cadastro está correto no produto correspondente. A visualização no Workspace depende das permissões configuradas em cada solução.

**6. O que fazer se o acesso continuar falhando?**

Confira o cadastro, o e-mail corporativo, o acesso ao Sankhya Pass e a situação da ativação do Workspace RH. Se o problema persistir, abra um chamado interno para o time Sankhya RH com as evidências disponíveis.
