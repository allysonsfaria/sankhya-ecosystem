---
id: "360050441933"
titulo: "Nenhum e-mail foi enviado. Verifique o endereço de e-mail do(s) destinatário(s) e as configurações de envio de e-mail na TOP"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360050441933-Nenhum-e-mail-foi-enviado-Verifique-o-endere%C3%A7o-de-e-mail-do-s-destinat%C3%A1rio-s-e-as-configura%C3%A7%C3%B5es-de-envio-de-e-mail-na-TOP"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-09-29T11:56:19Z"
rotulos: ["Configuração", "Parceiro", "TOP", "CORE_E05183", "Cheque endereço e configurações na TOP", "Confirme e-mail no cadastro e tipo configurado", "Aba ‘E-mails da TOP’ define envio", "Erro"]
---

# Nenhum e-mail foi enviado. Verifique o endereço de e-mail do(s) destinatário(s) e as configurações de envio de e-mail na TOP

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/18612246786839) MENSAGEM**:

Nenhum e-mail foi enviado. Verifique o endereço de e-mail do(s) destinatário(s) e as configurações de envio de e-mail na TOP XX em:
Arquivos->Cadastros->Tipos de Operação - TOP na aba E-Mail.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18612246793879) SOLUÇÃO:**

Verifique as configurações da aba 'E-mails da TOP' do 'Tipo de Operação' utilizado:

- Tela 'Tipos de Operação-TOP' >> Aba**'E-mails da TOP'**:

Será utilizada para enviar e-mails quando se confirmar um Pedido/Nota, podendo este ser enviado para um Funcionário, Parceiro, Usuário etc. de acordo com as configurações do campo **"Tipo"** na grade desta tela.

**Importante:**

| Tratando-se de uma TOP utilizada no lançamento de uma **Nota Fiscal Eletrônica**, **esta aba não deverá ser configurada**; neste caso já tem-se o envio automático do Danfe na confirmação da mesma. |
| --- |

Conforme 'Tipo' definido na aba 'E-mails da TOP' é necessário analisar:

- **Parceiro, Parc. destinat., Parc. transp., Parc. consig., Parc.remetente e Matriz do parceiro:**

Através dessas opções o sistema irá validar as informações cadastradas no sistema (Cadastro de Parceiros, aba Endereço, campo**"E-mail"**).

- **Usuário resp. pelo CR:**

O sistema realizará a validação do campo **"E-mail"** localizado no Cadastro de Usuários, aba Identificação; posto isto, para este caso, faz-se necessário que os acessos destes usuários estejam vinculados ao Centro de Resultado, aba Usuários.

- **Fixo:**

Utilizando a opção **Fixo,** o sistema irá validar se na TOP cadastrada há registro no campo E-mail.

- **Usuário:**

O sistema validará as informações do Cadastro de Usuários e verificará se há um e-mail cadastrado (aba Identificação, campo E-mail).

- **Vendedor/Comprador:**

O sistema irá validar o Cadastro de Vendedores/Compradores verificando o registro do campo **"E-mail"**, aba Geral.

- **Funcionário:**

O sistema validará o Cadastro de Funcionários e irá verificar se há um e-mail cadastrado (aba Endereço, campo **"E-mail"**).

- **Contatos:**

O sistema considerará o registro inserido no campo "E-mail" (Cadastros de Parceiros, aba Contatos). Além disso, é necessário que a marcação **"Recebe Nota por email"** esteja habilitada (Cadastro de Parceiros, aba Contatos, dentro do contato que deseja que seja enviado).

| - Usando o campo Tipo definido com a opção Contatos, se o parâmetro **"Envia e-mail preferencialmente para o contato da nota/pedido - ENVMAILCONTNOT"** estiver ligado, ao enviar um e-mail da nota, o mesmo será enviado para o e-mail do contato que está vinculado à nota (campo Contato do cabeçalho da nota), caso o campo Contato do cabeçalho da nota/pedido não esteja configurado ou o contato não esteja ativo o sistema irá enviar para o(s) contato(s) do parceiro da nota. Caso este parâmetro esteja desligado, o sistema irá enviar para o(s) contato(s) do parceiro da nota. |
| --- |

**Nota:** 

Os e-mails cadastrados somente serão enviados caso o Tipo configurado na TOP seja o mesmo utilizado no Pedido/Nota. Teremos então o exemplo:

- Caso na TOP seja selecionado no campo Tipo, a opção Funcionário e em suas configurações esteja vinculado um e-mail, faz-se necessário realizar o preenchimento dos campos "Funcionário" e "Empresa do Funcionário" no cabeçalho do Pedido/Nota para que os e-mails sejam devidamente enviados; caso contrário, deve-se inserir os mencionados campos com suas respectivas informações no Layout do Pedido/Nota.
