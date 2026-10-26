---
id: "33883850079639"
titulo: "Funcionamento do filtro da aba Telas nas configurações de Tarefas - Flow"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33883850079639-Funcionamento-do-filtro-da-aba-Telas-nas-configura%C3%A7%C3%B5es-de-Tarefas-Flow"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-07-22T14:28:07Z"
rotulos: ["Configuração", "Parceiro", "Parceiros", "Tarefas", "sankhyaflow", "Funcionamento do filtro", "da aba Telas nas configurações de Tarefas", "Flow", "filtro"]
---

# Funcionamento do filtro da aba Telas nas configurações de Tarefas - Flow

Neste artigo, vamos explorar o funcionamento e a finalidade do filtro disponível ao adicionar uma tela a uma tarefa no processo de negócio do Flow.

#### Funcionamento do recurso

O filtro pretende garantir que, ao abrir a tela configurada na tarefa, os dados já sejam exibidos de forma pré-filtrada conforme critérios previamente definidos.
Por exemplo, ao adicionar a tela ''**Parceiros''** (Configurações» Cadastros» Parceiros), é possível configurar o filtro para que, ao chegar a essa etapa do processo, a tela seja aberta com um parceiro específico já selecionado.

Essa funcionalidade é especialmente útil para dar continuidade a um cadastro ou visualização iniciados anteriormente no processo, assegurando que o usuário acesse diretamente o registro que deve ser manipulado, sem precisar localizá-lo manualmente.

![Imagem 1: Essa funcionalidade é especialmente útil para dar continuidade a um cadastro ou visualização iniciados anteriormente no…](https://ajuda.sankhya.com.br/hc/article_attachments/34047025027351)

**No exemplo citado, o filtro aplicado seria:**

```
this.CODPARC IN (
  SELECT CODPARC
  FROM TGFPAR_TNF
  WHERE TNF_IDINSTPRN = ${IDINSTPRN}
)
```

Esse filtro utiliza o identificador da instância do processo (`IDINSTPRN`) para localizar o registro do parceiro criado em uma tarefa anterior.
Ele só funciona se o parceiro tiver sido efetivamente criado dentro do **Flow**, pois, nesse caso, o sistema registra automaticamente o vínculo entre a instância do processo e o dado criado na tabela auxiliar `TGFPAR_TNF`.

As tabelas com sufixo `_TNF` são versões paralelas das tabelas principais (como `TGFPAR`) e, além dos dados comuns, armazenam informações sobre o processo e a tarefa em que o registro foi gerado.
Essa lógica se aplica também a outras telas/tabelas do Flow que exijam filtragem com base na instância do processo.

**Para que o filtro funcione corretamente:**

- O registro precisa ter sido criado por uma tarefa anterior dentro do mesmo Flow.
- O objeto (por exemplo, parceiro) deve ter sido salvo na tabela principal e automaticamente registrado na tabela `_TNF`.

#### Exemplo na prática

Suponha que você tenha duas tarefas no **Flow**:

**Tarefa 1:** o responsável cria o parceiro com os dados básicos;

**Tarefa 2:** outro usuário complementa o cadastro, preenchendo os dados fiscais do mesmo parceiro.

**Configuração:**

- Na primeira tarefa, a tela **Parceiros** é adicionada **sem filtro;**
- Na segunda tarefa, a mesma tela **Parceiros** é adicionada **com o filtro** mencionado anteriormente, de forma que seja exibido apenas o parceiro criado na tarefa anterior.

Dessa forma, o sistema identifica, por meio da instância do processo, qual parceiro foi criado anteriormente e o apresenta já filtrado na segunda tarefa, evitando buscas manuais.

#### Conclusão

O filtro só funciona corretamente se o registro foi criado por uma tarefa anterior dentro do mesmo Flow e salvo tanto na tabela principal quanto na tabela **\_TNF**. Isso permite ao sistema relacionar a instância do processo ao dado criado, garantindo continuidade e eficiência entre as etapas.
