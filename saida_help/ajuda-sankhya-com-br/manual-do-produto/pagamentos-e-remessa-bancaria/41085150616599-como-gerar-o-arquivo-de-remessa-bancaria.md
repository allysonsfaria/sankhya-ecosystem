---
id: "41085150616599"
titulo: "Como gerar o arquivo de remessa bancária (EDI)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/41085150616599-Como-gerar-o-arquivo-de-remessa-banc%C3%A1ria-EDI"
trilha: "Manual do Produto > Pessoas+ > Integração Contábil e Financeira > Pagamentos e Remessa Bancária"
atualizado_em: "2026-10-02T17:52:08Z"
rotulos: ["Configuração", "Financeiro", "Arquivo de Remessa", "br.com.sankhya.rh.geracao.arquivo.remessa", "Geração de Arquivo de Remessa para pagamento de funcionários", "Pessoal+", "EDI Bancário"]
---

# Como gerar o arquivo de remessa bancária (EDI)

**Módulo:** Pessoal+
**Caminho de acesso:** Pessoal+ › EDI Bancários
**ID da tela:** br.com.sankhya.rh.geracao.arquivo.remessa

---

## Descrição e Usabilidade

A tela **Geração de Arquivo de Remessa** permite reunir os pagamentos já calculados na folha de pagamento e gerar um arquivo de remessa bancária (EDI) para envio à instituição financeira responsável pelo processamento dos créditos aos colaboradores.

Durante a geração, é possível selecionar empresas, departamentos e demais filtros, conferir os valores que serão enviados e produzir o arquivo no layout exigido pelo banco.

**Essa rotina não realiza cálculos da folha de pagamento.** Ela apenas organiza os pagamentos já processados e gera o arquivo no formato esperado pela instituição financeira.

### Pré-requisitos

Antes de gerar o arquivo de remessa, certifique-se de que:

- Os cálculos de folha (ex: mensal, férias, rescisão) que você deseja pagar já foram processados.
- Os layouts de EDI bancário estão cadastrados e configurados na tela **Configuração de Arquivo de Remessa** (Pessoal+ > EDI Bancário).
- A empresa possui uma conta bancária cadastrada para pagamento.
- s colaboradores possuem dados bancários válidos.
- Seu usuário tem permissão de acesso às empresas e departamentos que precisa processar.

### Jornada de Uso

[GIF animado: Imagem 1: Jornada de Uso](https://ajuda.sankhya.com.br/hc/article_attachments/41086312698391)

**(1)** **Selecione as Empresas e os Departamentos**

No painel de filtros à esquerda, comece definindo o escopo dos pagamentos. Você pode selecionar um ou mais registros nos campos **Empresas/Matrizes** e **Departamentos**.

- **Como funciona:** clique no campo e pesquise por código ou nome para encontrar e selecionar os registros. Os itens escolhidos são exibidos com código e descrição no campo (ex: `"1-Empresa Y Ltda, 2-Empresa Z Ltda"`). Se o texto for muito longo, ele será abreviado e a lista completa aparecerá no tooltip ao lado do campo correspondente.
- **Regras de seleção:**
  - **Empresa:** apenas empresas ativas e vinculadas ao seu usuário estarão disponíveis.
  - **Departamento:** apenas departamentos analíticos e ativos estarão disponíveis.

    | **⚠️** **Atenção**   Ao selecionar mais de uma empresa, o filtro **Funcionário** é desabilitado. A busca por um colaborador específico só é permitida quando você está gerando a remessa para uma única empresa. |
    | --- |

**(2)** **Configure os Dados da Remessa**

Após definir o escopo, preencha os demais campos que determinam como o arquivo será gerado.

- **Layout:** escolha o layout de EDI correspondente ao banco de destino, previamente configurado na rotina **Configuração de Arquivo de Remessa** (Pessoal+ > EDI Bancário).

  | ℹ️ **Nota**  O **layout** funciona como um **tradutor** entre o Pessoal+ e a instituição financeira.  Ele define como as informações da folha serão organizadas dentro do arquivo para que o banco consiga interpretar corretamente os dados recebidos.  Por isso, sua configuração é indispensável. Um layout incompatível com o banco poderá causar rejeição do arquivo ou impedir o processamento dos pagamentos. |
  | --- |
- **Conta Bancária Empresa:** informe a conta bancária que será utilizada como conta pagadora da remessa. Este campo é obrigatório e seu comportamento muda conforme a seleção de empresas:
  - **Se você selecionou UMA empresa:** o sistema busca e preenche automaticamente a **Conta Bancária Intercâmbio** definida no [Cadastro da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/37988711948311). Caso essa informação não esteja cadastrada, será necessário informá-la manualmente.
  - **Se você selecionou VÁRIAS empresas:** o campo permanecerá **vazio** e você deverá informar manualmente a conta bancária que será utilizada para centralizar todos os pagamentos.

    | **⚠️** **Atenção**  Verifique se conta bancária informada pertence à instituição financeira correspondente ao layout selecionado. |
    | --- |
- **Data Efetiva de Pagamento:** informe a data em que o banco deverá realizar o crédito aos colaboradores. Essa é a mesma data utilizada no cálculo da folha de pagamento.

  Essa data deve ser compatível com o calendário bancário. Caso seja informado um feriado ou final de semana, o processamento dependerá das regras da instituição financeira.

**(3)** **Aplique os Filtros e Confira os Resultados**

Após informar todos os filtros, clique em **Aplicar** para localizar os pagamentos que serão incluídos na remessa.

No pop-up apresentado indique o que se deseja fazer com as seguintes opções:

- Aplicar o filtro e visualizar os resultados;
- Geração direta do arquivo.

  | ℹ️ **Nota**  Ao selecionar a segunda opção, a marcação **Ver totais antes de gerar o arquivo** será habilitada para conferência de valores antes da geração do arquivo. |
  | --- |

Confirme para que a grade à direita seja preenchida com todos os pagamentos que correspondem aos filtros definidos.

[GIF animado: Imagem 2: Confirme para que a grade à direita seja preenchida com todos os pagamentos que correspondem aos filtros definidos.](https://ajuda.sankhya.com.br/hc/article_attachments/41087168048663)

Confira os registros e verifique o valor total a ser pago no campo **Total Líquido**, localizado no rodapé da tela.

Antes de gerar o arquivo, confirme também:

- quantidade de colaboradores;
- empresas incluídas;
- data efetiva;
- conta bancária;
- valor líquido total.

**(4)** **Remover registros**

Se precisar, você pode remover pagamentos da lista clicando sobre a linha e usando os botões **Remover selecionados** ou **Remover não selecionados**.

[GIF animado: Imagem 3: Se precisar, você pode remover pagamentos da lista clicando sobre a linha e usando os botões Remover selecionados ou…](https://ajuda.sankhya.com.br/hc/article_attachments/41087237501719)

A remoção ocorre apenas na geração atual e não altera cálculos nem pagamentos registrados na folha.

**(5)** **Gere o Arquivo**
Após a conferência, clique em **Gerar Remessa** para criar o arquivo EDI.

O sistema:

- monta o arquivo conforme o layout bancário selecionado;
- organiza os pagamentos conforme os filtros;
- gera o arquivo EDI;
- disponibiliza o arquivo para envio ao banco.

| ℹ️ **Nota**  Após a geração do arquivo, os filtros selecionados serão mantidos na tela com os dados da última geração feita pelo usuário logado no sistema. |
| --- |

### Pontos de Atenção

- Esta rotina não calcula a folha de pagamento; ela apenas gera o arquivo de remessa dos pagamentos já processados.
- O layout bancário deve corresponder à instituição financeira que receberá o arquivo.
- A conta bancária da empresa deve estar corretamente configurada antes da geração da remessa.
- Ao selecionar várias empresas, o preenchimento automático da conta bancária é desabilitado. Caso nenhum filtro seja informado, serão considerados todos os pagamentos das empresas e departamentos aos quais o usuário possui acesso.
- A exclusão de registros na tela não altera os cálculos da folha nem os pagamentos cadastrados.
- O [Construtor de Expressões](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109213) disponibiliza apenas as funções **Dados\_Detalhe\_Folha** e **Dados\_Gerais\_Folha** para consultas utilizadas no layout do EDI.
- Sempre confira o valor líquido antes de gerar e enviar a remessa ao banco.

## Perguntas Frequentes (FAQ)

**1.O que é um arquivo EDI?**

É um arquivo eletrônico utilizado para transmitir informações financeiras entre o sistema e a instituição bancária em um formato padronizado.

**2. O layout muda de um banco para outro?**

Sim.

Cada banco possui seu próprio padrão de layout. Por isso, o arquivo deve ser gerado utilizando o layout correspondente à instituição financeira responsável pelo processamento dos pagamentos.

**3. Posso gerar arquivos separados para várias empresas de uma só vez?**

Não. Cada clique em **Gerar Remessa** cria um único arquivo. Para gerar arquivos diferentes, você precisa repetir o processo para cada grupo de filtros desejado.

**4. Selecionei várias empresas, mas o campo de conta bancária ficou em branco. É um erro?**

Não, isso é o comportamento esperado. O preenchimento automático da conta só ocorre quando uma única empresa é selecionada. Com várias empresas, você precisa informar manualmente qual será a conta pagadora.

**5.** **Posso editar o arquivo após gerá-lo?**

Não é recomendado.

Caso seja necessária alguma alteração, ajuste as informações no sistema e gere uma nova remessa.

**6. Como confirmo o valor total a ser pago antes de gerar o arquivo?**

Após clicar em **Aplicar**, o campo **Total Líquido**, localizado no rodapé da tela, mostra a soma de todos os pagamentos listados na grade.

**7. Posso gerar a remessa antes de calcular a folha?**

Não. A tela Geração de Arquivo de Remessa não realiza cálculos de folha. Ela apenas reúne os pagamentos já processados para envio ao banco.

Antes de gerar a remessa, certifique-se de que a folha de pagamento, férias ou rescisão já foi calculada e conferida.

**8. A geração da remessa realiza os pagamentos?**

Não.

A geração cria apenas o arquivo eletrônico. Os pagamentos somente serão processados após o envio e processamento desse arquivo pela instituição financeira.

**9. O que acontece se eu utilizar um layout incorreto?**

O banco poderá rejeitar o arquivo ou interpretar incorretamente as informações, impedindo o processamento da remessa.

**10. O sistema não encontrou pagamentos após aplicar os filtros. O que devo verificar?**

Verifique os seguintes pontos:

- Se a folha foi calculada para a referência desejada;
- Se a data efetiva de pagamento corresponde à utilizada no cálculo;
- Se os colaboradores pertencem às empresas e departamentos selecionados;
- Se existe algum filtro restringindo os resultados.

Caso todos os dados estejam corretos, revise também as permissões de acesso do usuário.

**11. Posso remover colaboradores da remessa antes de gerar o arquivo?**

Sim. Após aplicar os filtros, você pode selecionar registros específicos e utilizar as opções:

- Remover selecionados;
- Remover não selecionados.

Isso permite ajustar a composição da remessa antes da geração do arquivo.

⚠️ A remoção afeta apenas a geração atual e não altera os dados da folha de pagamento.

**12. O que acontece se eu gerar a remessa com a data de pagamento incorreta?**

A data efetiva de pagamento é enviada ao banco como orientação para processamento dos créditos.

Por isso, informe sempre a mesma data utilizada no cálculo da folha.

Caso a data esteja incorreta, pode ser necessário gerar uma nova remessa conforme os procedimentos adotados pela instituição bancária.

**13. Posso utilizar uma única conta bancária para pagar colaboradores de várias empresas?**

Sim. Ao selecionar múltiplas empresas, o sistema permite informar manualmente uma única conta bancária para centralizar os pagamentos.

Nesse cenário, a empresa deve validar previamente junto ao banco se a conta utilizada está autorizada para realizar os pagamentos de todas as empresas envolvidas.

**14. O que significa a opção "Ver totais antes de gerar o arquivo"?**

Essa opção permite que o sistema apresente os valores consolidados da remessa antes da geração do arquivo.

Ela é recomendada para conferência do valor líquido total que será enviado ao banco, reduzindo riscos de divergências ou pagamentos indevidos.

**15. O arquivo gerado fica salvo no sistema?**

Sim. Após a geração, os filtros utilizados permanecem disponíveis para o usuário logado, facilitando consultas e novas gerações.

A forma de armazenamento e controle do arquivo gerado pode variar de acordo com as políticas adotadas pela empresa.

**16. Posso gerar uma remessa apenas para um colaborador?**

Sim. Para isso, selecione apenas uma empresa.

Quando somente uma empresa estiver selecionada, o campo Funcionário ficará disponível e permitirá gerar a remessa para um colaborador específico.

⚠️ Quando mais de uma empresa é selecionada, o filtro de funcionário é desabilitado.

**17. O que acontece se eu não informar a Conta Bancária da Empresa?**

A geração da remessa não poderá ser concluída.

A conta bancária da empresa é obrigatória, pois representa a conta responsável pelo pagamento dos colaboradores junto ao banco.

**18. Posso exportar a lista de pagamentos antes de gerar a remessa?**

Sim. Após aplicar os filtros, utilize o botão **Download Planilha** para exportar os registros exibidos na grade para um arquivo Excel.

Essa funcionalidade é útil para conferências internas, validações financeiras e auditorias antes do envio ao banco.

**19. O layout bancário influencia a geração do arquivo?**

Sim.

O layout funciona como um **tradutor** entre o Pessoal+ e o banco, definindo a estrutura, a ordem e o formato das informações que compõem o arquivo de remessa.

Por isso, é fundamental selecionar o layout correspondente à instituição financeira e mantê-lo corretamente configurado na rotina **Configuração de Arquivo de Remessa**. Caso o layout esteja incorreto, o banco poderá rejeitar o arquivo ou impedir o processamento dos pagamentos.

**20. Posso gerar novamente uma remessa para os mesmos pagamentos?**

Sim. O sistema permite gerar uma nova remessa utilizando os mesmos filtros.

⚠️ Antes de reenviar um arquivo ao banco, confirme se a remessa anterior já foi processada para evitar pagamentos duplicados.

**21. O sistema valida se os colaboradores possuem dados bancários cadastrados?**

Os pagamentos somente serão processados corretamente quando os dados bancários dos colaboradores estiverem cadastrados e válidos.

Caso existam informações bancárias incompletas ou inconsistentes, o arquivo poderá ser rejeitado durante o processamento ou pelo banco recebedor.

Recomenda-se validar os cadastros antes da geração da remessa.

## Artigos Relacionados

- [Cálculos da Folha de Pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/39309113368599)
- [Configuração de Arquivo de Remessa](https://ajuda.sankhya.com.br/hc/pt-br/articles/5742188701079)
