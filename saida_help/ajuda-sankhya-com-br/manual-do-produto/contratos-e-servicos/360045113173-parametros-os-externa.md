---
id: "360045113173"
titulo: "Parâmetros OS Externa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113173-Par%C3%A2metros-OS-Externa"
trilha: "Manual do Produto > Contratos e Serviços > Contratos e Serviços"
atualizado_em: "2026-07-29T14:05:18Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Contratos e Serviços", "Ordem de Serviço", "Integração", "CODUSUVISITA", "CONTATOS", "Data de chamada", "Definir senha global", "e-mail", "Limite de acesso", "Nova ordem de serviço", "Número da OS", "OS WEB", "Parâmetros OS Externa", "Prevista para", "SERVOSEXTSNHGL", "Status da avaliação", "Visualizar em PDF", "br.com.sankhya.os.cad.oe.configosexterna", "Parâmetros OS Externa manual", "Configuração de Parâmetros para OS Externa", "Portal Corporativo"]
---

# Parâmetros OS Externa

```
![módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42311247946391) Módulo: Contratos e Serviços > Configurações > Integração com o portal corporativo
```

---

Nesta tela você irá cadastrar as informações necessárias para o lançamentos de uma OS Externa. 

| [Considerações Iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113173-Par%C3%A2metros-OS-Externa#considera%C3%A7%C3%B5esiniciais) |  | [Visualização do histórico da Sub-OS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113173-Par%C3%A2metros-OS-Externa#visualiza%C3%A7%C3%A3odohist%C3%B3ricodasub-os) |
| --- | --- | --- |
| [Configurações OS Externa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113173-Par%C3%A2metros-OS-Externa#configura%C3%A7%C3%B5esosexterna) |  |  |

![Imagem 2: Configurações OS Externa](https://ajuda.sankhya.com.br/hc/article_attachments/360097763713)

## Considerações iniciais

Para começar a utilizar esta tela, você deverá criar um usuário responsável pelo lançamento de OS's.

Logo após, você deverá adicioná-lo ao parâmetro **"Código Usuário Convidado - CODUSUVISITA"**. Esse usuário será utilizado internamente para o lançamento da OS. Quando o usuário logar na área restrita do site e lançar uma OS para o Sistema, quem estará lançando será o usuário visita. Na OS aparecerá **"Lançada por Visita"**.

Este parâmetro é configurado na tela **"Configurações > Avançado > Preferências"** no campo **"Inteiro"**.

**Observação:** mesmo estando esse usuário sem acesso no sistema, ou seja, mesmo que no cadastro de usuários o campo **"Limite de acesso"** já esteja com data expirada para este usuário, ele continuará sendo válido para OS’s externa. Nesse caso o sistema não verifica se o usuário possui ou não acesso.

Feito isto deve-se configurar as seguintes telas:

**1.**CONTRATOS E SERVIÇOS\CONFIGURAÇÕES\INTEGRAÇÃO COM O PORTAL CORPORATIVO\PARÂMETROS OS EXTERNA

**2.**CONTRATOS E SERVIÇOS\CONFIGURAÇÕES\INTEGRAÇÃO COM O PORTAL CORPORATIVO\PARÂMETROS VALIDAÇÃO OS EXTERNA

**3.**CONTRATOS E SERVIÇOS->CONFIGURAÇÕES->INTEGRAÇÃO COM O PORTAL CORPORATIVO->CONTATOS

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113173-Par%C3%A2metros-OS-Externa#top)

## Visualização do histórico da Sub-OS

Para que seja possível visualizar o histórico da SUB-OS, primeiramente configure o parâmetro **"Visualizar sub-OS na OS WEB - VERSUBOSWEB"**.

Se estiver habilitado, irá aparecer no cadastro do Contrato, na Aba **"Propriedades"**, a opção **"Visualizar histórico na consulta Web:"**. Posteriormente acesse o Portal da OS Web.

Se o parâmetro estiver habilitado e a marcação do contrato estiver desmarcada, então a consulta aparecerá com a mensagem na tela:

**"A ordem de serviço não pode ser avaliada na situação"**

**Nota:** o contrato que traz para efetuar abertura de OS Web são os contratos vinculados ao parceiro informado no link da OS Web.

**Observação:** o serviço para abrir a OS Web tem que estar vinculado ao parâmetro **"Código do Serviço da OS Externa - SERVOSEXTSERV"** e este deve ser cadastrado na **"Aba Serviços Autorizados"** do **"Cadastro da Natureza"** vinculado ao contrato.

#### Mensagem para ser apresentada quando o cliente estiver em atraso

O parâmetro **"Mensagem para ser apresentada quando o cliente estiver em atraso - MSGCLIATRAS"** poderá ser utilizado para configurar a mensagem, conforme desejar o usuário, que será apresentada no momento do lançamento de OS para clientes que estão com títulos em atraso, ou seja, quando informado o sistema trará a mensagem informada no parâmetro.

O sistema apresentará a mensagem padrão. Por exemplo: "Cliente em atraso desde o dia 04/06/2007. Total atrasado: R$247,24". 

O sistema faz ainda a validação de atraso, se o parâmetro **"Validação de Atraso - VALATRASOS"** estiver devidamente configurado. Desta forma, tem-se as opções **"Não Valida"**, **"Valida e Aceita"** ou **"Valida e Não Aceita"**, sendo que estas deverão ser configuradas da seguinte forma:

- Desejando que o sistema Valide e Aceite o atraso, insira o valor 1 no campo **"Inteiro"** da tela de configuração do parâmetro;
- Para Não validar e Não aceitar, configura-se o valor 2 no campo acima informado;
- Optando apenas por Não Validar registra-se o valor 0 neste campo.

**Observação:** se for Valida e Aceita o sistema permite o lançamento da OS, mas exibe a mensagem como alerta e se for Valida e Não Aceita o sistema impede o lançamento da OS e mostra a mensagem.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113173-Par%C3%A2metros-OS-Externa#top)

Configurações OS Externa

![Imagem 3: Configurações OS Externa](https://ajuda.sankhya.com.br/hc/article_attachments/360085465474)

Nessa tela defina como a OS externa será aberta. É nela que você informará:

- o serviço para o qual será aberta a OS,
- qual o status da sub-OS,
- qual o tempo do SLA,
- qual o executante da OS, que nesse caso deverá ser uma fila,
- e a forma de autenticação.

No campo **"Texto padrão para a descrição da OS"** pode-se informar um texto padrão para a OS.

A forma de autenticação pode ser: Usar do contato, Global e Sem senha.

Quando for utilizada a forma de autenticação **"Global"** o usuário deverá informar uma senha, clicando no botão **"Definir senha global"**.

No caso da opção **"Por contato"** é necessário definir uma senha na tela de **"Contatos"**.

 
Através da marcação deste do campo **"Origem de atendimento"** todas as Ordens de serviços lançadas pelo site passarão a ter indicadas as suas origens padrão.

A origem deverá ser previamente cadastrada na tela **"Contratos e Serviços > Arquivos > Cadastros > Origem de Atendimento"**.

Assim, após cadastrar uma origem de atendimento e informá-la na tela Parâmetros OS externa, todas as Ordens de serviços abertas pelo site terão o campo Origem do atendimento preenchido automaticamente.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113173-Par%C3%A2metros-OS-Externa#top)

![acesse](https://ajuda.sankhya.com.br/hc/article_attachments/16077918240663) Acesse também:

[Parâmetros Validação OS Externa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113353)

####
