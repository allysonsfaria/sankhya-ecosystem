---
id: "43873847386647"
titulo: "Como liberar ou bloquear holerites no Portal RH e app Pessoas+"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43873847386647-Como-liberar-ou-bloquear-holerites-no-Portal-RH-e-app-Pessoas"
trilha: "Manual do Produto > Pessoas+ > Folha Mensal > Conferência e Auditoria da Folha"
atualizado_em: "2026-10-02T15:40:27Z"
rotulos: ["FPBLOQPORTALRH", "Portal RH", "br.com.sankhya.rh.GerenciadorFolha", "Gerenciador de Folhas", "Bloquear Liberação", "APP Pessoas+", "Integra o Portal RH", "Modelo hollerit", "Liberar dados para Portal RH"]
---

# Como liberar ou bloquear holerites no Portal RH e app Pessoas+

**Módulo:** Pessoal+
**Caminho de Acesso:**Pessoal+ > Rotinas Folha > Gerenciador de Folhas
**ID da Tela:** br.com.sankhya.rh.GerenciadorFolha

---

### O que é e para que serve

O **Gerenciador de Folhas** permite controlar quando os holerites já calculados ficam disponíveis para consulta do colaborador no **Portal RH** e no aplicativo **Pessoas+**.

Você pode:

- **liberar** o holerite para que o colaborador possa consultá-lo;
- **bloquear** um holerite que já foi liberado, sem excluir o cálculo realizado.

A liberação e o bloqueio podem ser feitos por **tipo de folha, referência, empresa e funcionário**.

### Antes de começar

Para que o controle de liberação e bloqueio funcione corretamente, confira as configurações abaixo.

- **Configurações do Portal RH**

  Na tela **Preferências** (**Configurações > Avançado**), confira se o parâmetro **Bloqueia consulta de Holerite no Portal RH - FPBLOQPORTALRH** está desligado. Esse parâmetro controla o comportamento do Portal RH/app Pessoas+ em relação aos holerites bloqueados.

  | **⚠️** **Atenção**  Se o parâmetro não estiver configurado corretamente, o bloqueio realizado no **Gerenciador de Folhas** não terá efeito no Portal RH. |
  | --- |
- **Configurações da empresa**

  No **cadastro da empresa** (Pessoal+ > Cadastros > Empresa da Folha de Pagamento), aba **Portal RH**, confira:
- **Integra o Portal RH:** deve estar marcada para que a empresa esteja integrada ao Portal RH.
- **Modelo hollerit:** deve estar preenchido para definir o modelo utilizado na visualização e impressão do holerite.

  | ℹ️ **Nota**  Essas configurações são independentes. Para que o colaborador consiga visualizar o holerite, as configurações necessárias devem estar corretas. |
  | --- |
- **Outras condições**

  Além das configurações do Portal RH, confira:

  - **Folha calculada:** somente empresas ativas e funcionários com cálculo no tipo de folha e na referência selecionados são apresentados para liberação.
  - **Permissão de acesso:** o usuário precisa ter a permissão de fechar e reabrir folha no **Gerenciador de Folhas** para visualizar o botão **Liberação para Portal RH**.
  - **Acesso às empresas:** somente as empresas pertencentes aos grupos de acesso do usuário são apresentadas na rotina.

### Liberar holerites para o Portal RH

[GIF animado: Imagem 1: Liberar holerites para o Portal RH](https://ajuda.sankhya.com.br/hc/article_attachments/43874727791639)

1. Abra o **Gerenciador de Folhas** (Pessoal+ > Rotinas Folha).
2. No menu de ações flutuante, clique em **Liberação para Portal RH**.
3. No pop-up exibido, selecione o **Tipo de Folha** (por exemplo, Mensal, Adiantamento, Férias ou 13º Salário).
4. Informe a **Referência**, com mês e ano.
5. Na aba **Empresas**, clique nos cards das empresas desejadas.

   Para selecionar todas as empresas apresentadas, utilize a caixa de seleção do cabeçalho
6. Acesse a aba **Funcionários** e clique nos cards dos colaboradores que devem ver o holerite.

   Você pode pesquisar por nome ou código do funcionário.
7. Clique em **Liberar dados para Portal RH**.
8. Confirme a operação.

Após a confirmação, a mensagem **"O(s) holerite(s) do(s) funcionário(s) selecionado(s) foram liberados para o Portal RH"** indica que a operação foi concluída.

O holerite fica disponível para consulta no **Portal RH** e no aplicativo **Pessoas+**, desde que as configurações necessárias estejam corretas.

| ℹ️ **Nota**  Ao alterar a **Referência**, as seleções de empresas e funcionários são limpas. |
| --- |

### Bloquear holerites já liberados

Utilize o bloqueio quando precisar retirar temporariamente do Portal RH e app Pessoas+ um holerite que já foi disponibilizado ao colaborador.

O bloqueio **não exclui nem desfaz o cálculo da folha**. Ele apenas impede a consulta do holerite pelo colaborador.

1. Acesse o **Gerenciador de Folhas** (Pessoal+ > Rotinas Folha).
2. No menu de ações flutuante, clique em **Liberação para Portal RH**.
3. Selecione o **Tipo de Folha** e a **Referência**.
4. Na aba **Empresas**, selecione as empresas.
5. Na aba **Funcionários**, selecione os colaboradores.
6. Clique em **Bloquear Liberação**.
7. Confirme a operação.

A mensagem **"O(s) holerite(s) do(s) funcionário(s) foram bloqueados"** confirma o bloqueio.

Após o bloqueio, o holerite deixa de ser apresentado no **Portal RH** e no aplicativo **Pessoas+**.

| ℹ️ **Nota**  O holerite bloqueado também deixa de aparecer na lista de holerites, nos holerites recentes, na evolução salarial e na linha do tempo do colaborador. |
| --- |

### Pontos de Atenção

- **O botão "Liberação para Portal RH" não aparece**

  O usuário precisa ter a permissão de **fechar e reabrir folha** no Gerenciador de Folhas.

  Se o acesso ao Gerenciador de Folhas estiver configurado como **Apenas Consulta**, essa permissão fica desmarcada e o botão não é apresentado.
- **Os botões "Liberar dados para Portal RH" e "Bloquear Liberação" estão desabilitados**

  Selecione pelo menos um funcionário na aba **Funcionários**.
- **Liberei o holerite, mas o colaborador não consegue visualizar**

  Confira as configurações necessárias:

  - parâmetro **FPBLOQPORTALRH**;
  - opção **Integra o Portal RH** no cadastro da empresa;
  - campo **Modelo hollerit** preenchido no cadastro da empresa.

  Se essas configurações estiverem corretas e o colaborador ainda não conseguir visualizar o holerite, consulte o artigo [**Erro ao acessar holerite no Portal RH: como resolver?**](https://ajuda.sankhya.com.br/hc/pt-br/articles/43675117699479).

  Esse artigo apresenta outras situações que podem impedir o acesso, como e-mail ausente ou inválido no cadastro, acesso ao Portal RH ou aplicativo Pessoas+ não liberado e ausência de usuário OM.
- **Bloqueei o holerite, mas o colaborador continua visualizando**

  Confira se o parâmetro **FPBLOQPORTALRH** está configurado corretamente. Sem essa configuração, o Portal RH pode desconsiderar o bloqueio realizado no Gerenciador de Folhas.

### Perguntas Frequentes

**1. Como saber quais holerites já estão liberados?**

A janela de liberação não apresenta a situação atual de cada funcionário.

Se precisar garantir a liberação de determinados funcionários, selecione-os e realize novamente a liberação. Repetir a liberação não causa problema.

**2.** **Preciso recalcular a folha para bloquear um holerite?**

Não. O bloqueio é realizado diretamente pela opção **Bloquear Liberação** e não altera o cálculo da folha.

**3. O bloqueio exclui o holerite?**

Não. O cálculo permanece registrado. O bloqueio apenas impede que o colaborador consulte o holerite no Portal RH e no aplicativo Pessoas+.

**4. Posso liberar novamente um holerite que foi bloqueado?**

Sim. Selecione o tipo de folha, a referência, a empresa e o funcionário e utilize **Liberar dados para Portal RH** novamente.

**5. Liberei o holerite e recalculei a folha. Por que ele sumiu do Portal RH?**

Todo cálculo ou recálculo grava a folha novamente como bloqueada, enquanto o parâmetro FPBLOQPORTALRH estiver ativo. Libere o holerite outra vez depois de recalcular.

### Artigos Relacionados

- [Gerenciador de Folhas](https://ajuda.sankhya.com.br/hc/pt-br/articles/40106318532247)
- [Erro ao acessar holerite no Portal RH: como resolver?](https://ajuda.sankhya.com.br/hc/pt-br/articles/43675117699479)
- [Portal RH: visão geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108433)
- [Como configurar o Portal RH na empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/38131393345687)
- [Como liberar acesso somente de consulta ao Gerenciador de Folhas?](https://ajuda.sankhya.com.br/hc/pt-br/articles/40044327954071)
