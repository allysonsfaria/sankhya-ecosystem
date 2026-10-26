---
id: "38167049533079"
titulo: "Como reprocessar o plano de saúde"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38167049533079-Como-reprocessar-o-plano-de-sa%C3%BAde"
trilha: "Manual do Produto > Pessoas+ > Benefícios > Plano de Saúde"
atualizado_em: "2026-10-02T15:50:42Z"
rotulos: ["Configuração", "Funcionários", "Dependentes", "eSocial", "br.com.sankhya.rh.GerenciadorFolha", "Gerenciador de Folhas", "Central do eSocial", "Evento S-1210", "Plano de Saúde", "Pessoal+", "Reprocessamento de Plano de Saúde para Funcionários e Dependentes", "Correção de dados do IRRF no eSocial (S-1210) para anos anteriores", "Reprocessar plano de saúde"]
---

# Como reprocessar o plano de saúde

**Módulo:** Pessoal+
**Versão:** 5.82.0
**Caminho de Acesso:** Pessoal+ > Rotinas Folha > Gerenciador de Folhas 
**ID da Tela:** br.com.sankhya.rh.GerenciadorFolha

---

### Descrição e Usabilidade

Esta funcionalidade permite **reprocessar os dados de plano de saúde** de funcionários e dependentes **a partir dos eventos lançados em movimento e calculados na folha**.

O objetivo é **preencher automaticamente os cadastros de plano de saúde** quando existirem descontos em folha, mas não houver cadastro correspondente, garantindo **consistência entre movimento, folha, cadastro e eSocial**, sem a necessidade de ajustes manuais.

### Pré-requisitos

#### Permissões necessárias

- Possuir acesso às telas:

  - Gerenciador de Folhas;
  - Configuração Funcionários;
  - Central do eSocial.

📌 O reprocessamento considera **apenas as empresas às quais o usuário já possui acesso**.

#### Condições obrigatórias

- Existirem **eventos de desconto de plano de saúde** lançados em movimento e calculados em folha;
- Funcionários e/ou dependentes **sem plano de saúde cadastrado**, mas com evento de desconto.

### Jornada de Uso

**(1)** **Acessar o Gerenciador de Folhas**

1. Acesse a tela **Gerenciador de Folhas** (Pessoal+ > Rotinas Folha) e clique no botão **Reprocessar plano de saúde** ao lado direito da tela.

   ![Imagem 1: Acesse a tela Gerenciador de Folhas (Pessoal+ > Rotinas Folha) e clique no botão Reprocessar plano de saúde ao lado…](https://ajuda.sankhya.com.br/hc/article_attachments/38196709265431)
2. No pop-up apresentado, serão exibidas **as empresas às quais o usuário tem acesso**.
3. Selecione uma ou mais empresas.
4. Selecione a **Referência inicial**;

   ⚠️O período não pode ser **anterior a 2025** nem **posterior ao ano informado**;

   A partir desse período, o sistema define a **Referência inicial do Plano de Saúde** para colaboradores e dependentes ajustados.
5. Após preencher todos os campos, clique em **Iniciar reprocessamento**.

   [GIF animado: Imagem 2: Após preencher todos os campos, clique em Iniciar reprocessamento .](https://ajuda.sankhya.com.br/hc/article_attachments/38196709267863)

O sistema exibirá a mensagem de confirmação:

**"Atenção!**

**Os cadastros de plano de saúde de funcionários e dependentes sem cadastro serão atualizados com base nos eventos do período selecionado.**
**Esta ação é irreversível."**

Ao confirmar a ação, o sistema automaticamente:

- preenche o **código do plano de saúde** no cadastro do funcionário conforme o plano vinculado ao evento;
- define a **Referência inicial** do Plano de Saúde conforme o período informado;
- Marca automaticamente:

  - **Possui Plano de Saúde** no cadastro do funcionário;
  - **Dependente de Convênio Médico** no cadastro do dependente;
- Mantém os dados **inalterados** caso o plano já esteja corretamente cadastrado.

(2)** Processamento em lote**

- É possível selecionar **mais de uma empresa**;
- O sistema aplica o reprocessamento **em lote**, seguindo as mesmas regras para todas as empresas selecionadas.

(2)** Validações importantes**

- Se nenhuma empresa ou período for informado, o sistema exibirá uma mensagem de aviso solicitando o preenchimento;
- O reprocessamento **não altera folhas**, **não exige bloqueio/desbloqueio** e **não interfere em cálculos já realizados**.

(2)** Integração com o eSocial**

Após o ajuste, acesse a **Central do eSocial** (Pessoal+ > Rotina Folha) para gerar e enviar a **retificação do evento S-1210** dos períodos impactados.

As informações de plano de saúde são enviadas no grupo:
**infoIRComplem > planSaude**;

⚠️ Não é necessário refazer cálculos, nem reabrir a folha.

### Pontos de Atenção

- O processo é **irreversível**.
- Utilize apenas quando houver **desconto de plano de saúde sem cadastro correspondente**.
- Recomenda-se executar o reprocessamento **antes de novos envios ao eSocial**.

### Dicas de Usabilidade

- Verifique previamente se os eventos de plano de saúde estão corretos.
- Use o reprocessamento para **regularizar cadastros antigos ou incompletos**.
- Após o processamento, utilize a **Central do eSocial** para conferir as retificações geradas.

### Artigos relacionados

- [Cadastro e Vínculo de Plano de Saúde](https://ajuda.sankhya.com.br/hc/pt-br/articles/39280364021527)
- [Configuração de Tabelas de Faixas para Plano de Saúde](https://ajuda.sankhya.com.br/hc/pt-br/articles/39626660634519)
- [Configuração Funcionários](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639)
- [Cadastro de Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/33041194565911)
- [Valores de Plano de Saúde na DIRF](https://ajuda.sankhya.com.br/hc/pt-br/articles/28555465280663)
- [Encerramento de Plano de Saúde - Titular e Dependente](https://ajuda.sankhya.com.br/hc/pt-br/articles/39286360023959)
- [Correção de dados do IRRF no eSocial (S-1210) para anos anteriores](https://ajuda.sankhya.com.br/hc/pt-br/articles/37272130595223)
