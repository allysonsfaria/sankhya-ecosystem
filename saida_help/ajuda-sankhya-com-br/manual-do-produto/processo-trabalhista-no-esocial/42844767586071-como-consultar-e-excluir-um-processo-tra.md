---
id: "42844767586071"
titulo: "Como consultar e excluir um processo trabalhista"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42844767586071-Como-consultar-e-excluir-um-processo-trabalhista"
trilha: "Manual do Produto > Pessoas+ > Processos Trabalhistas > Processo Trabalhista no eSocial"
atualizado_em: "2026-10-02T17:47:29Z"
rotulos: ["Processo Trabalhista", "br.com.sankhya.ProcessoTrabalhista", "Excluir Processo Trabalhista"]
---

# Como consultar e excluir um processo trabalhista

**Módulo:** Pessoal+
**Caminho de Acesso:** Pessoal+ > Rotinas Folha > Processo Trabalhista
**Versão disponível:** A partir da 4.21
**ID da Tela:** br.com.sankhya.ProcessoTrabalhista

---

## Descrição e Usabilidade

### 1. Descrição da Funcionalidade

A rotina **Processo Trabalhista** permite consultar os processos cadastrados para uma empresa e excluir registros quando necessário.

A pesquisa pode ser realizada pela empresa, número do processo, nome ou CPF do trabalhador. Ao selecionar um trabalhador, os dados do processo são apresentados em grupos.

### 2. Pré-requisitos

- Permissão de acesso à tela **Processo Trabalhista** (Pessoal+ > Rotinas Folha). Essa liberação é feita na tela **Acessos** (Configurações > Controle de Acesso), pelo administrador do sistema.
- Para exclusões de processos já enviados ao eSocial, observar a ordem de exclusão dos eventos.

### 3. Jornada de Uso

#### Consultar um processo

1. Acesse a tela **Processo Trabalhista** (Pessoal+ > Rotinas Folha).
2. Informe a **Empresa** ou o **Número do Processo** no painel de filtros.
3. Clique em **Pesquisar**.
4. Utilize também a barra de pesquisa pelo **Nome**, **CPF do trabalhador** ou **Número do processo**.
5. Clique sobre o card do trabalhador para visualizar os dados do processo.

#### Excluir um processo

1. Localize o processo que deseja excluir.
2. No card do trabalhador, clique em **Excluir**.
3. Confirme a operação.
4. Caso existam eventos S-2501 e S-2500 gerados individualmente, observe a ordem de exclusão indicada pelo sistema.

   Quando houver S-2501 relacionado ao S-2500, o S-2501 deve ser excluído primeiro. Depois, deve ser realizada a exclusão do S-2500.

#### Excluir processos de mesmo número

Quando o **Número do Processo** estiver preenchido no painel de filtros, é possível realizar a exclusão de vários processos do mesmo número:

1. Informe o **Número do Processo**.
2. Clique em **Pesquisar**.
3. Ative a opção **Ativa Seleção**.
4. Selecione os trabalhadores desejados.
5. Clique em **Remover processos selecionados**.
6. Confirme a operação.

   Na exclusão coletiva, o S-2501 é excluído somente para os trabalhadores selecionados.

### 4. Pontos de Atenção

- A exclusão do S-2500 não pode ser realizada enquanto existir um S-2501 que faça referência a ele.
- Quando os eventos forem gerados individualmente, exclua primeiro o S-2501 e depois o S-2500.
- Na exclusão coletiva, confira cuidadosamente os trabalhadores selecionados, pois o S-2501 será excluído somente para os registros selecionados.
- A exclusão de um processo pode resultar na reversão de alterações realizadas no cadastro do funcionário em decorrência da decisão judicial.

### 5. Dicas de Usabilidade

- Utilize o **Número do Processo** para localizar rapidamente todos os trabalhadores relacionados ao mesmo processo.
- Antes de realizar uma exclusão coletiva, confira os cards selecionados.
- Verifique se existem eventos S-2501 relacionados antes de excluir o processo.
- Quando houver informações enviadas ao eSocial, siga a ordem de exclusão apresentada pelo sistema.

## Perguntas Frequentes (FAQ)

**1. Posso excluir um processo que possui S-2501?**

Sim, mas o S-2501 relacionado deve ser excluído antes do S-2500.

**2. Posso excluir vários processos de uma vez?**

Sim. Quando o número do processo estiver informado no painel de filtros, é possível selecionar vários trabalhadores e realizar a exclusão coletiva.

**3. Na exclusão coletiva, todos os S-2501 são excluídos?**

Não. O S-2501 é excluído somente para os trabalhadores selecionados.

**4. O que acontece com as alterações realizadas no cadastro do funcionário pelo processo trabalhista?**

Quando aplicável, a exclusão do processo retorna os dados do funcionário ao estado anterior ao processo.

## Artigos Relacionados

- [Cadastro de Processo Trabalhista](https://ajuda.sankhya.com.br/hc/pt-br/articles/42632245838871)
- [Informações do Contrato de Trabalho no Processo Trabalhista](https://ajuda.sankhya.com.br/hc/pt-br/articles/42634479723671)
- [Informações de Tributos Decorrentes de Processo Trabalhista](https://ajuda.sankhya.com.br/hc/pt-br/articles/42834315267351)
- [Central do eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/7064222145175)
