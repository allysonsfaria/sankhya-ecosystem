---
id: "39470148960663"
titulo: "Controle de Modificações de Eventos e Fórmulas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39470148960663-Controle-de-Modifica%C3%A7%C3%B5es-de-Eventos-e-F%C3%B3rmulas"
trilha: "Manual do Produto > Pessoas+ > Configurações e Cadastros > Eventos e Regras de Cálculo"
atualizado_em: "2026-10-07T15:39:36Z"
rotulos: ["Configuração", "Eventos", "Fórmulas", "Folha", "Pessoal+", "Auditoria", "br.com.sankhya.mgepes.TFPAuditaFolha", "Controle de Modificações", "Auditoria de Eventos e Fórmulas"]
---

# Controle de Modificações de Eventos e Fórmulas

**Módulo:** Pessoal+
**Versão Mínima:** 5.90.0 
**Caminho de Acesso:** Pessoal+ > Rotinas Folha > Controle de Modificações
**ID da Tela:** br.com.sankhya.mgepes.TFPAuditaFolha

---

## Sumário

[Descrição e Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/39470148960663-Controle-de-Modifica%C3%A7%C3%B5es-de-Eventos-e-F%C3%B3rmulas#h_01KN7428N7JN6XY1TH3110N3WK)

1. [Descrição da Funcionalidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/39470148960663-Controle-de-Modifica%C3%A7%C3%B5es-de-Eventos-e-F%C3%B3rmulas#h_01KN73PST8GPDXKV0HYTSJVCW5)
2. [Pré-requisitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/39470148960663-Controle-de-Modifica%C3%A7%C3%B5es-de-Eventos-e-F%C3%B3rmulas#h_01KN73PSTKXJ7JR73R6NRVEF30)
3. [Jornada de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/39470148960663-Controle-de-Modifica%C3%A7%C3%B5es-de-Eventos-e-F%C3%B3rmulas#h_01KN73PSTRQR6VC2PBMK9AH0Z5)
4. [Pontos de Atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/39470148960663-Controle-de-Modifica%C3%A7%C3%B5es-de-Eventos-e-F%C3%B3rmulas#h_01KN73PSVBPV58T68D8D71VA64)
5. [Dicas de Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/39470148960663-Controle-de-Modifica%C3%A7%C3%B5es-de-Eventos-e-F%C3%B3rmulas#h_01KN73PSVDVHCG0E54CCAP446P)

[Perguntas Frequente (FAQ)](https://ajuda.sankhya.com.br/hc/pt-br/articles/39470148960663-Controle-de-Modifica%C3%A7%C3%B5es-de-Eventos-e-F%C3%B3rmulas#h_01KN73PSVJ3S89GHFXKEZ0BDJA)

[Artigos Relacionados](https://ajuda.sankhya.com.br/hc/pt-br/articles/39470148960663-Controle-de-Modifica%C3%A7%C3%B5es-de-Eventos-e-F%C3%B3rmulas#h_01KN73PSVRJCNPTG5JP3964MPT)

---

## Descrição e Usabilidade

A tela **Controle de Modificações** foi criada para centralizar a **auditoria das alterações realizadas em Eventos e Fórmulas**, oferecendo uma visão clara do que foi modificado, por quem, quando e qual era o conteúdo antes e depois da alteração.

O principal objetivo dessa rotina é fortalecer a **governança das parametrizações da folha**, garantindo maior segurança operacional, rastreabilidade e apoio às áreas de:

- Produto;
- Suporte;
- Compliance;
- Auditoria interna e externa;
- Consultoria.

Com essa funcionalidade, torna-se possível identificar rapidamente alterações que possam impactar:

- Cálculo da folha;
- Encargos;
- Fórmulas de eventos;
- Incorporações;
- Bases de cálculo;
- Regras sindicais;
- Integrações legais.

A tela é **somente leitura**, ou seja, não permite alteração dos dados auditados.

### 1. Descrição da Funcionalidade

A rotina registra e apresenta o **histórico de alterações realizadas nas instâncias auditáveis dos cadastros de Eventos e Fórmulas.**

A auditoria de **Eventos** contempla os principais campos das abas abaixo.

**Aba Básico**

- Descrição Evento;
- Tipo;
- Evento como regra em cálculo de;
- Selecione a Fórmula;
- Sequência;
- Compõe eSocial.

**Aba Avançado**

- INSS e IRRF;
- Outros;
- Tem seus valores recalculados;
- Evento de indenização integrante do Aviso Prévio Indenizado;
- É evento da folha Recibo de Férias?;
- Incide sobre médias.

**Aba eSocial**

- Natureza da Rubrica;
- Incidência p/ Previdência;
- FGTS;
- Incidência p/ IRRF;
- Incidência p/ Contr. Sindical.

A rotina de **Fórmulas** também disponibiliza rastreabilidade para alterações nos seguintes campos:

- Código da característica;
- Característica;
- Descrição;
- Fórmula do Valor;
- Fórmula anterior;
- Fórmula atual.

Cada registro exibe de forma consolidada:

- **Instância:** eventos e fórmulas.
- **Campo alterado:** código e descrição.
- **Data** e **Hora** da alteração.
- **Usuário responsável.**

Ao selecionar um item da grade principal, a tela apresenta em uma grade inferior a comparação:

**Antes × Depois**

**⚠️ Campos do tipo marcação** serão apresentados como:

- **Sim**
- **Não**

Isso facilita a leitura por usuários não técnicos.

### 2. Pré-requisitos

Antes de utilizar a tela, valide:

- Acesso liberado à tela na rotina **Acessos** (Configurações > Controle de Acessos).
- Existência de alterações previamente realizadas em:
  - Eventos;
  - Fórmulas.
- Perfil com permissão de consulta para auditoria e governança.

### 3. Jornada de Uso

#### 3.1 Consultar alterações

1. Acesse a tela **Controle de Modificações** (Pessoal+ > Rotinas Folha).
2. Utilize os **filtros combináveis** em conjunto para investigações específicas:

   - **Período**

     - Data inicial e Data final.
   - **Usuário**
   - **Instância**

     - Eventos
     - Fórmulas
3. Ao definir cada filtro, clique em **Aplicar**.

   A **grade principal apresentará os registros auditados**.

   [GIF animado: Imagem 1: A grade principal apresentará os registros auditados .](https://ajuda.sankhya.com.br/hc/article_attachments/39471617619479)

**Exemplos de uso**

- Localizar alterações feitas por um consultor.
- Validar mudança em uma fórmula específica.
- Auditar alterações de um fechamento.
- Identificar ajustes realizados em data-base.

4. Na grade **Controle de Modificações**, clique nos três pontinhos de cada coluna para organizar os registros por:

- ordem crescente;
- ordem decrescente;
- Filtros dos registros por coluna;
- Coluna fixada.

  [GIF animado: Imagem 2: Coluna fixada.](https://ajuda.sankhya.com.br/hc/article_attachments/39471993887511)

Isso facilita análises cronológicas e específicas.

5. Visualize os detalhes da alteração, marcando **a linha da grade principal**. Dessa forma, na grade **Detalhes do Controle** serão exibidos:

   - nome do campo;
   - valor anterior;
   - valor atual;
   - tipo da alteração.

   [GIF animado: Imagem 3: tipo da alteração.](https://ajuda.sankhya.com.br/hc/article_attachments/39472412375447)

   Quando a alteração for em **Fórmulas**, a visualização mostrará o conteúdo completo:

   **Exemplo**

   **Antes:** SALARIO \* 0.08

   **Depois:** SALARIO \* 0.10

   Essa comparação permite identificar rapidamente mudanças em regras de cálculo.

#### 3.2 Exportar os registros

O botão **Exportar** permite gerar evidências para auditoria, compliance e compartilhamento com outras áreas.

[GIF animado: Imagem 4: O botão Exportar permite gerar evidências para auditoria, compliance e compartilhamento com outras áreas.](https://ajuda.sankhya.com.br/hc/article_attachments/39472408705047)

Você pode exportar:

- **todos os registros filtrados**;
- **somente a página atual**

A exportação pode ser realizada em:

- **PDF (.pdf)**;
- **Planilha (.xls)**.

  O mesmo comportamento está disponível tanto para a exportação completa quanto para a exportação apenas da página exibida.

Além da exportação local, a rotina também permite **enviar o resultado por e-mail**, facilitando o compartilhamento.

Essa opção é especialmente útil para formalização de evidências.

### 4. Pontos de Atenção

- A tela é **somente leitura**.
- Não é possível alterar dados por essa rotina
- A grade inferior só apresenta detalhes após seleção do registro na grade superior.
- Campos de marcação são convertidos para **Sim/Não**.
- O detalhamento inferior só será exibido após seleção do registro.
- Em grandes volumes de auditoria, recomenda-se utilizar filtros por período.

### 5. Dicas de Usabilidade

- Filtre por **usuário + período** para investigações rápidas.
- Utilize **instância Fórmulas** para validar impactos em cálculo
- Use **Eventos** para rastrear parametrizações
- Ordene por data decrescente para visualizar as alterações mais recentes.
- Use o recurso de **Exportar** para compartilhar evidências com auditoria ou compliance.

## Perguntas Frequentes (FAQ)

**1. Posso alterar informações por essa tela?**

Não. A rotina é exclusivamente para **consulta de auditoria**.

**2. A tela mostra quem alterou uma fórmula?**

Sim. Cada registro apresenta o **usuário responsável**, data e hora.

**3. Como identificar o valor anterior de um campo?**

Selecione o registro desejado para abrir a comparação **Antes × Depois**.

**4. Campos de marcação aparecem como verdadeiro/falso?**

Não. Para facilitar a leitura, o sistema apresenta:

- **Sim**
- **Não**

**5. Posso exportar os resultados?**

Sim. A grade possui a funcionalidade **Exportar**, conforme padrão do sistema.

## Artigos Relacionados

- [Cadastro de Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/33041194565911)
- [Cadastro de Fórmulas](https://ajuda.sankhya.com.br/hc/pt-br/articles/13061392411287)
