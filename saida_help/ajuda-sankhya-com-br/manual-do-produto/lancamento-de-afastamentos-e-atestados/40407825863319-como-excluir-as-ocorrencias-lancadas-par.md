---
id: "40407825863319"
titulo: "Como excluir as ocorrências lançadas para um colaborador"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/40407825863319-Como-excluir-as-ocorr%C3%AAncias-lan%C3%A7adas-para-um-colaborador"
trilha: "Manual do Produto > Pessoas+ > Afastamentos e Ocorrências > Lançamento de Afastamentos e Atestados"
atualizado_em: "2026-10-02T15:31:18Z"
rotulos: ["Ocorrências", "br.com.sankhya.rh.LancamentoOcorrencias", "eSocial", "Folha de Pagamento", "Pessoal+", "Excluir Ocorrências Lançadas para o Colaborador", "Exclusão"]
---

# Como excluir as ocorrências lançadas para um colaborador

**Módulo:** Pessoal+
**Caminho de acesso:** Pessoal+ > Rotinas Folha > Ocorrências
**ID da Tela:** br.com.sankhya.rh.LancamentoOcorrencias

---

### Descrição e Usabilidade

A rotina de exclusão de ocorrências permite remover afastamentos, atestados e demais registros lançados incorretamente para o colaborador.

Essa funcionalidade é utilizada quando:

- a ocorrência foi lançada indevidamente;
- houve duplicidade de lançamento;
- o afastamento foi cancelado;
- o registro foi realizado para o colaborador incorreto;
- existe necessidade de refazer o lançamento corretamente.

⚠️ A exclusão de ocorrências pode impactar cálculos da folha, férias, encargos trabalhistas e envio ao eSocial.

### Pré-requisitos

Antes de excluir uma ocorrência, verifique:

- permissão de acesso à tela **Ocorrências** (Pessoal+ > Rotinas Folha); Essa liberação é feita na tela **Acessos** (Configurações > Controle de Acesso), pelo administrador do sistema.
- existência da ocorrência lançada;
- se a folha relacionada já foi calculada ou integrada;
- se existem eventos enviados ao eSocial vinculados ao afastamento.

### Jornada de Uso

[GIF animado: Imagem 1: Jornada de Uso](https://ajuda.sankhya.com.br/hc/article_attachments/40407811047319)

1. Acesse a tela **Ocorrências** (Pessoal+ > Rotinas Folha);
2. Utilize o painel de filtros lateral para facilitar a busca do colaborador, selecionando:

   - **Empresa**;
   - **Tipo de filtro**.
3. Clique em **Pesquisar**, o card do colaborador será exibido;
4. Clique sobre o card do colaborador para visualizar o histórico das ocorrências lançadas;
5. Passe o cursor do mouse sobre a linha correspondente ao afastamento ou atestado;
6. Clique em **Excluir ocorrência** e confirme a exclusão quando o sistema solicitar validação.

   Após a confirmação, a ocorrência será removida do histórico do colaborador.

### Pontos de Atenção

- A exclusão pode impactar:
  - cálculos da folha;
  - férias;
  - médias;
  - encargos;
  - afastamentos;
  - envio ao eSocial.
- Ocorrências de **férias ou vinculadas a folhas já fechadas não podem ser excluídas**.
- Ocorrências marcadas como **Recorrente** sem anexo de atestado vinculado impedem a exclusão — inclusive do último lançamento do colaborador. Regularize o anexo da ocorrência recorrente antes de excluir.
- A exclusão de afastamentos vinculados ao INSS exige atenção para evitar inconsistências previdenciárias.

### Perguntas Frequentes (FAQ)

**1. Posso excluir qualquer ocorrência lançada?**

Não em todos os casos. Ocorrências de **férias** ou já vinculadas a uma **folha fechada** não podem ser excluídas. Fora esses casos, a exclusão é permitida desde que tenha permissão de acesso.

**2. Onde visualizo as ocorrências do colaborador?**

Na própria tela **Ocorrências**, clicando sobre o card do colaborador.

**3. Excluir uma ocorrência impacta a folha?**

Sim. Dependendo da ocorrência, pode ser necessário recalcular a folha.

**4. Posso excluir um afastamento recorrente?**

Sim. Porém é necessário validar os vínculos entre ocorrências reincidentes.

**5. Preciso recalcular a folha após excluir uma ocorrência?**

Em muitos casos, sim. Principalmente quando a ocorrência já participou do cálculo.

**6. O que acontece se a ocorrência já foi enviada ao eSocial?**

Pode ser necessário excluir, retificar ou reenviar eventos ao eSocial.

**7. Posso excluir afastamentos do INSS?**

Sim. Porém é importante validar os impactos previdenciários antes da exclusão.

**8. Por que recebo a mensagem "Falha ao deletar a ocorrência. Motivo: null" ao excluir?**

Isso ocorre quando a ocorrência está marcada como Recorrente e não possui anexo de atestado vinculado. Verifique e regularize o anexo da ocorrência recorrente e tente excluir novamente.

### Artigos Relacionados

- [Lançamento de Atestado Médico](https://ajuda.sankhya.com.br/hc/pt-br/articles/40388499298071)
- [Lançamento de Atestado Médico Recorrente](https://ajuda.sankhya.com.br/hc/pt-br/articles/37808779732503)
- [Consulta de Ocorrências Lançadas para o Colaborador](https://ajuda.sankhya.com.br/hc/pt-br/articles/40336545146519)
- [Edição de Ocorrências Lançadas para o Colaborador](https://ajuda.sankhya.com.br/hc/pt-br/articles/40407377343127)
- [Erro ao Excluir Ocorrência de Funcionário(a): "Falha ao deletar a ocorrência. Motivo: null"](https://ajuda.sankhya.com.br/hc/pt-br/articles/37361520919319)
