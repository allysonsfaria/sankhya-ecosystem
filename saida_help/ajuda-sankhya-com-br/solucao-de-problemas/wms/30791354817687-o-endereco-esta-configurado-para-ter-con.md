---
id: "30791354817687"
titulo: "O endereço '' está configurado para ter conexão mas não tem o endereço de conexão principal e/ou secundário informados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30791354817687-O-endere%C3%A7o-est%C3%A1-configurado-para-ter-conex%C3%A3o-mas-n%C3%A3o-tem-o-endere%C3%A7o-de-conex%C3%A3o-principal-e-ou-secund%C3%A1rio-informados"
trilha: "Solução de Problemas > WMS"
atualizado_em: "2026-07-22T14:34:41Z"
rotulos: ["Configuração", "WMS", "Estoque", "Endereço de Armazenamento", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Erro", "Movimentação Vertical", "Endereço preferencial", "Endereço secundário", "picking de nível zero", "Squad WMS"]
---

# O endereço '' está configurado para ter conexão mas não tem o endereço de conexão principal e/ou secundário informados

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/30791354808215) **MENSAGEM:**

O endereço '' está configurado para ter conexão mas não tem o endereço de conexão principal e/ou secundário informados

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30791369402263)SOLUÇÃO:**

**(1)** Acesse a tela de [**"Endereço de Armazenamento"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045120313-Endere%C3%A7o-de-Armazenamento) (WMS » Cadastros » Endereço de Armazenamento).

**(2)** Localize o endereço que está causando o erro.

**(3)** Na aba **"Movimentação Vertical"**, configure corretamente os seguintes campos:

- **''Endereço Preferencial''** → Define o endereço principal de conexão.
- **''Endereço Secundário''** → Corresponde ao endereço pai do endereço de conexão.

**(4)** Verifique as configurações para garantir que as opções estejam corretamente ativadas:

- **"Utiliza endereço de conexão para Entrada"** → Para permitir movimentação de entrada.
- **"Utiliza endereço de conexão para Saída"** → Para permitir movimentação de saída.

(5)** Após realizar as configurações**, tente novamente gerar as tarefas de armazenagem.

##### IMPORTANTE:

- Se o **endereço preferencial estiver inativo**, o sistema fará a busca automaticamente pelos endereços filhos do endereço secundário.
- Endereços de **picking de nível zero** não devem ter a aba ''Movimentação Vertical'' configurada.
- Para facilitar a identificação e evitar erros, recomenda-se utilizar **etiquetas coloridas** nos endereços de conexão.
- Após as configurações, o erro não deverá mais ocorrer ao clicar no botão **pré-visualizar** e confirmar na tela de tarefas de recebimento.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/30791369402775)CAUSA:**

O erro ocorre quando um endereço de armazenamento está configurado para **movimentação vertical (conexão)**, mas os endereços de conexão obrigatórios não foram informados corretamente.

Para que o sistema permita esse tipo de movimentação, é necessário que tanto o **endereço preferencial** quanto o **endereço secundário** estejam devidamente cadastrados.
