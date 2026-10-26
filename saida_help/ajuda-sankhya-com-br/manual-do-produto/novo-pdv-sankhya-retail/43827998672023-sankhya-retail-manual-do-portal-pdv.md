---
id: "43827998672023"
titulo: "Sankhya Retail: Manual do Portal PDV"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43827998672023-Sankhya-Retail-Manual-do-Portal-PDV"
trilha: "Manual do Produto > Comercial e Vendas > Vendas > Novo PDV – Sankhya Retail"
atualizado_em: "2026-10-01T13:56:21Z"
---

# Sankhya Retail: Manual do Portal PDV

**Módulo:** Sankhya Retail › Portal PDV
**Caminho de acesso:** Portal PDV (acesso via navegador, login com Sankhya Pass)

**Você encontra neste artigo:**

| [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/43827998672023-Sankhya-Retail-Manual-do-Portal-PDV#oque) [Acesso e Segurança](https://ajuda.sankhya.com.br/hc/pt-br/articles/43827998672023-Sankhya-Retail-Manual-do-Portal-PDV#acesso) [Perfis de PDV](https://ajuda.sankhya.com.br/hc/pt-br/articles/43827998672023-Sankhya-Retail-Manual-do-Portal-PDV#perfis) [Gestão de PDV](https://ajuda.sankhya.com.br/hc/pt-br/articles/43827998672023-Sankhya-Retail-Manual-do-Portal-PDV#gestao) | [Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/43827998672023-Sankhya-Retail-Manual-do-Portal-PDV#usuarios) [Certificados Digitais](https://ajuda.sankhya.com.br/hc/pt-br/articles/43827998672023-Sankhya-Retail-Manual-do-Portal-PDV#certificados) [Integrações](https://ajuda.sankhya.com.br/hc/pt-br/articles/43827998672023-Sankhya-Retail-Manual-do-Portal-PDV#integracoes) |
| --- | --- |

## O que é e para que serve

O **Portal PDV** é onde administradores e gerentes configuram e acompanham a operação de Sankhya Retail: perfis de operação, os PDVs (caixas) da loja, os usuários que acessam o Portal ou operam o caixa, os certificados digitais usados na emissão fiscal e as integrações com o ERP, gateways de pagamento e sistemas fiscais. O Portal **não é onde a venda acontece** — isso é feito na Frente de Caixa (PDV); veja o [Manual da Frente de Caixa](https://ajuda.sankhya.com.br/hc/pt-br/articles/43827988337815).

| **Jornada** | **Para que serve** |
| --- | --- |
| **Acesso e Segurança** | Controlar quem entra no Portal e proteger sua sessão |
| **Perfis de PDV** | Definir o que cada operador pode fazer no caixa |
| **Gestão de PDV** | Cadastrar e manter os caixas em funcionamento com licenças ativas |
| **Usuários** | Cadastrar as pessoas que acessam o Portal e vinculá-las a papéis e empresas |
| **Certificados Digitais** | Manter atualizados os certificados usados na emissão fiscal |
| **Integrações** | Conectar o Portal ao ERP, aos gateways de pagamento e ao sistema fiscal |

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/43827998672023-Sankhya-Retail-Manual-do-Portal-PDV#inicio)

---

## Acesso e Segurança

Esta jornada trata de como você entra no Portal, quem tem permissão para acessar cada área e o que acontece quando sua sessão precisa ser encerrada.

### Como funciona

Ao abrir o Portal, o sistema verifica se você já está autenticado. Se estiver, exibe o dashboard direto; se não, mostra a tela de login com o botão **Entrar com Sankhya Pass**. Depois do login, o Portal reconhece seu papel na empresa e libera apenas o que aquele papel pode ver e fazer.

### Quem pode entrar

Apenas dois papéis têm acesso ao Portal: **Administrador** e **Gerente**.

**⚠️ Atenção**

Se você for cadastrado como **Operador** ou **Supervisor**, o login é recusado e uma mensagem informa que seu papel não tem permissão — nenhuma informação da sessão fica guardada no navegador. Procure seu administrador para revisar seu papel.

Se sua conta estiver **inativa**, o sistema não permite a entrada e exibe uma mensagem de credenciais inválidas — procure o administrador para reativar seu acesso.

### Sessão

- **Sessão inválida ou corrompida** — o sistema limpa tudo automaticamente e leva você de volta ao login, para proteger sua conta.
- **Sessão expirada** — quando o prazo termina (ou o servidor detecta que a autenticação não é mais válida), o Portal limpa a sessão, leva você ao login e marca que a saída foi por segurança.

### Sair do Portal

1. Clique na opção de sair do sistema (logout).
2. Confirme na janela que explica que você será desconectado.
3. Ao confirmar, o Portal apaga as informações da sessão e leva você ao login. Se fechar a janela sem confirmar, a sessão continua ativa.

Exemplos: um Gerente que acabou de logar vê o dashboard e a barra lateral completa; um Operador que tenta logar recebe a mensagem de papel bloqueado; uma sessão parada por muito tempo expira sozinha ao clicar em qualquer tela.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/43827998672023-Sankhya-Retail-Manual-do-Portal-PDV#inicio)

---

## Perfis de PDV

Um Perfil de PDV é um conjunto de regras que define o que os operadores podem fazer no caixa: aplicar descontos, cancelar vendas, excluir itens, entre outras ações.

### Como funciona

Ao abrir **Perfis de PDV**, você vê a lista de perfis cadastrados. Para criar um, clique em **Novo** e preencha o formulário; para editar ou excluir, selecione um perfil na lista e clique em **Editar** ou **Excluir** (a exclusão pede confirmação).

#### Descrição do perfil

**O que faz:** identifica o perfil na lista.

**Como funciona:** é obrigatória e precisa ter no mínimo 2 caracteres — preencher só com espaço em branco conta como vazio. Sem preencher, o sistema mostra "Descrição é obrigatório"; com menos de 2 caracteres, "Descrição deve ter ao menos 2 caracteres", e o formulário permanece aberto.

#### Percentual máximo de desconto

**O que faz:** define o teto de desconto (no item ou no total) que operadores desse perfil podem aplicar sem autorização de um gerente.

**Quando usar:** preencha sempre que habilitar **desconto no total da venda** ou **desconto no item**.

**Como funciona:** marcar qualquer uma dessas duas opções sem informar o percentual máximo bloqueia o salvamento com a mensagem "Percentual obrigatório". Se nenhum desconto for habilitado, o sistema grava o percentual como zero automaticamente.

#### Estado ativo

**O que faz:** define se o perfil está disponível para uso.

**Como funciona:** ao **criar**, o perfil é sempre gravado como **ativo**, independentemente do que você marcar no formulário. Ao **editar**, o estado ativo/inativo respeita o que você escolher.

**ℹ️ Nota**

Se o servidor rejeitar o cadastro (ex.: descrição duplicada ou falha ao criar), o formulário permanece aberto com os dados preenchidos, e nada é perdido.

Exemplos: um perfil "Operador Padrão" sem nenhuma permissão de desconto, exclusão ou cancelamento; um perfil "Supervisor Loja" com desconto por item (até 10%), exclusão de itens e cancelamento de venda.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/43827998672023-Sankhya-Retail-Manual-do-Portal-PDV#inicio)

---

## Gestão de PDV

A Gestão de PDV é onde você cadastra e administra os pontos de venda (caixas) da operação. Cada PDV precisa de um identificador único, dados fiscais e uma licença ativa para funcionar.

### Como funciona

Ao abrir **Gestão de PDV**, você vê quatro cartões no topo (quantidade de licenças em cada estado: **Licenças Ativas**, **Aguardando ativação**, **Não registrado** e **Licenças Inativas**) e a lista de caixas cadastrados. Para criar um novo, clique em **Novo PDV**.

#### PDV ID (identificador)

**O que faz:** código único que identifica o caixa no sistema.

**Como funciona:** definido na criação. Depois de salvo, **fica bloqueado** — não pode ser alterado na edição, para preservar a integridade fiscal.

#### Séries fiscais (normal e contingência)

**O que faz:** numeram os documentos fiscais (NFC-e) emitidos pelo caixa, em modo normal e em modo contingência.

**Como funciona:** cada PDV recebe automaticamente as duas séries, ambas do tipo NFC-e, começando em 1 até o limite padrão configurado.

**Impacto no sistema:** depois de criadas, o tipo de documento fiscal e a numeração (início/fim) de ambas as séries ficam **bloqueados** na edição.

Você também pode editar livremente as informações não-fiscais de um PDV já cadastrado, como nome e perfil — mas não a **Empresa**, que também fica bloqueada após a criação.

**ℹ️ Nota**

Se o servidor rejeitar o cadastro (ex.: bloqueio administrativo), o formulário permanece aberto com a mensagem do motivo, e nenhum caixa é criado.

### Ciclo de licenças

Cada PDV nasce **Não Registrado** e precisa de um PIN para se conectar:

1. **Gerar PIN** — disponível para um PDV Não Registrado; o sistema gera um código de 6 dígitos (ex.: 123 456) para você repassar ao operador do caixa. Assim que o PDV usa o PIN, a licença passa a **Aguardando ativação** e depois a **Ativa**.
2. **Revogar Licença** — só para PDVs com licença **Ativa**; pede confirmação antes de encerrar.
3. **Resolver Conflito** — aparece quando o mesmo identificador foi ativado em outro dispositivo; ao clicar em **Resolver Pendência**, o sistema encerra o conflito e gera um novo PIN para reativação.

Exemplos: cadastrar o "Caixa 03" e vê-lo como Não Registrado; gerar o PIN e repassar ao operador para concluir a ativação; detectar ativação duplicada, resolver o conflito e gerar um novo PIN para o equipamento correto.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/43827998672023-Sankhya-Retail-Manual-do-Portal-PDV#inicio)

---

## Usuários

A tela de Usuários é onde você cadastra as pessoas que acessam o Portal ou operam o PDV, define seus papéis e vincula às empresas.

### Como funciona

A lista mostra os cadastros identificados pelo e-mail. Para criar, clique em **Novo Usuário** e preencha nome, sobrenome, CPF, celular (apenas números), e-mail, **papel** (Administrador, Gerente, Operador ou Supervisor) e as empresas vinculadas.

#### Cadastro em três etapas

**Como funciona:** ao salvar, o Portal executa em sequência: (1) cadastra o usuário, (2) vincula o papel selecionado, (3) vincula à conta principal. O cadastro só é considerado concluído quando as três etapas terminam com sucesso.

**Impacto no sistema:** se a 1ª etapa falhar (ex.: e-mail já existente), o sistema mostra a mensagem do servidor (ex.: "E-mail já cadastrado no sistema") e o formulário permanece aberto. Se a 2ª falhar, a cadeia é interrompida e a 3ª não acontece. Em qualquer falha, a lista de usuários não muda.

#### Estado ativo

**Como funciona:** ao **criar**, o usuário é sempre gravado como **ativo**, e o padrão é **não enviar e-mail de verificação**, independentemente do formulário. Ao **editar**, o estado ativo/inativo respeita o que você marcar.

#### Celular

**Como funciona:** informe apenas números — o campo não aceita caracteres especiais, como parênteses e hífen. Se um valor cadastrado antigamente não seguir esse padrão, o campo abre **vazio** na edição — você precisa preencher de novo antes de salvar.

#### Empresas vinculadas

**Como funciona:** marque ou desmarque empresas na lista para vincular ou remover. A atualização é sempre enviada como a **lista completa** de empresas escolhidas — não um incremento.

**ℹ️ Nota**

O papel selecionado é sempre reenviado ao salvar, mesmo sem troca, para garantir que o vínculo permaneça correto.

Exemplos: cadastrar "Ana Oliveira" como Gerente vinculada à Matriz e à Filial; tentar um e-mail duplicado e ver "E-mail já cadastrado no sistema"; adicionar a Filial a um usuário que só tinha a Matriz — o Portal envia a lista completa (Matriz + Filial) ao salvar.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/43827998672023-Sankhya-Retail-Manual-do-Portal-PDV#inicio)

---

## Certificados Digitais

Gerencie os certificados digitais A1 usados pelas empresas para emissão de notas fiscais (NFC-e).

### Como funciona

A lista mostra os certificados cadastrados, identificados pelo alias. Para cadastrar, clique em **Novo Certificado** e preencha o arquivo do certificado (.pfx), a senha, a empresa vinculada, o **ID do CSC** e o **Token do CSC**.

**⚠️ Atenção**

O botão **Enviar** só fica habilitado depois de você selecionar um arquivo — sem arquivo, mesmo forçando o clique, nada é transmitido. Todos os campos (senha, empresa, CSC ID e CSC Token) são obrigatórios.

Se o servidor rejeitar o envio (erro ou timeout), a janela permanece aberta com os dados preenchidos e a lista não muda — você pode tentar novamente sem preencher tudo de novo. Para excluir, selecione um certificado, clique em **Excluir** e confirme; só o certificado selecionado é removido.

Exemplos: renovar o certificado da Empresa Matriz enviando o novo .pfx; cadastrar um certificado por filial; tentar enviar com senha errada e ver a janela permanecer aberta para correção.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/43827998672023-Sankhya-Retail-Manual-do-Portal-PDV#inicio)

---

## Integrações

Cadastre as conexões do Portal com outros sistemas: ERP Sankhya, gateways de pagamento e sistemas fiscais.

### Como funciona

O menu lateral organiza as integrações em três subitens — **ERP Sankhya**, **Gateway de Pagamento** e **Fiscal** — e cada um mostra só as integrações daquele tipo. Para cadastrar, clique em **Novo** e preencha a descrição e os campos específicos do tipo:

| **Tipo** | **Campos específicos** |
| --- | --- |
| **ERP Sankhya** | xToken, tentativas, timeout |
| **Gateway de Pagamento** | URL, provedor, apiKey, apiSecret |
| **Fiscal** | ID da empresa |

#### Campos sensíveis na edição

**Como funciona:** para proteger informações críticas, alguns campos ficam **bloqueados** ao editar, mesmo visíveis: xToken (ERP Sankhya); apiKey e apiSecret (Gateway de Pagamento); idempresa (Fiscal).

**Impacto no sistema:** para trocar um campo sensível, o caminho é excluir a integração e cadastrar uma nova com as credenciais atualizadas — não há edição direta desses campos.

Ao excluir uma integração, só o registro daquele tipo é removido; os demais tipos e registros continuam intactos.

Exemplos: cadastrar uma integração ERP Sankhya com 3 tentativas e timeout de 30s; trocar a apiKey de um gateway excluindo e recriando a integração; excluir uma integração fiscal antiga sem afetar as demais.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/43827998672023-Sankhya-Retail-Manual-do-Portal-PDV#inicio)
