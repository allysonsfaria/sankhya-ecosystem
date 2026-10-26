---
id: "42427280460951"
titulo: "R06 - Como gerar a Planilha de Apontamentos Customizável (Filtros Avançados)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427280460951-R06-Como-gerar-a-Planilha-de-Apontamentos-Customiz%C3%A1vel-Filtros-Avan%C3%A7ados"
trilha: "PONTOTEL: Sistema de marcação de ponto > Relatórios, Importadores e Exportadores"
atualizado_em: "2026-08-03T12:53:21Z"
rotulos: ["sync_hc", "pontotel", "pontotel_6a3329f94fc2b2b31f66db23", "sync_hash_5a9d95616f7f"]
---

# R06 - Como gerar a Planilha de Apontamentos Customizável (Filtros Avançados)

O **R06 - Planilha de apontamentos customizável** é a ferramenta ideal para uma **gestão por exceção**. Diferente do R05, que traz os totais de todos os apontamentos, o R06 permite que você crie uma **regra de busca** para encontrar apenas as informações desejadas que atendam a um critério específico.

---

## Como Configurar e Gerar o Relatório

1. No menu de navegação do [site Gestão](https://gestao.pontotel.com.br/), selecione a opção **Relatórios e Registros**.
2. Na lista à direita, selecione **R06 - Planilha de apontamentos customizável**.
3. **Configure os filtros básicos**

![Imagem 1: Configure os filtros básicos](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1fry9uz.png)

- Defina os filtros básicos, selecionando os locais, empregadores, empregados ou grupos desejados.
- Defina o período, informando a **data de início e término** nos campos correspondentes.
- Configure as demais opções:

  - **Enviar os resultados do relatório por e-mail:** Marque essa opção para receber o relatório por e-mail após a geração.
  - **Considerar horas que estão no banco de horas:** Inclui no relatório os valores que foram convertidos para o banco.
  - **Considerar empregados demitidos:** Inclui no relatório os empregados que foram desligados antes ou durante o período selecionado.
  - **Ordenar por:**
    - **Nome**: Ordena os dados alfabeticamente pelos nomes dos empregados.
    - **Métricas**: Agrupa e ordena os dados com base em indicadores quantitativos.
  - **Tipo de relatório:**
    - **Soma**: Apresenta os totais acumulados dos apontamentos dentro do período filtrado.
    - **Por dia**: Exibe os dados dia a dia, detalhando os apontamentos por dia dentro do período filtrado.
  - **Apresentação:**
    - **Decimal**: Exibe os valores no formato decimal.
    - **Hora e Minuto**: Mostra os valores no formato padrão de horas (HH:MM).
  - **Mostrar:**
    - **Local de trabalho cadastrado**: Mostra os dados do local de trabalho selecionado no cadastro do empregado.
    - **Posto trabalhado**: Exibe os dados do local de trabalho no qual o colaborador realizou suas atividades.
  - **Apontamentos abreviados na regra de cálculo:** Selecione a regra de cálculo cuja nomenclatura será exibida nos filtros e no relatório. Cada regra de cálculo possui a sua própria forma de nomear os apontamentos (Dentro da regra de cálculo, em Apontamentos > Nomear apontamentos).

4. **Personalize os filtros avançados**

![Imagem 2: Personalize os filtros avançados](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_phpdhj.png)

**4.1. Seleção do filtro desejado**
Escolha um ou mais tipos de apontamentos, como adicional noturno, horas extras ou atrasos. Basta marcar a caixa correspondente à opção que deseja aplicar, por exemplo, selecionar “H. Extra” para filtrar horas extras.

**4.2. Definição do critério de comparação**

- Após selecionar o apontamento, ajuste a condição utilizando os operadores:
  - **Maior que** (>): Exibe somente registros que ultrapassam o valor informado. Exemplo: Filtrar colaboradores com mais de 2 horas extras (insira 02:00).
  - **Igual a** (=): Mostra apenas os registros que correspondem exatamente ao valor especificado. Exemplo: Visualizar atrasos exatos de 10 minutos (insira 00:10).
  - **Menor que** (<): Filtra registros abaixo do valor informado. Exemplo: Identificar colaboradores com intervalo de pausa refeição menor que 1 hora (insira 01:00).
  - **Intervalo**: Filtra jornadas trabalhadas dentro do horário de início e término definido

**4.3. Opções adicionais**
Ative opções extras que podem refinar ainda mais o relatório, tais como:

- Sem intervalos: Exclui os períodos de pausa do cálculo dos apontamentos.
- Sem adicional noturno: Remove o impacto do adicional noturno, caso seja necessário focar apenas em outros tipos de apontamentos.

5. Clique em **Gerar Excel** para iniciar a geração do relatório.

---

> ⚠️ Observação sobre Pausa Refeição e Duração de Pausa

O sistema não deixa de registrar nenhum evento em dias trabalhados.
Quando o colaborador cumpre corretamente sua pausa (sem exercer atividades nesse período), o sistema entende que **não houve horas trabalhadas durante a pausa** e, por isso, o evento **Pausa Refeição** recebe o valor **00:00**.

É importante destacar que:

- **Pausa Refeição** representa o **tempo trabalhado durante o intervalo de refeição**.
- **Duração de Pausa** indica o **tempo total da pausa realizada** pelo colaborador.

---

## Como Baixar o Relatório

Após clicar em "gerar excel", a plataforma processará o relatório em segundo plano:

1. No menu de navegação, clique no **ícone de sino** (Notificações), para acompanhar o arquivo ser gerado.
2. Quando chegar a "100%", o relatório será baixado automaticamente.
3. O R06 é baixado como um arquivo compactado (ZIP). Ao extrair o arquivo, você verá três planilhas:

   - **r06-sucesso:** O relatório principal com todos os dados.
   - **r06-status:** Um arquivo técnico sobre o status da geração.
   - **r06-erro:** Lista eventuais erros na geração.
4. Abra o arquivo **r06-sucesso** para iniciar sua análise.

---

## Como fazer a leitura do relatório

A planilha gerada trará apenas as linhas que obedeceram à sua regra. Com a nova atualização, a leitura ficou mais completa:
Veja o que cada coluna representa:

| Grupo de Colunas | Informações Principais | Dicas de Auditoria (Sua Gestão) |
| --- | --- | --- |
| **Identificação do Colaborador** | **Nome**,**CPF, PIS, Cargo.** | Utilize a coluna **Cargo** para identificar se um problema específico (ex: excesso de horas extras) está concentrado em uma função específica da empresa. |
| **Estrutura Organizacional** | **Local de Trabalho**, **Empregador.** | Use para filtrar e analisar os dados por filial ou empresa do grupo. |
| **Apontamentos** | **Apontamento** (o valor que ativou o filtro) | A coluna de um apontamento mostra o valor exato do evento filtrado (ex: "01:48" de atraso), facilitando a identificação da gravidade da ocorrência. |

![Exemplo de planilha do R06 na aba "Todos os Funcionários"](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_vrg36t.png)

Exemplo de planilha do R06 na aba "Todos os Funcionários"

- Além da planilha principal, temos também a planilha da aba "Resumo por local, que entrega um valor consolidado dos apontamentos filtrados por local de trabalho.

![Exemplo de planilha do R06 na aba "Resumo por local"](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1f8sfxq.png)

Exemplo de planilha do R06 na aba "Resumo por local"

---

O R06 é a sua "lupa" sobre a folha de ponto. Com ele, você investiga problemas específicos sem precisar abrir a folha de cada colaborador um a um.

Caso ainda tenha dúvidas ou precise de auxílio, entre em contato com o nosso time de Suporte pelo chat integrado ao [site Pontotel Gestão](https://gestao.pontotel.com.br/#/cognito/login) ou pelo [WhatsApp](https://api.whatsapp.com/send/?phone=551131852700&text&type=phone_number&app_absent=0)!
