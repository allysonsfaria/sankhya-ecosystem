---
id: "360045113353"
titulo: "Parâmetros Validação OS Externa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113353-Par%C3%A2metros-Valida%C3%A7%C3%A3o-OS-Externa"
trilha: "Manual do Produto > Contratos e Serviços > Contratos e Serviços"
atualizado_em: "2026-07-29T14:05:27Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Parceiro", "Contratos e Serviços", "Ordem de Serviço", "Integração", "CODUSUVISITA", "CONTATOS", "Data de chamada", "Definir senha global", "e-mail", "Limite de acesso", "Nova ordem de serviço", "Número da OS", "OS WEB", "Parâmetros OS Externa", "Prevista para", "SERVOSEXTSNHGL", "Status da avaliação", "Visualizar em PDF", "Parâmetros Validação OS Externa", "br.com.sankhya.os.cad.oe.validacaoosexterna", "Parâmetros Validação OS Externa manual", "Configuração de Validação de Parâmetros para OS Externa"]
---

# Parâmetros Validação OS Externa

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42311232169367) Módulo: Contratos e Serviços > Configurações > Integração com o portal corporativo
```

---

Nesta, realize as configurações necessárias para a validação dos parâmetros lançados na tela [Parâmetros OS Externa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113173).

| [Considerações Iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113353-Par%C3%A2metros-Valida%C3%A7%C3%A3o-OS-Externa#considera%C3%A7%C3%B5esiniciais) |  | [Configuração dos parâmetros OS Externa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113353-Par%C3%A2metros-Valida%C3%A7%C3%A3o-OS-Externa#configura%C3%A7%C3%A3odospar%C3%A2metrososexterna) |
| --- | --- | --- |

![Imagem 2: Configuração dos parâmetros OS Externa](https://ajuda.sankhya.com.br/hc/article_attachments/360095458354)

## Considerações iniciais

Para começar a utilizar esta tela, você deverá criar um usuário responsável pelo lançamento de OS's.

Logo após, deve-se adicioná-lo ao parâmetro **"Código Usuário Convidado - CODUSUVISITA"**. Esse usuário será utilizado internamente para o lançamento da OS. Quando o usuário logar na área restrita do site e lançar uma OS para o Sistema, quem estará lançando-a será o usuário visita. Na OS aparecerá “Lançada por Visita”.

Este parâmetro é configurado na tela **"Configurações > Avançado > Preferências"** no campo **"Inteiro"**.

**Observação:** mesmo com esse usuário sem acesso no sistema, ou seja, mesmo que no cadastro de usuários o campo **"Limite de acesso"** já esteja com data expirada para este usuário, ele continuará sendo válido para OS’s externa. Nesse caso o sistema não verifica se o usuário possui ou não acesso.

Feito isto deve-se configurar as seguintes telas:

**1.**CONTRATOS E SERVIÇOS\CONFIGURAÇÕES\INTEGRAÇÃO COM O PORTAL CORPORATIVO\PARÂMETROS OS EXTERNA

**2.**CONTRATOS E SERVIÇOS\CONFIGURAÇÕES\INTEGRAÇÃO COM O PORTAL CORPORATIVO\PARÂMETROS VALIDAÇÃO OS EXTERNA.

**3.**CONTRATOS E SERVIÇOS->CONFIGURAÇÕES->INTEGRAÇÃO COM O PORTAL CORPORATIVO->CONTATOS.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113353-Par%C3%A2metros-Valida%C3%A7%C3%A3o-OS-Externa#top)

## Configuração dos Parâmetros Validação OS Externa

Assim que o problema descrito no lançamento da OS for solucionado e um item da OS encaminhado para uma determinada fila, utilizando o serviço 50324-INT-VALIDAÇÃO DE VERSÃO, com Status para validação PENDENTE: VALIDAÇÃO CLIENTE PENDENTE, o sistema irá disparar um e-mail com o conteúdo do campo **"Email de notificação do parceiro"** mais o conteúdo adicionado no item da sub - OS, para o contato da OS.

Na tela **"Configurações > Cadastros > Parceiros"** na aba **"Contatos"** verifique, se o e-mail do **"Contato do Parceiro"** está correto.

Será enviado no e-mail de validação da OS o Nome do Parceiro da OS.

Tela Lançamento de OS:

![Imagem 3: Tela Lançamento de OS:](https://ajuda.sankhya.com.br/hc/article_attachments/9304891187607)

Tela Parâmetros Validação OS Externa:

![Imagem 4: Tela Parâmetros Validação OS Externa:](https://ajuda.sankhya.com.br/hc/article_attachments/9304881692823)

Configurações> Avançado> Envio de Mensagens> Fila:

![Imagem 5: Configurações> Avançado> Envio de Mensagens> Fila:](https://ajuda.sankhya.com.br/hc/article_attachments/360086684333)

Assim, o e-mail enviado conterá um link que ao ser clicado abrirá uma tela do Sankhya-Om para o usuário validar ou não, a solução.

Caso o parceiro não realize a verificação o sistema irá reenviar o e-mail a cada X dias, conforme configurado no campo **"Reenviar a cada X dia(s)"**, cobrando a validação.

Validando ou não, ao salvar automaticamente é enviado um e-mail para o destinatário vinculado à fila, para validação que foi definida na tela Parâmetros Validação OS Externa. Esse e-mail terá a informação se o parceiro validou ou não, a solução da OS.

**Observação:** vinculou-se um destinatário a uma fila através do campo Código de Usuário.

Para integrar o componente de lançamento/visualização de OS no portal da empresa é necessário que o Webmaster responsável pela criação/manutenção do site adicione um FRAME html para a seguinte URL:

**$URL\_DO\_SERVIDOR**/mge/MGEIntegracao?servico=guestacess&parceiro=$CODPARC&email=$EMAIL&senha=$SENHA&redirect=/mgeos/OSPortal.mgeos?acao=novaOS&codParc=$CODPARC&limparFiltro=1

- Descrição das variáveis prefixadas com $:

**$URL\_DO\_SERVIDOR**  = é a URL externa pela qual se pode acessar o Sankhya-W pela internet. Não é o endereço interno do servidor, ou seja, não é algo do tipo 192.168.0.1, mas sim algo do tipo http://minha\_empresa.com.br

**$CODPARC**  = Código do parceiro logado no site. Esse código é o código de cadastro do parceiro no Sankhya-W (ou MGE/Mitra/G1 etc). Geralmente o site possui um cadastro próprio de clientes, então esse campo deve ser vinculado a esse cadastro próprio do site pelo webmaster do site.

**$EMAIL**   = e-mail do contato do parceiro que está logado no site. Esse e-mail é o mesmo que foi cadastrado no Sankhya-W (ou MGE/Mitra/G1 etc) aba de contatos do cadastro de parceiros.

**$SENHA**  = senha de acesso definida no cadastro do contato (só é necessário se na configuração da OS externa o tipo de autenticação estiver como 'Contato'. Para testes pode-se usar o tipo de autenticação como "Sem senha" mas para colocar em produção deve-se usar Contato ou Senha global, veja mais detalhes na documentação de configuração da OS externa).

Importante: para a utilização da funcionalidade através do site do cliente, você deverá atentar-se aos seguintes pontos:

- Deve-se criar no site uma parte destinada a essa funcionalidade. O cliente deverá entrar em contato com o pessoal responsável pela manutenção do site da sua empresa e informar que deseja acrescentar uma área no site para esse tipo de acesso.
- Deve-se colocar um link que direcionará para a área de OS Externa.

Exemplo de link: https://skw.sankhya.com.br/mge/MGEIntegracao?servico=guestacess&parceiro=647&email=roberto.torres@sankhya.com.br&senha=ebdcf817c51f265309cb5dd74edc976b&redirect=/mgeos/OSPortal.mgeos.

O link possui o caminho do Servidor, o Parceiro, o E-mail e Senha.

O responsável pela manutenção do site deverá montar o link juntamente com o cliente.

Como é necessário informar no link a senha que é criptografada, no caso do uso da forma de autenticação Global, é necessário utilizar o parâmetro **"Senha global para acesso externo -SERVOSEXTSNHGL"** para capturá-la.

Então a senha deverá ser incluída no link, logo depois de “senha=”, conforme observado no link do exemplo acima.

Nessa tela o usuário poderá optar por filtrar OS ou lançar uma nova Ordem de Serviço.

Ao clicar em **"Aplicar filtro"**, será feita a busca seguindo os critérios de filtro que foram informados pelo usuário. Os resultados serão apresentados em uma grade logo abaixo dos campos, trazendo as OS’s encontradas.

O usuário também poderá visualizar, em arquivo PDF, ao clicar na opção **"Visualizar em PDF"**.

Após trazer as OS’s, quando o usuário clicar sobre o número da OS, abrirá as informações referentes a mesma:

**"Número da OS"**, **"Status"**, **"Prevista para"**, **"Contato"**, **"Produto"**, **"Data de chamada"**, **"Data de Fechamento"**, **"Status da avaliação"** e **"Descrição do problema"**.

O usuário pode também lançar uma nova OS utilizando a opção **"Nova ordem de serviço"** que fica logo acima dos campos que são utilizados para filtro.

Ao clicar nesta opção, serão abertos os campos, **"Contrato"**, **"Produto"**, **"Motivo"**, **"Problema"** e **"Anexo"**, onde o usuário deverá informar as opções referentes à situação.

O botão **"Salvar"** envia a OS para o usuário configurado no campo **"Executante"** da tela **"Parâmetros OS Externa"**.

Quando o problema da OS for resolvido e esta enviada para a fila, com o serviço cadastrado na tela Parâmetros para Validação OS Externa, será enviado um e-mail para o contato da OS validar ou não a solução, conforme já apresentado neste manual.

É importante lembrar que a OS interna do cliente deve estar corretamente configurada, juntamente com as configurações de envio de e-mail, para que a OS Web funcione sem problemas.

O parâmetro **"Endereço para acesso externo ao WGE - ENDACESSEXTWGE"** é utilizado para determinar a URL externa de acesso ao Sankhya-Om.

A empresa deverá ter um link (domínio) que será apontado para o servidor do Sankhya-Om, para que o sistema possa ser acessado pela internet, supondo que esse link seja http://fotos.sankhya.com.br/mge, este deverá ser informado nesse parâmetro dessa forma, inclusive o ?/mge?. Por exemplo:

Se for acessado em uma rede interna, este endereço poderia ser http://127.0.0.1:8080/mge, se for acessado internamente e externamente poderia ser <http://www.empresa.com.br/mge>.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113353-Par%C3%A2metros-Valida%C3%A7%C3%A3o-OS-Externa#top)

![acesse](https://ajuda.sankhya.com.br/hc/article_attachments/16077965357847) Acesse também:

[Parâmetros OS Externa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045113173)
