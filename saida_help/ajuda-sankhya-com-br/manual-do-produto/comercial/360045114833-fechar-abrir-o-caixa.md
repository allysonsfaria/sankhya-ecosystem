---
id: "360045114833"
titulo: "Fechar/Abrir o Caixa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114833-Fechar-Abrir-o-Caixa"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:32:36Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Relatórios", "Contas", "Movimentação Financeira", "Caixa", "Conta", "Fechar/Abrir o Caixa", "br.com.sankhya.fechar.abrir.caixa", "Fechar/Abrir o Caixa manual", "Financeiro", "Rotina Diária do Caixa", "Configurações de Usuário Caixa", "Cadastro de Contas para Caixa"]
---

# Fechar/Abrir o Caixa

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312100947351) Módulo: Comercial > Avançado
```

---

Através desta tela, você efetuará o fechamento e a abertura do caixa. Vejamos nos tópicos abaixo as configurações necessárias para utilização desta tela, bem como, suas características:

[Configurações para usuários do tipo "Caixa"](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114833-Fechar-Abrir-o-Caixa#h_01ENXHXHDRB3MHNPJSG8F5CVDX)                          [Cadastro de Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114833-Fechar-Abrir-o-Caixa#h_01ENXHXQ120JSWKKAMAMD1RCE4)

[Rotina diária do Usuário Caixa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114833-Fechar-Abrir-o-Caixa#h_01ENXHXWPCQFHWHBNF9D5CZRAG)

#### Configurações para usuários do tipo "Caixa"

Para que um usuário seja caixa, é necessário que no [Cadastro de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874), aba [Identificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abaidentificao), você marque a opção **"Caixa"**.

**Nota:** os [Controle de Acessos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596854-Acessos) às telas e rotinas do sistema deverão estar devidamente configurados para que o usuário possa executar as configurações.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114833-Fechar-Abrir-o-Caixa#top)

#### Cadastro de Contas

No [Cadastro de Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113) configure as contas que serão utilizadas pelos usuários Caixa. Para que uma conta possa ser utilizada por esses usuários, na aba [Cadastros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas#abacadastros), o campo **"Tipo de Conta"** deverá estar cadastrado com a opção **"Caixa (PDV)"**.

Caso você informe um usuário Caixa no campo **"Operador Exclusivo"**, a conta que esta sendo configurada estará vinculada exclusivamente a este usuário.

![Imagem 2: Caso você informe um usuário Caixa no campo "Operador Exclusivo" , a conta que esta sendo configurada estará vinculada…](https://ajuda.sankhya.com.br/hc/article_attachments/360083365413)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114833-Fechar-Abrir-o-Caixa#top)

#### Rotina diária do Usuário Caixa

Ao entrar no sistema com um usuário Caixa que possua uma conta exclusiva configurada, tem-se a abertura do caixa com as informações deferida conta:

![clip8956](https://ajuda.sankhya.com.br/hc/article_attachments/360061934533)

Caso o usuário não contenha uma conta exclusiva configurada, ao abrir o sistema será necessário informar o número da conta do caixa que será utilizada.

![clip8955 (2)](https://ajuda.sankhya.com.br/hc/article_attachments/360061012574)

Ao pesquisar uma conta, serão apresentadas somente as contas que não tenham um usuário já vinculado a elas e as contas que não estão com caixas abertos.

**Nota:** todo usuário Caixa deve obrigatoriamente selecionar uma conta.

Após a abertura do caixa, serão exibidas as informações do caixa que foi aberto. Se o caixa foi aberto em uma sessão anterior, não será mostrada nenhuma informação e o sistema continuará a gravar as informações.

Todas as movimentações que o usuário Caixa fizer no sistema ficarão registradas para uma análise posterior no relatório de fechamento de caixa. As movimentações que serão registradas no relatório de fechamento de caixa são:

- Os pedidos e notas que forem confirmados na central;
- Compensação financeira;
- Movimentação financeira (baixa de títulos e estornos);
- Movimentação bancária (transferências, depósitos, etc);
- Conciliação Bancária (botão de estorno também grava movimentação de caixa).

**Observação:** para que seja possível efetuar uma movimentação bancária, uma das contas (origem ou destino) deve ser a do caixa. O sistema não permite fazer esse tipo de movimento com contas padrão.

**Nota:** só é permitido executar a movimentação bancária e exclusão de títulos (mov. financeira) que tenham gerado movimentação no caixa caso o usuário seja Gerente do Financeiro, e só é permita a exclusão de notas que tenham gerado movimento no caixa caso o usuário seja Gerente da Central de Atendimento, porque afetarão os relatórios de controle de caixa.

Ao solicitar o fechamento do sistema, tem-se a solicitação de Fechamento de Caixa informando a data de sua abertura e a conta que foi utilizada, caso deseje sair sem fechar o caixa basta clicar no botão **"Cancelar"**, mas o caixa continuará aberto. Ao confirmar a operação, o sistema irá fechar o caixa, efetuar logoff e na próxima sessão será aberto outro caixa.

Caso o usuário feche a janela de solicitação e também a página do sistema, tem-se o questionamento se o mesmo deseja sair e fechar o caixa ou não.

![clip8958 (2)](https://ajuda.sankhya.com.br/hc/article_attachments/360061934553)

Se o usuário logado for um caixa, é possível fechar o caixa e abrir outro em seguida com a mesma conta, sem ser necessário sair do sistema.

![Imagem 6: Se o usuário logado for um caixa, é possível fechar o caixa e abrir outro em seguida com a mesma conta, sem ser…](https://ajuda.sankhya.com.br/hc/article_attachments/360082235474)

Caso um usuário padrão tente acessar a tela **"Fechar/Abrir o Caixa"**, o sistema apresentará a seguinte mensagem:

**"Usuário logado não é caixa."**

Pode-se acompanhar os movimentos realizados pelos usuários Caixa através da tela [Fechamento de Caixa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115233).

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114833-Fechar-Abrir-o-Caixa#top)
